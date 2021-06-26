from future.utils import with_metaclass
from ia32_python.utils.ia32_struct import *
from ia32_python.utils.ia32_enum import *
from ia32_python.utils.ia32_bit_field import *


__doc__ = """
@brief IA32_MTRR_FIX4K(x)

IA32_MTRR_FIX4K(x).
"""


IA32_MTRR_FIX4K_BASE = 0xc0000


IA32_MTRR_FIX4K_SIZE = 0x1000


IA32_MTRR_FIX4K_C0000 = 0x268


IA32_MTRR_FIX4K_C8000 = 0x269


IA32_MTRR_FIX4K_D0000 = 0x26a


IA32_MTRR_FIX4K_D8000 = 0x26b


IA32_MTRR_FIX4K_E0000 = 0x26c


IA32_MTRR_FIX4K_E8000 = 0x26d


IA32_MTRR_FIX4K_F0000 = 0x26e


IA32_MTRR_FIX4K_F8000 = 0x26f


IA32_MTRR_FIX_COUNT = ((1 + 2 + 8) * 8)


IA32_MTRR_VARIABLE_COUNT = 0xff


IA32_MTRR_COUNT = (IA32_MTRR_FIX_COUNT + IA32_MTRR_VARIABLE_COUNT)


IA32_PAT = 0x277


