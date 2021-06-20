from future.utils import with_metaclass
from ia32_python.utils.ia32_struct import *
from ia32_python.utils.ia32_bit_field import *


__doc__ = """
@brief Advanced Programmable Interrupt Controller (APIC)

Software interacts with the local APIC by reading
and writing its registers. APIC registers are memory-mapped to a 4-KByte region of the processors physical
address space with an initial starting address of FEE00000H. For correct APIC operation, this address space must
be mapped to an area of memory that has been designated as strong uncacheable (UC).
"""


APIC_BASE = 0xfee00000


APIC_ID = 0x20


APIC_VERSION = 0x30


APIC_TPR = 0x80


APIC_APR = 0x90


APIC_PPR = 0xa0


APIC_EOI = 0xb0


APIC_REMOTE_READ = 0xc0


APIC_LOGICAL_DESTINATION = 0xd0


APIC_DESTINATION_FORMAT = 0xe0


APIC_SIV = 0xf0


APIC_ISR_31_0 = 0x100


APIC_ISR_63_32 = 0x110


APIC_ISR_95_64 = 0x120


APIC_ISR_127_96 = 0x130


APIC_ISR_159_128 = 0x140


APIC_ISR_191_160 = 0x150


APIC_ISR_223_192 = 0x160


APIC_ISR_255_224 = 0x170


APIC_TMR_31_0 = 0x180


APIC_TMR_63_32 = 0x190


APIC_TMR_95_64 = 0x1a0


APIC_TMR_127_96 = 0x1b0


APIC_TMR_159_128 = 0x1c0


APIC_TMR_191_160 = 0x1d0


APIC_TMR_223_192 = 0x1e0


APIC_TMR_255_224 = 0x1f0


APIC_IRR_31_0 = 0x200


APIC_IRR_63_32 = 0x210


APIC_IRR_95_64 = 0x220


APIC_IRR_127_96 = 0x230


APIC_IRR_159_128 = 0x240


APIC_IRR_191_160 = 0x250


APIC_IRR_223_192 = 0x260


APIC_IRR_255_224 = 0x270


APIC_ERROR_STATUS = 0x280


APIC_CMCI = 0x2f0


APIC_ICR_0_31 = 0x300


APIC_ICR_32_63 = 0x310


APIC_LVT_TIMER = 0x320


APIC_LVT_THERMAL_SENSOR = 0x330


APIC_LVT_PERFORMANCE_MONITORING_COUNTERS = 0x340


APIC_LVT_LINT0 = 0x350


APIC_LVT_LINT1 = 0x360


APIC_LVT_ERROR = 0x370


APIC_INITIAL_COUNT = 0x380


APIC_CURRENT_COUNT = 0x390


APIC_DIVIDE_CONFIGURATION = 0x3e0


