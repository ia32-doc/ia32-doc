from future.utils import with_metaclass
from ia32_python.utils.ia32_struct import *
from ia32_python.utils.ia32_enum import *
from ia32_python.utils.ia32_bit_field import *


__doc__ = """
@brief Natural-Width Control Fields

Natural-Width Control Fields
"""


VMCS_CTRL_CR0_MASK = 0x6000


VMCS_CTRL_CR4_MASK = 0x6002


VMCS_CTRL_CR0_READ_SHADOW = 0x6004


VMCS_CTRL_CR4_READ_SHADOW = 0x6006


VMCS_CTRL_CR3_TARGET_VAL0 = 0x6008


VMCS_CTRL_CR3_TARGET_VAL1 = 0x600a


VMCS_CTRL_CR3_TARGET_VAL2 = 0x600c


VMCS_CTRL_CR3_TARGET_VAL3 = 0x600e


