from future.utils import with_metaclass
from ia32_python.utils.ia32_struct import *
from ia32_python.utils.ia32_enum import *
from ia32_python.utils.ia32_bit_field import *


__doc__ = """
@brief EAX = 0x12

When CPUID executes with EAX set to 12H and ECX = 0H, the processor returns information about Intel SGX capabilities.

When CPUID executes with EAX set to 12H and ECX = 1H, the processor returns information about Intel SGX attributes.

When CPUID executes with EAX set to 12H and ECX = n (n > 1), the processor returns information about Intel SGX
Enclave Page Cache.
"""


CPUID_INTEL_SGX = 0x12


class CpuidEax12Ecx00(Ia32Struct):
    """@brief Intel SGX Capability Enumeration Leaf, sub-leaf 0 (EAX = 12H, ECX = 0)

Intel SGX Capability Enumeration Leaf, sub-leaf 0 (EAX = 12H, ECX = 0)."""
    class _MemberContainerCpuidEax(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax12Ecx00._MemberContainerCpuidEax, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        SGX1 = Ia32BitFieldMember(
            "SGX1",
            """
            @brief If 1, Indicates Intel SGX supports the collection of SGX1 leaf functions
    
    If 1, Indicates Intel SGX supports the collection of SGX1 leaf functions.
            """,
    
            0,
            1
    
        )
    
    
        SGX2 = Ia32BitFieldMember(
            "SGX2",
            """
            @brief If 1, Indicates Intel SGX supports the collection of SGX2 leaf functions
    
    If 1, Indicates Intel SGX supports the collection of SGX2 leaf functions.
            """,
    
            1,
            1
    
        )
    
    
        SGX_ENCLV_ADVANCED = Ia32BitFieldMember(
            "SGX_ENCLV_ADVANCED",
            """
            @brief If 1, indicates Intel SGX supports ENCLV instruction leaves EINCVIRTCHILD, EDECVIRTCHILD, and ESETCONTEXT
    
    If 1, indicates Intel SGX supports ENCLV instruction leaves EINCVIRTCHILD, EDECVIRTCHILD, and ESETCONTEXT.
            """,
    
            5,
            1
    
        )
    
    
        SGX_ENCLS_ADVANCED = Ia32BitFieldMember(
            "SGX_ENCLS_ADVANCED",
            """
            @brief If 1, indicates Intel SGX supports ENCLS instruction leaves ETRACKC, ERDINFO, ELDBC, and ELDUC
    
    If 1, indicates Intel SGX supports ENCLS instruction leaves ETRACKC, ERDINFO, ELDBC, and ELDUC.
            """,
    
            6,
            1
    
        )
    
    
    
    class _MemberContainerCpuidEbx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax12Ecx00._MemberContainerCpuidEbx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        MISCSELECT = Ia32BitFieldMember(
            "MISCSELECT",
            """
            @brief Bit vector of supported extended SGX features
    
    Bit vector of supported extended SGX features.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEcx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax12Ecx00._MemberContainerCpuidEcx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
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
            super(CpuidEax12Ecx00._MemberContainerCpuidEdx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        MAX_ENCLAVE_SIZE_NOT64 = Ia32BitFieldMember(
            "MAX_ENCLAVE_SIZE_NOT64",
            """
            @brief The maximum supported enclave size in non-64-bit mode is 2^(EDX[7:0])
    
    The maximum supported enclave size in non-64-bit mode is 2^(EDX[7:0]).
            """,
    
            0,
            8
    
        )
    
    
        MAX_ENCLAVE_SIZE_64 = Ia32BitFieldMember(
            "MAX_ENCLAVE_SIZE_64",
            """
            @brief The maximum supported enclave size in 64-bit mode is 2^(EDX[15:8])
    
    The maximum supported enclave size in 64-bit mode is 2^(EDX[15:8]).
            """,
    
            8,
            8
    
        )
    
    
    
    _members = ["CPUID_EAX","CPUID_EBX","CPUID_ECX","CPUID_EDX",]

    def __init__(self, value):
        self._CPUID_EAX = self._MemberContainerCpuidEax(0, 0, 4 )
        self._CPUID_EBX = self._MemberContainerCpuidEbx(0, 4, 4 )
        self._CPUID_ECX = self._MemberContainerCpuidEcx(0, 8, 4 )
        self._CPUID_EDX = self._MemberContainerCpuidEdx(0, 12, 4 )
        super(CpuidEax12Ecx00, self).__init__(value)


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


class CpuidEax12Ecx01(Ia32Struct):
    """@brief Intel SGX Attributes Enumeration Leaf, sub-leaf 1 (EAX = 12H, ECX = 1)

Intel SGX Attributes Enumeration Leaf, sub-leaf 1 (EAX = 12H, ECX = 1)."""
    class _MemberContainerCpuidEax(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax12Ecx01._MemberContainerCpuidEax, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        VALID_SECS_ATTRIBUTES_0 = Ia32BitFieldMember(
            "VALID_SECS_ATTRIBUTES_0",
            """
            @brief Reports the valid bits of SECS.ATTRIBUTES[31:0] that software can set with ECREATE
    
    Reports the valid bits of SECS.ATTRIBUTES[31:0] that software can set with ECREATE.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEbx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax12Ecx01._MemberContainerCpuidEbx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        VALID_SECS_ATTRIBUTES_1 = Ia32BitFieldMember(
            "VALID_SECS_ATTRIBUTES_1",
            """
            @brief Reports the valid bits of SECS.ATTRIBUTES[63:32] that software can set with ECREATE
    
    Reports the valid bits of SECS.ATTRIBUTES[63:32] that software can set with ECREATE.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEcx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax12Ecx01._MemberContainerCpuidEcx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        VALID_SECS_ATTRIBUTES_2 = Ia32BitFieldMember(
            "VALID_SECS_ATTRIBUTES_2",
            """
            @brief Reports the valid bits of SECS.ATTRIBUTES[95:64] that software can set with ECREATE
    
    Reports the valid bits of SECS.ATTRIBUTES[95:64] that software can set with ECREATE.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEdx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax12Ecx01._MemberContainerCpuidEdx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        VALID_SECS_ATTRIBUTES_3 = Ia32BitFieldMember(
            "VALID_SECS_ATTRIBUTES_3",
            """
            @brief Reports the valid bits of SECS.ATTRIBUTES[127:96] that software can set with ECREATE
    
    Reports the valid bits of SECS.ATTRIBUTES[127:96] that software can set with ECREATE.
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
        super(CpuidEax12Ecx01, self).__init__(value)


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


class CpuidEax12Ecx02pSlt0(Ia32Struct):
    """@brief Intel SGX EPC Enumeration Leaf, sub-leaves (EAX = 12H, ECX = 2 or higher)

Intel SGX EPC Enumeration Leaf, sub-leaves (EAX = 12H, ECX = 2 or higher)."""
    class _MemberContainerCpuidEax(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax12Ecx02pSlt0._MemberContainerCpuidEax, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        SUB_LEAF_TYPE = Ia32BitFieldMember(
            "SUB_LEAF_TYPE",
            """
            @brief Sub-leaf Type 0. Indicates this sub-leaf is invalid
    
    Sub-leaf Type 0. Indicates this sub-leaf is invalid.
            """,
    
            0,
            4
    
        )
    
    
    
    class _MemberContainerCpuidEbx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax12Ecx02pSlt0._MemberContainerCpuidEbx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        ZERO = Ia32BitFieldMember(
            "ZERO",
            """
            @brief EBX is zero
    
    EBX is zero.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEcx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax12Ecx02pSlt0._MemberContainerCpuidEcx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        ZERO = Ia32BitFieldMember(
            "ZERO",
            """
            @brief ECX is zero
    
    ECX is zero.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEdx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax12Ecx02pSlt0._MemberContainerCpuidEdx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        ZERO = Ia32BitFieldMember(
            "ZERO",
            """
            @brief EDX is zero
    
    EDX is zero.
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
        super(CpuidEax12Ecx02pSlt0, self).__init__(value)


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


class CpuidEax12Ecx02pSlt1(Ia32Struct):
    """@brief Intel SGX EPC Enumeration Leaf, sub-leaves (EAX = 12H, ECX = 2 or higher)

Intel SGX EPC Enumeration Leaf, sub-leaves (EAX = 12H, ECX = 2 or higher)."""
    class _MemberContainerCpuidEax(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax12Ecx02pSlt1._MemberContainerCpuidEax, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        SUB_LEAF_TYPE = Ia32BitFieldMember(
            "SUB_LEAF_TYPE",
            """
            @brief Sub-leaf Type 1. This sub-leaf enumerates an EPC section. EBX:EAX and EDX:ECX provide information on the
    Enclave Page Cache (EPC) section
    
    Sub-leaf Type 1. This sub-leaf enumerates an EPC section. EBX:EAX and EDX:ECX provide information on the
    Enclave Page Cache (EPC) section.
            """,
    
            0,
            4
    
        )
    
    
        EPC_BASE_PHYSICAL_ADDRESS_1 = Ia32BitFieldMember(
            "EPC_BASE_PHYSICAL_ADDRESS_1",
            """
            @brief Bits 31:12 of the physical address of the base of the EPC section
    
    Bits 31:12 of the physical address of the base of the EPC section.
            """,
    
            12,
            20
    
        )
    
    
    
    class _MemberContainerCpuidEbx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax12Ecx02pSlt1._MemberContainerCpuidEbx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        EPC_BASE_PHYSICAL_ADDRESS_2 = Ia32BitFieldMember(
            "EPC_BASE_PHYSICAL_ADDRESS_2",
            """
            @brief Bits 51:32 of the physical address of the base of the EPC section
    
    Bits 51:32 of the physical address of the base of the EPC section.
            """,
    
            0,
            20
    
        )
    
    
    
    class _MemberContainerCpuidEcx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax12Ecx02pSlt1._MemberContainerCpuidEcx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        EPC_SECTION_PROPERTY = Ia32BitFieldMember(
            "EPC_SECTION_PROPERTY",
            """
            @brief EPC section property encoding defined as follows:
    
    - If EAX[3:0] 0000b, then all bits of the EDX:ECX pair are enumerated as 0.
    
    - If EAX[3:0] 0001b, then this section has confidentiality and integrity protection.
    
    All other encodings are reserved
    
    EPC section property encoding defined as follows:
    
    - If EAX[3:0] 0000b, then all bits of the EDX:ECX pair are enumerated as 0.
    
    - If EAX[3:0] 0001b, then this section has confidentiality and integrity protection.
    
    All other encodings are reserved.
            """,
    
            0,
            4
    
        )
    
    
        EPC_SIZE_1 = Ia32BitFieldMember(
            "EPC_SIZE_1",
            """
            @brief Bits 31:12 of the size of the corresponding EPC section within the Processor Reserved Memory
    
    Bits 31:12 of the size of the corresponding EPC section within the Processor Reserved Memory.
            """,
    
            12,
            20
    
        )
    
    
    
    class _MemberContainerCpuidEdx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax12Ecx02pSlt1._MemberContainerCpuidEdx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        EPC_SIZE_2 = Ia32BitFieldMember(
            "EPC_SIZE_2",
            """
            @brief Bits 51:32 of the size of the corresponding EPC section within the Processor Reserved Memory
    
    Bits 51:32 of the size of the corresponding EPC section within the Processor Reserved Memory.
            """,
    
            0,
            20
    
        )
    
    
    
    _members = ["CPUID_EAX","CPUID_EBX","CPUID_ECX","CPUID_EDX",]

    def __init__(self, value):
        self._CPUID_EAX = self._MemberContainerCpuidEax(0, 0, 4 )
        self._CPUID_EBX = self._MemberContainerCpuidEbx(0, 4, 4 )
        self._CPUID_ECX = self._MemberContainerCpuidEcx(0, 8, 4 )
        self._CPUID_EDX = self._MemberContainerCpuidEdx(0, 12, 4 )
        super(CpuidEax12Ecx02pSlt1, self).__init__(value)


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


