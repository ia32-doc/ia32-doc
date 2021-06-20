from future.utils import with_metaclass
from utils.ia32_struct import *
from utils.ia32_bit_field import *


__doc__ = """
@brief EPT Table level numbers

EPT Table level numbers.
"""


EPT_LEVEL_PML4E = 0x3


EPT_LEVEL_PDPTE = 0x2


EPT_LEVEL_PDE = 0x1


EPT_LEVEL_PTE = 0x0


