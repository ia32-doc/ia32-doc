from future.utils import with_metaclass
from utils.struct import *
from utils.bit_field import *


__doc__ = """
@brief EAX = 0x0F

When CPUID executes with EAX set to 0FH and ECX = 0, the processor returns information about the bit-vector
representation of QoS monitoring resource types that are supported in the processor and maximum range of RMID
values the processor can use to monitor of any supported resource types. Each bit, starting from bit 1, corresponds
to a specific resource type if the bit is set. The bit position corresponds to the sub-leaf index (or ResID) that software
must use to query QoS monitoring capability available for that type. See Table 3-8.

When CPUID executes with EAX set to 0FH and ECX = n (n >= 1, and is a valid ResID), the processor returns information
software can use to program IA32_PQR_ASSOC, IA32_QM_EVTSEL MSRs before reading QoS data from the
IA32_QM_CTR MSR.
"""


CPUID_INTEL_RDT_MONITORING = 0xf


class CpuidEax0fEcx00(Struct):
    """@brief Intel Resource Director Technology (Intel RDT) Monitoring Enumeration Sub-leaf (EAX = 0FH, ECX = 0)

Intel Resource Director Technology (Intel RDT) Monitoring Enumeration Sub-leaf (EAX = 0FH, ECX = 0)."""
    class _MemberContainerCpuidEax(with_metaclass(BitFieldMeta, BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super().__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        RESERVED = BitFieldMember(
            "RESERVED",
            """
            @brief EAX is reserved
    
    EAX is reserved.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEbx(with_metaclass(BitFieldMeta, BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super().__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        RMID_MAX_RANGE = BitFieldMember(
            "RMID_MAX_RANGE",
            """
            @brief Maximum range (zero-based) of RMID within this physical processor of all types
    
    Maximum range (zero-based) of RMID within this physical processor of all types.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEcx(with_metaclass(BitFieldMeta, BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super().__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        RESERVED = BitFieldMember(
            "RESERVED",
            """
            @brief ECX is reserved
    
    ECX is reserved.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEdx(with_metaclass(BitFieldMeta, BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super().__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        SUPPORTS_L3_CACHE_INTEL_RDT_MONITORING = BitFieldMember(
            "SUPPORTS_L3_CACHE_INTEL_RDT_MONITORING",
            """
            @brief Supports L3 Cache Intel RDT Monitoring if 1
    
    Supports L3 Cache Intel RDT Monitoring if 1.
            """,
    
            1,
            1
    
        )
    
    
    
    _members = ["CPUID_EAX","CPUID_EBX","CPUID_ECX","CPUID_EDX",]

    def __init__(self, value):
        self._CPUID_EAX = self._MemberContainerCpuidEax(0, 0, 4 )
        self._CPUID_EBX = self._MemberContainerCpuidEbx(0, 4, 4 )
        self._CPUID_ECX = self._MemberContainerCpuidEcx(0, 8, 4 )
        self._CPUID_EDX = self._MemberContainerCpuidEdx(0, 12, 4 )
        super().__init__(value)


    @property
    def CPUID_EAX(self):
        return self._CPUID_EAX

    @CPUID_EAX.setter
    def CPUID_EAX(self, value):
        return self._CPUID_EAX.set(value)

    @property
    def CPUID_EBX(self):
        return self._CPUID_EBX

    @CPUID_EBX.setter
    def CPUID_EBX(self, value):
        return self._CPUID_EBX.set(value)

    @property
    def CPUID_ECX(self):
        return self._CPUID_ECX

    @CPUID_ECX.setter
    def CPUID_ECX(self, value):
        return self._CPUID_ECX.set(value)

    @property
    def CPUID_EDX(self):
        return self._CPUID_EDX

    @CPUID_EDX.setter
    def CPUID_EDX(self, value):
        return self._CPUID_EDX.set(value)


class CpuidEax0fEcx01(Struct):
    """@brief L3 Cache Intel RDT Monitoring Capability Enumeration Sub-leaf (EAX = 0FH, ECX = 1)

L3 Cache Intel RDT Monitoring Capability Enumeration Sub-leaf (EAX = 0FH, ECX = 1)."""
    class _MemberContainerCpuidEax(with_metaclass(BitFieldMeta, BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super().__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        RESERVED = BitFieldMember(
            "RESERVED",
            """
            @brief EAX is reserved
    
    EAX is reserved.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEbx(with_metaclass(BitFieldMeta, BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super().__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        CONVERSION_FACTOR = BitFieldMember(
            "CONVERSION_FACTOR",
            """
            @brief Conversion factor from reported IA32_QM_CTR value to occupancy metric (bytes)
    
    Conversion factor from reported IA32_QM_CTR value to occupancy metric (bytes).
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEcx(with_metaclass(BitFieldMeta, BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super().__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        RMID_MAX_RANGE = BitFieldMember(
            "RMID_MAX_RANGE",
            """
            @brief Maximum range (zero-based) of RMID within this physical processor of all types
    
    Maximum range (zero-based) of RMID within this physical processor of all types.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEdx(with_metaclass(BitFieldMeta, BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super().__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        SUPPORTS_L3_OCCUPANCY_MONITORING = BitFieldMember(
            "SUPPORTS_L3_OCCUPANCY_MONITORING",
            """
            @brief Supports L3 occupancy monitoring if 1
    
    Supports L3 occupancy monitoring if 1.
            """,
    
            0,
            1
    
        )
    
    
        SUPPORTS_L3_TOTAL_BANDWIDTH_MONITORING = BitFieldMember(
            "SUPPORTS_L3_TOTAL_BANDWIDTH_MONITORING",
            """
            @brief Supports L3 Total Bandwidth monitoring if 1
    
    Supports L3 Total Bandwidth monitoring if 1.
            """,
    
            1,
            1
    
        )
    
    
        SUPPORTS_L3_LOCAL_BANDWIDTH_MONITORING = BitFieldMember(
            "SUPPORTS_L3_LOCAL_BANDWIDTH_MONITORING",
            """
            @brief Supports L3 Local Bandwidth monitoring if 1
    
    Supports L3 Local Bandwidth monitoring if 1.
            """,
    
            2,
            1
    
        )
    
    
    
    _members = ["CPUID_EAX","CPUID_EBX","CPUID_ECX","CPUID_EDX",]

    def __init__(self, value):
        self._CPUID_EAX = self._MemberContainerCpuidEax(0, 0, 4 )
        self._CPUID_EBX = self._MemberContainerCpuidEbx(0, 4, 4 )
        self._CPUID_ECX = self._MemberContainerCpuidEcx(0, 8, 4 )
        self._CPUID_EDX = self._MemberContainerCpuidEdx(0, 12, 4 )
        super().__init__(value)


    @property
    def CPUID_EAX(self):
        return self._CPUID_EAX

    @CPUID_EAX.setter
    def CPUID_EAX(self, value):
        return self._CPUID_EAX.set(value)

    @property
    def CPUID_EBX(self):
        return self._CPUID_EBX

    @CPUID_EBX.setter
    def CPUID_EBX(self, value):
        return self._CPUID_EBX.set(value)

    @property
    def CPUID_ECX(self):
        return self._CPUID_ECX

    @CPUID_ECX.setter
    def CPUID_ECX(self, value):
        return self._CPUID_ECX.set(value)

    @property
    def CPUID_EDX(self):
        return self._CPUID_EDX

    @CPUID_EDX.setter
    def CPUID_EDX(self, value):
        return self._CPUID_EDX.set(value)


