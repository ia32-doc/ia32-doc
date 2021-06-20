from future.utils import with_metaclass
from utils.ia32_struct import *
from utils.ia32_bit_field import *


__doc__ = """
@brief Natural-Width Read-Only Data Fields

Natural-Width Read-Only Data Fields.
"""


VMCS_EXIT_QUALIFICATION = 0x6400


VMCS_IO_RCX = 0x6402


VMCS_IO_RSX = 0x6404


VMCS_IO_RDI = 0x6406


VMCS_IO_RIP = 0x6408


VMCS_EXIT_GUEST_LINEAR_ADDR = 0x640a


