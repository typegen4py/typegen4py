import os
import typing as t
from ._internal import _DictAccessorProperty, _TAccessorValue
from .datastructures import Headers as Headers
from .exceptions import NotFound as NotFound, RequestedRangeNotSatisfiable as RequestedRangeNotSatisfiable
from .security import safe_join as safe_join
from .urls import url_quote as url_quote
from .wrappers import Response as Response
from .wsgi import wrap_file as wrap_file
from datetime import datetime
from typing import Any, Optional
from wsgiref.types import WSGIEnvironment as WSGIEnvironment

class cached_property(property):
    __name__: Any = ...
    __module__: Any = ...
    def __init__(self, fget: t.Callable[[t.Any], t.Any], name: t.Optional[str]=..., doc: t.Optional[str]=...) -> None: ...
    def __set__(self, obj: object, value: t.Any) -> None: ...
    def __get__(self, obj: object, type: type=...) -> t.Any: ...

def invalidate_cached_property(obj: object, name: str) -> None: ...

class environ_property(_DictAccessorProperty[_TAccessorValue]):
    read_only: bool = ...
    def lookup(self, obj: t.Any) -> WSGIEnvironment: ...

class header_property(_DictAccessorProperty[_TAccessorValue]):
    def lookup(self, obj: t.Any) -> Headers: ...

class HTMLBuilder:
    def __init__(self, dialect: Any) -> None: ...
    def __call__(self, s: Any): ...
    def __getattr__(self, tag: Any): ...

html: Any
xhtml: Any

def get_content_type(mimetype: str, charset: str) -> str: ...
def detect_utf_encoding(data: bytes) -> str: ...
def format_string(string: Any, context: Any): ...
def secure_filename(filename: str) -> str: ...
def escape(s: Any): ...
def unescape(s: Any): ...
def redirect(location: str, code: int=..., Response: t.Optional[t.Type[Response]]=...) -> Response: ...
def append_slash_redirect(environ: WSGIEnvironment, code: int=...) -> Response: ...
def send_file(path_or_file: t.Union[os.PathLike, str, t.BinaryIO], environ: WSGIEnvironment, mimetype: t.Optional[str]=..., as_attachment: bool=..., download_name: t.Optional[str]=..., conditional: bool=..., etag: t.Union[bool, str]=..., last_modified: t.Optional[t.Union[datetime, int, float]]=..., max_age: t.Optional[t.Union[int, t.Callable[[t.Optional[t.Union[os.PathLike, str]]], int]]]=..., use_x_sendfile: bool=..., response_class: t.Optional[t.Type[Response]]=..., _root_path: t.Optional[t.Union[os.PathLike, str]]=...) -> Any: ...
def send_from_directory(directory: t.Union[os.PathLike, str], path: t.Union[os.PathLike, str], environ: WSGIEnvironment, **kwargs: Any) -> Response: ...
def import_string(import_name: str, silent: bool=...) -> t.Any: ...
def find_modules(import_path: str, include_packages: bool=..., recursive: bool=...) -> t.Iterator[str]: ...
def validate_arguments(func: Any, args: Any, kwargs: Any, drop_extra: bool = ...): ...
def bind_arguments(func: Any, args: Any, kwargs: Any): ...

class ArgumentValidationError(ValueError):
    missing: Any = ...
    extra: Any = ...
    extra_positional: Any = ...
    def __init__(self, missing: Optional[Any] = ..., extra: Optional[Any] = ..., extra_positional: Optional[Any] = ...) -> None: ...

class ImportStringError(ImportError):
    import_name: str
    exception: BaseException
    def __init__(self, import_name: Any, exception: Any) -> None: ...