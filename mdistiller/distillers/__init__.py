from ._base import Vanilla
from .KD import KD
from .MTKD import MTKD
from .MLKD import MLKD
from .MTMLKD import MTMLKD
from .AT import AT
from .OFD import OFD
from .RKD import RKD
from .KDSVD import KDSVD
from .CRD import CRD
from .NST import NST
from .PKT import PKT
from .SP import SP
from .Sonly import Sonly
from .VID import VID
from .ReviewKD import ReviewKD
from .DKD import DKD
from .MTDKD import MTDKD
from .DoubleMLKD import DoubleMLKD
from .DoubleKD import DoubleKD
from .DoubleDKD import DoubleDKD

distiller_dict = {
    "NONE": Vanilla,
    "DoubleKD": DoubleKD,
    "DoubleMLKD": DoubleMLKD,
    "KD": KD,
    "MTKD": MTKD,
    "MTDKD": MTDKD,
    "MLKD": MLKD,
    "MTMLKD": MTMLKD,
    "AT": AT,
    "OFD": OFD,
    "RKD": RKD,
    "KDSVD": KDSVD,
    "CRD": CRD,
    "NST": NST,
    "PKT": PKT,
    "SP": SP,
    "Sonly": Sonly,
    "VID": VID,
    "REVIEWKD": ReviewKD,
    "DKD": DKD,
    "DoubleDKD": DoubleDKD,
}
