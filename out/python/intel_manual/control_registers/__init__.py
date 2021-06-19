from future.utils import with_metaclass
from utils.bit_field import *


description = """
Control registers (CR0, CR1, CR2, CR3, and CR4) determine operating mode of the processor and
the characteristics of the currently executing task. These registers are 32 bits in all 32-bit modes and compatibility
mode.

In 64-bit mode, control registers are expanded to 64 bits. The MOV CRn instructions are used to manipulate the
register bits. Operand-size prefixes for these instructions are ignored. The following is also true:

- The control registers can be read and loaded (or modified) using the move-to-or-from-control-registers forms
  of the MOV instruction. In protected mode, the MOV instructions allow the control registers to be read or loaded
  (at privilege level 0 only). This restriction means that application programs or operating-system procedures
  (running at privilege levels 1, 2, or 3) are prevented from reading or loading the control registers.

- Bits 63:32 of CR0 and CR4 are reserved and must be written with zeros. Writing a nonzero value to any of the
  upper 32 bits results in a general-protection exception, \#GP(0).

- All 64 bits of CR2 are writable by software.

- Bits 51:40 of CR3 are reserved and must be 0.

- The MOV CRn instructions do not check that addresses written to CR2 and CR3 are within the linear-address or
  physical-address limitations of the implementation.

- Register CR8 is available in 64-bit mode only.
  The control registers are summarized below, and each architecturally defined control field in these control registers
  is described individually.

- CR0  Contains system control flags that control operating mode and states of the processor.

- CR1  Reserved.

- CR2  Contains the page-fault linear address (the linear address that caused a page fault).

- CR3  Contains the physical address of the base of the paging-structure hierarchy and two flags (PCD and
  PWT). Only the most-significant bits (less the lower 12 bits) of the base address are specified; the lower 12 bits
  of the address are assumed to be 0. The first paging structure must thus be aligned to a page (4-KByte)
  boundary. The PCD and PWT flags control caching of that paging structure in the processors internal data
  caches (they do not control TLB caching of page-directory information).
  When using the physical address extension, the CR3 register contains the base address of the page-directorypointer
  table. In IA-32e mode, the CR3 register contains the base address of the PML4 table.

- CR4  Contains a group of flags that enable several architectural extensions, and indicate operating system or
  executive support for specific processor capabilities.

- CR8  Provides read and write access to the Task Priority Register (TPR). It specifies the priority threshold
  value that operating systems use to control the priority class of external interrupts allowed to interrupt the
  processor. This register is available only in 64-bit mode. However, interrupt filtering continues to apply in
  compatibility mode.
"""
class Cr0(with_metaclass(BitFieldMeta, BitField)):
    """"""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=8)

    _FIELDS = ["PE","MP","EM","TS","ET","NE","WP","AM","NW","CD","PG",]

    
    PE = BitFieldMember(
        "PE",
        """
        Protection Enable:
        Enables protected mode when set; enables real-address mode when
clear. This flag does not enable paging directly. It only enables segment-level protection. To enable paging,
both the PE and PG flags must be set.
        """,
        0,
        1
    )

    
    MP = BitFieldMember(
        "MP",
        """
        Monitor Coprocessor:
        Controls the interaction of the WAIT (or FWAIT) instruction with
the TS flag (bit 3 of CR0). If the MP flag is set, a WAIT instruction generates a device-not-available exception
(\#NM) if the TS flag is also set. If the MP flag is clear, the WAIT instruction ignores the setting of the TS flag.
        """,
        1,
        1
    )

    
    EM = BitFieldMember(
        "EM",
        """
        FPU Emulation:
        Indicates that the processor does not have an internal or external x87 FPU
when set; indicates an x87 FPU is present when clear. This flag also affects the execution of
MMX/SSE/SSE2/SSE3/SSSE3/SSE4 instructions.

When the EM flag is set, execution of an x87 FPU instruction generates a device-not-available exception
(\#NM). This flag must be set when the processor does not have an internal x87 FPU or is not connected to
an external math coprocessor. Setting this flag forces all floating-point instructions to be handled by software
emulation.

Also, when the EM flag is set, execution of an MMX instruction causes an invalid-opcode exception (\#UD)
to be generated. Thus, if an IA-32 or Intel 64 processor incorporates MMX technology, the
EM flag must be set to 0 to enable execution of MMX instructions.
Similarly for SSE/SSE2/SSE3/SSSE3/SSE4 extensions, when the EM flag is set, execution of most
SSE/SSE2/SSE3/SSSE3/SSE4 instructions causes an invalid opcode exception (\#UD) to be generated.
If an IA-32 or Intel 64 processor incorporates the SSE/SSE2/SSE3/SSSE3/SSE4 extensions,
the EM flag must be set to 0 to enable execution of these extensions. SSE/SSE2/SSE3/SSSE3/SSE4
instructions not affected by the EM flag include: PAUSE, PREFETCHh, SFENCE, LFENCE, MFENCE, MOVNTI,
CLFLUSH, CRC32, and POPCNT.
        """,
        2,
        1
    )

    
    TS = BitFieldMember(
        "TS",
        """
        Task Switched:
        Allows the saving of the x87 FPU/MMX/SSE/SSE2/SSE3/SSSE3/SSE4
context on a task switch to be delayed until an x87 FPU/MMX/SSE/SSE2/SSE3/SSSE3/SSE4 instruction is
actually executed by the new task. The processor sets this flag on every task switch and tests it when
executing x87 FPU/MMX/SSE/SSE2/SSE3/SSSE3/SSE4 instructions.

- If the TS flag is set and the EM flag (bit 2 of CR0) is clear, a device-not-available exception (\#NM) is
  raised prior to the execution of any x87 FPU/MMX/SSE/SSE2/SSE3/SSSE3/SSE4 instruction; with the
  exception of PAUSE, PREFETCHh, SFENCE, LFENCE, MFENCE, MOVNTI, CLFLUSH, CRC32, and POPCNT.

- If the TS flag is set and the MP flag (bit 1 of CR0) and EM flag are clear, an \#NM exception is not raised
  prior to the execution of an x87 FPU WAIT/FWAIT instruction.

- If the EM flag is set, the setting of the TS flag has no effect on the execution of x87
  FPU/MMX/SSE/SSE2/SSE3/SSSE3/SSE4 instructions.

  The processor does not automatically save the context of the x87 FPU, XMM, and MXCSR registers on a
  task switch. Instead, it sets the TS flag, which causes the processor to raise an \#NM exception whenever
  it encounters an x87 FPU/MMX/SSE/SSE2/SSE3/SSSE3/SSE4 instruction in the instruction stream for the
  new task (with the exception of the instructions listed above).

  The fault handler for the \#NM exception can then be used to clear the TS flag (with the CLTS instruction)
  and save the context of the x87 FPU, XMM, and MXCSR registers. If the task never encounters an x87
  FPU/MMX/SSE/SSE2/SSE3/SSSE3/SSE4 instruction, the x87 FPU/MMX/SSE/SSE2/SSE3/SSSE3/SSE4
  context is never saved.
        """,
        3,
        1
    )

    
    ET = BitFieldMember(
        "ET",
        """
        Extension Type:
        Reserved in the Pentium 4, Intel Xeon, P6 family, and Pentium processors.
In the Pentium 4, Intel Xeon, and P6 family processors, this flag is hardcoded to 1. In the Intel386
and Intel486 processors, this flag indicates support of Intel 387 DX math coprocessor instructions when
set.
        """,
        4,
        1
    )

    
    NE = BitFieldMember(
        "NE",
        """
        Numeric Error:
        Enables the native (internal) mechanism for reporting x87 FPU errors
when set; enables the PC-style x87 FPU error reporting mechanism when clear. When the NE flag is clear
and the IGNNE\# input is asserted, x87 FPU errors are ignored. When the NE flag is clear and the IGNNE\#
input is deasserted, an unmasked x87 FPU error causes the processor to assert the FERR\# pin to generate
an external interrupt and to stop instruction execution immediately before executing the next waiting
floating-point instruction or WAIT/FWAIT instruction.

The FERR\# pin is intended to drive an input to an external interrupt controller (the FERR\# pin emulates the
ERROR\# pin of the Intel 287 and Intel 387 DX math coprocessors). The NE flag, IGNNE\# pin, and FERR\#
pin are used with external logic to implement PC-style error reporting. Using FERR\# and IGNNE\# to handle
floating-point exceptions is deprecated by modern operating systems; this non-native approach also limits
newer processors to operate with one logical processor active.
        """,
        5,
        1
    )

    
    WP = BitFieldMember(
        "WP",
        """
        Write Protect:
        When set, inhibits supervisor-level procedures from writing into readonly
pages; when clear, allows supervisor-level procedures to write into read-only pages (regardless of the
U/S bit setting). This flag facilitates implementation of the copy-onwrite
method of creating a new process (forking) used by operating systems such as UNIX.
        """,
        16,
        1
    )

    
    AM = BitFieldMember(
        "AM",
        """
        Alignment Mask:
        Enables automatic alignment checking when set; disables alignment
checking when clear. Alignment checking is performed only when the AM flag is set, the AC flag in the
EFLAGS register is set, CPL is 3, and the processor is operating in either protected or virtual-8086 mode.
        """,
        18,
        1
    )

    
    NW = BitFieldMember(
        "NW",
        """
        Not Write-through:
        When the NW and CD flags are clear, write-back (for Pentium 4,
Intel Xeon, P6 family, and Pentium processors) or write-through (for Intel486 processors) is enabled for
writes that hit the cache and invalidation cycles are enabled.
        """,
        29,
        1
    )

    
    CD = BitFieldMember(
        "CD",
        """
        Cache Disable:
        When the CD and NW flags are clear, caching of memory locations for
the whole of physical memory in the processors internal (and external) caches is enabled. When the CD
flag is set, caching is restricted. To prevent the processor from accessing and
updating its caches, the CD flag must be set and the caches must be invalidated so that no cache hits can
occur.
        """,
        30,
        1
    )

    
    PG = BitFieldMember(
        "PG",
        """
        Paging Enable:
        Enables paging when set; disables paging when clear. When paging is
disabled, all linear addresses are treated as physical addresses. The PG flag has no effect if the PE flag (bit
0 of register CR0) is not also set; setting the PG flag when the PE flag is clear causes a general-protection
exception (\#GP).

On Intel 64 processors, enabling and disabling IA-32e mode operation also requires modifying CR0.PG.
        """,
        31,
        1
    )

    

