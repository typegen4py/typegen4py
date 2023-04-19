from . import constants as constants
from .escprober import EscCharSetProber as EscCharSetProber
from .latin1prober import Latin1Prober as Latin1Prober
from .mbcsgroupprober import MBCSGroupProber as MBCSGroupProber
from .sbcsgroupprober import SBCSGroupProber as SBCSGroupProber
from typing import Any

MINIMUM_THRESHOLD: float
ePureAscii: int
eEscAscii: int
eHighbyte: int

class UniversalDetector:
    def __init__(self) -> None: ...
    result: Any = ...
    done: bool = ...
    def reset(self) -> None: ...
    def feed(self, aBuf: Any) -> None: ...
    def close(self): ...