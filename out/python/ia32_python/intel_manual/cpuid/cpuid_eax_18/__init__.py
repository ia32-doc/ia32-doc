from future.utils import with_metaclass
from ia32_python.utils.ia32_struct import *
from ia32_python.utils.ia32_enum import *
from ia32_python.utils.ia32_bit_field import *


__doc__ = """
@brief EAX = 0x18

When CPUID executes with EAX set to 18H, the processor returns information about the Deterministic Address
Translation Parameters.
"""


CPUID_DETERMINISTIC_ADDRESS_TRANSLATION_PARAMETERS = 0x18


class CpuidEax18Ecx00(Ia32Struct):
    """@brief Deterministic Address Translation Parameters Main Leaf (EAX = 18H, ECX = 0)

Deterministic Address Translation Parameters Main Leaf (EAX = 18H, ECX = 0)."""
    class _MemberContainerCpuidEax(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax18Ecx00._MemberContainerCpuidEax, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        MAX_SUB_LEAF = Ia32BitFieldMember(
            "MAX_SUB_LEAF",
            """
            @brief Reports the maximum input value of supported sub-leaf in leaf 18H
    
    Reports the maximum input value of supported sub-leaf in leaf 18H.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEbx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax18Ecx00._MemberContainerCpuidEbx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        PAGE_ENTRIES_4KB_SUPPORTED = Ia32BitFieldMember(
            "PAGE_ENTRIES_4KB_SUPPORTED",
            """
            @brief 4K page size entries supported by this structure
    
    4K page size entries supported by this structure.
            """,
    
            0,
            1
    
        )
    
    
        PAGE_ENTRIES_2MB_SUPPORTED = Ia32BitFieldMember(
            "PAGE_ENTRIES_2MB_SUPPORTED",
            """
            @brief 2MB page size entries supported by this structure
    
    2MB page size entries supported by this structure.
            """,
    
            1,
            1
    
        )
    
    
        PAGE_ENTRIES_4MB_SUPPORTED = Ia32BitFieldMember(
            "PAGE_ENTRIES_4MB_SUPPORTED",
            """
            @brief 4MB page size entries supported by this structure
    
    4MB page size entries supported by this structure.
            """,
    
            2,
            1
    
        )
    
    
        PAGE_ENTRIES_1GB_SUPPORTED = Ia32BitFieldMember(
            "PAGE_ENTRIES_1GB_SUPPORTED",
            """
            @brief 1 GB page size entries supported by this structure
    
    1 GB page size entries supported by this structure.
            """,
    
            3,
            1
    
        )
    
    
        PARTITIONING = Ia32BitFieldMember(
            "PARTITIONING",
            """
            @brief Partitioning (0: Soft partitioning between the logical processors sharing this structure)
    
    Partitioning (0: Soft partitioning between the logical processors sharing this structure).
            """,
    
            8,
            3
    
        )
    
    
        W = Ia32BitFieldMember(
            "W",
            """
            @brief W = Ways of associativity
    
    W = Ways of associativity.
            """,
    
            16,
            16
    
        )
    
    
    
    class _MemberContainerCpuidEcx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax18Ecx00._MemberContainerCpuidEcx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        S = Ia32BitFieldMember(
            "S",
            """
            @brief Number of Sets
    
    Number of Sets.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEdx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax18Ecx00._MemberContainerCpuidEdx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        TRANSLATION_CACHE_TYPE_FIELD = Ia32BitFieldMember(
            "TRANSLATION_CACHE_TYPE_FIELD",
            """
            @brief Translation cache type field.
    
    - 00000b: Null (indicates this sub-leaf is not valid).
    
    - 00001b: Data TLB.
    
    - 00010b: Instruction TLB.
    
    - 00011b: Unified TLB.
    
    All other encodings are reserved
    
    Translation cache type field.
    
    - 00000b: Null (indicates this sub-leaf is not valid).
    
    - 00001b: Data TLB.
    
    - 00010b: Instruction TLB.
    
    - 00011b: Unified TLB.
    
    All other encodings are reserved.
            """,
    
            0,
            5
    
        )
    
    
        TRANSLATION_CACHE_LEVEL = Ia32BitFieldMember(
            "TRANSLATION_CACHE_LEVEL",
            """
            @brief Translation cache level (starts at 1)
    
    Translation cache level (starts at 1).
            """,
    
            5,
            3
    
        )
    
    
        FULLY_ASSOCIATIVE_STRUCTURE = Ia32BitFieldMember(
            "FULLY_ASSOCIATIVE_STRUCTURE",
            """
            @brief Fully associative structure
    
    Fully associative structure.
            """,
    
            8,
            1
    
        )
    
    
        MAX_ADDRESSABLE_IDS_FOR_LOGICAL_PROCESSORS = Ia32BitFieldMember(
            "MAX_ADDRESSABLE_IDS_FOR_LOGICAL_PROCESSORS",
            """
            @brief Maximum number of addressable IDs for logical processors sharing this translation cache
    
    Maximum number of addressable IDs for logical processors sharing this translation cache.
            """,
    
            14,
            12
    
        )
    
    
    
    _members = ["CPUID_EAX","CPUID_EBX","CPUID_ECX","CPUID_EDX",]

    def __init__(self, value):
        self._CPUID_EAX = self._MemberContainerCpuidEax(0, 0, 4 )
        self._CPUID_EBX = self._MemberContainerCpuidEbx(0, 4, 4 )
        self._CPUID_ECX = self._MemberContainerCpuidEcx(0, 8, 4 )
        self._CPUID_EDX = self._MemberContainerCpuidEdx(0, 12, 4 )
        super(CpuidEax18Ecx00, self).__init__(value)


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


class CpuidEax18Ecx01p(Ia32Struct):
    """@brief Deterministic Address Translation Parameters Sub-leaf (EAX = 18H, ECX  1)

Deterministic Address Translation Parameters Sub-leaf (EAX = 18H, ECX  1)."""
    class _MemberContainerCpuidEax(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax18Ecx01p._MemberContainerCpuidEax, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        RESERVED = Ia32BitFieldMember(
            "RESERVED",
            """
            @brief EAX is reserved
    
    EAX is reserved.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEbx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax18Ecx01p._MemberContainerCpuidEbx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        PAGE_ENTRIES_4KB_SUPPORTED = Ia32BitFieldMember(
            "PAGE_ENTRIES_4KB_SUPPORTED",
            """
            @brief 4K page size entries supported by this structure
    
    4K page size entries supported by this structure.
            """,
    
            0,
            1
    
        )
    
    
        PAGE_ENTRIES_2MB_SUPPORTED = Ia32BitFieldMember(
            "PAGE_ENTRIES_2MB_SUPPORTED",
            """
            @brief 2MB page size entries supported by this structure
    
    2MB page size entries supported by this structure.
            """,
    
            1,
            1
    
        )
    
    
        PAGE_ENTRIES_4MB_SUPPORTED = Ia32BitFieldMember(
            "PAGE_ENTRIES_4MB_SUPPORTED",
            """
            @brief 4MB page size entries supported by this structure
    
    4MB page size entries supported by this structure.
            """,
    
            2,
            1
    
        )
    
    
        PAGE_ENTRIES_1GB_SUPPORTED = Ia32BitFieldMember(
            "PAGE_ENTRIES_1GB_SUPPORTED",
            """
            @brief 1 GB page size entries supported by this structure
    
    1 GB page size entries supported by this structure.
            """,
    
            3,
            1
    
        )
    
    
        PARTITIONING = Ia32BitFieldMember(
            "PARTITIONING",
            """
            @brief Partitioning (0: Soft partitioning between the logical processors sharing this structure)
    
    Partitioning (0: Soft partitioning between the logical processors sharing this structure).
            """,
    
            8,
            3
    
        )
    
    
        W = Ia32BitFieldMember(
            "W",
            """
            @brief W = Ways of associativity
    
    W = Ways of associativity.
            """,
    
            16,
            16
    
        )
    
    
    
    class _MemberContainerCpuidEcx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax18Ecx01p._MemberContainerCpuidEcx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        S = Ia32BitFieldMember(
            "S",
            """
            @brief Number of Sets
    
    Number of Sets.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEdx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax18Ecx01p._MemberContainerCpuidEdx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        TRANSLATION_CACHE_TYPE_FIELD = Ia32BitFieldMember(
            "TRANSLATION_CACHE_TYPE_FIELD",
            """
            @brief Translation cache type field.
    
    - 00000b: Null (indicates this sub-leaf is not valid).
    
    - 00001b: Data TLB.
    
    - 00010b: Instruction TLB.
    
    - 00011b: Unified TLB.
    
    All other encodings are reserved
    
    Translation cache type field.
    
    - 00000b: Null (indicates this sub-leaf is not valid).
    
    - 00001b: Data TLB.
    
    - 00010b: Instruction TLB.
    
    - 00011b: Unified TLB.
    
    All other encodings are reserved.
            """,
    
            0,
            5
    
        )
    
    
        TRANSLATION_CACHE_LEVEL = Ia32BitFieldMember(
            "TRANSLATION_CACHE_LEVEL",
            """
            @brief Translation cache level (starts at 1)
    
    Translation cache level (starts at 1).
            """,
    
            5,
            3
    
        )
    
    
        FULLY_ASSOCIATIVE_STRUCTURE = Ia32BitFieldMember(
            "FULLY_ASSOCIATIVE_STRUCTURE",
            """
            @brief Fully associative structure
    
    Fully associative structure.
            """,
    
            8,
            1
    
        )
    
    
        MAX_ADDRESSABLE_IDS_FOR_LOGICAL_PROCESSORS = Ia32BitFieldMember(
            "MAX_ADDRESSABLE_IDS_FOR_LOGICAL_PROCESSORS",
            """
            @brief Maximum number of addressable IDs for logical processors sharing this translation cache
    
    Maximum number of addressable IDs for logical processors sharing this translation cache.
            """,
    
            14,
            12
    
        )
    
    
    
    _members = ["CPUID_EAX","CPUID_EBX","CPUID_ECX","CPUID_EDX",]

    def __init__(self, value):
        self._CPUID_EAX = self._MemberContainerCpuidEax(0, 0, 4 )
        self._CPUID_EBX = self._MemberContainerCpuidEbx(0, 4, 4 )
        self._CPUID_ECX = self._MemberContainerCpuidEcx(0, 8, 4 )
        self._CPUID_EDX = self._MemberContainerCpuidEdx(0, 12, 4 )
        super(CpuidEax18Ecx01p, self).__init__(value)


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


CPUID_EXTENDED_FUNCTION = 0x80000000


class CpuidEax80000000(Ia32Struct):
    """"""
    class _MemberContainerCpuidEax(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax80000000._MemberContainerCpuidEax, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        MAX_EXTENDED_FUNCTIONS = Ia32BitFieldMember(
            "MAX_EXTENDED_FUNCTIONS",
            """
            @brief Maximum Input Value for Extended Function CPUID Information
    
    Maximum Input Value for Extended Function CPUID Information.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEbx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax80000000._MemberContainerCpuidEbx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
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
            super(CpuidEax80000000._MemberContainerCpuidEcx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
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
            super(CpuidEax80000000._MemberContainerCpuidEdx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
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
        super(CpuidEax80000000, self).__init__(value)


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


CPUID_EXTENDED_CPU_SIGNATURE = 0x80000001


class CpuidEax80000001(Ia32Struct):
    """"""
    class _MemberContainerCpuidEax(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax80000001._MemberContainerCpuidEax, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        RESERVED = Ia32BitFieldMember(
            "RESERVED",
            """
            @brief EAX is reserved
    
    EAX is reserved.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEbx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax80000001._MemberContainerCpuidEbx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
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
            super(CpuidEax80000001._MemberContainerCpuidEcx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        LAHF_SAHF_AVAILABLE_IN_64_BIT_MODE = Ia32BitFieldMember(
            "LAHF_SAHF_AVAILABLE_IN_64_BIT_MODE",
            """
            @brief LAHF/SAHF available in 64-bit mode
    
    LAHF/SAHF available in 64-bit mode.
            """,
    
            0,
            1
    
        )
    
    
        LZCNT = Ia32BitFieldMember(
            "LZCNT",
            """
            @brief LZCNT
    
    LZCNT.
            """,
    
            5,
            1
    
        )
    
    
        PREFETCHW = Ia32BitFieldMember(
            "PREFETCHW",
            """
            @brief PREFETCHW
    
    PREFETCHW.
            """,
    
            8,
            1
    
        )
    
    
    
    class _MemberContainerCpuidEdx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax80000001._MemberContainerCpuidEdx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        SYSCALL_SYSRET_AVAILABLE_IN_64_BIT_MODE = Ia32BitFieldMember(
            "SYSCALL_SYSRET_AVAILABLE_IN_64_BIT_MODE",
            """
            @brief SYSCALL/SYSRET available in 64-bit mode
    
    SYSCALL/SYSRET available in 64-bit mode.
            """,
    
            11,
            1
    
        )
    
    
        XD_AVAILABLE = Ia32BitFieldMember(
            "XD_AVAILABLE",
            """
            @brief Execute Disable Bit available
    
    Execute Disable Bit available.
            """,
    
            20,
            1
    
        )
    
    
        PAGES_1GB_AVAILABLE = Ia32BitFieldMember(
            "PAGES_1GB_AVAILABLE",
            """
            @brief 1-GByte pages are available if 1
    
    1-GByte pages are available if 1.
            """,
    
            26,
            1
    
        )
    
    
        RDTSCP_AVAILABLE = Ia32BitFieldMember(
            "RDTSCP_AVAILABLE",
            """
            @brief RDTSCP and IA32_TSC_AUX are available if 1
    
    RDTSCP and IA32_TSC_AUX are available if 1.
            """,
    
            27,
            1
    
        )
    
    
        IA64_AVAILABLE = Ia32BitFieldMember(
            "IA64_AVAILABLE",
            """
            @brief Intel 64 Architecture available if 1
    
    Intel 64 Architecture available if 1.
            """,
    
            29,
            1
    
        )
    
    
    
    _members = ["CPUID_EAX","CPUID_EBX","CPUID_ECX","CPUID_EDX",]

    def __init__(self, value):
        self._CPUID_EAX = self._MemberContainerCpuidEax(0, 0, 4 )
        self._CPUID_EBX = self._MemberContainerCpuidEbx(0, 4, 4 )
        self._CPUID_ECX = self._MemberContainerCpuidEcx(0, 8, 4 )
        self._CPUID_EDX = self._MemberContainerCpuidEdx(0, 12, 4 )
        super(CpuidEax80000001, self).__init__(value)


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


CPUID_BRAND_STRING1 = 0x80000002


CPUID_BRAND_STRING2 = 0x80000003


CPUID_BRAND_STRING3 = 0x80000004


class CpuidEax80000002(Ia32Struct):
    """"""
    class _MemberContainerCpuidEax(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax80000002._MemberContainerCpuidEax, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        PROCESSOR_BRAND_STRING_1 = Ia32BitFieldMember(
            "PROCESSOR_BRAND_STRING_1",
            """
            @brief Processor Brand String
    
    Processor Brand String.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEbx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax80000002._MemberContainerCpuidEbx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        PROCESSOR_BRAND_STRING_2 = Ia32BitFieldMember(
            "PROCESSOR_BRAND_STRING_2",
            """
            @brief Processor Brand String Continued
    
    Processor Brand String Continued.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEcx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax80000002._MemberContainerCpuidEcx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        PROCESSOR_BRAND_STRING_3 = Ia32BitFieldMember(
            "PROCESSOR_BRAND_STRING_3",
            """
            @brief Processor Brand String Continued
    
    Processor Brand String Continued.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEdx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax80000002._MemberContainerCpuidEdx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        PROCESSOR_BRAND_STRING_4 = Ia32BitFieldMember(
            "PROCESSOR_BRAND_STRING_4",
            """
            @brief Processor Brand String Continued
    
    Processor Brand String Continued.
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
        super(CpuidEax80000002, self).__init__(value)


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


class CpuidEax80000003(Ia32Struct):
    """@brief Extended Function CPUID Information

Extended Function CPUID Information."""
    class _MemberContainerCpuidEax(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax80000003._MemberContainerCpuidEax, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        PROCESSOR_BRAND_STRING_5 = Ia32BitFieldMember(
            "PROCESSOR_BRAND_STRING_5",
            """
            @brief Processor Brand String Continued
    
    Processor Brand String Continued.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEbx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax80000003._MemberContainerCpuidEbx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        PROCESSOR_BRAND_STRING_6 = Ia32BitFieldMember(
            "PROCESSOR_BRAND_STRING_6",
            """
            @brief Processor Brand String Continued
    
    Processor Brand String Continued.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEcx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax80000003._MemberContainerCpuidEcx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        PROCESSOR_BRAND_STRING_7 = Ia32BitFieldMember(
            "PROCESSOR_BRAND_STRING_7",
            """
            @brief Processor Brand String Continued
    
    Processor Brand String Continued.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEdx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax80000003._MemberContainerCpuidEdx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        PROCESSOR_BRAND_STRING_8 = Ia32BitFieldMember(
            "PROCESSOR_BRAND_STRING_8",
            """
            @brief Processor Brand String Continued
    
    Processor Brand String Continued.
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
        super(CpuidEax80000003, self).__init__(value)


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


class CpuidEax80000004(Ia32Struct):
    """@brief Extended Function CPUID Information

Extended Function CPUID Information."""
    class _MemberContainerCpuidEax(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax80000004._MemberContainerCpuidEax, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        PROCESSOR_BRAND_STRING_9 = Ia32BitFieldMember(
            "PROCESSOR_BRAND_STRING_9",
            """
            @brief Processor Brand String Continued
    
    Processor Brand String Continued.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEbx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax80000004._MemberContainerCpuidEbx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        PROCESSOR_BRAND_STRING_10 = Ia32BitFieldMember(
            "PROCESSOR_BRAND_STRING_10",
            """
            @brief Processor Brand String Continued
    
    Processor Brand String Continued.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEcx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax80000004._MemberContainerCpuidEcx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        PROCESSOR_BRAND_STRING_11 = Ia32BitFieldMember(
            "PROCESSOR_BRAND_STRING_11",
            """
            @brief Processor Brand String Continued
    
    Processor Brand String Continued.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEdx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax80000004._MemberContainerCpuidEdx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        PROCESSOR_BRAND_STRING_12 = Ia32BitFieldMember(
            "PROCESSOR_BRAND_STRING_12",
            """
            @brief Processor Brand String Continued
    
    Processor Brand String Continued.
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
        super(CpuidEax80000004, self).__init__(value)


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


class CpuidEax80000005(Ia32Struct):
    """@brief Extended Function CPUID Information

Extended Function CPUID Information."""
    class _MemberContainerCpuidEax(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax80000005._MemberContainerCpuidEax, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        RESERVED = Ia32BitFieldMember(
            "RESERVED",
            """
            @brief EAX is reserved
    
    EAX is reserved.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEbx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax80000005._MemberContainerCpuidEbx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
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
            super(CpuidEax80000005._MemberContainerCpuidEcx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
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
            super(CpuidEax80000005._MemberContainerCpuidEdx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
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
        super(CpuidEax80000005, self).__init__(value)


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


CPUID_EXTENDED_CACHE_INFO = 0x80000006


class CpuidEax80000006(Ia32Struct):
    """"""
    class _MemberContainerCpuidEax(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax80000006._MemberContainerCpuidEax, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        RESERVED = Ia32BitFieldMember(
            "RESERVED",
            """
            @brief EAX is reserved
    
    EAX is reserved.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEbx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax80000006._MemberContainerCpuidEbx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
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
            super(CpuidEax80000006._MemberContainerCpuidEcx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        CACHE_LINE_SIZE_IN_BYTES = Ia32BitFieldMember(
            "CACHE_LINE_SIZE_IN_BYTES",
            """
            @brief Cache Line size in bytes
    
    Cache Line size in bytes.
            """,
    
            0,
            8
    
        )
    
    
        L2_ASSOCIATIVITY_FIELD = Ia32BitFieldMember(
            "L2_ASSOCIATIVITY_FIELD",
            """
            @brief L2 Associativity field.
    
    L2 associativity field encodings:
    
    - 00H - Disabled.
    
    - 01H - Direct mapped.
    
    - 02H - 2-way.
    
    - 04H - 4-way.
    
    - 06H - 8-way.
    
    - 08H - 16-way.
    
    - 0FH - Fully associative
    
    L2 Associativity field.
    
    L2 associativity field encodings:
    
    - 00H - Disabled.
    
    - 01H - Direct mapped.
    
    - 02H - 2-way.
    
    - 04H - 4-way.
    
    - 06H - 8-way.
    
    - 08H - 16-way.
    
    - 0FH - Fully associative.
            """,
    
            12,
            4
    
        )
    
    
        CACHE_SIZE_IN_1K_UNITS = Ia32BitFieldMember(
            "CACHE_SIZE_IN_1K_UNITS",
            """
            @brief Cache size in 1K units
    
    Cache size in 1K units.
            """,
    
            16,
            16
    
        )
    
    
    
    class _MemberContainerCpuidEdx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax80000006._MemberContainerCpuidEdx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
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
        super(CpuidEax80000006, self).__init__(value)


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


CPUID_EXTENDED_TIME_STAMP_COUNTER = 0x80000007


class CpuidEax80000007(Ia32Struct):
    """"""
    class _MemberContainerCpuidEax(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax80000007._MemberContainerCpuidEax, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        RESERVED = Ia32BitFieldMember(
            "RESERVED",
            """
            @brief EAX is reserved
    
    EAX is reserved.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEbx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax80000007._MemberContainerCpuidEbx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
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
            super(CpuidEax80000007._MemberContainerCpuidEcx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
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
            super(CpuidEax80000007._MemberContainerCpuidEdx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        INVARIANT_TSC_AVAILABLE = Ia32BitFieldMember(
            "INVARIANT_TSC_AVAILABLE",
            """
            @brief Invariant TSC available if 1
    
    Invariant TSC available if 1.
            """,
    
            8,
            1
    
        )
    
    
    
    _members = ["CPUID_EAX","CPUID_EBX","CPUID_ECX","CPUID_EDX",]

    def __init__(self, value):
        self._CPUID_EAX = self._MemberContainerCpuidEax(0, 0, 4 )
        self._CPUID_EBX = self._MemberContainerCpuidEbx(0, 4, 4 )
        self._CPUID_ECX = self._MemberContainerCpuidEcx(0, 8, 4 )
        self._CPUID_EDX = self._MemberContainerCpuidEdx(0, 12, 4 )
        super(CpuidEax80000007, self).__init__(value)


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


