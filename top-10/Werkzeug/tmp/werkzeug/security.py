import codecs
import hashlib
import hmac
import os
import posixpath
import secrets
import typing as t

from ._internal import _to_bytes

if t.TYPE_CHECKING:
    pass

SALT_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
DEFAULT_PBKDF2_ITERATIONS = 260000

_os_alt_seps: t.List[str] = list(
    sep for sep in [os.path.sep, os.path.altsep] if sep is not None and sep != "/"
)


def pbkdf2_hex(
    data: t.AnyStr,
    salt: t.AnyStr,
    iterations: int = DEFAULT_PBKDF2_ITERATIONS,
    keylen: t.Optional[int] = None,
    hashfunc: t.Optional[str] = None,
) -> str:
    """Like :func:`pbkdf2_bin`, but returns a hex-encoded string.

    .. versionadded:: 0.9

    :param data: the data to derive.
    :param salt: the salt for the derivation.
    :param iterations: the number of iterations.
    :param keylen: the length of the resulting key.  If not provided,
                   the digest size will be used.
    :param hashfunc: the hash function to use.  This can either be the
                     string name of a known hash function, or a function
                     from the hashlib module.  Defaults to sha256.
    """
    rv = pbkdf2_bin(data, salt, iterations, keylen, hashfunc)
    return codecs.encode(rv, "hex_codec").decode("ascii")


def pbkdf2_bin(
    data: t.AnyStr,
    salt: t.AnyStr,
    iterations: int = DEFAULT_PBKDF2_ITERATIONS,
    keylen: t.Optional[int] = None,
    hashfunc: t.Optional[str] = None,
) -> bytes:
    """Returns a binary digest for the PBKDF2 hash algorithm of `data`
    with the given `salt`. It iterates `iterations` times and produces a
    key of `keylen` bytes. By default, SHA-256 is used as hash function;
    a different hashlib `hashfunc` can be provided.

    .. versionadded:: 0.9

    :param data: the data to derive.
    :param salt: the salt for the derivation.
    :param iterations: the number of iterations.
    :param keylen: the length of the resulting key.  If not provided
                   the digest size will be used.
    :param hashfunc: the hash function to use.  This can either be the
                     string name of a known hash function or a function
                     from the hashlib module.  Defaults to sha256.
    """
    if not hashfunc:
        hashfunc = "sha256"

    data = _to_bytes(data)
    salt = _to_bytes(salt)

    if callable(hashfunc):
        _test_hash = hashfunc()
        hash_name = getattr(_test_hash, "name", None)
    else:
        hash_name = hashfunc
    return hashlib.pbkdf2_hmac(hash_name, data, salt, iterations, keylen)


def safe_str_cmp(a: str, b: str) -> bool:
    """This function compares strings in somewhat constant time.  This
    requires that the length of at least one string is known in advance.

    Returns `True` if the two strings are equal, or `False` if they are not.

    .. versionadded:: 0.7
    """
    if isinstance(a, str):
        a = a.encode("utf-8")  # type: ignore
    if isinstance(b, str):
        b = b.encode("utf-8")  # type: ignore

    return hmac.compare_digest(a, b)


def gen_salt(length: int) -> str:
    """Generate a random string of SALT_CHARS with specified ``length``."""
    if length <= 0:
        raise ValueError("Salt length must be positive")
    return "".join(secrets.choice(SALT_CHARS) for _ in range(length))


def _hash_internal(method: str, salt: str, password: str) -> t.Tuple[str, str]:
    """Internal password hash helper.  Supports plaintext without salt,
    unsalted and salted passwords.  In case salted passwords are used
    hmac is used.
    """
    if method == "plain":
        return password, method

    if isinstance(password, str):
        password = password.encode("utf-8")  # type: ignore

    if method.startswith("pbkdf2:"):
        args = method[7:].split(":")
        if len(args) not in (1, 2):
            raise ValueError("Invalid number of arguments for PBKDF2")
        method = args.pop(0)
        iterations = int(args[0] or 0) if args else DEFAULT_PBKDF2_ITERATIONS
        is_pbkdf2 = True
        actual_method = f"pbkdf2:{method}:{iterations}"
    else:
        is_pbkdf2 = False
        actual_method = method

    if is_pbkdf2:
        if not salt:
            raise ValueError("Salt is required for PBKDF2")
        rv = pbkdf2_hex(password, salt, iterations, hashfunc=method)
    elif salt:
        if isinstance(salt, str):
            salt = salt.encode("utf-8")  # type: ignore
        mac = _create_mac(salt, password, method)  # type: ignore
        rv = mac.hexdigest()
    else:
        rv = hashlib.new(method, password).hexdigest()  # type: ignore
    return rv, actual_method


def _create_mac(key: bytes, msg: bytes, method: str) -> hmac.HMAC:
    if callable(method):
        return hmac.new(key, msg, method)

    def hashfunc(d=b""):
        return hashlib.new(method, d)

    return hmac.new(key, msg, hashfunc)


def generate_password_hash(
    password: str, method: str = "pbkdf2:sha256", salt_length: int = 16
) -> str:
    """Hash a password with the given method and salt with a string of
    the given length. The format of the string returned includes the method
    that was used so that :func:`check_password_hash` can check the hash.

    The format for the hashed string looks like this::

        method$salt$hash

    This method can **not** generate unsalted passwords but it is possible
    to set param method='plain' in order to enforce plaintext passwords.
    If a salt is used, hmac is used internally to salt the password.

    If PBKDF2 is wanted it can be enabled by setting the method to
    ``pbkdf2:method:iterations`` where iterations is optional::

        pbkdf2:sha256:80000$salt$hash
        pbkdf2:sha256$salt$hash

    :param password: the password to hash.
    :param method: the hash method to use (one that hashlib supports). Can
                   optionally be in the format ``pbkdf2:method:iterations``
                   to enable PBKDF2.
    :param salt_length: the length of the salt in letters.
    """
    salt = gen_salt(salt_length) if method != "plain" else ""
    h, actual_method = _hash_internal(method, salt, password)
    return f"{actual_method}${salt}${h}"


def check_password_hash(pwhash: str, password: str) -> bool:
    """check a password against a given salted and hashed password value.
    In order to support unsalted legacy passwords this method supports
    plain text passwords, md5 and sha1 hashes (both salted and unsalted).

    Returns `True` if the password matched, `False` otherwise.

    :param pwhash: a hashed string like returned by
                   :func:`generate_password_hash`.
    :param password: the plaintext password to compare against the hash.
    """
    if pwhash.count("$") < 2:
        return False
    method, salt, hashval = pwhash.split("$", 2)
    return safe_str_cmp(_hash_internal(method, salt, password)[0], hashval)


def safe_join(directory: str, *pathnames: str) -> t.Optional[str]:
    """Safely join zero or more untrusted path components to a base
    directory to avoid escaping the base directory.

    :param directory: The trusted base directory.
    :param pathnames: The untrusted path components relative to the
        base directory.
    :return: A safe path, otherwise ``None``.
    """
    parts = [directory]

    for filename in pathnames:
        if filename != "":
            filename = posixpath.normpath(filename)

        if (
            any(sep in filename for sep in _os_alt_seps)
            or os.path.isabs(filename)
            or filename == ".."
            or filename.startswith("../")
        ):
            return None

        parts.append(filename)

    return posixpath.join(*parts)
