from utils.bit_field import BitField

class Dr6(BitField):
    """"""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=8)

    _FIELDS = ["BREAKPOINT_CONDITION","BD","BS","BT","RTM",]

    
    @property
    def BREAKPOINT_CONDITION(self):
        """
        B0 through B3 (breakpoint condition detected) flags
        Indicates (when set) that its
associated breakpoint condition was met when a debug exception was generated. These flags are set if the
condition described for each breakpoint by the LENn, and R/Wn flags in debug control register DR7 is true. They
may or may not be set if the breakpoint is not enabled by the Ln or the Gn flags in register DR7. Therefore on
a \#DB, a debug handler should check only those B0-B3 bits which correspond to an enabled breakpoint.
        """
        return self[0:4]

    @BREAKPOINT_CONDITION.setter
    def BREAKPOINT_CONDITION(self, value):
        self[0:4] = value
    
    @property
    def BD(self):
        """
        BD (debug register access detected) flag
        Indicates that the next instruction in the instruction
stream accesses one of the debug registers (DR0 through DR7). This flag is enabled when the GD (general
detect) flag in debug control register DR7 is set.
        """
        return self[13:14]

    @BD.setter
    def BD(self, value):
        self[13:14] = value
    
    @property
    def BS(self):
        """
        BS (single step) flag
        Indicates (when set) that the debug exception was triggered by the singlestep
execution mode (enabled with the TF flag in the EFLAGS register). The single-step mode is the highestpriority
debug exception. When the BS flag is set, any of the other debug status bits also may be set.
        """
        return self[14:15]

    @BS.setter
    def BS(self, value):
        self[14:15] = value
    
    @property
    def BT(self):
        """
        BT (task switch) flag
        Indicates (when set) that the debug exception was triggered by the singlestep
execution mode (enabled with the TF flag in the EFLAGS register). The single-step mode is the highestpriority
debug exception. When the BS flag is set, any of the other debug status bits also may be set.
        """
        return self[15:16]

    @BT.setter
    def BT(self, value):
        self[15:16] = value
    
    @property
    def RTM(self):
        """
        RTM (restricted transactional memory) flag
        Indicates (when clear) that a debug exception
(\#DB) or breakpoint exception (\#BP) occurred inside an RTM region while advanced debugging of RTM transactional
regions was enabled. This bit is set for any other debug exception (including all
those that occur when advanced debugging of RTM transactional regions is not enabled). This bit is always 1 if
the processor does not support RTM.
        """
        return self[16:17]

    @RTM.setter
    def RTM(self, value):
        self[16:17] = value
    