from future.utils import with_metaclass
from ia32_python.utils.ia32_struct import *
from ia32_python.utils.ia32_enum import *
from ia32_python.utils.ia32_bit_field import *


__doc__ = """
@brief Natural-Width Host-State Fields

Natural-Width Host-State Fields.
"""


VMCS_HOST_CR0 = 0x6c00


VMCS_HOST_CR3 = 0x6c02


VMCS_HOST_CR4 = 0x6c04


VMCS_HOST_FS_BASE = 0x6c06


VMCS_HOST_GS_BASE = 0x6c08


VMCS_HOST_TR_BASE = 0x6c0a


VMCS_HOST_GDTR_BASE = 0x6c0c


VMCS_HOST_IDTR_BASE = 0x6c0e


VMCS_HOST_SYSENTER_ESP = 0x6c10


VMCS_HOST_SYSENTER_EIP = 0x6c12


VMCS_HOST_RSP = 0x6c14


VMCS_HOST_RIP = 0x6c16


VMCS_HOST_S_CET = 0x6c18


VMCS_HOST_SSP = 0x6c1a


VMCS_HOST_INTERRUPT_SSP_TABLE_ADDR = 0x6c1c


class InterruptionType(with_metaclass(Ia32EnumMeta, Ia32Enum)):
    """
    @brief Valid interruption types

Valid interruption types.
    """


    EXTERNAL = Ia32EnumField(
        "EXTERNAL",
        0x0,
        """@brief External interrupt

External interrupt.""",
   )

    NMI = Ia32EnumField(
        "NMI",
        0x2,
        """@brief Non-maskable interrupt (NMI)

Non-maskable interrupt (NMI).""",
   )

    HARDWARE_EXCEPTION = Ia32EnumField(
        "HARDWARE_EXCEPTION",
        0x3,
        """@brief Hardware exception (e.g,. \#PF)

Hardware exception (e.g,. \#PF).""",
   )

    SOFTWARE = Ia32EnumField(
        "SOFTWARE",
        0x4,
        """@brief Software interrupt (INT n)

Software interrupt (INT n).""",
   )

    PRIVILEGED_EXCEPTION = Ia32EnumField(
        "PRIVILEGED_EXCEPTION",
        0x5,
        """@brief Privileged software exception (INT1)

Privileged software exception (INT1).""",
   )

    SOFTWARE_EXCEPTION = Ia32EnumField(
        "SOFTWARE_EXCEPTION",
        0x6,
        """@brief Software exception (INT3 or INTO)

Software exception (INT3 or INTO).""",
   )

    OTHER = Ia32EnumField(
        "OTHER",
        0x7,
        """@brief Other event. This type is used for injection of events that are not delivered through the IDT

Other event. This type is used for injection of events that are not delivered through the IDT.""",
   )

class VmentryInterruptInformation(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
    """
    @brief VM entry can be configured to conclude by delivering an event through the IDT (after all guest state and MSRs have
been loaded). This process is called event injection and is controlled by these VM-entry control
fields

VM entry can be configured to conclude by delivering an event through the IDT (after all guest state and MSRs have
been loaded). This process is called event injection and is controlled by these VM-entry control
fields.
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super(VmentryInterruptInformation, self).__init__(value, byte_offset, byte_width, max_bytes=4)



    VECTOR = Ia32BitFieldMember(
        "VECTOR",
        """
        @brief Vector of interrupt or exception

Determines which entry in the IDT is used or which other event is injected.
        """,

        0,
        8

    )


    TYPE = Ia32BitFieldMember(
        "TYPE",
        """
        @brief Interruption type

Determines details of how the injection is performed.
        """,

        8,
        3

    )


    DELIVER_ERROR_CODE = Ia32BitFieldMember(
        "DELIVER_ERROR_CODE",
        """
        @brief Deliver error code (0 = do not deliver; 1 = deliver)

Determines whether delivery pushes an error code on the guest stack.
        """,

        11,
        1

    )


    VALID = Ia32BitFieldMember(
        "VALID",
        """
        @brief Valid

VM entry injects an event if and only if the valid bit is 1. The valid bit in this field is cleared on every
VM exit.
        """,

        31,
        1

    )


class VmexitInterruptInformation(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
    """
    @brief VM entry can be configured to conclude by delivering an event through the IDT (after all guest state and MSRs have
been loaded). This process is called event injection and is controlled by these VM-entry control
fields

VM entry can be configured to conclude by delivering an event through the IDT (after all guest state and MSRs have
been loaded). This process is called event injection and is controlled by these VM-entry control
fields.
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super(VmexitInterruptInformation, self).__init__(value, byte_offset, byte_width, max_bytes=4)



    VECTOR = Ia32BitFieldMember(
        "VECTOR",
        """
        @brief Vector of interrupt or exception

Vector of interrupt or exception.
        """,

        0,
        8

    )


    TYPE = Ia32BitFieldMember(
        "TYPE",
        """
        @brief Interruption type

Interruption type.
        """,

        8,
        3

    )


    ERROR_CODE_VALID = Ia32BitFieldMember(
        "ERROR_CODE_VALID",
        """
        @brief Deliver error code (0 = do not deliver; 1 = deliver)

Deliver error code (0 = do not deliver; 1 = deliver).
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


    VALID = Ia32BitFieldMember(
        "VALID",
        """
        @brief Valid

Valid.
        """,

        31,
        1

    )


