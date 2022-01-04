from .big5prober import Big5Prober as Big5Prober
from .charsetgroupprober import CharSetGroupProber as CharSetGroupProber
from .cp949prober import CP949Prober as CP949Prober
from .eucjpprober import EUCJPProber as EUCJPProber
from .euckrprober import EUCKRProber as EUCKRProber
from .euctwprober import EUCTWProber as EUCTWProber
from .gb2312prober import GB2312Prober as GB2312Prober
from .sjisprober import SJISProber as SJISProber
from .utf8prober import UTF8Prober as UTF8Prober

class MBCSGroupProber(CharSetGroupProber):
    def __init__(self) -> None: ...