class Cr3(with_metaclass(BitFieldMeta, BitField)):
    """"""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=8)

    _FIELDS = ["PWT","PCD","PD_PHYS_ADDR",]

    
    PWT = BitFieldMember(
        "PWT",
        """
        Page-level Write-Through:
        Controls the memory type used to access the first paging
structure of the current paging-structure hierarchy. This bit is not used if paging is disabled,
with PAE paging, or with 4-level paging if CR4.PCIDE=1.
        """,
        3,
        1
    )

    
    PCD = BitFieldMember(
        "PCD",
        """
        Page-level Cache Disable:
        Controls the memory type used to access the first paging
structure of the current paging-structure hierarchy. This bit is not used if paging is disabled,
with PAE paging, or with 4-level paging2 if CR4.PCIDE=1.
        """,
        4,
        1
    )

    
    PD_PHYS_ADDR = BitFieldMember(
        "PD_PHYS_ADDR",
        """
        Address of page directory:
        Physical address of the 4-KByte aligned page directory (32-bit paging) or PML4 table (64-bit paging)
used for linear-address translation.
        """,
        12,
        36
    )

    

class Cr4(with_metaclass(BitFieldMeta, BitField)):
    """"""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=8)

    _FIELDS = ["VME","PVI","TSD","DE","PSE","PAE","MCE","PGE","PCE","OSFXSR","OSXMMEXCPT","UMIP","VMXE","SMXE","FSGSBASE","PCIDE","OSXSAVE","SMEP","SMAP","PKE",]

    
    VME = BitFieldMember(
        "VME",
        """
        Virtual-8086 Mode Extensions:
        Enables interrupt- and exception-handling extensions
in virtual-8086 mode when set; disables the extensions when clear. Use of the virtual mode extensions can
improve the performance of virtual-8086 applications by eliminating the overhead of calling the virtual-
8086 monitor to handle interrupts and exceptions that occur while executing an 8086 program and,
instead, redirecting the interrupts and exceptions back to the 8086 programs handlers. It also provides
hardware support for a virtual interrupt flag (VIF) to improve reliability of running 8086 programs in multitasking
and multiple-processor environments.
        """,
        0,
        1
    )

    
    PVI = BitFieldMember(
        "PVI",
        """
        Protected-Mode Virtual Interrupts:
        Enables hardware support for a virtual interrupt
flag (VIF) in protected mode when set; disables the VIF flag in protected mode when clear.
        """,
        1,
        1
    )

    
    TSD = BitFieldMember(
        "TSD",
        """
        Time Stamp Disable:
        Restricts the execution of the RDTSC instruction to procedures
running at privilege level 0 when set; allows RDTSC instruction to be executed at any privilege level when
clear. This bit also applies to the RDTSCP instruction if supported (if CPUID.80000001H:EDX[27] = 1).
        """,
        2,
        1
    )

    
    DE = BitFieldMember(
        "DE",
        """
        Debugging Extensions:
        References to debug registers DR4 and DR5 cause an undefined
opcode (\#UD) exception to be generated when set; when clear, processor aliases references to registers
DR4 and DR5 for compatibility with software written to run on earlier IA-32 processors.
        """,
        3,
        1
    )

    
    PSE = BitFieldMember(
        "PSE",
        """
        Page Size Extensions:
        Enables 4-MByte pages with 32-bit paging when set; restricts
32-bit paging to pages of 4 KBytes when clear.
        """,
        4,
        1
    )

    
    PAE = BitFieldMember(
        "PAE",
        """
        Physical Address Extension:
        When set, enables paging to produce physical addresses
with more than 32 bits. When clear, restricts physical addresses to 32 bits. PAE must be set before entering
IA-32e mode.
        """,
        5,
        1
    )

    
    MCE = BitFieldMember(
        "MCE",
        """
        Machine-Check Enable:
        Enables the machine-check exception when set; disables the
machine-check exception when clear.
        """,
        6,
        1
    )

    
    PGE = BitFieldMember(
        "PGE",
        """
        Page Global Enable:
        (Introduced in the P6 family processors.) Enables the global page
feature when set; disables the global page feature when clear. The global page feature allows frequently
used or shared pages to be marked as global to all users (done with the global flag, bit 8, in a page-directory
or page-table entry). Global pages are not flushed from the translation-lookaside buffer (TLB) on a
task switch or a write to register CR3.
When enabling the global page feature, paging must be enabled (by setting the PG flag in control register
CR0) before the PGE flag is set. Reversing this sequence may affect program correctness, and processor
performance will be impacted.
        """,
        7,
        1
    )

    
    PCE = BitFieldMember(
        "PCE",
        """
        Performance-Monitoring Counter Enable:
        Enables execution of the RDPMC instruction
for programs or procedures running at any protection level when set; RDPMC instruction can be
executed only at protection level 0 when clear.
        """,
        8,
        1
    )

    
    OSFXSR = BitFieldMember(
        "OSFXSR",
        """
        Operating System Support for FXSAVE and FXRSTOR instructions:
        When set, this flag:

-# indicates to software that the operating system supports the use of the FXSAVE and FXRSTOR
   instructions,

-# enables the FXSAVE and FXRSTOR instructions to save and restore the contents of the
   XMM and MXCSR registers along with the contents of the x87 FPU and MMX registers, and

-# enables the processor to execute SSE/SSE2/SSE3/SSSE3/SSE4 instructions, with the exception of the
   PAUSE, PREFETCHh, SFENCE, LFENCE, MFENCE, MOVNTI, CLFLUSH, CRC32, and POPCNT.

If this flag is clear, the FXSAVE and FXRSTOR instructions will save and restore the contents of the x87 FPU
and MMX registers, but they may not save and restore the contents of the XMM and MXCSR registers. Also,
the processor will generate an invalid opcode exception (\#UD) if it attempts to execute any
SSE/SSE2/SSE3 instruction, with the exception of PAUSE, PREFETCHh, SFENCE, LFENCE, MFENCE,
MOVNTI, CLFLUSH, CRC32, and POPCNT. The operating system or executive must explicitly set this flag.
        """,
        9,
        1
    )

    
    OSXMMEXCPT = BitFieldMember(
        "OSXMMEXCPT",
        """
        Operating System Support for Unmasked SIMD Floating-Point Exceptions:
        Operating System Support for Unmasked SIMD Floating-Point Exceptions 
When set, indicates that the operating system supports the handling of unmasked SIMD floating-point
exceptions through an exception handler that is invoked when a SIMD floating-point exception (\#XM) is
generated. SIMD floating-point exceptions are only generated by SSE/SSE2/SSE3/SSE4.1 SIMD floatingpoint
instructions.

The operating system or executive must explicitly set this flag. If this flag is not set, the processor will
generate an invalid opcode exception (\#UD) whenever it detects an unmasked SIMD floating-point exception.
        """,
        10,
        1
    )

    
    UMIP = BitFieldMember(
        "UMIP",
        """
        User-Mode Instruction Prevention:
        When set, the following instructions cannot be
executed if CPL > 0: SGDT, SIDT, SLDT, SMSW, and STR. An attempt at such execution causes a generalprotection
exception (\#GP).
        """,
        11,
        1
    )

    
    VMXE = BitFieldMember(
        "VMXE",
        """
        VMX-Enable:
        Enables VMX operation when set.
        """,
        13,
        1
    )

    
    SMXE = BitFieldMember(
        "SMXE",
        """
        SMX-Enable:
        Enables SMX operation when set.
        """,
        14,
        1
    )

    
    FSGSBASE = BitFieldMember(
        "FSGSBASE",
        """
        FSGSBASE-Enable:
        Enables the instructions RDFSBASE, RDGSBASE, WRFSBASE,
and WRGSBASE.
        """,
        16,
        1
    )

    
    PCIDE = BitFieldMember(
        "PCIDE",
        """
        PCID-Enable:
        Enables process-context identifiers (PCIDs) when set.
Can be set only in IA-32e mode (if IA32_EFER.LMA = 1).
        """,
        17,
        1
    )

    
    OSXSAVE = BitFieldMember(
        "OSXSAVE",
        """
        XSAVE and Processor Extended States-Enable:
        When set, this flag:

-# indicates (via CPUID.01H:ECX.OSXSAVE[bit 27]) that the operating system supports
   the use of the XGETBV, XSAVE and XRSTOR instructions by general software;

-# enables the XSAVE and XRSTOR instructions to save and restore the x87 FPU state
   (including MMX registers), the SSE state (XMM registers and MXCSR), along with other
   processor extended states enabled in XCR0;

-# enables the processor to execute XGETBV and XSETBV instructions in order to read
   and write XCR0.
        """,
        18,
        1
    )

    
    SMEP = BitFieldMember(
        "SMEP",
        """
        SMEP-Enable:
        Enables supervisor-mode execution prevention (SMEP) when set.
        """,
        20,
        1
    )

    
    SMAP = BitFieldMember(
        "SMAP",
        """
        SMAP-Enable:
        Enables supervisor-mode access prevention (SMAP) when set.
        """,
        21,
        1
    )

    
    PKE = BitFieldMember(
        "PKE",
        """
        Protection-Key-Enable:
        Enables 4-level paging to associate each linear address
with a protection key. The PKRU register specifies, for each protection key, whether user-mode linear
addresses with that protection key can be read or written. This bit also enables access to the PKRU register
using the RDPKRU and WRPKRU instructions.
        """,
        22,
        1
    )

    

class Cr8(with_metaclass(BitFieldMeta, BitField)):
    """"""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=8)

    _FIELDS = ["TPL","RESERVED",]

    
    TPL = BitFieldMember(
        "TPL",
        """
        Task Priority Level:
        This sets the threshold value corresponding to the highestpriority
interrupt to be blocked. A value of 0 means all interrupts are enabled. This field is available in 64-
bit mode. A value of 15 means all interrupts will be disabled.
        """,
        0,
        4
    )

    
    RESERVED = BitFieldMember(
        "RESERVED",
        """
        Reserved:
        Reserved and must be written with zeros. Failure to do this causes a general-protection exception.
        """,
        4,
        60
    )

    

