from future.utils import with_metaclass
from utils.struct import *
from utils.bit_field import *


__doc__ = """
@brief Debug registers

Eight debug registers control the debug
operation of the processor. These registers can be written to and read using the move to/from debug register form
of the MOV instruction. A debug register may be the source or destination operand for one of these instructions.

Debug registers are privileged resources; a MOV instruction that accesses these registers can only be executed in
real-address mode, in SMM or in protected mode at a CPL of 0. An attempt to read or write the debug registers
from any other privilege level generates a general-protection exception (\#GP).
The primary function of the debug registers is to set up and monitor from 1 to 4 breakpoints, numbered 0 though
3. For each breakpoint, the following information can be specified:

- The linear address where the breakpoint is to occur.

- The length of the breakpoint location: 1, 2, 4, or 8 bytes.

- The operation that must be performed at the address for a debug exception to be generated.

- Whether the breakpoint is enabled.

- Whether the breakpoint condition was present when the debug exception was generated.

@see Vol3B[17.2.4(Debug Control Register (DR7))]
"""


class Dr6(with_metaclass(BitFieldMeta, BitField)):
    """
    
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super().__init__(value, byte_offset, byte_width, max_bytes=8)



    BREAKPOINT_CONDITION = BitFieldMember(
        "BREAKPOINT_CONDITION",
        """
        @brief B0 through B3 (breakpoint condition detected) flags

Indicates (when set) that its
associated breakpoint condition was met when a debug exception was generated. These flags are set if the
condition described for each breakpoint by the LENn, and R/Wn flags in debug control register DR7 is true. They
may or may not be set if the breakpoint is not enabled by the Ln or the Gn flags in register DR7. Therefore on
a \#DB, a debug handler should check only those B0-B3 bits which correspond to an enabled breakpoint.
        """,

        0,
        4

    )


    BD = BitFieldMember(
        "BD",
        """
        @brief BD (debug register access detected) flag

Indicates that the next instruction in the instruction
stream accesses one of the debug registers (DR0 through DR7). This flag is enabled when the GD (general
detect) flag in debug control register DR7 is set.

@see Vol3B[17.2.4(Debug Control Register (DR7))]
        """,

        13,
        1

    )


    BS = BitFieldMember(
        "BS",
        """
        @brief BS (single step) flag

Indicates (when set) that the debug exception was triggered by the singlestep
execution mode (enabled with the TF flag in the EFLAGS register). The single-step mode is the highestpriority
debug exception. When the BS flag is set, any of the other debug status bits also may be set.
        """,

        14,
        1

    )


    BT = BitFieldMember(
        "BT",
        """
        @brief BT (task switch) flag

Indicates (when set) that the debug exception was triggered by the singlestep
execution mode (enabled with the TF flag in the EFLAGS register). The single-step mode is the highestpriority
debug exception. When the BS flag is set, any of the other debug status bits also may be set.
        """,

        15,
        1

    )


    RTM = BitFieldMember(
        "RTM",
        """
        @brief RTM (restricted transactional memory) flag

