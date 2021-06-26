from future.utils import with_metaclass
from ia32_python.utils.ia32_struct import *
from ia32_python.utils.ia32_enum import *
from ia32_python.utils.ia32_bit_field import *


__doc__ = """
@brief EAX = 0x0D

When CPUID executes with EAX set to 0DH and ECX = 0, the processor returns information about the bit-vector
representation of all processor state extensions that are supported in the processor and storage size requirements
of the XSAVE/XRSTOR area.

When CPUID executes with EAX set to 0DH and ECX = n (n > 1, and is a valid sub-leaf index), the processor returns
information about the size and offset of each processor extended state save area within the XSAVE/XRSTOR area.
Software can use the forward-extendable technique depicted below to query the valid sub-leaves
and obtain size and offset information for each processor extended state save area:

<pre>
For i = 2 to 62 // sub-leaf 1 is reserved
  IF (CPUID.(EAX=0DH, ECX=0):VECTOR[i] = 1) // VECTOR is the 64-bit value of EDX:EAX
    Execute CPUID.(EAX=0DH, ECX = i) to examine size and offset for sub-leaf i;
  FI;
</pre>
"""


CPUID_EXTENDED_STATE = 0xd


class CpuidEax0dEcx00(Ia32Struct):
    """@brief Processor Extended State Enumeration Main Leaf (EAX = 0DH, ECX = 0)

Processor Extended State Enumeration Main Leaf (EAX = 0DH, ECX = 0)."""
    class _MemberContainerCpuidEax(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        @brief Reports the supported bits of the lower 32 bits of XCR0. XCR0[n] can be set to 1 only if EAX[n] is 1
    
    Reports the supported bits of the lower 32 bits of XCR0. XCR0[n] can be set to 1 only if EAX[n] is 1.
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax0dEcx00._MemberContainerCpuidEax, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        X87_STATE = Ia32BitFieldMember(
            "X87_STATE",
            """
            @brief x87 state
    
    x87 state.
            """,
    
            0,
            1
    
        )
    
    
        SSE_STATE = Ia32BitFieldMember(
            "SSE_STATE",
            """
            @brief SSE state
    
    SSE state.
            """,
    
            1,
            1
    
        )
    
    
        AVX_STATE = Ia32BitFieldMember(
            "AVX_STATE",
            """
            @brief AVX state
    
    AVX state.
            """,
    
            2,
            1
    
        )
    
    
        MPX_STATE = Ia32BitFieldMember(
            "MPX_STATE",
            """
            @brief MPX state
    
    MPX state.
            """,
    
            3,
            2
    
        )
    
    
        AVX_512_STATE = Ia32BitFieldMember(
            "AVX_512_STATE",
            """
            @brief AVX-512 state
    
    AVX-512 state.
            """,
    
            5,
            3
    
        )
    
    
        USED_FOR_IA32_XSS_1 = Ia32BitFieldMember(
            "USED_FOR_IA32_XSS_1",
            """
            @brief Used for IA32_XSS
    
    Used for IA32_XSS.
            """,
    
            8,
            1
    
        )
    
    
        PKRU_STATE = Ia32BitFieldMember(
            "PKRU_STATE",
            """
            @brief PKRU state
    
    PKRU state.
            """,
    
            9,
            1
    
        )
    
    
        USED_FOR_IA32_XSS_2 = Ia32BitFieldMember(
            "USED_FOR_IA32_XSS_2",
            """
            @brief Used for IA32_XSS
    
    Used for IA32_XSS.
            """,
    
            13,
            1
    
        )
    
    
    
    class _MemberContainerCpuidEbx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax0dEcx00._MemberContainerCpuidEbx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        MAX_SIZE_REQUIRED_BY_ENABLED_FEATURES_IN_XCR0 = Ia32BitFieldMember(
            "MAX_SIZE_REQUIRED_BY_ENABLED_FEATURES_IN_XCR0",
            """
            @brief Maximum size (bytes, from the beginning of the XSAVE/XRSTOR save area) required by
    enabled features in XCR0. May be different than ECX if some features at the end of the XSAVE save area
    are not enabled
    
    Maximum size (bytes, from the beginning of the XSAVE/XRSTOR save area) required by
    enabled features in XCR0. May be different than ECX if some features at the end of the XSAVE save area
    are not enabled.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEcx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax0dEcx00._MemberContainerCpuidEcx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        MAX_SIZE_OF_XSAVE_XRSTOR_SAVE_AREA = Ia32BitFieldMember(
            "MAX_SIZE_OF_XSAVE_XRSTOR_SAVE_AREA",
            """
            @brief Maximum size (bytes, from the beginning of the XSAVE/XRSTOR save area) of the
    XSAVE/XRSTOR save area required by all supported features in the processor, i.e., all the valid bit fields in
    XCR0
    
    Maximum size (bytes, from the beginning of the XSAVE/XRSTOR save area) of the
    XSAVE/XRSTOR save area required by all supported features in the processor, i.e., all the valid bit fields in
    XCR0.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEdx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax0dEcx00._MemberContainerCpuidEdx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        XCR0_SUPPORTED_BITS = Ia32BitFieldMember(
            "XCR0_SUPPORTED_BITS",
            """
            @brief Reports the supported bits of the upper 32 bits of XCR0. XCR0[n+32] can be set to 1 only if EDX[n] is 1
    
    Reports the supported bits of the upper 32 bits of XCR0. XCR0[n+32] can be set to 1 only if EDX[n] is 1.
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
        super(CpuidEax0dEcx00, self).__init__(value)


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


class CpuidEax0dEcx01(Ia32Struct):
    """@brief Direct Cache Access Information Leaf

Direct Cache Access Information Leaf."""
    class _MemberContainerCpuidEax(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax0dEcx01._MemberContainerCpuidEax, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        SUPPORTS_XSAVEC_AND_COMPACTED_XRSTOR = Ia32BitFieldMember(
            "SUPPORTS_XSAVEC_AND_COMPACTED_XRSTOR",
            """
            @brief Supports XSAVEC and the compacted form of XRSTOR if set
    
    Supports XSAVEC and the compacted form of XRSTOR if set.
            """,
    
            1,
            1
    
        )
    
    
        SUPPORTS_XGETBV_WITH_ECX_1 = Ia32BitFieldMember(
            "SUPPORTS_XGETBV_WITH_ECX_1",
            """
            @brief Supports XGETBV with ECX = 1 if set
    
    Supports XGETBV with ECX = 1 if set.
            """,
    
            2,
            1
    
        )
    
    
        SUPPORTS_XSAVE_XRSTOR_AND_IA32_XSS = Ia32BitFieldMember(
            "SUPPORTS_XSAVE_XRSTOR_AND_IA32_XSS",
            """
            @brief Supports XSAVES/XRSTORS and IA32_XSS if set
    
    Supports XSAVES/XRSTORS and IA32_XSS if set.
            """,
    
            3,
            1
    
        )
    
    
    
    class _MemberContainerCpuidEbx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax0dEcx01._MemberContainerCpuidEbx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        SIZE_OF_XSAVE_AREAD = Ia32BitFieldMember(
            "SIZE_OF_XSAVE_AREAD",
            """
            @brief The size in bytes of the XSAVE area containing all states enabled by XCRO | IA32_XSS
    
    The size in bytes of the XSAVE area containing all states enabled by XCRO | IA32_XSS.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEcx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax0dEcx01._MemberContainerCpuidEcx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        USED_FOR_XCR0_1 = Ia32BitFieldMember(
            "USED_FOR_XCR0_1",
            """
            @brief Used for XCR0
    
    Used for XCR0.
            """,
    
            0,
            8
    
        )
    
    
        PT_STATE = Ia32BitFieldMember(
            "PT_STATE",
            """
            @brief PT state
    
    PT state.
            """,
    
            8,
            1
    
        )
    
    
        USED_FOR_XCR0_2 = Ia32BitFieldMember(
            "USED_FOR_XCR0_2",
            """
            @brief Used for XCR0
    
    Used for XCR0.
            """,
    
            9,
            1
    
        )
    
    
        HWP_STATE = Ia32BitFieldMember(
            "HWP_STATE",
            """
            @brief HWP state
    
    HWP state.
            """,
    
            13,
            1
    
        )
    
    
    
    class _MemberContainerCpuidEdx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax0dEcx01._MemberContainerCpuidEdx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
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
        super(CpuidEax0dEcx01, self).__init__(value)


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


class CpuidEax0dEcxN(Ia32Struct):
    """@brief Processor Extended State Enumeration Sub-leaves (EAX = 0DH, ECX = n, n > 1)

Processor Extended State Enumeration Sub-leaves (EAX = 0DH, ECX = n, n > 1)."""
    class _MemberContainerCpuidEax(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax0dEcxN._MemberContainerCpuidEax, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        IA32_PLATFORM_DCA_CAP = Ia32BitFieldMember(
            "IA32_PLATFORM_DCA_CAP",
            """
            @brief The size in bytes (from the offset specified in EBX) of the save area for an extended state
    feature associated with a valid sub-leaf index, n
    
    The size in bytes (from the offset specified in EBX) of the save area for an extended state
    feature associated with a valid sub-leaf index, n.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEbx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax0dEcxN._MemberContainerCpuidEbx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        RESERVED = Ia32BitFieldMember(
            "RESERVED",
            """
            @brief The offset in bytes of this extended state components save area from the beginning of the
    XSAVE/XRSTOR area.
    
    This field reports 0 if the sub-leaf index, n, does not map to a valid bit in the XCR0 register
    
    The offset in bytes of this extended state components save area from the beginning of the
    XSAVE/XRSTOR area.
    
    This field reports 0 if the sub-leaf index, n, does not map to a valid bit in the XCR0 register.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEcx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax0dEcxN._MemberContainerCpuidEcx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        ECX_2 = Ia32BitFieldMember(
            "ECX_2",
            """
            @brief Is set if the bit n (corresponding to the sub-leaf index) is supported in the IA32_XSS MSR; it is clear
    if bit n is instead supported in XCR0
    
    Is set if the bit n (corresponding to the sub-leaf index) is supported in the IA32_XSS MSR; it is clear
    if bit n is instead supported in XCR0.
            """,
    
            0,
            1
    
        )
    
    
        ECX_1 = Ia32BitFieldMember(
            "ECX_1",
            """
            @brief Is set if, when the compacted format of an XSAVE area is used, this extended state component
    located on the next 64-byte boundary following the preceding state component (otherwise, it is located
    immediately following the preceding state component)
    
    Is set if, when the compacted format of an XSAVE area is used, this extended state component
    located on the next 64-byte boundary following the preceding state component (otherwise, it is located
    immediately following the preceding state component).
            """,
    
            1,
            1
    
        )
    
    
    
    class _MemberContainerCpuidEdx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax0dEcxN._MemberContainerCpuidEdx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        RESERVED = Ia32BitFieldMember(
            "RESERVED",
            """
            @brief This field reports 0 if the sub-leaf index, n, is invalid; otherwise it is reserved
    
    This field reports 0 if the sub-leaf index, n, is invalid; otherwise it is reserved.
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
        super(CpuidEax0dEcxN, self).__init__(value)


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


