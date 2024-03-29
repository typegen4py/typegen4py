import typing as t
from ..datastructures import CombinedMultiDict as CombinedMultiDict, EnvironHeaders as EnvironHeaders, FileStorage as FileStorage, ImmutableMultiDict as ImmutableMultiDict, MultiDict as MultiDict, iter_multi_items as iter_multi_items
from ..formparser import FormDataParser as FormDataParser, default_stream_factory as default_stream_factory
from ..http import parse_options_header as parse_options_header
from ..sansio.request import Request as _SansIORequest
from ..utils import cached_property as cached_property, environ_property as environ_property
from ..wsgi import get_content_length as get_content_length, get_input_stream as get_input_stream
from typing import Any
from werkzeug.exceptions import BadRequest as BadRequest
from wsgiref.types import WSGIApplication as WSGIApplication, WSGIEnvironment as WSGIEnvironment

class Request(_SansIORequest):
    max_content_length: t.Optional[int] = ...
    max_form_memory_size: t.Optional[int] = ...
    form_data_parser_class: t.Type[FormDataParser] = ...
    disable_data_descriptor: bool = ...
    environ: WSGIEnvironment
    shallow: bool
    def __init__(self, environ: WSGIEnvironment, populate_request: bool=..., shallow: bool=...) -> None: ...
    @classmethod
    def from_values(cls: Any, *args: Any, **kwargs: Any) -> Request: ...
    @classmethod
    def application(cls: Any, f: t.Callable[[Request], WSGIApplication]) -> WSGIApplication: ...
    @property
    def want_form_data_parsed(self) -> bool: ...
    def make_form_data_parser(self) -> FormDataParser: ...
    def close(self) -> None: ...
    def __enter__(self) -> Request: ...
    def __exit__(self, exc_type: Any, exc_value: Any, tb: Any) -> None: ...
    def stream(self) -> t.BinaryIO: ...
    input_stream: Any = ...
    def data(self) -> bytes: ...
    def get_data(self, cache: bool=..., as_text: bool=..., parse_form_data: bool=...) -> bytes: ...
    def form(self) -> ImmutableMultiDict[str, str]: ...
    def values(self) -> CombinedMultiDict[str, str]: ...
    def files(self) -> ImmutableMultiDict[str, FileStorage]: ...
    @property
    def script_root(self) -> str: ...
    def url_root(self): ...
    remote_user: Any = ...
    is_multithread: Any = ...
    is_multiprocess: Any = ...
    is_run_once: Any = ...
    json_module: Any = ...
    @property
    def json(self) -> t.Optional[t.Any]: ...
    def get_json(self, force: bool=..., silent: bool=..., cache: bool=...) -> t.Optional[t.Any]: ...
    def on_json_loading_failed(self, e: ValueError) -> t.Any: ...

class StreamOnlyMixin:
    disable_data_descriptor: bool = ...
    want_form_data_parsed: bool = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class PlainRequest(StreamOnlyMixin, Request):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
