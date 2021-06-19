from future.utils import with_metaclass
from utils.bit_field import *


__doc__ = """
Information for VM Exits Due to Instruction Execution.
"""
class VmxVmexitInstructionInfoInsOuts(with_metaclass(BitFieldMeta, BitField)):
    """VM-Exit Instruction-Information Field as Used for INS and OUTS."""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=8)


    
    ADDRESS_SIZE = BitFieldMember(
        "ADDRESS_SIZE",
        """
        Address size:
        0: 16-bit

1: 32-bit

2: 64-bit (used only on processors that support Intel 64 architecture)

Other values not used.
        """,
        7,
        3
    )

    
    SEGMENT_REGISTER = BitFieldMember(
        "SEGMENT_REGISTER",
        """
        Segment register:
        0: ES

1: CS

2: SS

3: DS

4: FS

5: GS

Other values not used. Undefined for VM exits due to execution of INS.
        """,
        15,
        3
    )

    

class VmxVmexitInstructionInfoInvalidate(with_metaclass(BitFieldMeta, BitField)):
    """VM-Exit Instruction-Information Field as Used for INVEPT, INVPCID, and INVVPID."""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=8)


    
    SCALING = BitFieldMember(
        "SCALING",
        """
        Scaling:
        0: no scaling

1: scale by 2

2: scale by 4

3: scale by 8 (used only on processors that support Intel 64 architecture)

Undefined for instructions with no index register (bit 22 is set).
        """,
        0,
        2
    )

    
    ADDRESS_SIZE = BitFieldMember(
        "ADDRESS_SIZE",
        """
        Address size:
        0: 16-bit

1: 32-bit

2: 64-bit (used only on processors that support Intel 64 architecture)

Other values not used.
        """,
        7,
        3
    )

    
    SEGMENT_REGISTER = BitFieldMember(
        "SEGMENT_REGISTER",
        """
        Segment register:
        0: ES

1: CS

2: SS

3: DS

4: FS

5: GS

Other values not used. Undefined for VM exits due to execution of INS.
        """,
        15,
        3
    )

    
    INDEX_REG = BitFieldMember(
        "INDEX_REG",
        """
        General-purpose register. Undefined for instructions with no index register (bit 22 is set):
        General-purpose register. Undefined for instructions with no index register (bit 22 is set).
        """,
        18,
        4
    )

    
    INDEX_REG_INVALID = BitFieldMember(
        "INDEX_REG_INVALID",
        """
        IndexReg invalid (0 = valid; 1 = invalid):
        IndexReg invalid (0 = valid; 1 = invalid).
        """,
        22,
        1
    )

    
    BASE_REG = BitFieldMember(
        "BASE_REG",
        """
        BaseReg (encoded as IndexReg above).
Undefined for memory instructions with no base register (bit 27 is set):
        BaseReg (encoded as IndexReg above).
Undefined for memory instructions with no base register (bit 27 is set).
        """,
        23,
        4
    )

    
    BASE_REG_INVALID = BitFieldMember(
        "BASE_REG_INVALID",
        """
        BaseReg invalid (0 = valid; 1 = invalid):
        BaseReg invalid (0 = valid; 1 = invalid).
        """,
        27,
        1
    )

    
    REG_2 = BitFieldMember(
        "REG_2",
        """
        Reg2 (same encoding as IndexReg above):
        Reg2 (same encoding as IndexReg above).
        """,
        28,
        4
    )

    

