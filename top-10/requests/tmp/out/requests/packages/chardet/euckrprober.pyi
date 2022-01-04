from .chardistribution import EUCKRDistributionAnalysis as EUCKRDistributionAnalysis
from .codingstatemachine import CodingStateMachine as CodingStateMachine
from .mbcharsetprober import MultiByteCharSetProber as MultiByteCharSetProber
from .mbcssm import EUCKRSMModel as EUCKRSMModel

class EUCKRProber(MultiByteCharSetProber):
    def __init__(self) -> None: ...
    def get_charset_name(self): ...
