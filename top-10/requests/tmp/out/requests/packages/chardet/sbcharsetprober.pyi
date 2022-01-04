from . import constants as constants
from .charsetprober import CharSetProber as CharSetProber
from .compat import wrap_ord as wrap_ord
from typing import Any, Optional

SAMPLE_SIZE: int
SB_ENOUGH_REL_THRESHOLD: int
POSITIVE_SHORTCUT_THRESHOLD: float
NEGATIVE_SHORTCUT_THRESHOLD: float
SYMBOL_CAT_ORDER: int
NUMBER_OF_SEQ_CAT: int
POSITIVE_CAT: Any

class SingleByteCharSetProber(CharSetProber):
    def __init__(self, model: Any, reversed: bool = ..., nameProber: Optional[Any] = ...) -> None: ...
    def reset(self) -> None: ...
    def get_charset_name(self): ...
    def feed(self, aBuf: Any): ...
    def get_confidence(self): ...
