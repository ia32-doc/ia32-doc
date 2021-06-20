from future.utils import with_metaclass
from utils.ia32_struct import *
from utils.ia32_bit_field import *


__doc__ = """
@brief IA32_FIXED_CTR(n)

Fixed-Function Performance Counter n.
"""


IA32_FIXED_CTR0 = 0x309


IA32_FIXED_CTR1 = 0x30a


IA32_FIXED_CTR2 = 0x30b


IA32_PERF_CAPABILITIES = 0x345


IA32_FIXED_CTR_CTRL = 0x38d


IA32_PERF_GLOBAL_STATUS = 0x38e


IA32_PERF_GLOBAL_CTRL = 0x38f


IA32_PERF_GLOBAL_STATUS_RESET = 0x390


IA32_PERF_GLOBAL_STATUS_SET = 0x391


IA32_PERF_GLOBAL_INUSE = 0x392


IA32_PEBS_ENABLE = 0x3f1