class VmxVmexitInstructionInfoGdtrIdtrAccess(with_metaclass(BitFieldMeta, BitField)):
    """VM-Exit Instruction-Information Field as Used for LIDT, LGDT, SIDT, or SGDT."""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=8)


    
    SCALING = BitFieldMember(
        "SCALING",
        """
        Scaling:
        0: no scaling

1: scale by 2

2: scale by 4

3: scale by 8 (used only on processors that support Intel 64 architecture)

Undefined for instructions with no index register (bit 22 is set).
        """,
        0,
        2
    )

    
    ADDRESS_SIZE = BitFieldMember(
        "ADDRESS_SIZE",
        """
        Address size:
        0: 16-bit

1: 32-bit

2: 64-bit (used only on processors that support Intel 64 architecture)

Other values not used.
        """,
        7,
        3
    )

    
    OPERAND_SIZE = BitFieldMember(
        "OPERAND_SIZE",
        """
        Operand size:
        0: 16-bit

1: 32-bit

Undefined for VM exits from 64-bit mode.
        """,
        11,
        1
    )

    
    SEGMENT_REGISTER = BitFieldMember(
        "SEGMENT_REGISTER",
        """
        Segment register:
        0: ES

1: CS

2: SS

3: DS

4: FS

5: GS

Other values not used.
        """,
        15,
        3
    )

    
    INDEX_REG = BitFieldMember(
        "INDEX_REG",
        """
        General-purpose register. Undefined for instructions with no index register (bit 22 is set):
        General-purpose register. Undefined for instructions with no index register (bit 22 is set).
        """,
        18,
        4
    )

    
    INDEX_REG_INVALID = BitFieldMember(
        "INDEX_REG_INVALID",
        """
        IndexReg invalid (0 = valid; 1 = invalid):
        IndexReg invalid (0 = valid; 1 = invalid).
        """,
        22,
        1
    )

    
    BASE_REG = BitFieldMember(
        "BASE_REG",
        """
        BaseReg (encoded as IndexReg above).
Undefined for memory instructions with no base register (bit 27 is set):
        BaseReg (encoded as IndexReg above).
Undefined for memory instructions with no base register (bit 27 is set).
        """,
        23,
        4
    )

    
    BASE_REG_INVALID = BitFieldMember(
        "BASE_REG_INVALID",
        """
        BaseReg invalid (0 = valid; 1 = invalid):
        BaseReg invalid (0 = valid; 1 = invalid).
        """,
        27,
        1
    )

    
    INSTR = BitFieldMember(
        "INSTR",
        """
        Instruction identity:
        0: SGDT

1: SIDT

2: LGDT

3: LIDT
        """,
        28,
        2
    )

    

class VmxVmexitInstructionInfoLdtrTrAccess(with_metaclass(BitFieldMeta, BitField)):
    """VM-Exit Instruction-Information Field as Used for LLDT, LTR, SLDT, and STR."""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=8)


    
    SCALING = BitFieldMember(
        "SCALING",
        """
        Scaling:
        0: no scaling

1: scale by 2

2: scale by 4

3: scale by 8 (used only on processors that support Intel 64 architecture)

Undefined for instructions with no index register (bit 22 is set).
        """,
        0,
        2
    )

    
    REG_1 = BitFieldMember(
        "REG_1",
        """
        Reg1. Undefined for memory instructions (bit 10 is clear):
        Reg1. Undefined for memory instructions (bit 10 is clear).
        """,
        3,
        4
    )

    
    ADDRESS_SIZE = BitFieldMember(
        "ADDRESS_SIZE",
        """
        Address size:
        0: 16-bit

1: 32-bit

2: 64-bit (used only on processors that support Intel 64 architecture)

Other values not used. Undefined for register instructions (bit 10 is set).
        """,
        7,
        3
    )

    
    MEM_REG = BitFieldMember(
        "MEM_REG",
        """
        Mem/Reg (0 = memory; 1 = register):
        Mem/Reg (0 = memory; 1 = register).
        """,
        10,
        1
    )

    
    SEGMENT_REGISTER = BitFieldMember(
        "SEGMENT_REGISTER",
        """
        Segment register:
        0: ES

1: CS

2: SS

3: DS

4: FS

5: GS

Other values not used. Undefined for register instructions (bit 10 is set).
        """,
        15,
        3
    )

    
    INDEX_REG = BitFieldMember(
        "INDEX_REG",
        """
        General-purpose register. Undefined for register instructions (bit 10 is set) and for memory
instructions with no index register (bit 10 is clear and bit 22 is set):
        General-purpose register. Undefined for register instructions (bit 10 is set) and for memory
instructions with no index register (bit 10 is clear and bit 22 is set).
        """,
        18,
        4
    )

    
    INDEX_REG_INVALID = BitFieldMember(
        "INDEX_REG_INVALID",
        """
        IndexReg invalid (0 = valid; 1 = invalid). Undefined for register instructions (bit 10 is set):
        IndexReg invalid (0 = valid; 1 = invalid). Undefined for register instructions (bit 10 is set).
        """,
        22,
        1
    )

    
    BASE_REG = BitFieldMember(
        "BASE_REG",
        """
        BaseReg (encoded as IndexReg above).
Undefined for register instructions (bit 10 is set) and for memory instructions with no base register
(bit 10 is clear and bit 27 is set):
        BaseReg (encoded as IndexReg above).
Undefined for register instructions (bit 10 is set) and for memory instructions with no base register
(bit 10 is clear and bit 27 is set).
        """,
        23,
        4
    )

    
    BASE_REG_INVALID = BitFieldMember(
        "BASE_REG_INVALID",
        """
        BaseReg invalid (0 = valid; 1 = invalid). Undefined for register instructions (bit 10 is set):
        BaseReg invalid (0 = valid; 1 = invalid). Undefined for register instructions (bit 10 is set).
        """,
        27,
        1
    )

    
    INSTR = BitFieldMember(
        "INSTR",
        """
        Instruction identity:
        0: SLDT

1: STR

2: LLDT

3: LTR
        """,
        28,
        2
    )

    

