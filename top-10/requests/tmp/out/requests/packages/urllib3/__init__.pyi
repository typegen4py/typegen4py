import logging
from .connectionpool import HTTPConnectionPool as HTTPConnectionPool, HTTPSConnectionPool as HTTPSConnectionPool, connection_from_url as connection_from_url
from .filepost import encode_multipart_formdata as encode_multipart_formdata
from .poolmanager import PoolManager as PoolManager, ProxyManager as ProxyManager, proxy_from_url as proxy_from_url
from .response import HTTPResponse as HTTPResponse
from .util.request import make_headers as make_headers
from .util.retry import Retry as Retry
from .util.timeout import Timeout as Timeout
from .util.url import get_host as get_host
from typing import Any

class NullHandler(logging.Handler):
    def emit(self, record: Any) -> None: ...

def add_stderr_logger(level: Any = ...): ...
def disable_warnings(category: Any = ...) -> None: ...
