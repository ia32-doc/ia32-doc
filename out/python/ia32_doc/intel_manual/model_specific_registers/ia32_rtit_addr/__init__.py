from future.utils import with_metaclass
from utils.ia32_struct import *
from utils.ia32_bit_field import *


__doc__ = """
@brief IA32_RTIT_ADDR(x)

The role of the IA32_RTIT_ADDRn_A/B register pairs, for each n, is determined by the corresponding ADDRn_CFG
fields in IA32_RTIT_CTL. The number of these register pairs is enumerated by
CPUID.(EAX=14H, ECX=1):EAX.RANGECNT[2:0].

@see Vol3C[35.2.7.2(IA32_RTIT_CTL MSR)]
"""


