from future.utils import with_metaclass
from utils.struct import *
from utils.bit_field import *


__doc__ = """
@brief 32-Bit Read-Only Data Fields

32-Bit Read-Only Data Fields.
"""


VMCS_VM_INSTR_ERROR = 0x4400


VMCS_EXIT_REASON = 0x4402


VMCS_EXIT_INTERRUPTION_INFO = 0x4404


VMCS_EXIT_INTERRUPTION_ERROR_CODE = 0x4406


VMCS_IDT_VECTORING_INFO = 0x4408


VMCS_IDT_VECTORING_ERROR_CODE = 0x440a


VMCS_EXIT_INSTR_LENGTH = 0x440c


VMCS_EXIT_INSTR_INFO = 0x440e