class VmxVmexitInstructionInfoRdrandRdseed(with_metaclass(BitFieldMeta, BitField)):
    """VM-Exit Instruction-Information Field as Used for RDRAND and RDSEED."""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=8)


    
    DEST_REGISTER = BitFieldMember(
        "DEST_REGISTER",
        """
        Destination register:
        Destination register.
        """,
        3,
        4
    )

    
    OPERAND_SIZE = BitFieldMember(
        "OPERAND_SIZE",
        """
        Operand size:
        0: 16-bit

1: 32-bit

2: 64-bit

The value 3 is not used.
        """,
        11,
        2
    )

    

class VmxVmexitInstructionInfoVmxAndXsaves(with_metaclass(BitFieldMeta, BitField)):
    """VM-Exit Instruction-Information Field as Used for VMCLEAR, VMPTRLD, VMPTRST, VMXON, XRSTORS, and XSAVES."""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=8)


    
    SCALING = BitFieldMember(
        "SCALING",
        """
        Scaling:
        0: no scaling

1: scale by 2

2: scale by 4

3: scale by 8 (used only on processors that support Intel 64 architecture)

Undefined for instructions with no index register (bit 22 is set).
        """,
        0,
        2
    )

    
    ADDRESS_SIZE = BitFieldMember(
        "ADDRESS_SIZE",
        """
        Address size:
        0: 16-bit

1: 32-bit

2: 64-bit (used only on processors that support Intel 64 architecture)

Other values not used.
        """,
        7,
        3
    )

    
    SEGMENT_REGISTER = BitFieldMember(
        "SEGMENT_REGISTER",
        """
        Segment register:
        0: ES

1: CS

2: SS

3: DS

4: FS

5: GS

Other values not used.
        """,
        15,
        3
    )

    
    INDEX_REG = BitFieldMember(
        "INDEX_REG",
        """
        General-purpose register. Undefined for instructions with no index register (bit 22 is set):
        General-purpose register. Undefined for instructions with no index register (bit 22 is set).
        """,
        18,
        4
    )

    
    INDEX_REG_INVALID = BitFieldMember(
        "INDEX_REG_INVALID",
        """
        IndexReg invalid (0 = valid; 1 = invalid):
        IndexReg invalid (0 = valid; 1 = invalid).
        """,
        22,
        1
    )

    
    BASE_REG = BitFieldMember(
        "BASE_REG",
        """
        BaseReg (encoded as IndexReg above).
Undefined for memory instructions with no base register (bit 27 is set):
        BaseReg (encoded as IndexReg above).
Undefined for memory instructions with no base register (bit 27 is set).
        """,
        23,
        4
    )

    
    BASE_REG_INVALID = BitFieldMember(
        "BASE_REG_INVALID",
        """
        BaseReg invalid (0 = valid; 1 = invalid):
        BaseReg invalid (0 = valid; 1 = invalid).
        """,
        27,
        1
    )

    

