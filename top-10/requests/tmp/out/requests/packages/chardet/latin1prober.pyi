from .charsetprober import CharSetProber as CharSetProber
from .compat import wrap_ord as wrap_ord
from .constants import eNotMe as eNotMe
from typing import Any

FREQ_CAT_NUM: int
UDF: int
OTH: int
ASC: int
ASS: int
ACV: int
ACO: int
ASV: int
ASO: int
CLASS_NUM: int
Latin1_CharToClass: Any
Latin1ClassModel: Any

class Latin1Prober(CharSetProber):
    def __init__(self) -> None: ...
    def reset(self) -> None: ...
    def get_charset_name(self): ...
    def feed(self, aBuf: Any): ...
    def get_confidence(self): ...
