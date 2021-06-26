from future.utils import with_metaclass
from ia32_python.utils.ia32_struct import *
from ia32_python.utils.ia32_enum import *
from ia32_python.utils.ia32_bit_field import *


__doc__ = """
@brief IA32_PMC(n)

General Performance Counters.
"""


IA32_PMC0 = 0xc1


IA32_PMC1 = 0xc2


IA32_PMC2 = 0xc3


IA32_PMC3 = 0xc4


IA32_PMC4 = 0xc5


IA32_PMC5 = 0xc6


IA32_PMC6 = 0xc7


IA32_PMC7 = 0xc8


IA32_MPERF = 0xe7


IA32_APERF = 0xe8


IA32_MTRRCAP = 0xfe


IA32_SYSENTER_CS = 0x174


IA32_SYSENTER_ESP = 0x175


IA32_SYSENTER_EIP = 0x176


IA32_MCG_CAP = 0x179


IA32_MCG_STATUS = 0x17a


IA32_MCG_CTL = 0x17b


