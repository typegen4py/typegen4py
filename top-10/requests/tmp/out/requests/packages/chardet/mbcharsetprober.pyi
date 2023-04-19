from . import constants as constants
from .charsetprober import CharSetProber as CharSetProber
from typing import Any

class MultiByteCharSetProber(CharSetProber):
    def __init__(self) -> None: ...
    def reset(self) -> None: ...
    def get_charset_name(self) -> None: ...
    def feed(self, aBuf: Any): ...
    def get_confidence(self): ...