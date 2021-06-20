from future.utils import with_metaclass
from utils.struct import *
from utils.bit_field import *


__doc__ = """
@brief EAX = 0x17

When CPUID executes with EAX set to 17H, the processor returns information about the System-On-Chip Vendor
Attribute Enumeration.
"""


CPUID_SOC_VENDOR = 0x17


class CpuidEax17Ecx00(Struct):
    """@brief System-On-Chip Vendor Attribute Enumeration Main Leaf (EAX = 17H, ECX = 0)

System-On-Chip Vendor Attribute Enumeration Main Leaf (EAX = 17H, ECX = 0)."""
    class _MemberContainerCpuidEax(with_metaclass(BitFieldMeta, BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super().__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        MAX_SOC_ID_INDEX = BitFieldMember(
            "MAX_SOC_ID_INDEX",
            """
            @brief Reports the maximum input value of supported sub-leaf in leaf 17H
    
    Reports the maximum input value of supported sub-leaf in leaf 17H.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEbx(with_metaclass(BitFieldMeta, BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super().__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        SOC_VENDOR_ID = BitFieldMember(
            "SOC_VENDOR_ID",
            """
            @brief SOC Vendor ID
    
    SOC Vendor ID.
            """,
    
            0,
            16
    
        )
    
    
        IS_VENDOR_SCHEME = BitFieldMember(
            "IS_VENDOR_SCHEME",
            """
            @brief If 1, the SOC Vendor ID field is assigned via an industry standard enumeration
    scheme. Otherwise, the SOC Vendor ID field is assigned by Intel
    
    If 1, the SOC Vendor ID field is assigned via an industry standard enumeration
    scheme. Otherwise, the SOC Vendor ID field is assigned by Intel.
            """,
    
            16,
            1
    
        )
    
    
    
    class _MemberContainerCpuidEcx(with_metaclass(BitFieldMeta, BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super().__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        PROJECT_ID = BitFieldMember(
            "PROJECT_ID",
            """
            @brief A unique number an SOC vendor assigns to its SOC projects
    
    A unique number an SOC vendor assigns to its SOC projects.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEdx(with_metaclass(BitFieldMeta, BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super().__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        STEPPING_ID = BitFieldMember(
            "STEPPING_ID",
            """
            @brief A unique number within an SOC project that an SOC vendor assigns
    
    A unique number within an SOC project that an SOC vendor assigns.
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


class CpuidEax17Ecx0103(Struct):
    """@brief System-On-Chip Vendor Attribute Enumeration Sub-leaf (EAX = 17H, ECX = 1..3)

System-On-Chip Vendor Attribute Enumeration Sub-leaf (EAX = 17H, ECX = 1..3)."""
    class _MemberContainerCpuidEax(with_metaclass(BitFieldMeta, BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super().__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        SOC_VENDOR_BRAND_STRING = BitFieldMember(
            "SOC_VENDOR_BRAND_STRING",
            """
            @brief SOC Vendor Brand String. UTF-8 encoded string
    
    SOC Vendor Brand String. UTF-8 encoded string.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEbx(with_metaclass(BitFieldMeta, BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super().__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        SOC_VENDOR_BRAND_STRING = BitFieldMember(
            "SOC_VENDOR_BRAND_STRING",
            """
            @brief SOC Vendor Brand String. UTF-8 encoded string
    
    SOC Vendor Brand String. UTF-8 encoded string.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEcx(with_metaclass(BitFieldMeta, BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super().__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        SOC_VENDOR_BRAND_STRING = BitFieldMember(
            "SOC_VENDOR_BRAND_STRING",
            """
            @brief SOC Vendor Brand String. UTF-8 encoded string
    
    SOC Vendor Brand String. UTF-8 encoded string.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEdx(with_metaclass(BitFieldMeta, BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super().__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        SOC_VENDOR_BRAND_STRING = BitFieldMember(
            "SOC_VENDOR_BRAND_STRING",
            """
            @brief SOC Vendor Brand String. UTF-8 encoded string
    
    SOC Vendor Brand String. UTF-8 encoded string.
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


class CpuidEax17EcxN(Struct):
    """@brief System-On-Chip Vendor Attribute Enumeration Sub-leaves (EAX = 17H, ECX > MaxSOCID_Index)

System-On-Chip Vendor Attribute Enumeration Sub-leaves (EAX = 17H, ECX > MaxSOCID_Index)."""
    class _MemberContainerCpuidEax(with_metaclass(BitFieldMeta, BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super().__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        RESERVED = BitFieldMember(
            "RESERVED",
            """
            @brief Reserved = 0
    
    Reserved = 0.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEbx(with_metaclass(BitFieldMeta, BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super().__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        RESERVED = BitFieldMember(
            "RESERVED",
            """
            @brief Reserved = 0
    
    Reserved = 0.
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
            @brief Reserved = 0
    
    Reserved = 0.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEdx(with_metaclass(BitFieldMeta, BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super().__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        RESERVED = BitFieldMember(
            "RESERVED",
            """
            @brief Reserved = 0
    
    Reserved = 0.
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


