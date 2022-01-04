from ..exceptions import ConnectTimeoutError as ConnectTimeoutError, MaxRetryError as MaxRetryError, ProtocolError as ProtocolError, ReadTimeoutError as ReadTimeoutError, ResponseError as ResponseError
from typing import Any, Optional

log: Any

class Retry:
    DEFAULT_METHOD_WHITELIST: Any = ...
    BACKOFF_MAX: int = ...
    total: Any = ...
    connect: Any = ...
    read: Any = ...
    redirect: Any = ...
    status_forcelist: Any = ...
    method_whitelist: Any = ...
    backoff_factor: Any = ...
    raise_on_redirect: Any = ...
    def __init__(self, total: int = ..., connect: Optional[Any] = ..., read: Optional[Any] = ..., redirect: Optional[Any] = ..., method_whitelist: Any = ..., status_forcelist: Optional[Any] = ..., backoff_factor: int = ..., raise_on_redirect: bool = ..., _observed_errors: int = ...) -> None: ...
    def new(self, **kw: Any): ...
    @classmethod
    def from_int(cls, retries: Any, redirect: bool = ..., default: Optional[Any] = ...): ...
    def get_backoff_time(self): ...
    def sleep(self) -> None: ...
    def is_forced_retry(self, method: Any, status_code: Any): ...
    def is_exhausted(self): ...
    def increment(self, method: Optional[Any] = ..., url: Optional[Any] = ..., response: Optional[Any] = ..., error: Optional[Any] = ..., _pool: Optional[Any] = ..., _stacktrace: Optional[Any] = ...): ...