class VmxVmexitInstructionInfoVmreadVmwrite(with_metaclass(BitFieldMeta, BitField)):
    """VM-Exit Instruction-Information Field as Used for VMREAD and VMWRITE."""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=8)


    
    SCALING = BitFieldMember(
        "SCALING",
        """
        Scaling:
        0: no scaling

1: scale by 2

2: scale by 4

3: scale by 8 (used only on processors that support Intel 64 architecture)

Undefined for register instructions (bit 10 is set) and for memory instructions with no index register
(bit 10 is clear and bit 22 is set).
        """,
        0,
        2
    )

    
    REG_1 = BitFieldMember(
        "REG_1",
        """
        Reg1. Undefined for memory instructions (bit 10 is clear):
        Reg1. Undefined for memory instructions (bit 10 is clear).
        """,
        3,
        4
    )

    
    ADDRESS_SIZE = BitFieldMember(
        "ADDRESS_SIZE",
        """
        Address size:
        0: 16-bit

1: 32-bit

2: 64-bit (used only on processors that support Intel 64 architecture)

Other values not used. Undefined for register instructions (bit 10 is set).
        """,
        7,
        3
    )

    
    MEM_REG = BitFieldMember(
        "MEM_REG",
        """
        Mem/Reg (0 = memory; 1 = register):
        Mem/Reg (0 = memory; 1 = register).
        """,
        10,
        1
    )

    
    SEGMENT_REGISTER = BitFieldMember(
        "SEGMENT_REGISTER",
        """
        Segment register:
        0: ES

1: CS

2: SS

3: DS

4: FS

5: GS

Other values not used. Undefined for register instructions (bit 10 is set).
        """,
        15,
        3
    )

    
    INDEX_REG = BitFieldMember(
        "INDEX_REG",
        """
        General-purpose register. Undefined for register instructions (bit 10 is set) and for
memory instructions with no index register (bit 10 is clear and bit 22 is set):
        General-purpose register. Undefined for register instructions (bit 10 is set) and for
memory instructions with no index register (bit 10 is clear and bit 22 is set).
        """,
        18,
        4
    )

    
    INDEX_REG_INVALID = BitFieldMember(
        "INDEX_REG_INVALID",
        """
        IndexReg invalid (0 = valid; 1 = invalid). Undefined for register instructions (bit 10 is set):
        IndexReg invalid (0 = valid; 1 = invalid). Undefined for register instructions (bit 10 is set).
        """,
        22,
        1
    )

    
    BASE_REG = BitFieldMember(
        "BASE_REG",
        """
        BaseReg (encoded as Reg1 above).
Undefined for register instructions (bit 10 is set) and for memory instructions with no base
register (bit 10 is clear and bit 27 is set):
        BaseReg (encoded as Reg1 above).
Undefined for register instructions (bit 10 is set) and for memory instructions with no base
register (bit 10 is clear and bit 27 is set).
        """,
        23,
        4
    )

    
    BASE_REG_INVALID = BitFieldMember(
        "BASE_REG_INVALID",
        """
        BaseReg invalid (0 = valid; 1 = invalid):
        BaseReg invalid (0 = valid; 1 = invalid).
        """,
        27,
        1
    )

    
    REG_2 = BitFieldMember(
        "REG_2",
        """
        Reg2 (same encoding as IndexReg above):
        Reg2 (same encoding as IndexReg above).
        """,
        28,
        4
    )

    

