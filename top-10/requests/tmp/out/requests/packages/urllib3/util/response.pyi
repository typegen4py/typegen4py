from ..exceptions import HeaderParsingError as HeaderParsingError
from typing import Any

def is_fp_closed(obj: Any): ...
def assert_header_parsing(headers: Any) -> None: ...
def is_response_to_head(response: Any): ...
