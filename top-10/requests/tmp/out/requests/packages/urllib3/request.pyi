from typing import Any, Optional

class RequestMethods:
    headers: Any = ...
    def __init__(self, headers: Optional[Any] = ...) -> None: ...
    def urlopen(self, method: Any, url: Any, body: Optional[Any] = ..., headers: Optional[Any] = ..., encode_multipart: bool = ..., multipart_boundary: Optional[Any] = ..., **kw: Any) -> None: ...
    def request(self, method: Any, url: Any, fields: Optional[Any] = ..., headers: Optional[Any] = ..., **urlopen_kw: Any): ...
    def request_encode_url(self, method: Any, url: Any, fields: Optional[Any] = ..., headers: Optional[Any] = ..., **urlopen_kw: Any): ...
    def request_encode_body(self, method: Any, url: Any, fields: Optional[Any] = ..., headers: Optional[Any] = ..., encode_multipart: bool = ..., multipart_boundary: Optional[Any] = ..., **urlopen_kw: Any): ...
