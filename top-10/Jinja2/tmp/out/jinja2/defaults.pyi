from ._compat import range_type as range_type
from .utils import Cycler as Cycler, Joiner as Joiner, Namespace as Namespace, generate_lorem_ipsum as generate_lorem_ipsum
from typing import Any

BLOCK_START_STRING: str
BLOCK_END_STRING: str
VARIABLE_START_STRING: str
VARIABLE_END_STRING: str
COMMENT_START_STRING: str
COMMENT_END_STRING: str
LINE_STATEMENT_PREFIX: Any
LINE_COMMENT_PREFIX: Any
TRIM_BLOCKS: bool
LSTRIP_BLOCKS: bool
NEWLINE_SEQUENCE: str
KEEP_TRAILING_NEWLINE: bool
DEFAULT_NAMESPACE: Any
DEFAULT_POLICIES: Any