class VmxSegmentAccessRights(with_metaclass(BitFieldMeta, BitField)):
    """- The low 16 bits correspond to bits 23:8 of the upper 32 bits of a 64-bit segment descriptor. While bits
  19:16 of code-segment and data-segment descriptors correspond to the upper 4 bits of the segment
  limit, the corresponding bits (bits 11:8) are reserved in this VMCS field.

- Bit 16 indicates an unusable segment. Attempts to use such a segment fault except in 64-bit mode.
  In general, a segment register is unusable if it has been loaded with a null selector.

- Bits 31:17 are reserved."""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=4)


    
    TYPE = BitFieldMember(
        "TYPE",
        """
        Segment type:
        Segment type.
        """,
        0,
        4
    )

    
    S_FLAG = BitFieldMember(
        "S_FLAG",
        """
        S  Descriptor type (0 = system; 1 = code or data):
        S  Descriptor type (0 = system; 1 = code or data).
        """,
        4,
        1
    )

    
    DPL = BitFieldMember(
        "DPL",
        """
        DPL  Descriptor privilege level:
        DPL  Descriptor privilege level.
        """,
        5,
        2
    )

    
    P = BitFieldMember(
        "P",
        """
        P  Segment present:
        P  Segment present.
        """,
        7,
        1
    )

    
    AVL = BitFieldMember(
        "AVL",
        """
        AVL  Available for use by system software:
        AVL  Available for use by system software.
        """,
        12,
        1
    )

    
    L = BitFieldMember(
        "L",
        """
        Reserved (except for CS). L  64-bit mode active (for CS only):
        Reserved (except for CS). L  64-bit mode active (for CS only).
        """,
        13,
        1
    )

    
    DB = BitFieldMember(
        "DB",
        """
        D/B  Default operation size (0 = 16-bit segment; 1 = 32-bit segment):
        D/B  Default operation size (0 = 16-bit segment; 1 = 32-bit segment).
        """,
        14,
        1
    )

    
    G = BitFieldMember(
        "G",
        """
        G  Granularity:
        G  Granularity.
        """,
        15,
        1
    )

    
    UNUSABLE = BitFieldMember(
        "UNUSABLE",
        """
        Segment unusable (0 = usable; 1 = unusable):
        Segment unusable (0 = usable; 1 = unusable).
        """,
        16,
        1
    )

    

class VmxInterruptibilityState(with_metaclass(BitFieldMeta, BitField)):
    """The IA-32 architecture includes features that permit certain events to be
blocked for a period of time. This field contains information about such blocking"""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=4)


    
    BLOCKING_BY_STI = BitFieldMember(
        "BLOCKING_BY_STI",
        """
        Execution of STI with RFLAGS.IF = 0 blocks maskable interrupts on the instruction boundary
following its execution.1 Setting this bit indicates that this blocking is in effect:
        Execution of STI with RFLAGS.IF = 0 blocks maskable interrupts on the instruction boundary
following its execution.1 Setting this bit indicates that this blocking is in effect.
        """,
        0,
        1
    )

    
    BLOCKING_BY_MOV_SS = BitFieldMember(
        "BLOCKING_BY_MOV_SS",
        """
        Execution of a MOV to SS or a POP to SS blocks or suppresses certain debug exceptions as well
as interrupts (maskable and nonmaskable) on the instruction boundary following its execution.
Setting this bit indicates that this blocking is in effect. This document uses the term blocking
by MOV SS, but it applies equally to POP SS:
        Execution of a MOV to SS or a POP to SS blocks or suppresses certain debug exceptions as well
as interrupts (maskable and nonmaskable) on the instruction boundary following its execution.
Setting this bit indicates that this blocking is in effect. This document uses the term blocking
by MOV SS, but it applies equally to POP SS.
        """,
        1,
        1
    )

    
    BLOCKING_BY_SMI = BitFieldMember(
        "BLOCKING_BY_SMI",
        """
        System-management interrupts (SMIs) are disabled while the processor is in system-management mode (SMM).
Setting this bit indicates that blocking of SMIs is in effect:
        System-management interrupts (SMIs) are disabled while the processor is in system-management mode (SMM).
Setting this bit indicates that blocking of SMIs is in effect.
        """,
        2,
        1
    )

    
    BLOCKING_BY_NMI = BitFieldMember(
        "BLOCKING_BY_NMI",
        """
        Delivery of a non-maskable interrupt (NMI) or a system-management interrupt (SMI) blocks
subsequent NMIs until the next execution of IRET. Setting this bit indicates that blocking of NMIs is
in effect. Clearing this bit does not imply that NMIs are not (temporarily) blocked for other
reasons.
If the virtual NMIs VM-execution control is 1, this bit does not control the
blocking of NMIs. Instead, it refers to virtual-NMI blocking (the fact that guest software is not
ready for an NMI):
        Delivery of a non-maskable interrupt (NMI) or a system-management interrupt (SMI) blocks
subsequent NMIs until the next execution of IRET. Setting this bit indicates that blocking of NMIs is
in effect. Clearing this bit does not imply that NMIs are not (temporarily) blocked for other
reasons.
If the virtual NMIs VM-execution control is 1, this bit does not control the
blocking of NMIs. Instead, it refers to virtual-NMI blocking (the fact that guest software is not
ready for an NMI).
        """,
        3,
        1
    )

    
    ENCLAVE_INTERRUPTION = BitFieldMember(
        "ENCLAVE_INTERRUPTION",
        """
        A VM exit saves this bit as 1 to indicate that the VM exit was incident to enclave mode:
        A VM exit saves this bit as 1 to indicate that the VM exit was incident to enclave mode.
        """,
        4,
        1
    )

    

