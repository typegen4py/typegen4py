from typing import Any, Optional

class HTTPError(Exception): ...
class HTTPWarning(Warning): ...

class PoolError(HTTPError):
    pool: Any = ...
    def __init__(self, pool: Any, message: Any) -> None: ...
    def __reduce__(self): ...

class RequestError(PoolError):
    url: Any = ...
    def __init__(self, pool: Any, url: Any, message: Any) -> None: ...
    def __reduce__(self): ...

class SSLError(HTTPError): ...
class ProxyError(HTTPError): ...
class DecodeError(HTTPError): ...
class ProtocolError(HTTPError): ...
ConnectionError = ProtocolError

class MaxRetryError(RequestError):
    reason: Any = ...
    def __init__(self, pool: Any, url: Any, reason: Optional[Any] = ...) -> None: ...

class HostChangedError(RequestError):
    retries: Any = ...
    def __init__(self, pool: Any, url: Any, retries: int = ...) -> None: ...

class TimeoutStateError(HTTPError): ...
class TimeoutError(HTTPError): ...
class ReadTimeoutError(TimeoutError, RequestError): ...
class ConnectTimeoutError(TimeoutError): ...
class NewConnectionError(ConnectTimeoutError, PoolError): ...
class EmptyPoolError(PoolError): ...
class ClosedPoolError(PoolError): ...
class LocationValueError(ValueError, HTTPError): ...

class LocationParseError(LocationValueError):
    location: Any = ...
    def __init__(self, location: Any) -> None: ...

class ResponseError(HTTPError):
    GENERIC_ERROR: str = ...
    SPECIFIC_ERROR: str = ...

class SecurityWarning(HTTPWarning): ...
class SubjectAltNameWarning(SecurityWarning): ...
class InsecureRequestWarning(SecurityWarning): ...
class SystemTimeWarning(SecurityWarning): ...
class InsecurePlatformWarning(SecurityWarning): ...
class SNIMissingWarning(HTTPWarning): ...
class ResponseNotChunked(ProtocolError, ValueError): ...

class ProxySchemeUnknown(AssertionError, ValueError):
    def __init__(self, scheme: Any) -> None: ...

class HeaderParsingError(HTTPError):
    def __init__(self, defects: Any, unparsed_data: Any) -> None: ...