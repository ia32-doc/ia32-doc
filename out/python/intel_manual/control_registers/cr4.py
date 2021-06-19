from utils.bit_field import BitField

class Cr4(BitField):
    """"""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=8)

    _FIELDS = ["VME","PVI","TSD","DE","PSE","PAE","MCE","PGE","PCE","OSFXSR","OSXMMEXCPT","UMIP","VMXE","SMXE","FSGSBASE","PCIDE","OSXSAVE","SMEP","SMAP","PKE",]

    
    @property
    def VME(self):
        """
        Virtual-8086 Mode Extensions
        Enables interrupt- and exception-handling extensions
in virtual-8086 mode when set; disables the extensions when clear. Use of the virtual mode extensions can
improve the performance of virtual-8086 applications by eliminating the overhead of calling the virtual-
8086 monitor to handle interrupts and exceptions that occur while executing an 8086 program and,
instead, redirecting the interrupts and exceptions back to the 8086 programs handlers. It also provides
hardware support for a virtual interrupt flag (VIF) to improve reliability of running 8086 programs in multitasking
and multiple-processor environments.
        """
        return self[0:1]

    @VME.setter
    def VME(self, value):
        self[0:1] = value
    
    @property
    def PVI(self):
        """
        Protected-Mode Virtual Interrupts
        Enables hardware support for a virtual interrupt
flag (VIF) in protected mode when set; disables the VIF flag in protected mode when clear.
        """
        return self[1:2]

    @PVI.setter
    def PVI(self, value):
        self[1:2] = value
    
    @property
    def TSD(self):
        """
        Time Stamp Disable
        Restricts the execution of the RDTSC instruction to procedures
running at privilege level 0 when set; allows RDTSC instruction to be executed at any privilege level when
clear. This bit also applies to the RDTSCP instruction if supported (if CPUID.80000001H:EDX[27] = 1).
        """
        return self[2:3]

    @TSD.setter
    def TSD(self, value):
        self[2:3] = value
    
    @property
    def DE(self):
        """
        Debugging Extensions
        References to debug registers DR4 and DR5 cause an undefined
opcode (\#UD) exception to be generated when set; when clear, processor aliases references to registers
DR4 and DR5 for compatibility with software written to run on earlier IA-32 processors.
        """
        return self[3:4]

    @DE.setter
    def DE(self, value):
        self[3:4] = value
    
    @property
    def PSE(self):
        """
        Page Size Extensions
        Enables 4-MByte pages with 32-bit paging when set; restricts
32-bit paging to pages of 4 KBytes when clear.
        """
        return self[4:5]

    @PSE.setter
    def PSE(self, value):
        self[4:5] = value
    
    @property
    def PAE(self):
        """
        Physical Address Extension
        When set, enables paging to produce physical addresses
with more than 32 bits. When clear, restricts physical addresses to 32 bits. PAE must be set before entering
IA-32e mode.
        """
        return self[5:6]

    @PAE.setter
    def PAE(self, value):
        self[5:6] = value
    
    @property
    def MCE(self):
        """
        Machine-Check Enable
        Enables the machine-check exception when set; disables the
machine-check exception when clear.
        """
        return self[6:7]

    @MCE.setter
    def MCE(self, value):
        self[6:7] = value
    
    @property
    def PGE(self):
        """
        Page Global Enable
        (Introduced in the P6 family processors.) Enables the global page
feature when set; disables the global page feature when clear. The global page feature allows frequently
used or shared pages to be marked as global to all users (done with the global flag, bit 8, in a page-directory
or page-table entry). Global pages are not flushed from the translation-lookaside buffer (TLB) on a
task switch or a write to register CR3.
When enabling the global page feature, paging must be enabled (by setting the PG flag in control register
CR0) before the PGE flag is set. Reversing this sequence may affect program correctness, and processor
performance will be impacted.
        """
        return self[7:8]

    @PGE.setter
    def PGE(self, value):
        self[7:8] = value
    
    @property
    def PCE(self):
        """
        Performance-Monitoring Counter Enable
        Enables execution of the RDPMC instruction
for programs or procedures running at any protection level when set; RDPMC instruction can be
executed only at protection level 0 when clear.
        """
        return self[8:9]

    @PCE.setter
    def PCE(self, value):
        self[8:9] = value
    
    @property
    def OSFXSR(self):
        """
        Operating System Support for FXSAVE and FXRSTOR instructions
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
        """
        return self[9:10]

    @OSFXSR.setter
    def OSFXSR(self, value):
        self[9:10] = value
    
    @property
    def OSXMMEXCPT(self):
        """
        Operating System Support for Unmasked SIMD Floating-Point Exceptions
        Operating System Support for Unmasked SIMD Floating-Point Exceptions 
When set, indicates that the operating system supports the handling of unmasked SIMD floating-point
exceptions through an exception handler that is invoked when a SIMD floating-point exception (\#XM) is
generated. SIMD floating-point exceptions are only generated by SSE/SSE2/SSE3/SSE4.1 SIMD floatingpoint
instructions.

The operating system or executive must explicitly set this flag. If this flag is not set, the processor will
generate an invalid opcode exception (\#UD) whenever it detects an unmasked SIMD floating-point exception.
        """
        return self[10:11]

    @OSXMMEXCPT.setter
    def OSXMMEXCPT(self, value):
        self[10:11] = value
    
    @property
    def UMIP(self):
        """
        User-Mode Instruction Prevention
        When set, the following instructions cannot be
executed if CPL > 0: SGDT, SIDT, SLDT, SMSW, and STR. An attempt at such execution causes a generalprotection
exception (\#GP).
        """
        return self[11:12]

    @UMIP.setter
    def UMIP(self, value):
        self[11:12] = value
    
    @property
    def VMXE(self):
        """
        VMX-Enable
        Enables VMX operation when set.
        """
        return self[13:14]

    @VMXE.setter
    def VMXE(self, value):
        self[13:14] = value
    
    @property
    def SMXE(self):
        """
        SMX-Enable
        Enables SMX operation when set.
        """
        return self[14:15]

    @SMXE.setter
    def SMXE(self, value):
        self[14:15] = value
    
    @property
    def FSGSBASE(self):
        """
        FSGSBASE-Enable
        Enables the instructions RDFSBASE, RDGSBASE, WRFSBASE,
and WRGSBASE.
        """
        return self[16:17]

    @FSGSBASE.setter
    def FSGSBASE(self, value):
        self[16:17] = value
    
    @property
    def PCIDE(self):
        """
        PCID-Enable
        Enables process-context identifiers (PCIDs) when set.
Can be set only in IA-32e mode (if IA32_EFER.LMA = 1).
        """
        return self[17:18]

    @PCIDE.setter
    def PCIDE(self, value):
        self[17:18] = value
    
    @property
    def OSXSAVE(self):
        """
        XSAVE and Processor Extended States-Enable
        When set, this flag:

-# indicates (via CPUID.01H:ECX.OSXSAVE[bit 27]) that the operating system supports
   the use of the XGETBV, XSAVE and XRSTOR instructions by general software;

-# enables the XSAVE and XRSTOR instructions to save and restore the x87 FPU state
   (including MMX registers), the SSE state (XMM registers and MXCSR), along with other
   processor extended states enabled in XCR0;

-# enables the processor to execute XGETBV and XSETBV instructions in order to read
   and write XCR0.
        """
        return self[18:19]

    @OSXSAVE.setter
    def OSXSAVE(self, value):
        self[18:19] = value
    
    @property
    def SMEP(self):
        """
        SMEP-Enable
        Enables supervisor-mode execution prevention (SMEP) when set.
        """
        return self[20:21]

    @SMEP.setter
    def SMEP(self, value):
        self[20:21] = value
    
    @property
    def SMAP(self):
        """
        SMAP-Enable
        Enables supervisor-mode access prevention (SMAP) when set.
        """
        return self[21:22]

    @SMAP.setter
    def SMAP(self, value):
        self[21:22] = value
    
    @property
    def PKE(self):
        """
        Protection-Key-Enable
        Enables 4-level paging to associate each linear address
with a protection key. The PKRU register specifies, for each protection key, whether user-mode linear
addresses with that protection key can be read or written. This bit also enables access to the PKRU register
using the RDPKRU and WRPKRU instructions.
        """
        return self[22:23]

    @PKE.setter
    def PKE(self, value):
        self[22:23] = value
    