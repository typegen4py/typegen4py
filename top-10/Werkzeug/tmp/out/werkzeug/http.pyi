import typing as t
import typing_extensions as te
from . import datastructures as ds
from datetime import date, datetime, timedelta
from enum import Enum
from time import struct_time
from typing import Any
from wsgiref.types import WSGIEnvironment as WSGIEnvironment

HTTP_STATUS_CODES: Any

class COEP(Enum):
    UNSAFE_NONE: str = ...
    REQUIRE_CORP: str = ...

class COOP(Enum):
    UNSAFE_NONE: str = ...
    SAME_ORIGIN_ALLOW_POPUPS: str = ...
    SAME_ORIGIN: str = ...

def quote_header_value(value: t.Union[str, int], extra_chars: str=..., allow_token: bool=...) -> str: ...
def unquote_header_value(value: str, is_filename: bool=...) -> str: ...
def dump_options_header(header: str, options: t.Dict[str, t.Optional[t.Union[str, int]]]) -> str: ...
def dump_header(iterable: t.Union[t.Dict[str, t.Union[str, int]], t.Iterable[str]], allow_token: bool=...) -> str: ...
def dump_csp_header(header: ds.ContentSecurityPolicy) -> str: ...
def parse_list_header(value: str) -> t.List[str]: ...
def parse_dict_header(value: str, cls: t.Type[dict]=...) -> t.Dict[str, str]: ...
def parse_options_header(value: t.Optional[str], multiple: te.Literal[False]=...) -> t.Tuple[str, t.Dict[str, str]]: ...
def parse_accept_header(value: t.Optional[str], cls: None=...) -> ds.Accept: ...
def parse_cache_control_header(value: t.Optional[str], on_update: _t_cc_update, cls: None=...) -> ds.RequestCacheControl: ...
def parse_csp_header(value: t.Optional[str], on_update: _t_csp_update, cls: None=...) -> ds.ContentSecurityPolicy: ...
def parse_set_header(value: t.Optional[str], on_update: t.Optional[t.Callable[[ds.HeaderSet], None]]=...) -> ds.HeaderSet: ...
def parse_authorization_header(value: t.Optional[str]) -> t.Optional[ds.Authorization]: ...
def parse_www_authenticate_header(value: t.Optional[str], on_update: t.Optional[t.Callable[[ds.WWWAuthenticate], None]]=...) -> ds.WWWAuthenticate: ...
def parse_if_range_header(value: t.Optional[str]) -> ds.IfRange: ...
def parse_range_header(value: t.Optional[str], make_inclusive: bool=...) -> t.Optional[ds.Range]: ...
def parse_content_range_header(value: t.Optional[str], on_update: t.Optional[t.Callable[[ds.ContentRange], None]]=...) -> t.Optional[ds.ContentRange]: ...
def quote_etag(etag: str, weak: bool=...) -> str: ...
def unquote_etag(etag: t.Optional[str]) -> t.Union[t.Tuple[str, bool], t.Tuple[None, None]]: ...
def parse_etags(value: t.Optional[str]) -> ds.ETags: ...
def generate_etag(data: bytes) -> str: ...
def parse_date(value: t.Optional[str]) -> t.Optional[datetime]: ...
def cookie_date(expires: t.Optional[t.Union[datetime, date, int, float, struct_time]]=...) -> str: ...
def http_date(timestamp: t.Optional[t.Union[datetime, date, int, float, struct_time]]=...) -> str: ...
def parse_age(value: t.Optional[str]=...) -> t.Optional[timedelta]: ...
def dump_age(age: t.Optional[t.Union[timedelta, int]]=...) -> t.Optional[str]: ...
def is_resource_modified(environ: WSGIEnvironment, etag: t.Optional[str]=..., data: t.Optional[bytes]=..., last_modified: t.Optional[t.Union[datetime, str]]=..., ignore_if_range: bool=...) -> bool: ...
def remove_entity_headers(headers: t.Union[ds.Headers, t.List[t.Tuple[str, str]]], allowed: t.Iterable[str]=...) -> None: ...
def remove_hop_by_hop_headers(headers: t.Union[ds.Headers, t.List[t.Tuple[str, str]]]) -> None: ...
def is_entity_header(header: str) -> bool: ...
def is_hop_by_hop_header(header: str) -> bool: ...
def parse_cookie(header: t.Union[WSGIEnvironment, str, bytes, None], charset: str=..., errors: str=..., cls: t.Optional[t.Type[ds.MultiDict]]=...) -> ds.MultiDict[str, str]: ...
def dump_cookie(key: str, value: t.Union[bytes, str]=..., max_age: t.Optional[t.Union[timedelta, int]]=..., expires: t.Optional[t.Union[str, datetime, int, float]]=..., path: t.Optional[str]=..., domain: t.Optional[str]=..., secure: bool=..., httponly: bool=..., charset: str=..., sync_expires: bool=..., max_size: int=..., samesite: t.Optional[str]=...) -> str: ...
def is_byte_range_valid(start: t.Optional[int], stop: t.Optional[int], length: t.Optional[int]) -> bool: ...
