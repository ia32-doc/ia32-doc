from future.utils import with_metaclass
from ia32_python.utils.ia32_struct import *
from ia32_python.utils.ia32_bit_field import *


__doc__ = """
@brief EAX = 0x10

When CPUID executes with EAX set to 10H and ECX = 0, the processor returns information about the bit-vector
representation of QoS Enforcement resource types that are supported in the processor. Each bit, starting from bit
1, corresponds to a specific resource type if the bit is set. The bit position corresponds to the sub-leaf index (or
ResID) that software must use to query QoS enforcement capability available for that type.

When CPUID executes with EAX set to 10H and ECX = n (n >= 1, and is a valid ResID), the processor returns information
about available classes of service and range of QoS mask MSRs that software can use to configure each
class of services using capability bit masks in the QoS Mask registers, IA32_resourceType_Mask_n.
"""


CPUID_INTEL_RDT_ALLOCATION = 0x10


class CpuidEax10Ecx00(Ia32Struct):
    """@brief Intel Resource Director Technology (Intel RDT) Allocation Enumeration Sub-leaf (EAX = 10H, ECX = 0)

Intel Resource Director Technology (Intel RDT) Allocation Enumeration Sub-leaf (EAX = 10H, ECX = 0)."""
    class _MemberContainerCpuidEax(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax10Ecx00._MemberContainerCpuidEax, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        IA32_PLATFORM_DCA_CAP = Ia32BitFieldMember(
            "IA32_PLATFORM_DCA_CAP",
            """
            @brief Value of bits [31:0] of IA32_PLATFORM_DCA_CAP MSR (address 1F8H)
    
    Value of bits [31:0] of IA32_PLATFORM_DCA_CAP MSR (address 1F8H).
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEbx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax10Ecx00._MemberContainerCpuidEbx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        SUPPORTS_L3_CACHE_ALLOCATION_TECHNOLOGY = Ia32BitFieldMember(
            "SUPPORTS_L3_CACHE_ALLOCATION_TECHNOLOGY",
            """
            @brief Supports L3 Cache Allocation Technology if 1
    
    Supports L3 Cache Allocation Technology if 1.
            """,
    
            1,
            1
    
        )
    
    
        SUPPORTS_L2_CACHE_ALLOCATION_TECHNOLOGY = Ia32BitFieldMember(
            "SUPPORTS_L2_CACHE_ALLOCATION_TECHNOLOGY",
            """
            @brief Supports L2 Cache Allocation Technology if 1
    
    Supports L2 Cache Allocation Technology if 1.
            """,
    
            2,
            1
    
        )
    
    
        SUPPORTS_MEMORY_BANDWIDTH_ALLOCATION = Ia32BitFieldMember(
            "SUPPORTS_MEMORY_BANDWIDTH_ALLOCATION",
            """
            @brief Supports Memory Bandwidth Allocation if 1
    
    Supports Memory Bandwidth Allocation if 1.
            """,
    
            3,
            1
    
        )
    
    
    
    class _MemberContainerCpuidEcx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax10Ecx00._MemberContainerCpuidEcx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        RESERVED = Ia32BitFieldMember(
            "RESERVED",
            """
            @brief ECX is reserved
    
    ECX is reserved.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEdx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax10Ecx00._MemberContainerCpuidEdx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        RESERVED = Ia32BitFieldMember(
            "RESERVED",
            """
            @brief EDX is reserved
    
    EDX is reserved.
            """,
    
            0,
            32
    
        )
    
    
    
    _members = ["CPUID_EAX","CPUID_EBX","CPUID_ECX","CPUID_EDX",]

    def __init__(self, value):
        self._CPUID_EAX = self._MemberContainerCpuidEax(0, 0, 4 )
        self._CPUID_EBX = self._MemberContainerCpuidEbx(0, 4, 4 )
        self._CPUID_ECX = self._MemberContainerCpuidEcx(0, 8, 4 )
        self._CPUID_EDX = self._MemberContainerCpuidEdx(0, 12, 4 )
        super(CpuidEax10Ecx00, self).__init__(value)


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


class CpuidEax10Ecx01(Ia32Struct):
    """@brief L3 Cache Allocation Technology Enumeration Sub-leaf (EAX = 10H, ECX = ResID = 1)

L3 Cache Allocation Technology Enumeration Sub-leaf (EAX = 10H, ECX = ResID = 1)."""
    class _MemberContainerCpuidEax(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax10Ecx01._MemberContainerCpuidEax, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        LENGTH_OF_CAPACITY_BIT_MASK = Ia32BitFieldMember(
            "LENGTH_OF_CAPACITY_BIT_MASK",
            """
            @brief Length of the capacity bit mask for the corresponding ResID using minus-one notation
    
    Length of the capacity bit mask for the corresponding ResID using minus-one notation.
            """,
    
            0,
            5
    
        )
    
    
    
    class _MemberContainerCpuidEbx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax10Ecx01._MemberContainerCpuidEbx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        EBX_0 = Ia32BitFieldMember(
            "EBX_0",
            """
            @brief Bit-granular map of isolation/contention of allocation units
    
    Bit-granular map of isolation/contention of allocation units.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEcx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax10Ecx01._MemberContainerCpuidEcx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        CODE_AND_DATA_PRIORIZATION_TECHNOLOGY_SUPPORTED = Ia32BitFieldMember(
            "CODE_AND_DATA_PRIORIZATION_TECHNOLOGY_SUPPORTED",
            """
            @brief Code and Data Prioritization Technology supported if 1
    
    Code and Data Prioritization Technology supported if 1.
            """,
    
            2,
            1
    
        )
    
    
    
    class _MemberContainerCpuidEdx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax10Ecx01._MemberContainerCpuidEdx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        HIGHEST_COS_NUMBER_SUPPORTED = Ia32BitFieldMember(
            "HIGHEST_COS_NUMBER_SUPPORTED",
            """
            @brief Highest COS number supported for this ResID
    
    Highest COS number supported for this ResID.
            """,
    
            0,
            16
    
        )
    
    
    
    _members = ["CPUID_EAX","CPUID_EBX","CPUID_ECX","CPUID_EDX",]

    def __init__(self, value):
        self._CPUID_EAX = self._MemberContainerCpuidEax(0, 0, 4 )
        self._CPUID_EBX = self._MemberContainerCpuidEbx(0, 4, 4 )
        self._CPUID_ECX = self._MemberContainerCpuidEcx(0, 8, 4 )
        self._CPUID_EDX = self._MemberContainerCpuidEdx(0, 12, 4 )
        super(CpuidEax10Ecx01, self).__init__(value)


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


class CpuidEax10Ecx02(Ia32Struct):
    """@brief L2 Cache Allocation Technology Enumeration Sub-leaf (EAX = 10H, ECX = ResID = 2)

L2 Cache Allocation Technology Enumeration Sub-leaf (EAX = 10H, ECX = ResID = 2)."""
    class _MemberContainerCpuidEax(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax10Ecx02._MemberContainerCpuidEax, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        LENGTH_OF_CAPACITY_BIT_MASK = Ia32BitFieldMember(
            "LENGTH_OF_CAPACITY_BIT_MASK",
            """
            @brief Length of the capacity bit mask for the corresponding ResID using minus-one notation
    
    Length of the capacity bit mask for the corresponding ResID using minus-one notation.
            """,
    
            0,
            5
    
        )
    
    
    
    class _MemberContainerCpuidEbx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax10Ecx02._MemberContainerCpuidEbx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        EBX_0 = Ia32BitFieldMember(
            "EBX_0",
            """
            @brief Bit-granular map of isolation/contention of allocation units
    
    Bit-granular map of isolation/contention of allocation units.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEcx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax10Ecx02._MemberContainerCpuidEcx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        RESERVED = Ia32BitFieldMember(
            "RESERVED",
            """
            @brief ECX is reserved
    
    ECX is reserved.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEdx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax10Ecx02._MemberContainerCpuidEdx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        HIGHEST_COS_NUMBER_SUPPORTED = Ia32BitFieldMember(
            "HIGHEST_COS_NUMBER_SUPPORTED",
            """
            @brief Highest COS number supported for this ResID
    
    Highest COS number supported for this ResID.
            """,
    
            0,
            16
    
        )
    
    
    
    _members = ["CPUID_EAX","CPUID_EBX","CPUID_ECX","CPUID_EDX",]

    def __init__(self, value):
        self._CPUID_EAX = self._MemberContainerCpuidEax(0, 0, 4 )
        self._CPUID_EBX = self._MemberContainerCpuidEbx(0, 4, 4 )
        self._CPUID_ECX = self._MemberContainerCpuidEcx(0, 8, 4 )
        self._CPUID_EDX = self._MemberContainerCpuidEdx(0, 12, 4 )
        super(CpuidEax10Ecx02, self).__init__(value)


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


class CpuidEax10Ecx03(Ia32Struct):
    """@brief Memory Bandwidth Allocation Enumeration Sub-leaf (EAX = 10H, ECX = ResID = 3)

Memory Bandwidth Allocation Enumeration Sub-leaf (EAX = 10H, ECX = ResID = 3)."""
    class _MemberContainerCpuidEax(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax10Ecx03._MemberContainerCpuidEax, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        MAX_MBA_THROTTLING_VALUE = Ia32BitFieldMember(
            "MAX_MBA_THROTTLING_VALUE",
            """
            @brief Reports the maximum MBA throttling value supported for the corresponding ResID using
    minus-one notation
    
    Reports the maximum MBA throttling value supported for the corresponding ResID using
    minus-one notation.
            """,
    
            0,
            12
    
        )
    
    
    
    class _MemberContainerCpuidEbx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax10Ecx03._MemberContainerCpuidEbx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        RESERVED = Ia32BitFieldMember(
            "RESERVED",
            """
            @brief EBX is reserved
    
    EBX is reserved.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEcx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax10Ecx03._MemberContainerCpuidEcx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        RESPONSE_OF_DELAY_IS_LINEAR = Ia32BitFieldMember(
            "RESPONSE_OF_DELAY_IS_LINEAR",
            """
            @brief Reports whether the response of the delay values is linear
    
    Reports whether the response of the delay values is linear.
            """,
    
            2,
            1
    
        )
    
    
    
    class _MemberContainerCpuidEdx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax10Ecx03._MemberContainerCpuidEdx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        HIGHEST_COS_NUMBER_SUPPORTED = Ia32BitFieldMember(
            "HIGHEST_COS_NUMBER_SUPPORTED",
            """
            @brief Highest COS number supported for this ResID
    
    Highest COS number supported for this ResID.
            """,
    
            0,
            16
    
        )
    
    
    
    _members = ["CPUID_EAX","CPUID_EBX","CPUID_ECX","CPUID_EDX",]

    def __init__(self, value):
        self._CPUID_EAX = self._MemberContainerCpuidEax(0, 0, 4 )
        self._CPUID_EBX = self._MemberContainerCpuidEbx(0, 4, 4 )
        self._CPUID_ECX = self._MemberContainerCpuidEcx(0, 8, 4 )
        self._CPUID_EDX = self._MemberContainerCpuidEdx(0, 12, 4 )
        super(CpuidEax10Ecx03, self).__init__(value)


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


