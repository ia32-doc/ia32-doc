from utils.bit_field import BitField

class Dr7(BitField):
    """"""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=8)

    _FIELDS = ["L0","G0","L1","G1","L2","G2","L3","G3","LE","GE","RTM","GD","RW0","LEN0","RW1","LEN1","RW2","LEN2","RW3","LEN3",]

    
    @property
    def L0(self):
        """
        L0 through L3 (local breakpoint enable) flags (bits 0, 2, 4, and 6)
        Enables (when set) the breakpoint
condition for the associated breakpoint for the current task. When a breakpoint condition is detected and its
associated Ln flag is set, a debug exception is generated. The processor automatically clears these flags on
every task switch to avoid unwanted breakpoint conditions in the new task.
        """
        return self[0:1]

    @L0.setter
    def L0(self, value):
        self[0:1] = value
    
    @property
    def G0(self):
        """
        G0 through G3 (global breakpoint enable) flags (bits 1, 3, 5, and 7)
        Enables (when set) the
breakpoint condition for the associated breakpoint for all tasks. When a breakpoint condition is detected and its
associated Gn flag is set, a debug exception is generated. The processor does not clear these flags on a task
switch, allowing a breakpoint to be enabled for all tasks.
        """
        return self[1:2]

    @G0.setter
    def G0(self, value):
        self[1:2] = value
    
    @property
    def L1(self):
        """
        
        
        """
        return self[2:3]

    @L1.setter
    def L1(self, value):
        self[2:3] = value
    
    @property
    def G1(self):
        """
        
        
        """
        return self[3:4]

    @G1.setter
    def G1(self, value):
        self[3:4] = value
    
    @property
    def L2(self):
        """
        
        
        """
        return self[4:5]

    @L2.setter
    def L2(self, value):
        self[4:5] = value
    
    @property
    def G2(self):
        """
        
        
        """
        return self[5:6]

    @G2.setter
    def G2(self, value):
        self[5:6] = value
    
    @property
    def L3(self):
        """
        
        
        """
        return self[6:7]

    @L3.setter
    def L3(self, value):
        self[6:7] = value
    
    @property
    def G3(self):
        """
        
        
        """
        return self[7:8]

    @G3.setter
    def G3(self, value):
        self[7:8] = value
    
    @property
    def LE(self):
        """
        LE (local exact breakpoint enable)
        This feature is not supported in
the P6 family processors, later IA-32 processors, and Intel 64 processors. When set, these flags cause the
processor to detect the exact instruction that caused a data breakpoint condition. For backward and forward
compatibility with other Intel processors, we recommend that the LE and GE flags be set to 1 if exact
breakpoints are required.
        """
        return self[8:9]

    @LE.setter
    def LE(self, value):
        self[8:9] = value
    
    @property
    def GE(self):
        """
        GE (global exact breakpoint enable)
        
        """
        return self[9:10]

    @GE.setter
    def GE(self, value):
        self[9:10] = value
    
    @property
    def RTM(self):
        """
        RTM (restricted transactional memory) flag
        Enables (when set) advanced debugging of RTM
transactional regions. This advanced debugging is enabled only if IA32_DEBUGCTL.RTM is
also set.
        """
        return self[11:12]

    @RTM.setter
    def RTM(self, value):
        self[11:12] = value
    
    @property
    def GD(self):
        """
        GD (general detect enable) flag
        Enables (when set) debug-register protection, which causes a
debug exception to be generated prior to any MOV instruction that accesses a debug register. When such a
condition is detected, the BD flag in debug status register DR6 is set prior to generating the exception. This
condition is provided to support in-circuit emulators.

When the emulator needs to access the debug registers, emulator software can set the GD flag to prevent
interference from the program currently executing on the processor.

The processor clears the GD flag upon entering to the debug exception handler, to allow the handler access to
the debug registers.
        """
        return self[13:14]

    @GD.setter
    def GD(self, value):
        self[13:14] = value
    
    @property
    def RW0(self):
        """
        R/W0 through R/W3 (read/write) fields (bits 16, 17, 20, 21, 24, 25, 28, and 29)
        Specifies the
breakpoint condition for the corresponding breakpoint. The DE (debug extensions) flag in control register CR4
determines how the bits in the R/Wn fields are interpreted. When the DE flag is set, the processor interprets
bits as follows:

- 00 - Break on instruction execution only.

- 01 - Break on data writes only.

- 10 - Break on I/O reads or writes.

- 11 - Break on data reads or writes but not instruction fetches.

When the DE flag is clear, the processor interprets the R/Wn bits the same as for the Intel386 and Intel486
processors, which is as follows:

- 00 - Break on instruction execution only.

- 01 - Break on data writes only.

- 10 - Undefined.

- 11 - Break on data reads or writes but not instruction fetches.
        """
        return self[16:18]

    @RW0.setter
    def RW0(self, value):
        self[16:18] = value
    
    @property
    def LEN0(self):
        """
        LEN0 through LEN3 (Length) fields (bits 18, 19, 22, 23, 26, 27, 30, and 31)
        Specify the size of the
memory location at the address specified in the corresponding breakpoint address register (DR0 through DR3).
These fields are interpreted as follows:

- 00 - 1-byte length.

- 01 - 2-byte length.

- 10 - Undefined (or 8 byte length, see note below).

- 11 - 4-byte length.

If the corresponding RWn field in register DR7 is 00 (instruction execution), then the LENn field should also be 00.
The effect of using other lengths is undefined.
        """
        return self[18:20]

    @LEN0.setter
    def LEN0(self, value):
        self[18:20] = value
    
    @property
    def RW1(self):
        """
        
        
        """
        return self[20:22]

    @RW1.setter
    def RW1(self, value):
        self[20:22] = value
    
    @property
    def LEN1(self):
        """
        
        
        """
        return self[22:24]

    @LEN1.setter
    def LEN1(self, value):
        self[22:24] = value
    
    @property
    def RW2(self):
        """
        
        
        """
        return self[24:26]

    @RW2.setter
    def RW2(self, value):
        self[24:26] = value
    
    @property
    def LEN2(self):
        """
        
        
        """
        return self[26:28]

    @LEN2.setter
    def LEN2(self, value):
        self[26:28] = value
    
    @property
    def RW3(self):
        """
        
        
        """
        return self[28:30]

    @RW3.setter
    def RW3(self, value):
        self[28:30] = value
    
    @property
    def LEN3(self):
        """
        
        
        """
        return self[30:32]

    @LEN3.setter
    def LEN3(self, value):
        self[30:32] = value
    