class Eflags(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
    """
    The 32-bit EFLAGS register contains a group of status flags, a control flag, and a group of system flags.
The status flags (bits 0, 2, 4, 6, 7, and 11) of the EFLAGS register indicate the results of arithmetic instructions,
such as the ADD, SUB, MUL, and DIV instructions.

The system flags and IOPL field in the EFLAGS register control operating-system or executive operations.
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super(Eflags, self).__init__(value, byte_offset, byte_width, max_bytes=4)



    CF = Ia32BitFieldMember(
        "CF",
        """
        @brief Carry flag

Set if an arithmetic operation generates a carry or a borrow out of the mostsignificant
bit of the result; cleared otherwise. This flag indicates an overflow condition for
unsigned-integer arithmetic. It is also used in multiple-precision arithmetic.
        """,

        0,
        1

    )


    RA1 = Ia32BitFieldMember(
        "RA1",
        """
        @brief Reserved - always 1

Reserved - always 1
        """,

        1,
        1

    )


    PF = Ia32BitFieldMember(
        "PF",
        """
        @brief Parity flag

Set if the least-significant byte of the result contains an even number of 1 bits;
cleared otherwise.
        """,

        2,
        1

    )


    AF = Ia32BitFieldMember(
        "AF",
        """
        @brief Auxiliary Carry flag

Set if an arithmetic operation generates a carry or a borrow out of bit
3 of the result; cleared otherwise. This flag is used in binary-coded decimal (BCD) arithmetic.
        """,

        4,
        1

    )


    ZF = Ia32BitFieldMember(
        "ZF",
        """
        @brief Zero flag

Set if the result is zero; cleared otherwise.
        """,

        6,
        1

    )


    SF = Ia32BitFieldMember(
        "SF",
        """
        @brief Sign flag

Set equal to the most-significant bit of the result, which is the sign bit of a signed
integer. (0 indicates a positive value and 1 indicates a negative value.)
        """,

        7,
        1

    )


    TF = Ia32BitFieldMember(
        "TF",
        """
        @brief Trap flag

Set to enable single-step mode for debugging; clear to disable single-step mode.
        """,

        8,
        1

    )


    IF = Ia32BitFieldMember(
        "IF",
        """
        @brief Interrupt enable flag

Controls the response of the processor to maskable interrupt
requests. Set to respond to maskable interrupts; cleared to inhibit maskable interrupts.
        """,

        9,
        1

    )


    DF = Ia32BitFieldMember(
        "DF",
        """
        @brief Direction flag

Controls string instructions (MOVS, CMPS, SCAS, LODS, and STOS). Setting the DF flag
causes the string instructions to auto-decrement (to process strings from high addresses to low addresses).
Clearing the DF flag causes the string instructions to auto-increment (process strings from low addresses
to high addresses).
        """,

        10,
        1

    )


    OF = Ia32BitFieldMember(
        "OF",
        """
        @brief Overflow flag

Set if the integer result is too large a positive number or too small a negative
number (excluding the sign-bit) to fit in the destination operand; cleared otherwise. This flag
indicates an overflow condition for signed-integer (twos complement) arithmetic.
        """,

        11,
        1

    )


    IOPL = Ia32BitFieldMember(
        "IOPL",
        """
        @brief I/O privilege level field

Indicates the I/O privilege level of the currently running program
or task. The current privilege level (CPL) of the currently running program or task must be less
than or equal to the I/O privilege level to access the I/O address space. The POPF and IRET
instructions can modify this field only when operating at a CPL of 0.
        """,

        12,
        2

    )


    NT = Ia32BitFieldMember(
        "NT",
        """
        @brief Nested task flag

Controls the chaining of interrupted and called tasks. Set when the
current task is linked to the previously executed task; cleared when the current task is not
linked to another task.
        """,

        14,
        1

    )


    RF = Ia32BitFieldMember(
        "RF",
        """
        @brief Resume flag

Controls the processors response to debug exceptions.
        """,

        16,
        1

    )


    VM = Ia32BitFieldMember(
        "VM",
        """
        @brief Virtual-8086 mode flag

Set to enable virtual-8086 mode; clear to return to protected
mode without virtual-8086 mode semantics.
        """,

        17,
        1

    )


    AC = Ia32BitFieldMember(
        "AC",
        """
        @brief Alignment check (or access control) flag

If the AM bit is set in the CR0 register, alignment
checking of user-mode data accesses is enabled if and only if this flag is 1.
If the SMAP bit is set in the CR4 register, explicit supervisor-mode data accesses to user-mode
pages are allowed if and only if this bit is 1.

@see Vol3A[4.6(ACCESS RIGHTS)]
        """,

        18,
        1

    )


    VIF = Ia32BitFieldMember(
        "VIF",
        """
        @brief Virtual interrupt flag

Virtual image of the IF flag. Used in conjunction with the VIP flag.
(To use this flag and the VIP flag the virtual mode extensions are enabled by setting the VME
flag in control register CR4.)
        """,

        19,
        1

    )


    VIP = Ia32BitFieldMember(
        "VIP",
        """
        @brief Virtual interrupt pending flag

Set to indicate that an interrupt is pending; clear when no
interrupt is pending. (Software sets and clears this flag; the processor only reads it.) Used in
conjunction with the VIF flag.
        """,

        20,
        1

    )


    IF = Ia32BitFieldMember(
        "IF",
        """
        @brief Identification flag

The ability of a program to set or clear this flag indicates support for
the CPUID instruction.
        """,

        21,
        1

    )


class Rflags(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
    """
    The 64-bit RFLAGS register contains a group of status flags, a control flag, and a group of system flags in 64-bit mode.

The upper 32 bits of RFLAGS register is reserved. The lower 32 bits of RFLAGS is the same as EFLAGS.

@see EFLAGS
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super(Rflags, self).__init__(value, byte_offset, byte_width, max_bytes=8)



    CF = Ia32BitFieldMember(
        "CF",
        """
        @brief Carry flag

See the description in EFLAGS.
        """,

        0,
        1

    )


    RA1 = Ia32BitFieldMember(
        "RA1",
        """
        @brief Reserved - always 1

Reserved - always 1
        """,

        1,
        1

    )


    PF = Ia32BitFieldMember(
        "PF",
        """
        @brief Parity flag

See the description in EFLAGS.
        """,

        2,
        1

    )


    AF = Ia32BitFieldMember(
        "AF",
        """
        @brief Auxiliary Carry flag

See the description in EFLAGS.
        """,

        4,
        1

    )


    ZF = Ia32BitFieldMember(
        "ZF",
        """
        @brief Zero flag

See the description in EFLAGS.
        """,

        6,
        1

    )


    SF = Ia32BitFieldMember(
        "SF",
        """
        @brief Sign flag

See the description in EFLAGS.
        """,

        7,
        1

    )


    TF = Ia32BitFieldMember(
        "TF",
        """
        @brief Trap flag

See the description in EFLAGS.
        """,

        8,
        1

    )


    IF = Ia32BitFieldMember(
        "IF",
        """
        @brief Interrupt enable flag

See the description in EFLAGS.
        """,

        9,
        1

    )


    DF = Ia32BitFieldMember(
        "DF",
        """
        @brief Direction flag

See the description in EFLAGS.
        """,

        10,
        1

    )


    OF = Ia32BitFieldMember(
        "OF",
        """
        @brief Overflow flag

See the description in EFLAGS.
        """,

        11,
        1

    )


    IOPL = Ia32BitFieldMember(
        "IOPL",
        """
        @brief I/O privilege level field

See the description in EFLAGS.
        """,

        12,
        2

    )


    NT = Ia32BitFieldMember(
        "NT",
        """
        @brief Nested task flag

See the description in EFLAGS.
        """,

        14,
        1

    )


    RF = Ia32BitFieldMember(
        "RF",
        """
        @brief Resume flag

See the description in EFLAGS.
        """,

        16,
        1

    )


    VM = Ia32BitFieldMember(
        "VM",
        """
        @brief Virtual-8086 mode flag

See the description in EFLAGS.
        """,

        17,
        1

    )


    AC = Ia32BitFieldMember(
        "AC",
        """
        @brief Alignment check (or access control) flag

See the description in EFLAGS.

@see Vol3A[4.6(ACCESS RIGHTS)]
        """,

        18,
        1

    )


    VIF = Ia32BitFieldMember(
        "VIF",
        """
        @brief Virtual interrupt flag

See the description in EFLAGS.
        """,

        19,
        1

    )


    VIP = Ia32BitFieldMember(
        "VIP",
        """
        @brief Virtual interrupt pending flag

See the description in EFLAGS.
        """,

        20,
        1

    )


    IF = Ia32BitFieldMember(
        "IF",
        """
        @brief Identification flag

See the description in EFLAGS.
        """,

        21,
        1

    )


