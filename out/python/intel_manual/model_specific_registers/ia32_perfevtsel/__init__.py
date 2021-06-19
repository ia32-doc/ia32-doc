from future.utils import with_metaclass
from utils.bit_field import *


__doc__ = """
Performance Event Select Register n.
"""
IA32_PERFEVTSEL0 = 0x186

IA32_PERFEVTSEL1 = 0x187

IA32_PERFEVTSEL2 = 0x188

IA32_PERFEVTSEL3 = 0x189

class Ia32PerfevtselRegister(with_metaclass(BitFieldMeta, BitField)):
    """"""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=8)


    
    EVENT_SELECT = BitFieldMember(
        "EVENT_SELECT",
        """
        Selects a performance event logic unit:
        Selects a performance event logic unit.
        """,
        0,
        8
    )

    
    U_MASK = BitFieldMember(
        "U_MASK",
        """
        Qualifies the microarchitectural condition to detect on the selected event logic:
        Qualifies the microarchitectural condition to detect on the selected event logic.
        """,
        8,
        8
    )

    
    USR = BitFieldMember(
        "USR",
        """
        Counts while in privilege level is not ring 0:
        Counts while in privilege level is not ring 0.
        """,
        16,
        1
    )

    
    OS = BitFieldMember(
        "OS",
        """
        Counts while in privilege level is ring 0:
        Counts while in privilege level is ring 0.
        """,
        17,
        1
    )

    
    EDGE = BitFieldMember(
        "EDGE",
        """
        Enables edge detection if set:
        Enables edge detection if set.
        """,
        18,
        1
    )

    
    PC = BitFieldMember(
        "PC",
        """
        Enables pin control:
        Enables pin control.
        """,
        19,
        1
    )

    
    INTR = BitFieldMember(
        "INTR",
        """
        Enables interrupt on counter overflow:
        Enables interrupt on counter overflow.
        """,
        20,
        1
    )

    
    ANY_THREAD = BitFieldMember(
        "ANY_THREAD",
        """
        When set to 1, it enables counting the associated event conditions
occurring across all logical processors sharing a processor core. When set to 0, the
counter only increments the associated event conditions occurring in the logical
processor which programmed the MSR:
        When set to 1, it enables counting the associated event conditions
occurring across all logical processors sharing a processor core. When set to 0, the
counter only increments the associated event conditions occurring in the logical
processor which programmed the MSR.
        """,
        21,
        1
    )

    
    EN = BitFieldMember(
        "EN",
        """
        Enables the corresponding performance counter to commence counting when this
bit is set:
        Enables the corresponding performance counter to commence counting when this
bit is set.
        """,
        22,
        1
    )

    
    INV = BitFieldMember(
        "INV",
        """
        Invert the CMASK:
        Invert the CMASK.
        """,
        23,
        1
    )

    
    CMASK = BitFieldMember(
        "CMASK",
        """
        When CMASK is not zero, the corresponding performance counter
increments each cycle if the event count is greater than or equal to the CMASK:
        When CMASK is not zero, the corresponding performance counter
increments each cycle if the event count is greater than or equal to the CMASK.
        """,
        24,
        8
    )

    

IA32_PERF_STATUS = 0x198

IA32_PERF_CTL = 0x199

IA32_CLOCK_MODULATION = 0x19a

IA32_THERM_INTERRUPT = 0x19b

IA32_THERM_STATUS = 0x19c

IA32_MISC_ENABLE = 0x1a0

IA32_ENERGY_PERF_BIAS = 0x1b0

IA32_PACKAGE_THERM_STATUS = 0x1b1

IA32_PACKAGE_THERM_INTERRUPT = 0x1b2

IA32_DEBUGCTL = 0x1d9

IA32_SMRR_PHYSBASE = 0x1f2

IA32_SMRR_PHYSMASK = 0x1f3

IA32_PLATFORM_DCA_CAP = 0x1f8

IA32_CPU_DCA_CAP = 0x1f9

IA32_DCA_0_CAP = 0x1fa

