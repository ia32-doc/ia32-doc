from future.utils import with_metaclass
from utils.bit_field import *


__doc__ = """
EPT Entry counts.
"""
EPML4_ENTRY_COUNT = 0x200

EPDPTE_ENTRY_COUNT = 0x200

EPDE_ENTRY_COUNT = 0x200

EPTE_ENTRY_COUNT = 0x200

class InveptType:
    """"""

    
      INVEPT_SINGLE_CONTEXT = 0x1
    
      INVEPT_ALL_CONTEXT = 0x2
    
class InvvpidType:
    """"""

    
      INVVPID_INDIVIDUAL_ADDRESS = 0x0
    
      INVVPID_SINGLE_CONTEXT = 0x1
    
      INVVPID_ALL_CONTEXT = 0x2
    
      INVVPID_SINGLE_CONTEXT_RETAINING_GLOBALS = 0x3
    
class InveptDescriptor(with_metaclass(BitFieldMeta, BitField)):
    """"""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=16)

    
    
    EPTP = BitFieldMember(
        "EPTP",
        """
        :
        
        """,
        0,
        64
        
    )

    
    RESERVED = BitFieldMember(
        "RESERVED",
        """
        Must be zero:
        Must be zero.
        """,
        64,
        64
        
    )

    

class InvvpidDescriptor(with_metaclass(BitFieldMeta, BitField)):
    """"""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=16)

    
    
    VPID = BitFieldMember(
        "VPID",
        """
        :
        
        """,
        0,
        16
        
    )

    
    RESERVED1 = BitFieldMember(
        "RESERVED1",
        """
        Must be zero:
        Must be zero.
        """,
        16,
        16
        
    )

    
    RESERVED2 = BitFieldMember(
        "RESERVED2",
        """
        Must be zero:
        Must be zero.
        """,
        32,
        32
        
    )

    
    LINEAR_ADDRESS = BitFieldMember(
        "LINEAR_ADDRESS",
        """
        :
        
        """,
        64,
        64
        
    )

    

class Vmcs(with_metaclass(BitFieldMeta, BitField)):
    """A logical processor uses virtual-machine control data structures (VMCSs) while it is in VMX operation. These
manage transitions into and out of VMX non-root operation (VM entries and VM exits) as well as processor behavior
in VMX non-root operation. This structure is manipulated by the new instructions VMCLEAR, VMPTRLD, VMREAD,
and VMWRITE.

A VMCS region comprises up to 4-KBytes. The exact size is implementation specific and can be determined
by consulting the VMX capability MSR IA32_VMX_BASIC."""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=4092)

    
    
    ABORT_INDICATOR = BitFieldMember(
        "ABORT_INDICATOR",
        """
        VMX-abort indicator:
        The contents of these bits do not
control processor operation in any way. A logical processor writes a non-zero value into these bits if a VMX abort
occurs. Software may also write into this field.
        """,
        0,
        32
        
    )

    
    DATA = BitFieldMember(
        "DATA",
        """
        VMCS data (implementation-specific format):
        These parts of the VMCS control VMX non-root operation and the VMX transitions.

The format of these data is implementation-specific. To ensure proper behavior in VMX operation,
software should maintain the VMCS region and related structures in writeback cacheable memory. Future
implementations may allow or require a different memory type. Software should consult the VMX capability MSR
IA32_VMX_BASIC.
        """,
        32,
        32704
        
    )

    

class Vmxon(with_metaclass(BitFieldMeta, BitField)):
    """Before executing VMXON, software allocates a region of memory that the logical processor uses to support
VMX operation. This region is called the VMXON region.

A VMXON region comprises up to 4-KBytes. The exact size is implementation specific and can be determined
by consulting the VMX capability MSR IA32_VMX_BASIC."""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=4092)

    
    
    DATA = BitFieldMember(
        "DATA",
        """
        VMXON data (implementation-specific format):
        The format of these data is implementation-specific. To ensure proper behavior in VMX operation,
software should not access or modify the VMXON region of a logical processor between execution of VMXON and
VMXOFF on that logical processor. Doing otherwise may lead to unpredictable behavior.
        """,
        0,
        32736
        
    )

    

