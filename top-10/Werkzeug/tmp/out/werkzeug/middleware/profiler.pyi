import typing as t
from wsgiref.types import StartResponse, WSGIApplication as WSGIApplication, WSGIEnvironment as WSGIEnvironment

class ProfilerMiddleware:
    def __init__(self, app: WSGIApplication, stream: t.TextIO=..., sort_by: t.Iterable[str]=..., restrictions: t.Iterable[t.Union[str, int, float]]=..., profile_dir: t.Optional[str]=..., filename_format: str=...) -> None: ...
    def __call__(self, environ: WSGIEnvironment, start_response: StartResponse) -> t.Iterable[bytes]: ...