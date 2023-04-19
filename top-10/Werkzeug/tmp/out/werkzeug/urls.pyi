import typing as t
from . import datastructures as ds
from typing import Any, Optional

class _URLTuple(t.NamedTuple):
    scheme: str
    netloc: str
    path: str
    query: str
    fragment: str

class BaseURL(_URLTuple):
    def replace(self, **kwargs: Any) -> BaseURL: ...
    @property
    def host(self) -> t.Optional[str]: ...
    @property
    def ascii_host(self) -> t.Optional[str]: ...
    @property
    def port(self) -> t.Optional[int]: ...
    @property
    def auth(self) -> t.Optional[str]: ...
    @property
    def username(self) -> t.Optional[str]: ...
    @property
    def raw_username(self) -> t.Optional[str]: ...
    @property
    def password(self) -> t.Optional[str]: ...
    @property
    def raw_password(self) -> t.Optional[str]: ...
    def decode_query(self, *args: Any, **kwargs: Any) -> ds.MultiDict[str, str]: ...
    def join(self, *args: Any, **kwargs: Any) -> BaseURL: ...
    def to_url(self) -> str: ...
    def encode_netloc(self) -> str: ...
    def decode_netloc(self) -> str: ...
    def to_uri_tuple(self) -> BaseURL: ...
    def to_iri_tuple(self) -> BaseURL: ...
    def get_file_location(self, pathformat: t.Optional[str]=...) -> t.Tuple[t.Optional[str], t.Optional[str]]: ...

class URL(BaseURL):
    def encode(self, charset: Any=..., errors: Any=...) -> BytesURL: ...

class BytesURL(BaseURL):
    def encode_netloc(self) -> bytes: ...
    def decode(self, charset: Any=..., errors: Any=...) -> URL: ...

def url_parse(url: str, scheme: t.Optional[str]=..., allow_fragments: bool=...) -> BaseURL: ...
def url_quote(string: t.Union[str, bytes], charset: str=..., errors: str=..., safe: t.Union[str, bytes]=..., unsafe: t.Union[str, bytes]=...) -> str: ...
def url_quote_plus(string: str, charset: str=..., errors: str=..., safe: str=...) -> str: ...
def url_unparse(components: t.Tuple[str, str, str, str, str]) -> str: ...
def url_unquote(s: t.Union[str, bytes], charset: str=..., errors: str=..., unsafe: str=...) -> str: ...
def url_unquote_plus(s: t.Union[str, bytes], charset: str=..., errors: str=...) -> str: ...
def url_fix(s: str, charset: str=...) -> str: ...
def uri_to_iri(uri: t.Union[str, t.Tuple[str, str, str, str, str]], charset: str=..., errors: str=...) -> str: ...
def iri_to_uri(iri: t.Union[str, t.Tuple[str, str, str, str, str]], charset: str=..., errors: str=..., safe_conversion: bool=...) -> str: ...
def url_decode(s: t.AnyStr, charset: str=..., decode_keys: None=..., include_empty: bool=..., errors: str=..., separator: str=..., cls: t.Optional[t.Type[ds.MultiDict]]=...) -> ds.MultiDict[str, str]: ...
def url_decode_stream(stream: t.BinaryIO, charset: Any=..., decode_keys: None=..., include_empty: bool=..., errors: str=..., separator: bytes=..., cls: t.Optional[t.Type[ds.MultiDict]]=..., limit: t.Optional[int]=..., return_iterator: bool=...) -> ds.MultiDict[str, str]: ...
def url_encode(obj: t.Union[t.Mapping[str, str], t.Iterable[t.Tuple[str, str]]], charset: str=..., encode_keys: None=..., sort: bool=..., key: t.Optional[t.Callable[[t.Tuple[str, str]], t.Any]]=..., separator: str=...) -> str: ...
def url_encode_stream(obj: t.Union[t.Mapping[str, str], t.Iterable[t.Tuple[str, str]]], stream: t.Optional[t.TextIO]=..., charset: str=..., encode_keys: None=..., sort: bool=..., key: t.Optional[t.Callable[[t.Tuple[str, str]], t.Any]]=..., separator: str=...) -> None: ...
def url_join(base: t.Union[str, t.Tuple[str, str, str, str, str]], url: t.Union[str, t.Tuple[str, str, str, str, str]], allow_fragments: bool=...) -> Any: ...

class Href:
    base: Any = ...
    charset: Any = ...
    sort: Any = ...
    key: Any = ...
    def __init__(self, base: str = ..., charset: str = ..., sort: bool = ..., key: Optional[Any] = ...) -> None: ...
    def __getattr__(self, name: Any): ...
    def __call__(self, *path: Any, **query: Any): ...