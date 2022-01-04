from .request import RequestMethods
from typing import Any, Optional

class PoolManager(RequestMethods):
    proxy: Any = ...
    connection_pool_kw: Any = ...
    pools: Any = ...
    def __init__(self, num_pools: int = ..., headers: Optional[Any] = ..., **connection_pool_kw: Any): ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any): ...
    def clear(self) -> None: ...
    def connection_from_host(self, host: Any, port: Optional[Any] = ..., scheme: str = ...): ...
    def connection_from_url(self, url: Any): ...
    def urlopen(self, method: Any, url: Any, redirect: bool = ..., **kw: Any): ...

class ProxyManager(PoolManager):
    proxy: Any = ...
    proxy_headers: Any = ...
    def __init__(self, proxy_url: Any, num_pools: int = ..., headers: Optional[Any] = ..., proxy_headers: Optional[Any] = ..., **connection_pool_kw: Any) -> None: ...
    def connection_from_host(self, host: Any, port: Optional[Any] = ..., scheme: str = ...): ...
    def urlopen(self, method: Any, url: Any, redirect: bool = ..., **kw: Any): ...

def proxy_from_url(url: Any, **kw: Any): ...