class VmxGuestActivityState:
    """"""

    
      VMX_ACTIVE = 0x0
    
      VMX_HLT = 0x1
    
      VMX_SHUTDOWN = 0x2
    
      VMX_WAIT_FOR_SIPI = 0x3
    
class VmxVmexitReason(with_metaclass(BitFieldMeta, BitField)):
    """Exit reason (32 bits). This field encodes the reason for the VM exit and has the structure."""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=4)


    
    BASIC_EXIT_REASON = BitFieldMember(
        "BASIC_EXIT_REASON",
        """
        Provides basic information about the cause of the VM exit (if bit 31 is clear) or of the VM-entry
failure (if bit 31 is set):
        Provides basic information about the cause of the VM exit (if bit 31 is clear) or of the VM-entry
failure (if bit 31 is set).
        """,
        0,
        16
    )

    
    ALWAYS0 = BitFieldMember(
        "ALWAYS0",
        """
        Always cleared to 0:
        Always cleared to 0.
        """,
        16,
        1
    )

    
    RESERVED1 = BitFieldMember(
        "RESERVED1",
        """
        :
        
        """,
        17,
        10
    )

    
    ENCLAVE_MODE = BitFieldMember(
        "ENCLAVE_MODE",
        """
        A VM exit saves this bit as 1 to indicate that the VM exit was incident to enclave mode:
        A VM exit saves this bit as 1 to indicate that the VM exit was incident to enclave mode.
        """,
        27,
        1
    )

    
    PENDING_MTF_VM_EXIT = BitFieldMember(
        "PENDING_MTF_VM_EXIT",
        """
        Pending MTF VM exit:
        Pending MTF VM exit.
        """,
        28,
        1
    )

    
    VM_EXIT_FROM_VMX_ROOT = BitFieldMember(
        "VM_EXIT_FROM_VMX_ROOT",
        """
        VM exit from VMX root operation:
        VM exit from VMX root operation.
        """,
        29,
        1
    )

    
    RESERVED2 = BitFieldMember(
        "RESERVED2",
        """
        :
        
        """,
        30,
        1
    )

    
    VM_ENTRY_FAILURE = BitFieldMember(
        "VM_ENTRY_FAILURE",
        """
        VM-entry failure:

  - 0 = true VM exit

  - 1 = VM-entry failure:
        VM-entry failure:

  - 0 = true VM exit

  - 1 = VM-entry failure
        """,
        31,
        1
    )

    

class VmxIoBitmap(with_metaclass(BitFieldMeta, BitField)):
    """"""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=8192)

    
    
    A = BitFieldMember(
        "A",
        """
        :
        
        """,
        0,
        32768
        
    )

    
    B = BitFieldMember(
        "B",
        """
        :
        
        """,
        32768,
        32768
        
    )

    

class VmxMsrBitmap(with_metaclass(BitFieldMeta, BitField)):
    """"""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=4096)

    
    
    RDMSR_LOW = BitFieldMember(
        "RDMSR_LOW",
        """
        :
        
        """,
        0,
        8192
        
    )

    
    RDMSR_HIGH = BitFieldMember(
        "RDMSR_HIGH",
        """
        :
        
        """,
        8192,
        8192
        
    )

    
    WRMSR_LOW = BitFieldMember(
        "WRMSR_LOW",
        """
        :
        
        """,
        16384,
        8192
        
    )

    
    WRMSR_HIGH = BitFieldMember(
        "WRMSR_HIGH",
        """
        :
        
        """,
        24576,
        8192
        
    )

    

