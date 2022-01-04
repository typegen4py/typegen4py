from .chardistribution import GB2312DistributionAnalysis as GB2312DistributionAnalysis
from .codingstatemachine import CodingStateMachine as CodingStateMachine
from .mbcharsetprober import MultiByteCharSetProber as MultiByteCharSetProber
from .mbcssm import GB2312SMModel as GB2312SMModel

class GB2312Prober(MultiByteCharSetProber):
    def __init__(self) -> None: ...
    def get_charset_name(self): ...
