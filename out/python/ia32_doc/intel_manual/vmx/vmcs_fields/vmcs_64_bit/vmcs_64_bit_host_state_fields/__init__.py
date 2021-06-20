from future.utils import with_metaclass
from utils.ia32_struct import *
from utils.ia32_bit_field import *


__doc__ = """
@brief 64-Bit Host-State Fields

64-Bit Host-State Fields.
"""


VMCS_HOST_PAT = 0x2c00


VMCS_HOST_EFER = 0x2c02


VMCS_HOST_PERF_GLOBAL_CTRL = 0x2c04


