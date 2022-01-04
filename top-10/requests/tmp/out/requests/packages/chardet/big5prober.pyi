from .chardistribution import Big5DistributionAnalysis as Big5DistributionAnalysis
from .codingstatemachine import CodingStateMachine as CodingStateMachine
from .mbcharsetprober import MultiByteCharSetProber as MultiByteCharSetProber
from .mbcssm import Big5SMModel as Big5SMModel

class Big5Prober(MultiByteCharSetProber):
    def __init__(self) -> None: ...
    def get_charset_name(self): ...
