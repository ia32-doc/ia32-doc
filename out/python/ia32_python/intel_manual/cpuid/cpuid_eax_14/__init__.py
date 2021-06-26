from future.utils import with_metaclass
from ia32_python.utils.ia32_struct import *
from ia32_python.utils.ia32_enum import *
from ia32_python.utils.ia32_bit_field import *


__doc__ = """
@brief EAX = 0x14

When CPUID executes with EAX set to 14H and ECX = 0H, the processor returns information about Intel Processor
Trace extensions.

When CPUID executes with EAX set to 14H and ECX = n (n > 0 and less than the number of non-zero bits in
CPUID.(EAX=14H, ECX= 0H).EAX), the processor returns information about packet generation in Intel Processor
Trace.
"""


CPUID_INTEL_PROCESSOR_TRACE = 0x14


class CpuidEax14Ecx00(Ia32Struct):
    """@brief Intel Processor Trace Enumeration Main Leaf (EAX = 14H, ECX = 0)

Intel Processor Trace Enumeration Main Leaf (EAX = 14H, ECX = 0)."""
    class _MemberContainerCpuidEax(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax14Ecx00._MemberContainerCpuidEax, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        MAX_SUB_LEAF = Ia32BitFieldMember(
            "MAX_SUB_LEAF",
            """
            @brief Reports the maximum sub-leaf supported in leaf 14H
    
    Reports the maximum sub-leaf supported in leaf 14H.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEbx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax14Ecx00._MemberContainerCpuidEbx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        FLAG0 = Ia32BitFieldMember(
            "FLAG0",
            """
            @brief If 1, indicates that IA32_RTIT_CTL.CR3Filter can be set to 1, and that IA32_RTIT_CR3_MATCH MSR can be accessed
    
    If 1, indicates that IA32_RTIT_CTL.CR3Filter can be set to 1, and that IA32_RTIT_CR3_MATCH MSR can be accessed.
            """,
    
            0,
            1
    
        )
    
    
        FLAG1 = Ia32BitFieldMember(
            "FLAG1",
            """
            @brief If 1, indicates support of Configurable PSB and Cycle-Accurate Mode
    
    If 1, indicates support of Configurable PSB and Cycle-Accurate Mode.
            """,
    
            1,
            1
    
        )
    
    
        FLAG2 = Ia32BitFieldMember(
            "FLAG2",
            """
            @brief If 1, indicates support of IP Filtering, TraceStop filtering, and preservation of Intel PT MSRs across warm reset
    
    If 1, indicates support of IP Filtering, TraceStop filtering, and preservation of Intel PT MSRs across warm reset.
            """,
    
            2,
            1
    
        )
    
    
        FLAG3 = Ia32BitFieldMember(
            "FLAG3",
            """
            @brief If 1, indicates support of MTC timing packet and suppression of COFI-based packets
    
    If 1, indicates support of MTC timing packet and suppression of COFI-based packets.
            """,
    
            3,
            1
    
        )
    
    
        FLAG4 = Ia32BitFieldMember(
            "FLAG4",
            """
            @brief If 1, indicates support of PTWRITE. Writes can set IA32_RTIT_CTL[12] (PTWEn) and IA32_RTIT_CTL[5] (FUPonPTW), and PTWRITE can generate packets
    
    If 1, indicates support of PTWRITE. Writes can set IA32_RTIT_CTL[12] (PTWEn) and IA32_RTIT_CTL[5] (FUPonPTW), and PTWRITE can generate packets.
            """,
    
            4,
            1
    
        )
    
    
        FLAG5 = Ia32BitFieldMember(
            "FLAG5",
            """
            @brief If 1, indicates support of Power Event Trace. Writes can set IA32_RTIT_CTL[4] (PwrEvtEn), enabling Power Event Trace packet generation
    
    If 1, indicates support of Power Event Trace. Writes can set IA32_RTIT_CTL[4] (PwrEvtEn), enabling Power Event Trace packet generation.
            """,
    
            5,
            1
    
        )
    
    
    
    class _MemberContainerCpuidEcx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax14Ecx00._MemberContainerCpuidEcx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        FLAG0 = Ia32BitFieldMember(
            "FLAG0",
            """
            @brief If 1, Tracing can be enabled with IA32_RTIT_CTL.ToPA = 1, hence utilizing the ToPA output scheme; IA32_RTIT_OUTPUT_BASE and IA32_RTIT_OUTPUT_MASK_PTRS MSRs can be accessed
    
    If 1, Tracing can be enabled with IA32_RTIT_CTL.ToPA = 1, hence utilizing the ToPA output scheme; IA32_RTIT_OUTPUT_BASE and IA32_RTIT_OUTPUT_MASK_PTRS MSRs can be accessed.
            """,
    
            0,
            1
    
        )
    
    
        FLAG1 = Ia32BitFieldMember(
            "FLAG1",
            """
            @brief If 1, ToPA tables can hold any number of output entries, up to the maximum allowed by the MaskOrTableOffset field of IA32_RTIT_OUTPUT_MASK_PTRS
    
    If 1, ToPA tables can hold any number of output entries, up to the maximum allowed by the MaskOrTableOffset field of IA32_RTIT_OUTPUT_MASK_PTRS.
            """,
    
            1,
            1
    
        )
    
    
        FLAG2 = Ia32BitFieldMember(
            "FLAG2",
            """
            @brief If 1, indicates support of Single-Range Output scheme
    
    If 1, indicates support of Single-Range Output scheme.
            """,
    
            2,
            1
    
        )
    
    
        FLAG3 = Ia32BitFieldMember(
            "FLAG3",
            """
            @brief If 1, indicates support of output to Trace Transport subsystem
    
    If 1, indicates support of output to Trace Transport subsystem.
            """,
    
            3,
            1
    
        )
    
    
        FLAG31 = Ia32BitFieldMember(
            "FLAG31",
            """
            @brief If 1, generated packets which contain IP payloads have LIP values, which include the CS base component
    
    If 1, generated packets which contain IP payloads have LIP values, which include the CS base component.
            """,
    
            31,
            1
    
        )
    
    
    
    class _MemberContainerCpuidEdx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax14Ecx00._MemberContainerCpuidEdx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
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
        super(CpuidEax14Ecx00, self).__init__(value)


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


class CpuidEax14Ecx01(Ia32Struct):
    """@brief Intel Processor Trace Enumeration Sub-leaf (EAX = 14H, ECX = 1)

Intel Processor Trace Enumeration Sub-leaf (EAX = 14H, ECX = 1)."""
    class _MemberContainerCpuidEax(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax14Ecx01._MemberContainerCpuidEax, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        NUMBER_OF_CONFIGURABLE_ADDRESS_RANGES_FOR_FILTERING = Ia32BitFieldMember(
            "NUMBER_OF_CONFIGURABLE_ADDRESS_RANGES_FOR_FILTERING",
            """
            @brief Number of configurable Address Ranges for filtering
    
    Number of configurable Address Ranges for filtering.
            """,
    
            0,
            3
    
        )
    
    
        BITMAP_OF_SUPPORTED_MTC_PERIOD_ENCODINGS = Ia32BitFieldMember(
            "BITMAP_OF_SUPPORTED_MTC_PERIOD_ENCODINGS",
            """
            @brief Bitmap of supported MTC period encodings
    
    Bitmap of supported MTC period encodings.
            """,
    
            16,
            16
    
        )
    
    
    
    class _MemberContainerCpuidEbx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax14Ecx01._MemberContainerCpuidEbx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        BITMAP_OF_SUPPORTED_CYCLE_THRESHOLD_VALUE_ENCODINGS = Ia32BitFieldMember(
            "BITMAP_OF_SUPPORTED_CYCLE_THRESHOLD_VALUE_ENCODINGS",
            """
            @brief Bitmap of supported Cycle Threshold value encodings
    
    Bitmap of supported Cycle Threshold value encodings.
            """,
    
            0,
            16
    
        )
    
    
        BITMAP_OF_SUPPORTED_CONFIGURABLE_PSB_FREQUENCY_ENCODINGS = Ia32BitFieldMember(
            "BITMAP_OF_SUPPORTED_CONFIGURABLE_PSB_FREQUENCY_ENCODINGS",
            """
            @brief Bitmap of supported Configurable PSB frequency encodings
    
    Bitmap of supported Configurable PSB frequency encodings.
            """,
    
            16,
            16
    
        )
    
    
    
    class _MemberContainerCpuidEcx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax14Ecx01._MemberContainerCpuidEcx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
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
            super(CpuidEax14Ecx01._MemberContainerCpuidEdx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
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
        super(CpuidEax14Ecx01, self).__init__(value)


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


CPUID_TIME_STAMP_COUNTER = 0x15


class CpuidEax15(Ia32Struct):
    """"""
    class _MemberContainerCpuidEax(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax15._MemberContainerCpuidEax, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        DENOMINATOR = Ia32BitFieldMember(
            "DENOMINATOR",
            """
            @brief An unsigned integer which is the denominator of the TSC/core crystal clock ratio
    
    An unsigned integer which is the denominator of the TSC/core crystal clock ratio.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEbx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax15._MemberContainerCpuidEbx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        NUMERATOR = Ia32BitFieldMember(
            "NUMERATOR",
            """
            @brief An unsigned integer which is the numerator of the TSC/core crystal clock ratio
    
    An unsigned integer which is the numerator of the TSC/core crystal clock ratio.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEcx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax15._MemberContainerCpuidEcx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        NOMINAL_FREQUENCY = Ia32BitFieldMember(
            "NOMINAL_FREQUENCY",
            """
            @brief An unsigned integer which is the nominal frequency of the core crystal clock in Hz
    
    An unsigned integer which is the nominal frequency of the core crystal clock in Hz.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEdx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax15._MemberContainerCpuidEdx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
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
        super(CpuidEax15, self).__init__(value)


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


CPUID_PROCESSOR_FREQUENCY = 0x16


class CpuidEax16(Ia32Struct):
    """"""
    class _MemberContainerCpuidEax(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax16._MemberContainerCpuidEax, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        PROCESOR_BASE_FREQUENCY_MHZ = Ia32BitFieldMember(
            "PROCESOR_BASE_FREQUENCY_MHZ",
            """
            @brief Processor Base Frequency (in MHz)
    
    Processor Base Frequency (in MHz).
            """,
    
            0,
            16
    
        )
    
    
    
    class _MemberContainerCpuidEbx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax16._MemberContainerCpuidEbx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        PROCESSOR_MAXIMUM_FREQUENCY_MHZ = Ia32BitFieldMember(
            "PROCESSOR_MAXIMUM_FREQUENCY_MHZ",
            """
            @brief Maximum Frequency (in MHz)
    
    Maximum Frequency (in MHz).
            """,
    
            0,
            16
    
        )
    
    
    
    class _MemberContainerCpuidEcx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax16._MemberContainerCpuidEcx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        BUS_FREQUENCY_MHZ = Ia32BitFieldMember(
            "BUS_FREQUENCY_MHZ",
            """
            @brief Bus (Reference) Frequency (in MHz)
    
    Bus (Reference) Frequency (in MHz).
            """,
    
            0,
            16
    
        )
    
    
    
    class _MemberContainerCpuidEdx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax16._MemberContainerCpuidEdx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
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
        super(CpuidEax16, self).__init__(value)


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