Indicates (when clear) that a debug exception
(\#DB) or breakpoint exception (\#BP) occurred inside an RTM region while advanced debugging of RTM transactional
regions was enabled. This bit is set for any other debug exception (including all
those that occur when advanced debugging of RTM transactional regions is not enabled). This bit is always 1 if
the processor does not support RTM.

@see Vol3B[17.3.3(Debug Exceptions, Breakpoint Exceptions, and Restricted Transactional Memory (RTM))]
        """,

        16,
        1

    )


class Dr7(with_metaclass(BitFieldMeta, BitField)):
    """
    
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super().__init__(value, byte_offset, byte_width, max_bytes=8)



    L0 = BitFieldMember(
        "L0",
        """
        @brief L0 through L3 (local breakpoint enable) flags (bits 0, 2, 4, and 6)

Enables (when set) the breakpoint
condition for the associated breakpoint for the current task. When a breakpoint condition is detected and its
associated Ln flag is set, a debug exception is generated. The processor automatically clears these flags on
every task switch to avoid unwanted breakpoint conditions in the new task.
        """,

        0,
        1

    )


    G0 = BitFieldMember(
        "G0",
        """
        @brief G0 through G3 (global breakpoint enable) flags (bits 1, 3, 5, and 7)

Enables (when set) the
breakpoint condition for the associated breakpoint for all tasks. When a breakpoint condition is detected and its
associated Gn flag is set, a debug exception is generated. The processor does not clear these flags on a task
switch, allowing a breakpoint to be enabled for all tasks.
        """,

        1,
        1

    )


    L1 = BitFieldMember(
        "L1",
        """
        

@see #L0
        """,

        2,
        1

    )


    G1 = BitFieldMember(
        "G1",
        """
        

@see #G0
        """,

        3,
        1

    )


    L2 = BitFieldMember(
        "L2",
        """
        

@see #L0
        """,

        4,
        1

    )


    G2 = BitFieldMember(
        "G2",
        """
        

@see #G0
        """,

        5,
        1

    )


    L3 = BitFieldMember(
        "L3",
        """
        

@see #L0
        """,

        6,
        1

    )


    G3 = BitFieldMember(
        "G3",
        """
        

@see #G0
        """,

        7,
        1

    )


    LE = BitFieldMember(
        "LE",
        """
        @brief LE (local exact breakpoint enable)

This feature is not supported in
the P6 family processors, later IA-32 processors, and Intel 64 processors. When set, these flags cause the
processor to detect the exact instruction that caused a data breakpoint condition. For backward and forward
compatibility with other Intel processors, we recommend that the LE and GE flags be set to 1 if exact
breakpoints are required.
        """,

        8,
        1

    )


    GE = BitFieldMember(
        "GE",
        """
        @brief GE (global exact breakpoint enable)



@see #LE
        """,

        9,
        1

    )


    RTM = BitFieldMember(
        "RTM",
        """
        @brief RTM (restricted transactional memory) flag

Enables (when set) advanced debugging of RTM
transactional regions. This advanced debugging is enabled only if IA32_DEBUGCTL.RTM is
also set.

@see Vol3B[17.3.3(Debug Exceptions, Breakpoint Exceptions, and Restricted Transactional Memory (RTM))]
        """,

        11,
        1

    )


    GD = BitFieldMember(
        "GD",
        """
        @brief GD (general detect enable) flag

Enables (when set) debug-register protection, which causes a
debug exception to be generated prior to any MOV instruction that accesses a debug register. When such a
condition is detected, the BD flag in debug status register DR6 is set prior to generating the exception. This
condition is provided to support in-circuit emulators.

When the emulator needs to access the debug registers, emulator software can set the GD flag to prevent
interference from the program currently executing on the processor.

The processor clears the GD flag upon entering to the debug exception handler, to allow the handler access to
the debug registers.
        """,

        13,
        1

    )


    RW0 = BitFieldMember(
        "RW0",
        """
        @brief R/W0 through R/W3 (read/write) fields (bits 16, 17, 20, 21, 24, 25, 28, and 29)

Specifies the
breakpoint condition for the corresponding breakpoint. The DE (debug extensions) flag in control register CR4
determines how the bits in the R/Wn fields are interpreted. When the DE flag is set, the processor interprets
bits as follows:

- 00 - Break on instruction execution only.

- 01 - Break on data writes only.

- 10 - Break on I/O reads or writes.

- 11 - Break on data reads or writes but not instruction fetches.

When the DE flag is clear, the processor interprets the R/Wn bits the same as for the Intel386 and Intel486
processors, which is as follows:

- 00 - Break on instruction execution only.

- 01 - Break on data writes only.

- 10 - Undefined.

- 11 - Break on data reads or writes but not instruction fetches.
        """,

        16,
        2

    )


    LEN0 = BitFieldMember(
        "LEN0",
        """
        @brief LEN0 through LEN3 (Length) fields (bits 18, 19, 22, 23, 26, 27, 30, and 31)

Specify the size of the
memory location at the address specified in the corresponding breakpoint address register (DR0 through DR3).
These fields are interpreted as follows:

- 00 - 1-byte length.

- 01 - 2-byte length.

- 10 - Undefined (or 8 byte length, see note below).

- 11 - 4-byte length.

If the corresponding RWn field in register DR7 is 00 (instruction execution), then the LENn field should also be 00.
The effect of using other lengths is undefined.

@see Vol3B[17.2.5(Breakpoint Field Recognition)]
        """,

        18,
        2

    )


    RW1 = BitFieldMember(
        "RW1",
        """
        

@see #RW0
        """,

        20,
        2

    )


    LEN1 = BitFieldMember(
        "LEN1",
        """
        

@see #LEN0
        """,

        22,
        2

    )


    RW2 = BitFieldMember(
        "RW2",
        """
        

@see #RW0
        """,

        24,
        2

    )


    LEN2 = BitFieldMember(
        "LEN2",
        """
        

@see #LEN0
        """,

        26,
        2

    )


    RW3 = BitFieldMember(
        "RW3",
        """
        

@see #RW0
        """,

        28,
        2

    )


    LEN3 = BitFieldMember(
        "LEN3",
        """
        

@see #LEN0
        """,

        30,
        2

    )


