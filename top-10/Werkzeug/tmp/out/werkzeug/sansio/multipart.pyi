from ..datastructures import Headers as Headers
from ..exceptions import RequestEntityTooLarge as RequestEntityTooLarge
from ..http import parse_options_header as parse_options_header
from enum import Enum
from typing import Any, Optional

class Event: ...

class Preamble(Event):
    data: bytes
    def __init__(self, data: Any) -> None: ...

class Field(Event):
    name: str
    headers: Headers
    def __init__(self, name: Any, headers: Any) -> None: ...

class File(Event):
    name: str
    filename: str
    headers: Headers
    def __init__(self, name: Any, filename: Any, headers: Any) -> None: ...

class Data(Event):
    data: bytes
    more_data: bool
    def __init__(self, data: Any, more_data: Any) -> None: ...

class Epilogue(Event):
    data: bytes
    def __init__(self, data: Any) -> None: ...

class NeedData(Event): ...

NEED_DATA: Any

class State(Enum):
    PREAMBLE: Any = ...
    PART: Any = ...
    DATA: Any = ...
    EPILOGUE: Any = ...
    COMPLETE: Any = ...

LINE_BREAK: bytes
BLANK_LINE_RE: Any
LINE_BREAK_RE: Any
HEADER_CONTINUATION_RE: Any

class MultipartDecoder:
    buffer: Any = ...
    complete: bool = ...
    max_form_memory_size: Any = ...
    state: Any = ...
    boundary: Any = ...
    preamble_re: Any = ...
    boundary_re: Any = ...
    def __init__(self, boundary: bytes, max_form_memory_size: Optional[int]=...) -> None: ...
    def last_newline(self) -> int: ...
    def receive_data(self, data: Optional[bytes]) -> None: ...
    def next_event(self) -> Event: ...

class MultipartEncoder:
    boundary: Any = ...
    state: Any = ...
    def __init__(self, boundary: bytes) -> None: ...
    def send_event(self, event: Event) -> bytes: ...
