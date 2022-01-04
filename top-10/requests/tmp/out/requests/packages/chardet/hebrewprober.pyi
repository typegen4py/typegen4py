from .charsetprober import CharSetProber as CharSetProber
from .compat import wrap_ord as wrap_ord
from .constants import eDetecting as eDetecting, eNotMe as eNotMe
from typing import Any

FINAL_KAF: int
NORMAL_KAF: int
FINAL_MEM: int
NORMAL_MEM: int
FINAL_NUN: int
NORMAL_NUN: int
FINAL_PE: int
NORMAL_PE: int
FINAL_TSADI: int
NORMAL_TSADI: int
MIN_FINAL_CHAR_DISTANCE: int
MIN_MODEL_DISTANCE: float
VISUAL_HEBREW_NAME: str
LOGICAL_HEBREW_NAME: str

class HebrewProber(CharSetProber):
    def __init__(self) -> None: ...
    def reset(self) -> None: ...
    def set_model_probers(self, logicalProber: Any, visualProber: Any) -> None: ...
    def is_final(self, c: Any): ...
    def is_non_final(self, c: Any): ...
    def feed(self, aBuf: Any): ...
    def get_charset_name(self): ...
    def get_state(self): ...
