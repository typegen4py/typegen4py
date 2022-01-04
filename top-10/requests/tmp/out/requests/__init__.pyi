import logging
from . import utils as utils
from .api import delete as delete, get as get, head as head, options as options, patch as patch, post as post, put as put, request as request
from .exceptions import ConnectTimeout as ConnectTimeout, ConnectionError as ConnectionError, HTTPError as HTTPError, ReadTimeout as ReadTimeout, RequestException as RequestException, Timeout as Timeout, TooManyRedirects as TooManyRedirects, URLRequired as URLRequired
from .models import PreparedRequest as PreparedRequest, Request as Request, Response as Response
from .sessions import Session as Session, session as session
from .status_codes import codes as codes
from typing import Any

__build__: int

class NullHandler(logging.Handler):
    def emit(self, record: Any) -> None: ...
