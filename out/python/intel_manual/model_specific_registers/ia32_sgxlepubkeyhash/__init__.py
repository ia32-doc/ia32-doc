from future.utils import with_metaclass
from utils.struct import *
from utils.bit_field import *


__doc__ = """
@brief IA32_SGXLEPUBKEYHASH[(64*n+63):(64*n)]

Bits (64*n+63):(64*n) of the
SHA256 digest of the SIGSTRUCT.MODULUS for SGX Launch Enclave. On reset, the
default value is the digest of Intels signing key.
"""


IA32_SGXLEPUBKEYHASH0 = 0x8c


IA32_SGXLEPUBKEYHASH1 = 0x8d


IA32_SGXLEPUBKEYHASH2 = 0x8e


IA32_SGXLEPUBKEYHASH3 = 0x8f


IA32_SMM_MONITOR_CTL = 0x9b


class Ia32MsegHeader(Struct):
    """"""
    class _MemberContainerMsegHeaderRevision(with_metaclass(BitFieldMeta, BitField)):
        """
        @brief MSEG revision identifier
    
    Different processors may use different MSEG revision identifiers.
    These identifiers enable software to avoid using an MSEG header formatted for one processor on a
    processor that uses a different format. Software can discover the MSEG revision identifier that a processor uses
    by reading the VMX capability MSR IA32_VMX_MISC.
    
    @see Vol3D[A.6(MISCELLANEOUS DATA)]
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super().__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
        value = BitFieldMember('value', 'value', 0, 32)
    
    
    class _MemberContainerMonitorFeatures(with_metaclass(BitFieldMeta, BitField)):
        """
        @brief SMM-transfer monitor features field
    
    Bits 31:1 of this field are reserved and must be
    zero. Bit 0 of the field is the IA-32e mode SMM feature bit. It indicates whether the logical processor will be
    in IA-32e mode after the STM is activated.
    
    @see Vol3C[34.15.6(Activating the Dual-Monitor Treatment)]
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super().__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
        value = BitFieldMember('value', 'value', 0, 32)
    
        IA32_STM_FEATURES_IA32E = BitFieldMember(
            "IA32_STM_FEATURES_IA32E",
            """
            @brief Define values for the MonitorFeatures field of MSEG_HEADER
    
    Define values for the MonitorFeatures field of MSEG_HEADER.
            """,
    
            0,
            
    
        )
    
    
    
    class _MemberContainerGdtrLimit(with_metaclass(BitFieldMeta, BitField)):
        """
        @brief Fields that determine how processor state is loaded when the STM is activated.
    SMM code should establish these fields so that activating of the STM invokes the STMs initialization
    code
    
    Fields that determine how processor state is loaded when the STM is activated.
    SMM code should establish these fields so that activating of the STM invokes the STMs initialization
    code.
    
    @see Vol3C[34.15.6.5(Loading Host State)]
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super().__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
        value = BitFieldMember('value', 'value', 0, 32)
    
    
    class _MemberContainerGdtrBaseOffset(with_metaclass(BitFieldMeta, BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super().__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
        value = BitFieldMember('value', 'value', 0, 32)
    
    
    class _MemberContainerCsSelector(with_metaclass(BitFieldMeta, BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super().__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
        value = BitFieldMember('value', 'value', 0, 32)
    
    
    class _MemberContainerEipOffset(with_metaclass(BitFieldMeta, BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super().__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
        value = BitFieldMember('value', 'value', 0, 32)
    
    
    class _MemberContainerEspOffset(with_metaclass(BitFieldMeta, BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super().__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
        value = BitFieldMember('value', 'value', 0, 32)
    
    
    class _MemberContainerCr3Offset(with_metaclass(BitFieldMeta, BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super().__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
        value = BitFieldMember('value', 'value', 0, 32)
    
    
    _members = ["MSEG_HEADER_REVISION","MONITOR_FEATURES","GDTR_LIMIT","GDTR_BASE_OFFSET","CS_SELECTOR","EIP_OFFSET","ESP_OFFSET","CR3_OFFSET",]

    def __init__(self, value):
        self._MSEG_HEADER_REVISION = self._MemberContainerMsegHeaderRevision(0, 0, 4 )
        self._MONITOR_FEATURES = self._MemberContainerMonitorFeatures(0, 4, 4 )
        self._GDTR_LIMIT = self._MemberContainerGdtrLimit(0, 8, 4 )
        self._GDTR_BASE_OFFSET = self._MemberContainerGdtrBaseOffset(0, 12, 4 )
        self._CS_SELECTOR = self._MemberContainerCsSelector(0, 16, 4 )
        self._EIP_OFFSET = self._MemberContainerEipOffset(0, 20, 4 )
        self._ESP_OFFSET = self._MemberContainerEspOffset(0, 24, 4 )
        self._CR3_OFFSET = self._MemberContainerCr3Offset(0, 28, 4 )
        super().__init__(value)


    @property
    def MSEG_HEADER_REVISION(self):
        return self._MSEG_HEADER_REVISION

    @MSEG_HEADER_REVISION.setter
    def MSEG_HEADER_REVISION(self, value):
        return self._MSEG_HEADER_REVISION.set(value)

    @property
    def MONITOR_FEATURES(self):
        return self._MONITOR_FEATURES

    @MONITOR_FEATURES.setter
    def MONITOR_FEATURES(self, value):
        return self._MONITOR_FEATURES.set(value)

    @property
    def GDTR_LIMIT(self):
        return self._GDTR_LIMIT

    @GDTR_LIMIT.setter
    def GDTR_LIMIT(self, value):
        return self._GDTR_LIMIT.set(value)

    @property
    def GDTR_BASE_OFFSET(self):
        return self._GDTR_BASE_OFFSET

    @GDTR_BASE_OFFSET.setter
    def GDTR_BASE_OFFSET(self, value):
        return self._GDTR_BASE_OFFSET.set(value)

    @property
    def CS_SELECTOR(self):
        return self._CS_SELECTOR

    @CS_SELECTOR.setter
    def CS_SELECTOR(self, value):
        return self._CS_SELECTOR.set(value)

    @property
    def EIP_OFFSET(self):
        return self._EIP_OFFSET

    @EIP_OFFSET.setter
    def EIP_OFFSET(self, value):
        return self._EIP_OFFSET.set(value)

    @property
    def ESP_OFFSET(self):
        return self._ESP_OFFSET

    @ESP_OFFSET.setter
    def ESP_OFFSET(self, value):
        return self._ESP_OFFSET.set(value)

    @property
    def CR3_OFFSET(self):
        return self._CR3_OFFSET

    @CR3_OFFSET.setter
    def CR3_OFFSET(self, value):
        return self._CR3_OFFSET.set(value)


IA32_SMBASE = 0x9e


