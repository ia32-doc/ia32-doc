from future.utils import with_metaclass
from utils.struct import *
from utils.bit_field import *


__doc__ = """
@brief Virtualization Exceptions

Virtualization Exceptions.
"""


class VmxVirtualizationExceptionInformation(Struct):
    """"""
    class _MemberContainerReason(with_metaclass(BitFieldMeta, BitField)):
        """
        The 32-bit value that would have been saved into the VMCS as an exit reason had a VM exit occurred
    instead of the virtualization exception. For EPT violations, this value is 48 (00000030H).
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super().__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
        value = BitFieldMember('value', 'value', 0, 32)
    
    
    class _MemberContainerExceptionMask(with_metaclass(BitFieldMeta, BitField)):
        """
        @brief FFFFFFFFH
    
    FFFFFFFFH
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super().__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
        value = BitFieldMember('value', 'value', 0, 32)
    
    
    class _MemberContainerExit(with_metaclass(BitFieldMeta, BitField)):
        """
        The 64-bit value that would have been saved into the VMCS as an exit qualification had a VM exit
    occurred instead of the virtualization exception.
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super().__init__(value, byte_offset, byte_width, max_bytes=8)
    
    
        value = BitFieldMember('value', 'value', 0, 64)
    
    
    class _MemberContainerGuestLinearAddress(with_metaclass(BitFieldMeta, BitField)):
        """
        The 64-bit value that would have been saved into the VMCS as a guest-linear address had a VM exit
    occurred instead of the virtualization exception.
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super().__init__(value, byte_offset, byte_width, max_bytes=8)
    
    
        value = BitFieldMember('value', 'value', 0, 64)
    
    
    class _MemberContainerGuestPhysicalAddress(with_metaclass(BitFieldMeta, BitField)):
        """
        The 64-bit value that would have been saved into the VMCS as a guest-physical address had a VM
    exit occurred instead of the virtualization exception.
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super().__init__(value, byte_offset, byte_width, max_bytes=8)
    
    
        value = BitFieldMember('value', 'value', 0, 64)
    
    
    class _MemberContainerCurrentEptpIndex(with_metaclass(BitFieldMeta, BitField)):
        """
        The current 16-bit value of the EPTP index VM-execution control.
    
    @see Vol3C[24.6.18(Controls for Virtualization Exceptions)]
    
    @see Vol3C[25.5.5.3(EPTP Switching)]
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super().__init__(value, byte_offset, byte_width, max_bytes=2)
    
    
        value = BitFieldMember('value', 'value', 0, 16)
    
    
    _members = ["REASON","EXCEPT_MASK","EXIT","GLA","GPA","EPTP",]

    def __init__(self, value):
        self._REASON = self._MemberContainerReason(0, 0, 4 )
        self._EXCEPT_MASK = self._MemberContainerExceptionMask(0, 4, 4 )
        self._EXIT = self._MemberContainerExit(0, 8, 8 )
        self._GLA = self._MemberContainerGuestLinearAddress(0, 16, 8 )
        self._GPA = self._MemberContainerGuestPhysicalAddress(0, 24, 8 )
        self._EPTP = self._MemberContainerCurrentEptpIndex(0, 32, 2 )
        super().__init__(value)


    @property
    def REASON(self):
        return self._REASON

    @REASON.setter
    def REASON(self, value):
        return self._REASON.set(value)

    @property
    def EXCEPT_MASK(self):
        return self._EXCEPT_MASK

    @EXCEPT_MASK.setter
    def EXCEPT_MASK(self, value):
        return self._EXCEPT_MASK.set(value)

    @property
    def EXIT(self):
        return self._EXIT

    @EXIT.setter
    def EXIT(self, value):
        return self._EXIT.set(value)

    @property
    def GLA(self):
        return self._GLA

    @GLA.setter
    def GLA(self, value):
        return self._GLA.set(value)

    @property
    def GPA(self):
        return self._GPA

    @GPA.setter
    def GPA(self, value):
        return self._GPA.set(value)

    @property
    def EPTP(self):
        return self._EPTP

    @EPTP.setter
    def EPTP(self, value):
        return self._EPTP.set(value)


