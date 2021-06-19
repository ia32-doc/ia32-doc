from future.utils import with_metaclass
from utils.bit_field import *


__doc__ = """
Virtualization Exceptions.
"""
class VmxVeExceptInfo(with_metaclass(BitFieldMeta, BitField)):
    """"""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=34)

    
    
    REASON = BitFieldMember(
        "REASON",
        """
        :
        The 32-bit value that would have been saved into the VMCS as an exit reason had a VM exit occurred
instead of the virtualization exception. For EPT violations, this value is 48 (00000030H).
        """,
        0,
        32
        
    )

    
    EXCEPT_MASK = BitFieldMember(
        "EXCEPT_MASK",
        """
        FFFFFFFFH:
        FFFFFFFFH
        """,
        32,
        32
        
    )

    
    EXIT = BitFieldMember(
        "EXIT",
        """
        :
        The 64-bit value that would have been saved into the VMCS as an exit qualification had a VM exit
occurred instead of the virtualization exception.
        """,
        64,
        64
        
    )

    
    GLA = BitFieldMember(
        "GLA",
        """
        :
        The 64-bit value that would have been saved into the VMCS as a guest-linear address had a VM exit
occurred instead of the virtualization exception.
        """,
        128,
        64
        
    )

    
    GPA = BitFieldMember(
        "GPA",
        """
        :
        The 64-bit value that would have been saved into the VMCS as a guest-physical address had a VM
exit occurred instead of the virtualization exception.
        """,
        192,
        64
        
    )

    
    EPTP = BitFieldMember(
        "EPTP",
        """
        :
        The current 16-bit value of the EPTP index VM-execution control.
        """,
        256,
        16
        
    )

    

