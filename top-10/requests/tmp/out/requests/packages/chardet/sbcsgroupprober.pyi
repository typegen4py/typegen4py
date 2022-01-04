from .charsetgroupprober import CharSetGroupProber as CharSetGroupProber
from .hebrewprober import HebrewProber as HebrewProber
from .langbulgarianmodel import Latin5BulgarianModel as Latin5BulgarianModel, Win1251BulgarianModel as Win1251BulgarianModel
from .langcyrillicmodel import Ibm855Model as Ibm855Model, Ibm866Model as Ibm866Model, Koi8rModel as Koi8rModel, Latin5CyrillicModel as Latin5CyrillicModel, MacCyrillicModel as MacCyrillicModel, Win1251CyrillicModel as Win1251CyrillicModel
from .langgreekmodel import Latin7GreekModel as Latin7GreekModel, Win1253GreekModel as Win1253GreekModel
from .langhebrewmodel import Win1255HebrewModel as Win1255HebrewModel
from .langhungarianmodel import Latin2HungarianModel as Latin2HungarianModel, Win1250HungarianModel as Win1250HungarianModel
from .langthaimodel import TIS620ThaiModel as TIS620ThaiModel
from .sbcharsetprober import SingleByteCharSetProber as SingleByteCharSetProber

class SBCSGroupProber(CharSetGroupProber):
    def __init__(self) -> None: ...
