from future.utils import with_metaclass
from ia32_python.utils.ia32_struct import *
from ia32_python.utils.ia32_bit_field import *


__doc__ = """
@brief IA32_PERFEVTSEL(n)

Performance Event Select Register n.
"""


IA32_PERFEVTSEL0 = 0x186


IA32_PERFEVTSEL1 = 0x187


IA32_PERFEVTSEL2 = 0x188


IA32_PERFEVTSEL3 = 0x189


class Ia32PerfevtselRegister(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
    """
    
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super(Ia32PerfevtselRegister, self).__init__(value, byte_offset, byte_width, max_bytes=8)



    EVENT_SELECT = Ia32BitFieldMember(
        "EVENT_SELECT",
        """
        @brief Selects a performance event logic unit

Selects a performance event logic unit.
        """,

        0,
        8

    )


    U_MASK = Ia32BitFieldMember(
        "U_MASK",
        """
        @brief Qualifies the microarchitectural condition to detect on the selected event logic

Qualifies the microarchitectural condition to detect on the selected event logic.
        """,

        8,
        8

    )


    USR = Ia32BitFieldMember(
        "USR",
        """
        @brief Counts while in privilege level is not ring 0

Counts while in privilege level is not ring 0.
        """,

        16,
        1

    )


    OS = Ia32BitFieldMember(
        "OS",
        """
        @brief Counts while in privilege level is ring 0

Counts while in privilege level is ring 0.
        """,

        17,
        1

    )


    EDGE = Ia32BitFieldMember(
        "EDGE",
        """
        @brief Enables edge detection if set

Enables edge detection if set.
        """,

        18,
        1

    )


    PC = Ia32BitFieldMember(
        "PC",
        """
        @brief Enables pin control

Enables pin control.
        """,

        19,
        1

    )


    INTR = Ia32BitFieldMember(
        "INTR",
        """
        @brief Enables interrupt on counter overflow

Enables interrupt on counter overflow.
        """,

        20,
        1

    )


    ANY_THREAD = Ia32BitFieldMember(
        "ANY_THREAD",
        """
        @brief When set to 1, it enables counting the associated event conditions
occurring across all logical processors sharing a processor core. When set to 0, the
counter only increments the associated event conditions occurring in the logical
processor which programmed the MSR

When set to 1, it enables counting the associated event conditions
occurring across all logical processors sharing a processor core. When set to 0, the
counter only increments the associated event conditions occurring in the logical
processor which programmed the MSR.
        """,

        21,
        1

    )


    EN = Ia32BitFieldMember(
        "EN",
        """
        @brief Enables the corresponding performance counter to commence counting when this
bit is set

Enables the corresponding performance counter to commence counting when this
bit is set.
        """,

        22,
        1

    )


    INV = Ia32BitFieldMember(
        "INV",
        """
        @brief Invert the CMASK

Invert the CMASK.
        """,

        23,
        1

    )


    CMASK = Ia32BitFieldMember(
        "CMASK",
        """
        @brief When CMASK is not zero, the corresponding performance counter
increments each cycle if the event count is greater than or equal to the CMASK

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


