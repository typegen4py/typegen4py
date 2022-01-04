from .chardistribution import EUCTWDistributionAnalysis as EUCTWDistributionAnalysis
from .codingstatemachine import CodingStateMachine as CodingStateMachine
from .mbcharsetprober import MultiByteCharSetProber as MultiByteCharSetProber
from .mbcssm import EUCTWSMModel as EUCTWSMModel

class EUCTWProber(MultiByteCharSetProber):
    def __init__(self) -> None: ...
    def get_charset_name(self): ...
