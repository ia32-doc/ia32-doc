from future.utils import with_metaclass
from utils.struct import *
from utils.bit_field import *


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


class InterruptType:
    """
    @brief Valid interruption types

Valid interruption types.
    """

    
      EXTERNAL = 0x0
    
      NMI = 0x2
    
      HARDWARE_EXCEPTION = 0x3
    
      SOFTWARE = 0x4
    
      PRIVILEGED_EXCEPTION = 0x5
    
      SOFTWARE_EXCEPTION = 0x6
    
      OTHER = 0x7
    
class VmentryInterruptInformation(with_metaclass(BitFieldMeta, BitField)):
    """
    @brief VM entry can be configured to conclude by delivering an event through the IDT (after all guest state and MSRs have
been loaded). This process is called event injection and is controlled by these VM-entry control
fields

VM entry can be configured to conclude by delivering an event through the IDT (after all guest state and MSRs have
been loaded). This process is called event injection and is controlled by these VM-entry control
fields.
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super().__init__(value, byte_offset, byte_width, max_bytes=4)



    VECTOR = BitFieldMember(
        "VECTOR",
        """
        @brief Vector of interrupt or exception

Determines which entry in the IDT is used or which other event is injected.
        """,

        0,
        8

    )


    TYPE = BitFieldMember(
        "TYPE",
        """
        @brief Interruption type

Determines details of how the injection is performed.
        """,

        8,
        3

    )


    DELIVER_ERROR_CODE = BitFieldMember(
        "DELIVER_ERROR_CODE",
        """
        @brief Deliver error code (0 = do not deliver; 1 = deliver)

Determines whether delivery pushes an error code on the guest stack.
        """,

        11,
        1

    )


    VALID = BitFieldMember(
        "VALID",
        """
        @brief Valid

VM entry injects an event if and only if the valid bit is 1. The valid bit in this field is cleared on every
VM exit.
        """,

        31,
        1

    )


class VmexitInterruptInformation(with_metaclass(BitFieldMeta, BitField)):
    """
    @brief VM entry can be configured to conclude by delivering an event through the IDT (after all guest state and MSRs have
been loaded). This process is called event injection and is controlled by these VM-entry control
fields

VM entry can be configured to conclude by delivering an event through the IDT (after all guest state and MSRs have
been loaded). This process is called event injection and is controlled by these VM-entry control
fields.
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super().__init__(value, byte_offset, byte_width, max_bytes=4)



    VECTOR = BitFieldMember(
        "VECTOR",
        """
        @brief Vector of interrupt or exception

Vector of interrupt or exception.
        """,

        0,
        8

    )


    TYPE = BitFieldMember(
        "TYPE",
        """
        @brief Interruption type

Interruption type.
        """,

        8,
        3

    )


    ERROR_CODE_VALID = BitFieldMember(
        "ERROR_CODE_VALID",
        """
        @brief Deliver error code (0 = do not deliver; 1 = deliver)

Deliver error code (0 = do not deliver; 1 = deliver).
        """,

        11,
        1

    )


    NMI_UNBLOCKING = BitFieldMember(
        "NMI_UNBLOCKING",
        """
        @brief NMI unblocking due to IRET

NMI unblocking due to IRET.
        """,

        12,
        1

    )


    VALID = BitFieldMember(
        "VALID",
        """
        @brief Valid

Valid.
        """,

        31,
        1

    )


