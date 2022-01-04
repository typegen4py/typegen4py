import typing as t
from .wrappers.request import Request as Request
from .wrappers.response import Response as Response
from typing import Any
from wsgiref.types import StartResponse, WSGIEnvironment as WSGIEnvironment

logo: Any
TEMPLATE: str

def iter_sys_path() -> t.Iterator[t.Tuple[str, bool, bool]]: ...
def render_testapp(req: Request) -> bytes: ...
def test_app(environ: WSGIEnvironment, start_response: StartResponse) -> t.Iterable[bytes]: ...
