from future.utils import with_metaclass
from utils.ia32_struct import *
from utils.ia32_bit_field import *


__doc__ = """
@brief CPUID


"""


CPUID_SIGNATURE = 0x0


class CpuidEax00(Ia32Struct):
    """"""
    class _MemberContainerMaxCpuidInputValue(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        @brief EAX
    
    Maximum Input Value for Basic CPUID Information.
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax00._MemberContainerMaxCpuidInputValue, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
        value = Ia32BitFieldMember('value', 'value', 0, 32)
    
    
    class _MemberContainerEbxValueGenu(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        @brief EBX
    
    Genu
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax00._MemberContainerEbxValueGenu, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
        value = Ia32BitFieldMember('value', 'value', 0, 32)
    
    
    class _MemberContainerEcxValueNtel(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        @brief ECX
    
    ntel
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax00._MemberContainerEcxValueNtel, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
        value = Ia32BitFieldMember('value', 'value', 0, 32)
    
    
    class _MemberContainerEdxValueInei(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        @brief EDX
    
    ineI
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax00._MemberContainerEdxValueInei, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
        value = Ia32BitFieldMember('value', 'value', 0, 32)
    
    
    _members = ["MAXCPUIDINPUT","VALUEGENU","VALUENTEL","VALUEINEI",]

    def __init__(self, value):
        self._MAXCPUIDINPUT = self._MemberContainerMaxCpuidInputValue(0, 0, 4 )
        self._VALUEGENU = self._MemberContainerEbxValueGenu(0, 4, 4 )
        self._VALUENTEL = self._MemberContainerEcxValueNtel(0, 8, 4 )
        self._VALUEINEI = self._MemberContainerEdxValueInei(0, 12, 4 )
        super(CpuidEax00, self).__init__(value)


    @property
    def MAXCPUIDINPUT(self):
        return self._MAXCPUIDINPUT

    @MAXCPUIDINPUT.setter
    def MAXCPUIDINPUT(self, value):
        return self._MAXCPUIDINPUT.set(value)

    @property
    def VALUEGENU(self):
        return self._VALUEGENU

    @VALUEGENU.setter
    def VALUEGENU(self, value):
        return self._VALUEGENU.set(value)

    @property
    def VALUENTEL(self):
        return self._VALUENTEL

    @VALUENTEL.setter
    def VALUENTEL(self, value):
        return self._VALUENTEL.set(value)

    @property
    def VALUEINEI(self):
        return self._VALUEINEI

    @VALUEINEI.setter
    def VALUEINEI(self, value):
        return self._VALUEINEI.set(value)


CPUID_VERSION_INFO = 0x1


class CpuidEax01(Ia32Struct):
    """"""
    class _MemberContainerCpuidEax(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        @brief When CPUID executes with EAX set to 01H, version information is returned in EAX
    
    When CPUID executes with EAX set to 01H, version information is returned in EAX.
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax01._MemberContainerCpuidEax, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        STEPPING_ID = Ia32BitFieldMember(
            "STEPPING_ID",
            """
            
            """,
    
            0,
            4
    
        )
    
    
        MODEL = Ia32BitFieldMember(
            "MODEL",
            """
            
            """,
    
            4,
            4
    
        )
    
    
        FAMILY_ID = Ia32BitFieldMember(
            "FAMILY_ID",
            """
            
            """,
    
            8,
            4
    
        )
    
    
        PROCESSOR_TYPE = Ia32BitFieldMember(
            "PROCESSOR_TYPE",
            """
            @brief - 0 - Original OEM Processor
    
    - 1 - Intel OverDrive Processor
    
    - 2 - Dual processor (not applicable to Intel486 processors)
    
    - 3 - Intel reserved
    
    - 0 - Original OEM Processor
    
    - 1 - Intel OverDrive Processor
    
    - 2 - Dual processor (not applicable to Intel486 processors)
    
    - 3 - Intel reserved
            """,
    
            12,
            2
    
        )
    
    
        EXTENDED_MODEL_ID = Ia32BitFieldMember(
            "EXTENDED_MODEL_ID",
            """
            @brief The Extended Model ID needs to be examined only when the Family ID is 06H or 0FH
    
    The Extended Model ID needs to be examined only when the Family ID is 06H or 0FH.
            """,
    
            16,
            4
    
        )
    
    
        EXTENDED_FAMILY_ID = Ia32BitFieldMember(
            "EXTENDED_FAMILY_ID",
            """
            @brief The Extended Family ID needs to be examined only when the Family ID is 0FH
    
    The Extended Family ID needs to be examined only when the Family ID is 0FH.
            """,
    
            20,
            8
    
        )
    
    
    
    class _MemberContainerCpuidEbx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        @brief When CPUID executes with EAX set to 01H, additional information is returned to the EBX register
    
    When CPUID executes with EAX set to 01H, additional information is returned to the EBX register.
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax01._MemberContainerCpuidEbx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        BRAND_INDEX = Ia32BitFieldMember(
            "BRAND_INDEX",
            """
            @brief This number provides an entry into a brand string table that contains brand
    strings for IA-32 processors. More information about this field is provided later in this section
    
    This number provides an entry into a brand string table that contains brand
    strings for IA-32 processors. More information about this field is provided later in this section.
            """,
    
            0,
            8
    
        )
    
    
        CLFLUSH_LINE_SIZE = Ia32BitFieldMember(
            "CLFLUSH_LINE_SIZE",
            """
            @brief Value  8 = cache line size in bytes; used also by CLFLUSHOPT
    
    This number indicates the size of the cache line
    flushed by the CLFLUSH and CLFLUSHOPT instructions in 8-byte increments. This field was introduced in the
    Pentium 4 processor.
            """,
    
            8,
            8
    
        )
    
    
        MAX_ADDRESSABLE_IDS = Ia32BitFieldMember(
            "MAX_ADDRESSABLE_IDS",
            """
            @brief Maximum number of addressable IDs for logical processors in this physical package
    
    Maximum number of addressable IDs for logical processors in this physical package.
            """,
    
            16,
            8
    
        )
    
    
        INITIAL_APIC_ID = Ia32BitFieldMember(
            "INITIAL_APIC_ID",
            """
            @brief This number is the 8-bit ID that is assigned to the local APIC on the
    processor during power up. This field was introduced in the Pentium 4 processor
    
    This number is the 8-bit ID that is assigned to the local APIC on the
    processor during power up. This field was introduced in the Pentium 4 processor.
            """,
    
            24,
            8
    
        )
    
    
    
    class _MemberContainerCpuidEcx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        @brief When CPUID executes with EAX set to 01H, feature information is returned in ECX and EDX
    
    When CPUID executes with EAX set to 01H, feature information is returned in ECX and EDX.
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax01._MemberContainerCpuidEcx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        SSE3 = Ia32BitFieldMember(
            "SSE3",
            """
            @brief Streaming SIMD Extensions 3 (SSE3)
    
    A value of 1 indicates the processor supports this technology.
            """,
    
            0,
            1
    
        )
    
    
        PCLMULQDQ = Ia32BitFieldMember(
            "PCLMULQDQ",
            """
            @brief PCLMULQDQ instruction
    
    A value of 1 indicates the processor supports the PCLMULQDQ instruction.
            """,
    
            1,
            1
    
        )
    
    
        DTES64 = Ia32BitFieldMember(
            "DTES64",
            """
            @brief 64-bit DS Area
    
    A value of 1 indicates the processor supports DS area using 64-bit layout.
            """,
    
            2,
            1
    
        )
    
    
        MONITOR = Ia32BitFieldMember(
            "MONITOR",
            """
            @brief MONITOR/MWAIT instruction
    
    A value of 1 indicates the processor supports this feature.
            """,
    
            3,
            1
    
        )
    
    
        DSCPL = Ia32BitFieldMember(
            "DSCPL",
            """
            @brief CPL Qualified Debug Store
    
    A value of 1 indicates the processor supports the extensions to the
    Debug Store feature to allow for branch message storage qualified by CPL.
            """,
    
            4,
            1
    
        )
    
    
        VMX = Ia32BitFieldMember(
            "VMX",
            """
            @brief Virtual Machine Extensions
    
    A value of 1 indicates that the processor supports this technology.
            """,
    
            5,
            1
    
        )
    
    
        SMX = Ia32BitFieldMember(
            "SMX",
            """
            @brief Safer Mode Extensions
    
    A value of 1 indicates that the processor supports this technology.
    
    @see Vol2[6(SAFER MODE EXTENSIONS REFERENCE)]
            """,
    
            6,
            1
    
        )
    
    
        EIST = Ia32BitFieldMember(
            "EIST",
            """
            @brief Enhanced Intel SpeedStep technology
    
    A value of 1 indicates that the processor supports this technology.
            """,
    
            7,
            1
    
        )
    
    
        TM2 = Ia32BitFieldMember(
            "TM2",
            """
            @brief Thermal Monitor 2
    
    A value of 1 indicates whether the processor supports this technology.
            """,
    
            8,
            1
    
        )
    
    
        SSSE3 = Ia32BitFieldMember(
            "SSSE3",
            """
            @brief Supplemental Streaming SIMD Extensions 3 (SSSE3)
    
    A value of 1 indicates the presence of the Supplemental Streaming SIMD Extensions 3 (SSSE3). A
    value of 0 indicates the instruction extensions are not present in the processor.
            """,
    
            9,
            1
    
        )
    
    
        CNXTID = Ia32BitFieldMember(
            "CNXTID",
            """
            @brief L1 Context ID
    
    A value of 1 indicates the L1 data cache mode can be set to either adaptive mode
    or shared mode. A value of 0 indicates this feature is not supported. See definition of the
    IA32_MISC_ENABLE MSR Bit 24 (L1 Data Cache Context Mode) for details.
            """,
    
            10,
            1
    
        )
    
    
        SDBG = Ia32BitFieldMember(
            "SDBG",
            """
            @brief IA32_DEBUG_INTERFACE MSR for silicon debug
    
    A value of 1 indicates the processor supports IA32_DEBUG_INTERFACE MSR for silicon debug.
            """,
    
            11,
            1
    
        )
    
    
        FMA = Ia32BitFieldMember(
            "FMA",
            """
            @brief FMA extensions using YMM state
    
    A value of 1 indicates the processor supports FMA (Fused Multiple Add) extensions using YMM state.
            """,
    
            12,
            1
    
        )
    
    
        CMPXCHG16B = Ia32BitFieldMember(
            "CMPXCHG16B",
            """
            @brief CMPXCHG16B instruction
    
    A value of 1 indicates that the feature is available.
            """,
    
            13,
            1
    
        )
    
    
        XTPR_UPDATE_CONTROL = Ia32BitFieldMember(
            "XTPR_UPDATE_CONTROL",
            """
            @brief xTPR Update Control
    
    A value of 1 indicates that the processor supports changing IA32_MISC_ENABLE[bit 23].
            """,
    
            14,
            1
    
        )
    
    
        PDCM = Ia32BitFieldMember(
            "PDCM",
            """
            @brief Perfmon and Debug Capability
    
    A value of 1 indicates the processor supports the performance
    and debug feature indication MSR IA32_PERF_CAPABILITIES.
            """,
    
            15,
            1
    
        )
    
    
        PCID = Ia32BitFieldMember(
            "PCID",
            """
            @brief Process-context identifiers
    
    A value of 1 indicates that the processor supports PCIDs and that software may set CR4.PCIDE to 1.
            """,
    
            17,
            1
    
        )
    
    
        DCA = Ia32BitFieldMember(
            "DCA",
            """
            @brief Direct Cache Access
    
    A value of 1 indicates the processor supports the ability to prefetch data from a memory mapped
    device (Direct Cache Access).
            """,
    
            18,
            1
    
        )
    
    
        SSE41 = Ia32BitFieldMember(
            "SSE41",
            """
            @brief SSE4.1 support
    
    A value of 1 indicates that the processor supports SSE4.1.
            """,
    
            19,
            1
    
        )
    
    
        SSE42 = Ia32BitFieldMember(
            "SSE42",
            """
            @brief SSE4.2 support
    
    A value of 1 indicates that the processor supports SSE4.2.
            """,
    
            20,
            1
    
        )
    
    
        X2APIC = Ia32BitFieldMember(
            "X2APIC",
            """
            @brief x2APIC support
    
    A value of 1 indicates that the processor supports x2APIC feature.
            """,
    
            21,
            1
    
        )
    
    
        MOVBE = Ia32BitFieldMember(
            "MOVBE",
            """
            @brief MOVBE instruction
    
    A value of 1 indicates that the processor supports MOVBE instruction.
            """,
    
            22,
            1
    
        )
    
    
        POPCNT = Ia32BitFieldMember(
            "POPCNT",
            """
            @brief POPCNT instruction
    
    A value of 1 indicates that the processor supports the POPCNT instruction.
            """,
    
            23,
            1
    
        )
    
    
        TSC_DEADLINE = Ia32BitFieldMember(
            "TSC_DEADLINE",
            """
            @brief TSC Deadline
    
    A value of 1 indicates that the processors local APIC timer supports one-shot operation using a
    TSC deadline value.
            """,
    
            24,
            1
    
        )
    
    
        AESNI = Ia32BitFieldMember(
            "AESNI",
            """
            @brief AESNI instruction extensions
    
    A value of 1 indicates that the processor supports the AESNI instruction extensions.
            """,
    
            25,
            1
    
        )
    
    
        XSAVE = Ia32BitFieldMember(
            "XSAVE",
            """
            @brief XSAVE/XRSTOR instruction extensions
    
    A value of 1 indicates that the processor supports the XSAVE/XRSTOR processor extended states
    feature, the XSETBV/XGETBV instructions, and XCR0.
            """,
    
            26,
            1
    
        )
    
    
        OSXSAVE = Ia32BitFieldMember(
            "OSXSAVE",
            """
            @brief CR4.OSXSAVE[bit 18] set
    
    A value of 1 indicates that the OS has set CR4.OSXSAVE[bit 18] to enable XSETBV/XGETBV
    instructions to access XCR0 and to support processor extended state management using
    XSAVE/XRSTOR.
            """,
    
            27,
            1
    
        )
    
    
        AVX = Ia32BitFieldMember(
            "AVX",
            """
            @brief AVX instruction extensions support
    
    A value of 1 indicates the processor supports the AVX instruction extensions.
            """,
    
            28,
            1
    
        )
    
    
        F16C = Ia32BitFieldMember(
            "F16C",
            """
            @brief 16-bit floating-point conversion instructions support
    
    A value of 1 indicates that processor supports 16-bit floating-point conversion instructions.
            """,
    
            29,
            1
    
        )
    
    
        RDRAND = Ia32BitFieldMember(
            "RDRAND",
            """
            @brief RDRAND instruction support
    
    A value of 1 indicates that processor supports RDRAND instruction.
            """,
    
            30,
            1
    
        )
    
    
    
    class _MemberContainerCpuidEdx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        @brief When CPUID executes with EAX set to 01H, feature information is returned in ECX and EDX
    
    When CPUID executes with EAX set to 01H, feature information is returned in ECX and EDX.
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax01._MemberContainerCpuidEdx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        FPU = Ia32BitFieldMember(
            "FPU",
            """
            @brief Floating Point Unit On-Chip
    
    The processor contains an x87 FPU.
            """,
    
            0,
            1
    
        )
    
    
        VME = Ia32BitFieldMember(
            "VME",
            """
            @brief Virtual 8086 Mode Enhancements
    
    Virtual 8086 mode enhancements, including CR4.VME for controlling the
    feature, CR4.PVI for protected mode virtual interrupts, software interrupt indirection, expansion of the TSS
    with the software indirection bitmap, and EFLAGS.VIF and EFLAGS.VIP flags.
            """,
    
            1,
            1
    
        )
    
    
        DE = Ia32BitFieldMember(
            "DE",
            """
            @brief Debugging Extensions
    
    Support for I/O breakpoints, including CR4.DE for controlling the feature, and optional
    trapping of accesses to DR4 and DR5.
            """,
    
            2,
            1
    
        )
    
    
        PSE = Ia32BitFieldMember(
            "PSE",
            """
            @brief Page Size Extension
    
    Large pages of size 4 MByte are supported, including CR4.PSE for controlling the
    feature, the defined dirty bit in PDE (Page Directory Entries), optional reserved bit trapping in CR3, PDEs, and
    PTEs.
            """,
    
            3,
            1
    
        )
    
    
        TSC = Ia32BitFieldMember(
            "TSC",
            """
            @brief Time Stamp Counter
    
    The RDTSC instruction is supported, including CR4.TSD for controlling privilege.
            """,
    
            4,
            1
    
        )
    
    
        MSR = Ia32BitFieldMember(
            "MSR",
            """
            @brief Model Specific Registers RDMSR and WRMSR Instructions
    
    The RDMSR and WRMSR instructions are supported. Some of the MSRs are implementation dependent.
            """,
    
            5,
            1
    
        )
    
    
        PAE = Ia32BitFieldMember(
            "PAE",
            """
            @brief Physical Address Extension
    
    Physical addresses greater than 32 bits are supported: extended page table
    entry formats, an extra level in the page translation tables is defined, 2-MByte pages are supported instead of
    4 Mbyte pages if PAE bit is 1.
            """,
    
            6,
            1
    
        )
    
    
        MCE = Ia32BitFieldMember(
            "MCE",
            """
            @brief Machine Check Exception
    
    Exception 18 is defined for Machine Checks, including CR4.MCE for controlling the
    feature. This feature does not define the model-specific implementations of machine-check error logging,
    reporting, and processor shutdowns. Machine Check exception handlers may have to depend on processor
    version to do model specific processing of the exception, or test for the presence of the Machine Check feature.
            """,
    
            7,
            1
    
        )
    
    
        CX8 = Ia32BitFieldMember(
            "CX8",
            """
            @brief CMPXCHG8B Instruction
    
    The compare-and-exchange 8 bytes (64 bits) instruction is supported (implicitly
    locked and atomic).
            """,
    
            8,
            1
    
        )
    
    
        APIC = Ia32BitFieldMember(
            "APIC",
            """
            @brief APIC On-Chip
    
    The processor contains an Advanced Programmable Interrupt Controller (APIC), responding to
    memory mapped commands in the physical address range FFFE0000H to FFFE0FFFH (by default - some
    processors permit the APIC to be relocated).
            """,
    
            9,
            1
    
        )
    
    
        SEP = Ia32BitFieldMember(
            "SEP",
            """
            @brief SYSENTER and SYSEXIT Instructions
    
    The SYSENTER and SYSEXIT and associated MSRs are supported.
            """,
    
            11,
            1
    
        )
    
    
        MTRR = Ia32BitFieldMember(
            "MTRR",
            """
            @brief Memory Type Range Registers
    
    MTRRs are supported. The MTRRcap MSR contains feature bits that describe
    what memory types are supported, how many variable MTRRs are supported, and whether fixed MTRRs are
    supported.
            """,
    
            12,
            1
    
        )
    
    
        PGE = Ia32BitFieldMember(
            "PGE",
            """
            @brief Page Global Bit
    
    The global bit is supported in paging-structure entries that map a page, indicating TLB entries
    that are common to different processes and need not be flushed. The CR4.PGE bit controls this feature.
            """,
    
            13,
            1
    
        )
    
    
        MCA = Ia32BitFieldMember(
            "MCA",
            """
            @brief Machine Check Architecture
    
    A value of 1 indicates the Machine Check Architecture of reporting machine
    errors is supported. The MCG_CAP MSR contains feature bits describing how many banks of error reporting
    MSRs are supported.
            """,
    
            14,
            1
    
        )
    
    
        CMOV = Ia32BitFieldMember(
            "CMOV",
            """
            @brief Conditional Move Instructions
    
    The conditional move instruction CMOV is supported. In addition, if x87 FPU is
    present as indicated by the CPUID.FPU feature bit, then the FCOMI and FCMOV instructions are supported
            """,
    
            15,
            1
    
        )
    
    
        PAT = Ia32BitFieldMember(
            "PAT",
            """
            @brief Page Attribute Table
    
    Page Attribute Table is supported. This feature augments the Memory Type Range
    Registers (MTRRs), allowing an operating system to specify attributes of memory accessed through a linear
    address on a 4KB granularity.
            """,
    
            16,
            1
    
        )
    
    
        PSE36 = Ia32BitFieldMember(
            "PSE36",
            """
            @brief 36-Bit Page Size Extension
    
    4-MByte pages addressing physical memory beyond 4 GBytes are supported with
    32-bit paging. This feature indicates that upper bits of the physical address of a 4-MByte page are encoded in
    bits 20:13 of the page-directory entry. Such physical addresses are limited by MAXPHYADDR and may be up to
    40 bits in size.
            """,
    
            17,
            1
    
        )
    
    
        PSN = Ia32BitFieldMember(
            "PSN",
            """
            @brief Processor Serial Number
    
    The processor supports the 96-bit processor identification number feature and the
    feature is enabled.
            """,
    
            18,
            1
    
        )
    
    
        CLFSH = Ia32BitFieldMember(
            "CLFSH",
            """
            @brief CLFLUSH Instruction
    
    CLFLUSH Instruction is supported.
            """,
    
            19,
            1
    
        )
    
    
        DS = Ia32BitFieldMember(
            "DS",
            """
            @brief Debug Store
    
    The processor supports the ability to write debug information into a memory resident buffer.
    This feature is used by the branch trace store (BTS) and processor event-based sampling (PEBS) facilities.
    
    @see Vol3C[23(INTRODUCTION TO VIRTUAL MACHINE EXTENSIONS)]
    
            """,
    
            21,
            1
    
        )
    
    
        ACPI = Ia32BitFieldMember(
            "ACPI",
            """
            @brief Thermal Monitor and Software Controlled Clock Facilities
    
    The processor implements internal MSRs that
    allow processor temperature to be monitored and processor performance to be modulated in predefined duty
    cycles under software control.
            """,
    
            22,
            1
    
        )
    
    
        MMX = Ia32BitFieldMember(
            "MMX",
            """
            @brief Intel MMX Technology
    
    The processor supports the Intel MMX technology.
            """,
    
            23,
            1
    
        )
    
    
        FXSR = Ia32BitFieldMember(
            "FXSR",
            """
            @brief FXSAVE and FXRSTOR Instructions
    
    The FXSAVE and FXRSTOR instructions are supported for fast save and
    restore of the floating point context. Presence of this bit also indicates that CR4.OSFXSR is available for an
    operating system to indicate that it supports the FXSAVE and FXRSTOR instructions.
            """,
    
            24,
            1
    
        )
    
    
        SSE = Ia32BitFieldMember(
            "SSE",
            """
            @brief SSE extensions support
    
    The processor supports the SSE extensions.
            """,
    
            25,
            1
    
        )
    
    
        SSE2 = Ia32BitFieldMember(
            "SSE2",
            """
            @brief SSE2 extensions support
    
    The processor supports the SSE2 extensions.
            """,
    
            26,
            1
    
        )
    
    
        SS = Ia32BitFieldMember(
            "SS",
            """
            @brief Self Snoop
    
    The processor supports the management of conflicting memory types by performing a snoop of its
    own cache structure for transactions issued to the bus.
            """,
    
            27,
            1
    
        )
    
    
        HTT = Ia32BitFieldMember(
            "HTT",
            """
            @brief Max APIC IDs reserved field is Valid
    
    A value of 0 for HTT indicates there is only a single logical processor in
    the package and software should assume only a single APIC ID is reserved. A value of 1 for HTT indicates the
    value in CPUID.1.EBX[23:16] (the Maximum number of addressable IDs for logical processors in this package) is
    valid for the package.
            """,
    
            28,
            1
    
        )
    
    
        TM = Ia32BitFieldMember(
            "TM",
            """
            @brief Thermal Monitor
    
    The processor implements the thermal monitor automatic thermal control circuitry (TCC).
            """,
    
            29,
            1
    
        )
    
    
        PBE = Ia32BitFieldMember(
            "PBE",
            """
            @brief Pending Break Enable
    
    The processor supports the use of the FERR\#/PBE\# pin when the processor is in the
    stop-clock state (STPCLK\# is asserted) to signal the processor that an interrupt is pending and that the
    processor should return to normal operation to handle the interrupt. Bit 10 (PBE enable) in the
    IA32_MISC_ENABLE MSR enables this capability.
            """,
    
            31,
            1
    
        )
    
    
    
    _members = ["CPUID_EAX","CPUID_EBX","CPUID_ECX","CPUID_EDX",]

    def __init__(self, value):
        self._CPUID_EAX = self._MemberContainerCpuidEax(0, 0, 4 )
        self._CPUID_EBX = self._MemberContainerCpuidEbx(0, 4, 4 )
        self._CPUID_ECX = self._MemberContainerCpuidEcx(0, 8, 4 )
        self._CPUID_EDX = self._MemberContainerCpuidEdx(0, 12, 4 )
        super(CpuidEax01, self).__init__(value)


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


CPUID_CACHE_PARAMS = 0x4


class CpuidEax04(Ia32Struct):
    """"""
    class _MemberContainerCpuidEax(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax04._MemberContainerCpuidEax, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        CACHE_TYPE_FIELD = Ia32BitFieldMember(
            "CACHE_TYPE_FIELD",
            """
            @brief - 0 = Null - No more caches.
    
    - 1 = Data Cache.
    
    - 2 = Instruction Cache.
    
    - 3 = Unified Cache.
    
    - 4-31 = Reserved
    
    - 0 = Null - No more caches.
    
    - 1 = Data Cache.
    
    - 2 = Instruction Cache.
    
    - 3 = Unified Cache.
    
    - 4-31 = Reserved.
            """,
    
            0,
            5
    
        )
    
    
        CACHE_LEVEL = Ia32BitFieldMember(
            "CACHE_LEVEL",
            """
            @brief Cache Level (starts at 1)
    
    Cache Level (starts at 1).
            """,
    
            5,
            3
    
        )
    
    
        SELF_INITIALIZING_CACHE_LEVEL = Ia32BitFieldMember(
            "SELF_INITIALIZING_CACHE_LEVEL",
            """
            @brief Self Initializing cache level (does not need SW initialization)
    
    Self Initializing cache level (does not need SW initialization).
            """,
    
            8,
            1
    
        )
    
    
        FULLY_ASSOCIATIVE_CACHE = Ia32BitFieldMember(
            "FULLY_ASSOCIATIVE_CACHE",
            """
            @brief Fully Associative cache
    
    Fully Associative cache.
            """,
    
            9,
            1
    
        )
    
    
        MAX_ADDRESSABLE_IDS_FOR_LOGICAL_PROCESSORS_SHARING_THIS_CACHE = Ia32BitFieldMember(
            "MAX_ADDRESSABLE_IDS_FOR_LOGICAL_PROCESSORS_SHARING_THIS_CACHE",
            """
            @brief Maximum number of addressable IDs for logical processors sharing this cache
    
    Maximum number of addressable IDs for logical processors sharing this cache.
            """,
    
            14,
            12
    
        )
    
    
        MAX_ADDRESSABLE_IDS_FOR_PROCESSOR_CORES_IN_PHYSICAL_PACKAGE = Ia32BitFieldMember(
            "MAX_ADDRESSABLE_IDS_FOR_PROCESSOR_CORES_IN_PHYSICAL_PACKAGE",
            """
            @brief Maximum number of addressable IDs for processor cores in the physical package
    
    Maximum number of addressable IDs for processor cores in the physical package.
            """,
    
            26,
            6
    
        )
    
    
    
    class _MemberContainerCpuidEbx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax04._MemberContainerCpuidEbx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        L = Ia32BitFieldMember(
            "L",
            """
            @brief System Coherency Line Size
    
    System Coherency Line Size.
            """,
    
            0,
            12
    
        )
    
    
        P = Ia32BitFieldMember(
            "P",
            """
            @brief Physical Line partitions
    
    Physical Line partitions.
            """,
    
            12,
            10
    
        )
    
    
        W = Ia32BitFieldMember(
            "W",
            """
            @brief Ways of associativity
    
    Ways of associativity.
            """,
    
            22,
            10
    
        )
    
    
    
    class _MemberContainerCpuidEcx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax04._MemberContainerCpuidEcx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
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
            super(CpuidEax04._MemberContainerCpuidEdx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        WBINVD_INVD = Ia32BitFieldMember(
            "WBINVD_INVD",
            """
            @brief Write-Back Invalidate/Invalidate
    
    - 0 = WBINVD/INVD from threads sharing this cache acts upon lower level caches for threads sharing this
      cache.
    
    - 1 = WBINVD/INVD is not guaranteed to act upon lower level caches of non-originating threads sharing
      this cache.
            """,
    
            0,
            1
    
        )
    
    
        CACHE_INCLUSIVENESS = Ia32BitFieldMember(
            "CACHE_INCLUSIVENESS",
            """
            @brief Cache Inclusiveness
    
    - 0 = Cache is not inclusive of lower cache levels.
    
    - 1 = Cache is inclusive of lower cache levels.
            """,
    
            1,
            1
    
        )
    
    
        COMPLEX_CACHE_INDEXING = Ia32BitFieldMember(
            "COMPLEX_CACHE_INDEXING",
            """
            @brief Complex Cache Indexing
    
    - 0 = Direct mapped cache.
    
    - 1 = A complex function is used to index the cache, potentially using all address bits.
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
        super(CpuidEax04, self).__init__(value)


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


CPUID_MONITOR_MWAIT = 0x5


class CpuidEax05(Ia32Struct):
    """"""
    class _MemberContainerCpuidEax(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax05._MemberContainerCpuidEax, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        SMALLEST_MONITOR_LINE_SIZE = Ia32BitFieldMember(
            "SMALLEST_MONITOR_LINE_SIZE",
            """
            @brief Smallest monitor-line size in bytes (default is processor's monitor granularity)
    
    Smallest monitor-line size in bytes (default is processor's monitor granularity).
            """,
    
            0,
            16
    
        )
    
    
    
    class _MemberContainerCpuidEbx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax05._MemberContainerCpuidEbx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        LARGEST_MONITOR_LINE_SIZE = Ia32BitFieldMember(
            "LARGEST_MONITOR_LINE_SIZE",
            """
            @brief Largest monitor-line size in bytes (default is processor's monitor granularity)
    
    Largest monitor-line size in bytes (default is processor's monitor granularity).
            """,
    
            0,
            16
    
        )
    
    
    
    class _MemberContainerCpuidEcx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax05._MemberContainerCpuidEcx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        ENUMERATION_OF_MONITOR_MWAIT_EXTENSIONS = Ia32BitFieldMember(
            "ENUMERATION_OF_MONITOR_MWAIT_EXTENSIONS",
            """
            @brief Enumeration of Monitor-Mwait extensions (beyond EAX and EBX registers) supported
    
    Enumeration of Monitor-Mwait extensions (beyond EAX and EBX registers) supported.
            """,
    
            0,
            1
    
        )
    
    
        SUPPORTS_TREATING_INTERRUPTS_AS_BREAK_EVENT_FOR_MWAIT = Ia32BitFieldMember(
            "SUPPORTS_TREATING_INTERRUPTS_AS_BREAK_EVENT_FOR_MWAIT",
            """
            @brief Supports treating interrupts as break-event for MWAIT, even when interrupts disabled
    
    Supports treating interrupts as break-event for MWAIT, even when interrupts disabled.
            """,
    
            1,
            1
    
        )
    
    
    
    class _MemberContainerCpuidEdx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax05._MemberContainerCpuidEdx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        NUMBER_OF_C0_SUB_C_STATES = Ia32BitFieldMember(
            "NUMBER_OF_C0_SUB_C_STATES",
            """
            @brief Number of C0 sub C-states supported using MWAIT
    
    Number of C0 sub C-states supported using MWAIT.
            """,
    
            0,
            4
    
        )
    
    
        NUMBER_OF_C1_SUB_C_STATES = Ia32BitFieldMember(
            "NUMBER_OF_C1_SUB_C_STATES",
            """
            @brief Number of C1 sub C-states supported using MWAIT
    
    Number of C1 sub C-states supported using MWAIT.
            """,
    
            4,
            4
    
        )
    
    
        NUMBER_OF_C2_SUB_C_STATES = Ia32BitFieldMember(
            "NUMBER_OF_C2_SUB_C_STATES",
            """
            @brief Number of C2 sub C-states supported using MWAIT
    
    Number of C2 sub C-states supported using MWAIT.
            """,
    
            8,
            4
    
        )
    
    
        NUMBER_OF_C3_SUB_C_STATES = Ia32BitFieldMember(
            "NUMBER_OF_C3_SUB_C_STATES",
            """
            @brief Number of C3 sub C-states supported using MWAIT
    
    Number of C3 sub C-states supported using MWAIT.
            """,
    
            12,
            4
    
        )
    
    
        NUMBER_OF_C4_SUB_C_STATES = Ia32BitFieldMember(
            "NUMBER_OF_C4_SUB_C_STATES",
            """
            @brief Number of C4 sub C-states supported using MWAIT
    
    Number of C4 sub C-states supported using MWAIT.
            """,
    
            16,
            4
    
        )
    
    
        NUMBER_OF_C5_SUB_C_STATES = Ia32BitFieldMember(
            "NUMBER_OF_C5_SUB_C_STATES",
            """
            @brief Number of C5 sub C-states supported using MWAIT
    
    Number of C5 sub C-states supported using MWAIT.
            """,
    
            20,
            4
    
        )
    
    
        NUMBER_OF_C6_SUB_C_STATES = Ia32BitFieldMember(
            "NUMBER_OF_C6_SUB_C_STATES",
            """
            @brief Number of C6 sub C-states supported using MWAIT
    
    Number of C6 sub C-states supported using MWAIT.
            """,
    
            24,
            4
    
        )
    
    
        NUMBER_OF_C7_SUB_C_STATES = Ia32BitFieldMember(
            "NUMBER_OF_C7_SUB_C_STATES",
            """
            @brief Number of C7 sub C-states supported using MWAIT
    
    Number of C7 sub C-states supported using MWAIT.
            """,
    
            28,
            4
    
        )
    
    
    
    _members = ["CPUID_EAX","CPUID_EBX","CPUID_ECX","CPUID_EDX",]

    def __init__(self, value):
        self._CPUID_EAX = self._MemberContainerCpuidEax(0, 0, 4 )
        self._CPUID_EBX = self._MemberContainerCpuidEbx(0, 4, 4 )
        self._CPUID_ECX = self._MemberContainerCpuidEcx(0, 8, 4 )
        self._CPUID_EDX = self._MemberContainerCpuidEdx(0, 12, 4 )
        super(CpuidEax05, self).__init__(value)


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


CPUID_THERMAL_POWER_MANAGEMENT = 0x6


class CpuidEax06(Ia32Struct):
    """"""
    class _MemberContainerCpuidEax(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax06._MemberContainerCpuidEax, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        TEMPERATURE_SENSOR_SUPPORTED = Ia32BitFieldMember(
            "TEMPERATURE_SENSOR_SUPPORTED",
            """
            @brief Digital temperature sensor is supported if set
    
    Digital temperature sensor is supported if set.
            """,
    
            0,
            1
    
        )
    
    
        INTEL_TURBO_BOOST_TECHNOLOGY_AVAILABLE = Ia32BitFieldMember(
            "INTEL_TURBO_BOOST_TECHNOLOGY_AVAILABLE",
            """
            @brief Intel Turbo Boost Technology available (see description of IA32_MISC_ENABLE[38])
    
    Intel Turbo Boost Technology available (see description of IA32_MISC_ENABLE[38]).
            """,
    
            1,
            1
    
        )
    
    
        ARAT = Ia32BitFieldMember(
            "ARAT",
            """
            @brief ARAT. APIC-Timer-always-running feature is supported if set
    
    ARAT. APIC-Timer-always-running feature is supported if set.
            """,
    
            2,
            1
    
        )
    
    
        PLN = Ia32BitFieldMember(
            "PLN",
            """
            @brief PLN. Power limit notification controls are supported if set
    
    PLN. Power limit notification controls are supported if set.
            """,
    
            4,
            1
    
        )
    
    
        ECMD = Ia32BitFieldMember(
            "ECMD",
            """
            @brief ECMD. Clock modulation duty cycle extension is supported if set
    
    ECMD. Clock modulation duty cycle extension is supported if set.
            """,
    
            5,
            1
    
        )
    
    
        PTM = Ia32BitFieldMember(
            "PTM",
            """
            @brief PTM. Package thermal management is supported if set
    
    PTM. Package thermal management is supported if set.
            """,
    
            6,
            1
    
        )
    
    
        HWP = Ia32BitFieldMember(
            "HWP",
            """
            @brief HWP. HWP base registers (IA32_PM_ENABLE[bit 0], IA32_HWP_CAPABILITIES,
    IA32_HWP_REQUEST, IA32_HWP_STATUS) are supported if set
    
    HWP. HWP base registers (IA32_PM_ENABLE[bit 0], IA32_HWP_CAPABILITIES,
    IA32_HWP_REQUEST, IA32_HWP_STATUS) are supported if set.
            """,
    
            7,
            1
    
        )
    
    
        HWP_NOTIFICATION = Ia32BitFieldMember(
            "HWP_NOTIFICATION",
            """
            @brief HWP_Notification. IA32_HWP_INTERRUPT MSR is supported if set
    
    HWP_Notification. IA32_HWP_INTERRUPT MSR is supported if set.
            """,
    
            8,
            1
    
        )
    
    
        HWP_ACTIVITY_WINDOW = Ia32BitFieldMember(
            "HWP_ACTIVITY_WINDOW",
            """
            @brief HWP_Activity_Window. IA32_HWP_REQUEST[bits 41:32] is supported if set
    
    HWP_Activity_Window. IA32_HWP_REQUEST[bits 41:32] is supported if set.
            """,
    
            9,
            1
    
        )
    
    
        HWP_ENERGY_PERFORMANCE_PREFERENCE = Ia32BitFieldMember(
            "HWP_ENERGY_PERFORMANCE_PREFERENCE",
            """
            @brief HWP_Energy_Performance_Preference. IA32_HWP_REQUEST[bits 31:24] is supported if set
    
    HWP_Energy_Performance_Preference. IA32_HWP_REQUEST[bits 31:24] is supported if set.
            """,
    
            10,
            1
    
        )
    
    
        HWP_PACKAGE_LEVEL_REQUEST = Ia32BitFieldMember(
            "HWP_PACKAGE_LEVEL_REQUEST",
            """
            @brief HWP_Package_Level_Request. IA32_HWP_REQUEST_PKG MSR is supported if set
    
    HWP_Package_Level_Request. IA32_HWP_REQUEST_PKG MSR is supported if set.
            """,
    
            11,
            1
    
        )
    
    
        HDC = Ia32BitFieldMember(
            "HDC",
            """
            @brief HDC. HDC base registers IA32_PKG_HDC_CTL, IA32_PM_CTL1, IA32_THREAD_STALL MSRs are supported if set
    
    HDC. HDC base registers IA32_PKG_HDC_CTL, IA32_PM_CTL1, IA32_THREAD_STALL MSRs are supported if set.
            """,
    
            13,
            1
    
        )
    
    
        INTEL_TURBO_BOOST_MAX_TECHNOLOGY_3_AVAILABLE = Ia32BitFieldMember(
            "INTEL_TURBO_BOOST_MAX_TECHNOLOGY_3_AVAILABLE",
            """
            @brief Intel Turbo Boost Max Technology 3.0 available
    
    Intel Turbo Boost Max Technology 3.0 available.
            """,
    
            14,
            1
    
        )
    
    
        HWP_CAPABILITIES = Ia32BitFieldMember(
            "HWP_CAPABILITIES",
            """
            @brief HWP Capabilities. Highest Performance change is supported if set
    
    HWP Capabilities. Highest Performance change is supported if set.
            """,
    
            15,
            1
    
        )
    
    
        HWP_PECI_OVERRIDE = Ia32BitFieldMember(
            "HWP_PECI_OVERRIDE",
            """
            @brief HWP PECI override is supported if set
    
    HWP PECI override is supported if set.
            """,
    
            16,
            1
    
        )
    
    
        FLEXIBLE_HWP = Ia32BitFieldMember(
            "FLEXIBLE_HWP",
            """
            @brief Flexible HWP is supported if set
    
    Flexible HWP is supported if set.
            """,
    
            17,
            1
    
        )
    
    
        FAST_ACCESS_MODE_FOR_HWP_REQUEST_MSR = Ia32BitFieldMember(
            "FAST_ACCESS_MODE_FOR_HWP_REQUEST_MSR",
            """
            @brief Fast access mode for the IA32_HWP_REQUEST MSR is supported if set
    
    Fast access mode for the IA32_HWP_REQUEST MSR is supported if set.
            """,
    
            18,
            1
    
        )
    
    
        IGNORING_IDLE_LOGICAL_PROCESSOR_HWP_REQUEST = Ia32BitFieldMember(
            "IGNORING_IDLE_LOGICAL_PROCESSOR_HWP_REQUEST",
            """
            @brief Ignoring Idle Logical Processor HWP request is supported if set
    
    Ignoring Idle Logical Processor HWP request is supported if set.
            """,
    
            20,
            1
    
        )
    
    
    
    class _MemberContainerCpuidEbx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax06._MemberContainerCpuidEbx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        NUMBER_OF_INTERRUPT_THRESHOLDS = Ia32BitFieldMember(
            "NUMBER_OF_INTERRUPT_THRESHOLDS",
            """
            @brief Number of Interrupt Thresholds in Digital Thermal Sensor
    
    Number of Interrupt Thresholds in Digital Thermal Sensor.
            """,
    
            0,
            4
    
        )
    
    
    
    class _MemberContainerCpuidEcx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax06._MemberContainerCpuidEcx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        HARDWARE_COORDINATION_FEEDBACK_CAPABILITY = Ia32BitFieldMember(
            "HARDWARE_COORDINATION_FEEDBACK_CAPABILITY",
            """
            @brief Hardware Coordination Feedback Capability (Presence of IA32_MPERF and IA32_APERF). The
    capability to provide a measure of delivered processor performance (since last reset of the counters), as
    a percentage of the expected processor performance when running at the TSC frequency
    
    Hardware Coordination Feedback Capability (Presence of IA32_MPERF and IA32_APERF). The
    capability to provide a measure of delivered processor performance (since last reset of the counters), as
    a percentage of the expected processor performance when running at the TSC frequency.
            """,
    
            0,
            1
    
        )
    
    
        PERFORMANCE_ENERGY_BIAS_PREFERENCE = Ia32BitFieldMember(
            "PERFORMANCE_ENERGY_BIAS_PREFERENCE",
            """
            @brief The processor supports performance-energy bias preference if CPUID.06H:ECX.SETBH[bit 3] is set
    and it also implies the presence of a new architectural MSR called IA32_ENERGY_PERF_BIAS (1B0H)
    
    The processor supports performance-energy bias preference if CPUID.06H:ECX.SETBH[bit 3] is set
    and it also implies the presence of a new architectural MSR called IA32_ENERGY_PERF_BIAS (1B0H).
            """,
    
            3,
            1
    
        )
    
    
    
    class _MemberContainerCpuidEdx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax06._MemberContainerCpuidEdx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
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
        super(CpuidEax06, self).__init__(value)


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


CPUID_STRUCTURED_EXTENDED_FEATURE_FLAGS = 0x7


class CpuidEax07(Ia32Struct):
    """"""
    class _MemberContainerCpuidEax(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax07._MemberContainerCpuidEax, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        NUMBER_OF_SUB_LEAVES = Ia32BitFieldMember(
            "NUMBER_OF_SUB_LEAVES",
            """
            @brief Reports the maximum input value for supported leaf 7 sub-leaves
    
    Reports the maximum input value for supported leaf 7 sub-leaves.
            """,
    
            0,
            32
    
        )
    
    
    
    class _MemberContainerCpuidEbx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax07._MemberContainerCpuidEbx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        FSGSBASE = Ia32BitFieldMember(
            "FSGSBASE",
            """
            @brief Supports RDFSBASE/RDGSBASE/WRFSBASE/WRGSBASE if 1
    
    Supports RDFSBASE/RDGSBASE/WRFSBASE/WRGSBASE if 1.
            """,
    
            0,
            1
    
        )
    
    
        IA32_TSC_ADJUST_MSR = Ia32BitFieldMember(
            "IA32_TSC_ADJUST_MSR",
            """
            @brief IA32_TSC_ADJUST MSR is supported if 1
    
    IA32_TSC_ADJUST MSR is supported if 1.
            """,
    
            1,
            1
    
        )
    
    
        SGX = Ia32BitFieldMember(
            "SGX",
            """
            @brief Supports Intel Software Guard Extensions (Intel SGX Extensions) if 1
    
    Supports Intel Software Guard Extensions (Intel SGX Extensions) if 1.
            """,
    
            2,
            1
    
        )
    
    
        BMI1 = Ia32BitFieldMember(
            "BMI1",
            """
            @brief BMI1
    
    BMI1.
            """,
    
            3,
            1
    
        )
    
    
        HLE = Ia32BitFieldMember(
            "HLE",
            """
            @brief HLE
    
    HLE.
            """,
    
            4,
            1
    
        )
    
    
        AVX2 = Ia32BitFieldMember(
            "AVX2",
            """
            @brief AVX2
    
    AVX2.
            """,
    
            5,
            1
    
        )
    
    
        FDP_EXCPTN_ONLY = Ia32BitFieldMember(
            "FDP_EXCPTN_ONLY",
            """
            @brief x87 FPU Data Pointer updated only on x87 exceptions if 1
    
    x87 FPU Data Pointer updated only on x87 exceptions if 1.
            """,
    
            6,
            1
    
        )
    
    
        SMEP = Ia32BitFieldMember(
            "SMEP",
            """
            @brief Supports Supervisor-Mode Execution Prevention if 1
    
    Supports Supervisor-Mode Execution Prevention if 1.
            """,
    
            7,
            1
    
        )
    
    
        BMI2 = Ia32BitFieldMember(
            "BMI2",
            """
            @brief BMI2
    
    BMI2.
            """,
    
            8,
            1
    
        )
    
    
        ENHANCED_REP_MOVSB_STOSB = Ia32BitFieldMember(
            "ENHANCED_REP_MOVSB_STOSB",
            """
            @brief Supports Enhanced REP MOVSB/STOSB if 1
    
    Supports Enhanced REP MOVSB/STOSB if 1.
            """,
    
            9,
            1
    
        )
    
    
        INVPCID = Ia32BitFieldMember(
            "INVPCID",
            """
            @brief If 1, supports INVPCID instruction for system software that manages process-context identifiers
    
    If 1, supports INVPCID instruction for system software that manages process-context identifiers.
            """,
    
            10,
            1
    
        )
    
    
        RTM = Ia32BitFieldMember(
            "RTM",
            """
            @brief RTM
    
    RTM.
            """,
    
            11,
            1
    
        )
    
    
        RDT_M = Ia32BitFieldMember(
            "RDT_M",
            """
            @brief Supports Intel Resource Director Technology (Intel RDT) Monitoring capability if 1
    
    Supports Intel Resource Director Technology (Intel RDT) Monitoring capability if 1.
            """,
    
            12,
            1
    
        )
    
    
        DEPRECATES = Ia32BitFieldMember(
            "DEPRECATES",
            """
            @brief Deprecates FPU CS and FPU DS values if 1
    
    Deprecates FPU CS and FPU DS values if 1.
            """,
    
            13,
            1
    
        )
    
    
        MPX = Ia32BitFieldMember(
            "MPX",
            """
            @brief Supports Intel Memory Protection Extensions if 1
    
    Supports Intel Memory Protection Extensions if 1.
            """,
    
            14,
            1
    
        )
    
    
        RDT = Ia32BitFieldMember(
            "RDT",
            """
            @brief Supports Intel Resource Director Technology (Intel RDT) Allocation capability if 1
    
    Supports Intel Resource Director Technology (Intel RDT) Allocation capability if 1.
            """,
    
            15,
            1
    
        )
    
    
        AVX512F = Ia32BitFieldMember(
            "AVX512F",
            """
            @brief AVX512F
    
    AVX512F.
            """,
    
            16,
            1
    
        )
    
    
        AVX512DQ = Ia32BitFieldMember(
            "AVX512DQ",
            """
            @brief AVX512DQ
    
    AVX512DQ.
            """,
    
            17,
            1
    
        )
    
    
        RDSEED = Ia32BitFieldMember(
            "RDSEED",
            """
            @brief RDSEED
    
    RDSEED.
            """,
    
            18,
            1
    
        )
    
    
        ADX = Ia32BitFieldMember(
            "ADX",
            """
            @brief ADX
    
    ADX.
            """,
    
            19,
            1
    
        )
    
    
        SMAP = Ia32BitFieldMember(
            "SMAP",
            """
            @brief Supports Supervisor-Mode Access Prevention (and the CLAC/STAC instructions) if 1
    
    Supports Supervisor-Mode Access Prevention (and the CLAC/STAC instructions) if 1.
            """,
    
            20,
            1
    
        )
    
    
        AVX512_IFMA = Ia32BitFieldMember(
            "AVX512_IFMA",
            """
            @brief AVX512_IFMA
    
    AVX512_IFMA.
            """,
    
            21,
            1
    
        )
    
    
        CLFLUSHOPT = Ia32BitFieldMember(
            "CLFLUSHOPT",
            """
            @brief CLFLUSHOPT
    
    CLFLUSHOPT.
            """,
    
            23,
            1
    
        )
    
    
        CLWB = Ia32BitFieldMember(
            "CLWB",
            """
            @brief CLWB
    
    CLWB.
            """,
    
            24,
            1
    
        )
    
    
        INTEL = Ia32BitFieldMember(
            "INTEL",
            """
            @brief Intel Processor Trace
    
    Intel Processor Trace.
            """,
    
            25,
            1
    
        )
    
    
        AVX512PF = Ia32BitFieldMember(
            "AVX512PF",
            """
            @brief (Intel Xeon Phi only)
    
    (Intel Xeon Phi only).
            """,
    
            26,
            1
    
        )
    
    
        AVX512ER = Ia32BitFieldMember(
            "AVX512ER",
            """
            @brief (Intel Xeon Phi only)
    
    (Intel Xeon Phi only).
            """,
    
            27,
            1
    
        )
    
    
        AVX512CD = Ia32BitFieldMember(
            "AVX512CD",
            """
            @brief AVX512CD
    
    AVX512CD.
            """,
    
            28,
            1
    
        )
    
    
        SHA = Ia32BitFieldMember(
            "SHA",
            """
            @brief Supports Intel Secure Hash Algorithm Extensions (Intel SHA Extensions) if 1
    
    Supports Intel Secure Hash Algorithm Extensions (Intel SHA Extensions) if 1.
            """,
    
            29,
            1
    
        )
    
    
        AVX512BW = Ia32BitFieldMember(
            "AVX512BW",
            """
            @brief AVX512BW
    
    AVX512BW.
            """,
    
            30,
            1
    
        )
    
    
        AVX512VL = Ia32BitFieldMember(
            "AVX512VL",
            """
            @brief AVX512VL
    
    AVX512VL.
            """,
    
            31,
            1
    
        )
    
    
    
    class _MemberContainerCpuidEcx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax07._MemberContainerCpuidEcx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        PREFETCHWT1 = Ia32BitFieldMember(
            "PREFETCHWT1",
            """
            @brief (Intel Xeon Phi only)
    
    (Intel Xeon Phi only).
            """,
    
            0,
            1
    
        )
    
    
        AVX512_VBMI = Ia32BitFieldMember(
            "AVX512_VBMI",
            """
            @brief AVX512_VBMI
    
    AVX512_VBMI.
            """,
    
            1,
            1
    
        )
    
    
        UMIP = Ia32BitFieldMember(
            "UMIP",
            """
            @brief Supports user-mode instruction prevention if 1
    
    Supports user-mode instruction prevention if 1.
            """,
    
            2,
            1
    
        )
    
    
        PKU = Ia32BitFieldMember(
            "PKU",
            """
            @brief Supports protection keys for user-mode pages if 1
    
    Supports protection keys for user-mode pages if 1.
            """,
    
            3,
            1
    
        )
    
    
        OSPKE = Ia32BitFieldMember(
            "OSPKE",
            """
            @brief If 1, OS has set CR4.PKE to enable protection keys (and the RDPKRU/WRPKRU instructions)
    
    If 1, OS has set CR4.PKE to enable protection keys (and the RDPKRU/WRPKRU instructions).
            """,
    
            4,
            1
    
        )
    
    
        MAWAU = Ia32BitFieldMember(
            "MAWAU",
            """
            @brief The value of MAWAU used by the BNDLDX and BNDSTX instructions in 64-bit mode
    
    The value of MAWAU used by the BNDLDX and BNDSTX instructions in 64-bit mode.
            """,
    
            17,
            5
    
        )
    
    
        RDPID = Ia32BitFieldMember(
            "RDPID",
            """
            @brief RDPID and IA32_TSC_AUX are available if 1
    
    RDPID and IA32_TSC_AUX are available if 1.
            """,
    
            22,
            1
    
        )
    
    
        SGX_LC = Ia32BitFieldMember(
            "SGX_LC",
            """
            @brief Supports SGX Launch Configuration if 1
    
    Supports SGX Launch Configuration if 1.
            """,
    
            30,
            1
    
        )
    
    
    
    class _MemberContainerCpuidEdx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax07._MemberContainerCpuidEdx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
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
        super(CpuidEax07, self).__init__(value)


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


CPUID_DIRECT_CACHE_ACCESS_INFO = 0x9


class CpuidEax09(Ia32Struct):
    """"""
    class _MemberContainerCpuidEax(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax09._MemberContainerCpuidEax, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
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
            super(CpuidEax09._MemberContainerCpuidEbx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
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
            super(CpuidEax09._MemberContainerCpuidEcx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
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
            super(CpuidEax09._MemberContainerCpuidEdx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
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
        super(CpuidEax09, self).__init__(value)


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


CPUID_ARCHITECTURAL_PERFORMANCE_MONITORING = 0xa


class CpuidEax0a(Ia32Struct):
    """"""
    class _MemberContainerCpuidEax(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax0a._MemberContainerCpuidEax, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        VERSION_ID_OF_ARCHITECTURAL_PERFORMANCE_MONITORING = Ia32BitFieldMember(
            "VERSION_ID_OF_ARCHITECTURAL_PERFORMANCE_MONITORING",
            """
            @brief Version ID of architectural performance monitoring
    
    Version ID of architectural performance monitoring.
            """,
    
            0,
            8
    
        )
    
    
        NUMBER_OF_PERFORMANCE_MONITORING_COUNTER_PER_LOGICAL_PROCESSOR = Ia32BitFieldMember(
            "NUMBER_OF_PERFORMANCE_MONITORING_COUNTER_PER_LOGICAL_PROCESSOR",
            """
            @brief Number of general-purpose performance monitoring counter per logical processor
    
    Number of general-purpose performance monitoring counter per logical processor.
            """,
    
            8,
            8
    
        )
    
    
        BIT_WIDTH_OF_PERFORMANCE_MONITORING_COUNTER = Ia32BitFieldMember(
            "BIT_WIDTH_OF_PERFORMANCE_MONITORING_COUNTER",
            """
            @brief Bit width of general-purpose, performance monitoring counter
    
    Bit width of general-purpose, performance monitoring counter.
            """,
    
            16,
            8
    
        )
    
    
        EBX_BIT_VECTOR_LENGTH = Ia32BitFieldMember(
            "EBX_BIT_VECTOR_LENGTH",
            """
            @brief Length of EBX bit vector to enumerate architectural performance monitoring events
    
    Length of EBX bit vector to enumerate architectural performance monitoring events.
            """,
    
            24,
            8
    
        )
    
    
    
    class _MemberContainerCpuidEbx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax0a._MemberContainerCpuidEbx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        CORE_CYCLE_EVENT_NOT_AVAILABLE = Ia32BitFieldMember(
            "CORE_CYCLE_EVENT_NOT_AVAILABLE",
            """
            @brief Core cycle event not available if 1
    
    Core cycle event not available if 1.
            """,
    
            0,
            1
    
        )
    
    
        INSTRUCTION_RETIRED_EVENT_NOT_AVAILABLE = Ia32BitFieldMember(
            "INSTRUCTION_RETIRED_EVENT_NOT_AVAILABLE",
            """
            @brief Instruction retired event not available if 1
    
    Instruction retired event not available if 1.
            """,
    
            1,
            1
    
        )
    
    
        REFERENCE_CYCLES_EVENT_NOT_AVAILABLE = Ia32BitFieldMember(
            "REFERENCE_CYCLES_EVENT_NOT_AVAILABLE",
            """
            @brief Reference cycles event not available if 1
    
    Reference cycles event not available if 1.
            """,
    
            2,
            1
    
        )
    
    
        LAST_LEVEL_CACHE_REFERENCE_EVENT_NOT_AVAILABLE = Ia32BitFieldMember(
            "LAST_LEVEL_CACHE_REFERENCE_EVENT_NOT_AVAILABLE",
            """
            @brief Last-level cache reference event not available if 1
    
    Last-level cache reference event not available if 1.
            """,
    
            3,
            1
    
        )
    
    
        LAST_LEVEL_CACHE_MISSES_EVENT_NOT_AVAILABLE = Ia32BitFieldMember(
            "LAST_LEVEL_CACHE_MISSES_EVENT_NOT_AVAILABLE",
            """
            @brief Last-level cache misses event not available if 1
    
    Last-level cache misses event not available if 1.
            """,
    
            4,
            1
    
        )
    
    
        BRANCH_INSTRUCTION_RETIRED_EVENT_NOT_AVAILABLE = Ia32BitFieldMember(
            "BRANCH_INSTRUCTION_RETIRED_EVENT_NOT_AVAILABLE",
            """
            @brief Branch instruction retired event not available if 1
    
    Branch instruction retired event not available if 1.
            """,
    
            5,
            1
    
        )
    
    
        BRANCH_MISPREDICT_RETIRED_EVENT_NOT_AVAILABLE = Ia32BitFieldMember(
            "BRANCH_MISPREDICT_RETIRED_EVENT_NOT_AVAILABLE",
            """
            @brief Branch mispredict retired event not available if 1
    
    Branch mispredict retired event not available if 1.
            """,
    
            6,
            1
    
        )
    
    
    
    class _MemberContainerCpuidEcx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax0a._MemberContainerCpuidEcx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
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
            super(CpuidEax0a._MemberContainerCpuidEdx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        NUMBER_OF_FIXED_FUNCTION_PERFORMANCE_COUNTERS = Ia32BitFieldMember(
            "NUMBER_OF_FIXED_FUNCTION_PERFORMANCE_COUNTERS",
            """
            @brief Number of fixed-function performance counters (if Version ID > 1)
    
    Number of fixed-function performance counters (if Version ID > 1).
            """,
    
            0,
            5
    
        )
    
    
        BIT_WIDTH_OF_FIXED_FUNCTION_PERFORMANCE_COUNTERS = Ia32BitFieldMember(
            "BIT_WIDTH_OF_FIXED_FUNCTION_PERFORMANCE_COUNTERS",
            """
            @brief Bit width of fixed-function performance counters (if Version ID > 1)
    
    Bit width of fixed-function performance counters (if Version ID > 1).
            """,
    
            5,
            8
    
        )
    
    
        ANY_THREAD_DEPRECATION = Ia32BitFieldMember(
            "ANY_THREAD_DEPRECATION",
            """
            @brief AnyThread deprecation
    
    AnyThread deprecation.
            """,
    
            15,
            1
    
        )
    
    
    
    _members = ["CPUID_EAX","CPUID_EBX","CPUID_ECX","CPUID_EDX",]

    def __init__(self, value):
        self._CPUID_EAX = self._MemberContainerCpuidEax(0, 0, 4 )
        self._CPUID_EBX = self._MemberContainerCpuidEbx(0, 4, 4 )
        self._CPUID_ECX = self._MemberContainerCpuidEcx(0, 8, 4 )
        self._CPUID_EDX = self._MemberContainerCpuidEdx(0, 12, 4 )
        super(CpuidEax0a, self).__init__(value)


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


CPUID_EXTENDED_TOPOLOGY = 0xb


class CpuidEax0b(Ia32Struct):
    """"""
    class _MemberContainerCpuidEax(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax0b._MemberContainerCpuidEax, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        X2APIC_ID_TO_UNIQUE_TOPOLOGY_ID_SHIFT = Ia32BitFieldMember(
            "X2APIC_ID_TO_UNIQUE_TOPOLOGY_ID_SHIFT",
            """
            @brief Number of bits to shift right on x2APIC ID to get a unique topology ID of the next level type.
    All logical processors with the same next level ID share current level
    
    Number of bits to shift right on x2APIC ID to get a unique topology ID of the next level type.
    All logical processors with the same next level ID share current level.
            """,
    
            0,
            5
    
        )
    
    
    
    class _MemberContainerCpuidEbx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax0b._MemberContainerCpuidEbx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        NUMBER_OF_LOGICAL_PROCESSORS_AT_THIS_LEVEL_TYPE = Ia32BitFieldMember(
            "NUMBER_OF_LOGICAL_PROCESSORS_AT_THIS_LEVEL_TYPE",
            """
            @brief Number of logical processors at this level type. The number reflects configuration as shipped by Intel
    
    Number of logical processors at this level type. The number reflects configuration as shipped by Intel.
            """,
    
            0,
            16
    
        )
    
    
    
    class _MemberContainerCpuidEcx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax0b._MemberContainerCpuidEcx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        LEVEL_NUMBER = Ia32BitFieldMember(
            "LEVEL_NUMBER",
            """
            @brief Level number. Same value in ECX input
    
    Level number. Same value in ECX input.
            """,
    
            0,
            8
    
        )
    
    
        LEVEL_TYPE = Ia32BitFieldMember(
            "LEVEL_TYPE",
            """
            @brief Level type
    
    Level type.
            """,
    
            8,
            8
    
        )
    
    
    
    class _MemberContainerCpuidEdx(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(CpuidEax0b._MemberContainerCpuidEdx, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        X2APIC_ID = Ia32BitFieldMember(
            "X2APIC_ID",
            """
            @brief x2APIC ID the current logical processor
    
    x2APIC ID the current logical processor.
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
        super(CpuidEax0b, self).__init__(value)


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


