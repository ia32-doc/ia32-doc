from future.utils import with_metaclass
from utils.struct import *
from utils.bit_field import *


__doc__ = """
@brief IA32_P5_MC_(x)

When machine-check exceptions are enabled for the Pentium processor (MCE flag is set in control register CR4),
the machine-check exception handler uses the RDMSR instruction to read the error type from the P5_MC_TYPE
register and the machine check address from the P5_MC_ADDR register. The handler then normally reports these
register values to the system console before aborting execution.
"""


IA32_P5_MC_ADDR = 0x0


IA32_P5_MC_TYPE = 0x1


IA32_MONITOR_FILTER_SIZE = 0x6


IA32_TIME_STAMP_COUNTER = 0x10


IA32_PLATFORM_ID = 0x17


IA32_APIC_BASE = 0x1b


IA32_FEATURE_CONTROL = 0x3a


IA32_TSC_ADJUST = 0x3b


IA32_BIOS_UPDT_TRIG = 0x79


IA32_BIOS_SIGN_ID = 0x8b


