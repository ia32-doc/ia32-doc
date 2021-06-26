from future.utils import with_metaclass
from ia32_python.utils.ia32_struct import *
from ia32_python.utils.ia32_enum import *
from ia32_python.utils.ia32_bit_field import *


__doc__ = """
@brief Basic VM-Exit Information

Basic VM-Exit Information.
"""


class VmxExitQualificationDebugException(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
    """
    @brief Exit Qualification for Debug Exceptions

Exit Qualification for Debug Exceptions.
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super(VmxExitQualificationDebugException, self).__init__(value, byte_offset, byte_width, max_bytes=8)



    BREAKPOINT_CONDITION = Ia32BitFieldMember(
        "BREAKPOINT_CONDITION",
        """
        @brief B0  B3

When set, each of these bits indicates that the corresponding breakpoint condition was met. Any of
these bits may be set even if its corresponding enabling bit in DR7 is not set.
        """,

        0,
        4

    )


    BD = Ia32BitFieldMember(
        "BD",
        """
        @brief BD

When set, this bit indicates that the cause of the debug exception is debug register access detected.
        """,

        13,
        1

    )


    BS = Ia32BitFieldMember(
        "BS",
        """
        @brief BS

When set, this bit indicates that the cause of the debug exception is either the execution of a single
instruction (if RFLAGS.TF = 1 and IA32_DEBUGCTL.BTF = 0) or a taken branch (if
RFLAGS.TF = DEBUGCTL.BTF = 1).
        """,

        14,
        1

    )


class VmxExitQualificationTaskSwitch(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
    """
    @brief Exit Qualification for Task Switch

Exit Qualification for Task Switch.
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super(VmxExitQualificationTaskSwitch, self).__init__(value, byte_offset, byte_width, max_bytes=8)



    SELECTOR = Ia32BitFieldMember(
        "SELECTOR",
        """
        @brief Selector of task-state segment (TSS) to which the guest attempted to switch

Selector of task-state segment (TSS) to which the guest attempted to switch.
        """,

        0,
        16

    )


    TYPE = Ia32BitFieldMember(
        "TYPE",
        """
        @brief Source of task switch initiation

Source of task switch initiation.
        """,

        30,
        2

    )


class VmxExitQualificationControlRegisterAccess(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
    """
    @brief Exit Qualification for Control-Register Accesses

Exit Qualification for Control-Register Accesses.
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super(VmxExitQualificationControlRegisterAccess, self).__init__(value, byte_offset, byte_width, max_bytes=8)



    REGISTER = Ia32BitFieldMember(
        "REGISTER",
        """
        @brief Number of control register (0 for CLTS and LMSW). Bit 3 is always 0 on processors that do not support Intel 64
architecture as they do not support CR8

Number of control register (0 for CLTS and LMSW). Bit 3 is always 0 on processors that do not support Intel 64
architecture as they do not support CR8.
        """,

        0,
        4

    )


    ACCESS = Ia32BitFieldMember(
        "ACCESS",
        """
        @brief Access type

Access type.
        """,

        4,
        2

    )


    LMSW_OP = Ia32BitFieldMember(
        "LMSW_OP",
        """
        @brief LMSW operand type. For CLTS and MOV CR, cleared to 0

LMSW operand type. For CLTS and MOV CR, cleared to 0.
        """,

        6,
        1

    )


    GENREG = Ia32BitFieldMember(
        "GENREG",
        """
        @brief For MOV CR, the general-purpose register

For MOV CR, the general-purpose register.
        """,

        8,
        4

    )


    LMSW_DATA = Ia32BitFieldMember(
        "LMSW_DATA",
        """
        @brief For LMSW, the LMSW source data.
For CLTS and MOV CR, cleared to 0

For LMSW, the LMSW source data.
For CLTS and MOV CR, cleared to 0.
        """,

        16,
        16

    )


class VmxExitQualificationDebugRegisterAccess(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
    """
    @brief Exit Qualification for MOV DR

Exit Qualification for MOV DR
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super(VmxExitQualificationDebugRegisterAccess, self).__init__(value, byte_offset, byte_width, max_bytes=8)



    REGISTER = Ia32BitFieldMember(
        "REGISTER",
        """
        @brief Number of debug register

Number of debug register.
        """,

        0,
        3

    )


    DIRECTION = Ia32BitFieldMember(
        "DIRECTION",
        """
        @brief Direction of access (0 = MOV to DR; 1 = MOV from DR)

Direction of access (0 = MOV to DR; 1 = MOV from DR).
        """,

        4,
        1

    )


    GENREG = Ia32BitFieldMember(
        "GENREG",
        """
        @brief General-purpose register

General-purpose register.
        """,

        8,
        4

    )


class VmxExitQualificationIoInstruction(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
    """
    @brief Exit Qualification for I/O Instructions

Exit Qualification for I/O Instructions.
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super(VmxExitQualificationIoInstruction, self).__init__(value, byte_offset, byte_width, max_bytes=8)



    WIDTH = Ia32BitFieldMember(
        "WIDTH",
        """
        @brief Size of access

Size of access.
        """,

        0,
        3

    )


    DIRECTION = Ia32BitFieldMember(
        "DIRECTION",
        """
        @brief Direction of the attempted access (0 = OUT, 1 = IN)

Direction of the attempted access (0 = OUT, 1 = IN).
        """,

        3,
        1

    )


    IS_STRING = Ia32BitFieldMember(
        "IS_STRING",
        """
        @brief String instruction (0 = not string; 1 = string)

String instruction (0 = not string; 1 = string).
        """,

        4,
        1

    )


    IS_REP = Ia32BitFieldMember(
        "IS_REP",
        """
        @brief REP prefixed (0 = not REP; 1 = REP)

REP prefixed (0 = not REP; 1 = REP).
        """,

        5,
        1

    )


    ENCODING = Ia32BitFieldMember(
        "ENCODING",
        """
        @brief Operand encoding (0 = DX, 1 = immediate)

Operand encoding (0 = DX, 1 = immediate).
        """,

        6,
        1

    )


    PORT = Ia32BitFieldMember(
        "PORT",
        """
        @brief Port number (as specified in DX or in an immediate operand)

Port number (as specified in DX or in an immediate operand).
        """,

        16,
        16

    )


class VmxExitQualificationApicAccess(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
    """
    @brief Exit Qualification for APIC-Access VM Exits from Linear Accesses and Guest-Physical Accesses

Exit Qualification for APIC-Access VM Exits from Linear Accesses and Guest-Physical Accesses.
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super(VmxExitQualificationApicAccess, self).__init__(value, byte_offset, byte_width, max_bytes=8)



    OFFSET = Ia32BitFieldMember(
        "OFFSET",
        """
        @brief - If the APIC-access VM exit is due to a linear access, the offset of access within the APIC page.

- Undefined if the APIC-access VM exit is due a guest-physical access

- If the APIC-access VM exit is due to a linear access, the offset of access within the APIC page.

- Undefined if the APIC-access VM exit is due a guest-physical access.
        """,

        0,
        12

    )


    TYPE = Ia32BitFieldMember(
        "TYPE",
        """
        @brief Access type

Access type.
        """,

        12,
        4

    )


class VmxExitQualificationEptViolation(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
    """
    @brief Exit Qualification for EPT Violations

Exit Qualification for EPT Violations.
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super(VmxExitQualificationEptViolation, self).__init__(value, byte_offset, byte_width, max_bytes=8)



    DATA_READ = Ia32BitFieldMember(
        "DATA_READ",
        """
        @brief Set if the access causing the EPT violation was a data read

Set if the access causing the EPT violation was a data read.
        """,

        0,
        1

    )


    DATA_WRITE = Ia32BitFieldMember(
        "DATA_WRITE",
        """
        @brief Set if the access causing the EPT violation was a data write

Set if the access causing the EPT violation was a data write.
        """,

        1,
        1

    )


    INSTR_FETCH = Ia32BitFieldMember(
        "INSTR_FETCH",
        """
        @brief Set if the access causing the EPT violation was an instruction fetch

Set if the access causing the EPT violation was an instruction fetch.
        """,

        2,
        1

    )


    ENTRY_PRESENT = Ia32BitFieldMember(
        "ENTRY_PRESENT",
        """
        @brief The logical-AND of bit 0 in the EPT paging-structure entries used to translate the guest-physical address of the
access causing the EPT violation (indicates whether the guest-physical address was readable)

The logical-AND of bit 0 in the EPT paging-structure entries used to translate the guest-physical address of the
access causing the EPT violation (indicates whether the guest-physical address was readable).
        """,

        3,
        1

    )


    ENTRY_WRITE = Ia32BitFieldMember(
        "ENTRY_WRITE",
        """
        @brief The logical-AND of bit 1 in the EPT paging-structure entries used to translate the guest-physical address of the
access causing the EPT violation (indicates whether the guest-physical address was writeable)

The logical-AND of bit 1 in the EPT paging-structure entries used to translate the guest-physical address of the
access causing the EPT violation (indicates whether the guest-physical address was writeable).
        """,

        4,
        1

    )


    ENTRY_EXECUTE = Ia32BitFieldMember(
        "ENTRY_EXECUTE",
        """
        @brief The logical-AND of bit 2 in the EPT paging-structure entries used to translate the guest-physical address of the
access causing the EPT violation.

If the mode-based execute control for EPT VM-execution control is 0, this indicates whether the guest-physical
address was executable. If that control is 1, this indicates whether the guest-physical address was executable
for supervisor-mode linear addresses

The logical-AND of bit 2 in the EPT paging-structure entries used to translate the guest-physical address of the
access causing the EPT violation.

If the mode-based execute control for EPT VM-execution control is 0, this indicates whether the guest-physical
address was executable. If that control is 1, this indicates whether the guest-physical address was executable
for supervisor-mode linear addresses.
        """,

        5,
        1

    )


    ENTRY_EXECUTE_UM = Ia32BitFieldMember(
        "ENTRY_EXECUTE_UM",
        """
        @brief If the mode-based execute control VM-execution control is 0, the value of this bit is undefined. If that control is
1, this bit is the logical-AND of bit 10 in the EPT paging-structures entries used to translate the guest-physical
address of the access causing the EPT violation. In this case, it indicates whether the guest-physical address was
executable for user-mode linear addresses

If the mode-based execute control VM-execution control is 0, the value of this bit is undefined. If that control is
1, this bit is the logical-AND of bit 10 in the EPT paging-structures entries used to translate the guest-physical
address of the access causing the EPT violation. In this case, it indicates whether the guest-physical address was
executable for user-mode linear addresses.
        """,

        6,
        1

    )


    GUEST_ADDR_VALID = Ia32BitFieldMember(
        "GUEST_ADDR_VALID",
        """
        @brief Set if the guest linear-address field is valid.
The guest linear-address field is valid for all EPT violations except those resulting from an attempt to load the
guest PDPTEs as part of the execution of the MOV CR instruction

Set if the guest linear-address field is valid.
The guest linear-address field is valid for all EPT violations except those resulting from an attempt to load the
guest PDPTEs as part of the execution of the MOV CR instruction.
        """,

        7,
        1

    )


    EPT_TRANSLATED_ACCESS = Ia32BitFieldMember(
        "EPT_TRANSLATED_ACCESS",
        """
        @brief If bit 7 is 1:

- Set if the access causing the EPT violation is to a guest-physical address that is the translation of a linear
  address.

- Clear if the access causing the EPT violation is to a paging-structure entry as part of a page walk or the
  update of an accessed or dirty bit.

Reserved if bit 7 is 0 (cleared to 0)

If bit 7 is 1:

- Set if the access causing the EPT violation is to a guest-physical address that is the translation of a linear
  address.

- Clear if the access causing the EPT violation is to a paging-structure entry as part of a page walk or the
  update of an accessed or dirty bit.

Reserved if bit 7 is 0 (cleared to 0).
        """,

        8,
        1

    )


    USER_MODE_LINEAR_ADDRESS = Ia32BitFieldMember(
        "USER_MODE_LINEAR_ADDRESS",
        """
        @brief This bit is 0 if the linear address is a supervisor-mode linear address and 1 if it is a user-mode linear address.
Otherwise, this bit is undefined

This bit is 0 if the linear address is a supervisor-mode linear address and 1 if it is a user-mode linear address.
Otherwise, this bit is undefined.
        """,

        9,
        1

    )


    READABLE_WRITABLE_PAGE = Ia32BitFieldMember(
        "READABLE_WRITABLE_PAGE",
        """
        @brief This bit is 0 if paging translates the linear address to a read-only page and 1 if it translates to a read/write page.
Otherwise, this bit is undefined

This bit is 0 if paging translates the linear address to a read-only page and 1 if it translates to a read/write page.
Otherwise, this bit is undefined
        """,

        10,
        1

    )


    EXECUTE_DISABLE_PAGE = Ia32BitFieldMember(
        "EXECUTE_DISABLE_PAGE",
        """
        @brief This bit is 0 if paging translates the linear address to an executable page and 1 if it translates to an execute-disable page.
Otherwise, this bit is undefined

This bit is 0 if paging translates the linear address to an executable page and 1 if it translates to an execute-disable page.
Otherwise, this bit is undefined.
        """,

        11,
        1

    )


    NMI_UNBLOCKING = Ia32BitFieldMember(
        "NMI_UNBLOCKING",
        """
        @brief NMI unblocking due to IRET

NMI unblocking due to IRET.
        """,

        12,
        1

    )


