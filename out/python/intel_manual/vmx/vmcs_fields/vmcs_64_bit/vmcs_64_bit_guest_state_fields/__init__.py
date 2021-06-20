from future.utils import with_metaclass
from utils.struct import *
from utils.bit_field import *


__doc__ = """
@brief 64-Bit Guest-State Fields

64-Bit Guest-State Fields.
"""


VMCS_GUEST_VMCS_LINK_PTR = 0x2800


VMCS_GUEST_DEBUGCTL = 0x2802


VMCS_GUEST_PAT = 0x2804


VMCS_GUEST_EFER = 0x2806


VMCS_GUEST_PERF_GLOBAL_CTRL = 0x2808


VMCS_GUEST_PDPTE0 = 0x280a


VMCS_GUEST_PDPTE1 = 0x280c


VMCS_GUEST_PDPTE2 = 0x280e


VMCS_GUEST_PDPTE3 = 0x2810


VMCS_GUEST_BNDCFGS = 0x2812


VMCS_GUEST_RTIT_CTL = 0x2814


