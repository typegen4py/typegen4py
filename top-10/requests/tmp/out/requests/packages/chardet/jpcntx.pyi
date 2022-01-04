from .compat import wrap_ord as wrap_ord
from typing import Any

NUM_OF_CATEGORY: int
DONT_KNOW: int
ENOUGH_REL_THRESHOLD: int
MAX_REL_THRESHOLD: int
MINIMUM_DATA_THRESHOLD: int
jp2CharContext: Any

class JapaneseContextAnalysis:
    def __init__(self) -> None: ...
    def reset(self) -> None: ...
    def feed(self, aBuf: Any, aLen: Any) -> None: ...
    def got_enough_data(self): ...
    def get_confidence(self): ...
    def get_order(self, aBuf: Any): ...

class SJISContextAnalysis(JapaneseContextAnalysis):
    charset_name: str = ...
    def __init__(self) -> None: ...
    def get_charset_name(self): ...
    def get_order(self, aBuf: Any): ...

class EUCJPContextAnalysis(JapaneseContextAnalysis):
    def get_order(self, aBuf: Any): ...
