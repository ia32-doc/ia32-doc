from future.utils import with_metaclass
from utils.struct import *
from utils.bit_field import *


__doc__ = """
@brief 16-Bit Guest-State Fields

16-Bit Guest-State Fields.
"""


VMCS_GUEST_ES_SEL = 0x800


VMCS_GUEST_CS_SEL = 0x802


VMCS_GUEST_SS_SEL = 0x804


VMCS_GUEST_DS_SEL = 0x806


VMCS_GUEST_FS_SEL = 0x808


VMCS_GUEST_GS_SEL = 0x80a


VMCS_GUEST_LDTR_SEL = 0x80c


VMCS_GUEST_TR_SEL = 0x80e


VMCS_GUEST_INTR_STATUS = 0x810


VMCS_GUEST_PML_INDEX = 0x812


