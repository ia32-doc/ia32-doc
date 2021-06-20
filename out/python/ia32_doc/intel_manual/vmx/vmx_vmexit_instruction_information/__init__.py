from future.utils import with_metaclass
from utils.ia32_struct import *
from utils.ia32_bit_field import *


__doc__ = """
@brief Information for VM Exits Due to Instruction Execution

Information for VM Exits Due to Instruction Execution.
"""


class VmxVmexitInstructionInfoInsOuts(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
    """
    @brief VM-Exit Instruction-Information Field as Used for INS and OUTS

VM-Exit Instruction-Information Field as Used for INS and OUTS.
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super(VmxVmexitInstructionInfoInsOuts, self).__init__(value, byte_offset, byte_width, max_bytes=8)



    ADDRESS_SIZE = Ia32BitFieldMember(
        "ADDRESS_SIZE",
        """
        @brief Address size

0: 16-bit

1: 32-bit

2: 64-bit (used only on processors that support Intel 64 architecture)

Other values not used.
        """,

        7,
        3

    )


    SEGMENT_REGISTER = Ia32BitFieldMember(
        "SEGMENT_REGISTER",
        """
        @brief Segment register

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


class VmxVmexitInstructionInfoInvalidate(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
    """
    @brief VM-Exit Instruction-Information Field as Used for INVEPT, INVPCID, and INVVPID

VM-Exit Instruction-Information Field as Used for INVEPT, INVPCID, and INVVPID.
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super(VmxVmexitInstructionInfoInvalidate, self).__init__(value, byte_offset, byte_width, max_bytes=8)



    SCALING = Ia32BitFieldMember(
        "SCALING",
        """
        @brief Scaling

0: no scaling

1: scale by 2

2: scale by 4

3: scale by 8 (used only on processors that support Intel 64 architecture)

Undefined for instructions with no index register (bit 22 is set).
        """,

        0,
        2

    )


    ADDRESS_SIZE = Ia32BitFieldMember(
        "ADDRESS_SIZE",
        """
        @brief Address size

0: 16-bit

1: 32-bit

2: 64-bit (used only on processors that support Intel 64 architecture)

Other values not used.
        """,

        7,
        3

    )


    SEGMENT_REGISTER = Ia32BitFieldMember(
        "SEGMENT_REGISTER",
        """
        @brief Segment register

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


    INDEX_REG = Ia32BitFieldMember(
        "INDEX_REG",
        """
        @brief General-purpose register. Undefined for instructions with no index register (bit 22 is set)

General-purpose register. Undefined for instructions with no index register (bit 22 is set).
        """,

        18,
        4

    )


    INDEX_REG_INVALID = Ia32BitFieldMember(
        "INDEX_REG_INVALID",
        """
        @brief IndexReg invalid (0 = valid; 1 = invalid)

IndexReg invalid (0 = valid; 1 = invalid).
        """,

        22,
        1

    )


    BASE_REG = Ia32BitFieldMember(
        "BASE_REG",
        """
        @brief BaseReg (encoded as IndexReg above).
Undefined for memory instructions with no base register (bit 27 is set)

BaseReg (encoded as IndexReg above).
Undefined for memory instructions with no base register (bit 27 is set).
        """,

        23,
        4

    )


    BASE_REG_INVALID = Ia32BitFieldMember(
        "BASE_REG_INVALID",
        """
        @brief BaseReg invalid (0 = valid; 1 = invalid)

BaseReg invalid (0 = valid; 1 = invalid).
        """,

        27,
        1

    )


    REG_2 = Ia32BitFieldMember(
        "REG_2",
        """
        @brief Reg2 (same encoding as IndexReg above)

Reg2 (same encoding as IndexReg above).
        """,

        28,
        4

    )


class VmxVmexitInstructionInfoGdtrIdtrAccess(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
    """
    @brief VM-Exit Instruction-Information Field as Used for LIDT, LGDT, SIDT, or SGDT

VM-Exit Instruction-Information Field as Used for LIDT, LGDT, SIDT, or SGDT.
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super(VmxVmexitInstructionInfoGdtrIdtrAccess, self).__init__(value, byte_offset, byte_width, max_bytes=8)



    SCALING = Ia32BitFieldMember(
        "SCALING",
        """
        @brief Scaling

0: no scaling

1: scale by 2

2: scale by 4

3: scale by 8 (used only on processors that support Intel 64 architecture)

Undefined for instructions with no index register (bit 22 is set).
        """,

        0,
        2

    )


    ADDRESS_SIZE = Ia32BitFieldMember(
        "ADDRESS_SIZE",
        """
        @brief Address size

0: 16-bit

1: 32-bit

2: 64-bit (used only on processors that support Intel 64 architecture)

Other values not used.
        """,

        7,
        3

    )


    OPERAND_SIZE = Ia32BitFieldMember(
        "OPERAND_SIZE",
        """
        @brief Operand size

0: 16-bit

1: 32-bit

Undefined for VM exits from 64-bit mode.
        """,

        11,
        1

    )


    SEGMENT_REGISTER = Ia32BitFieldMember(
        "SEGMENT_REGISTER",
        """
        @brief Segment register

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


    INDEX_REG = Ia32BitFieldMember(
        "INDEX_REG",
        """
        @brief General-purpose register. Undefined for instructions with no index register (bit 22 is set)

General-purpose register. Undefined for instructions with no index register (bit 22 is set).
        """,

        18,
        4

    )


    INDEX_REG_INVALID = Ia32BitFieldMember(
        "INDEX_REG_INVALID",
        """
        @brief IndexReg invalid (0 = valid; 1 = invalid)

IndexReg invalid (0 = valid; 1 = invalid).
        """,

        22,
        1

    )


    BASE_REG = Ia32BitFieldMember(
        "BASE_REG",
        """
        @brief BaseReg (encoded as IndexReg above).
Undefined for memory instructions with no base register (bit 27 is set)

BaseReg (encoded as IndexReg above).
Undefined for memory instructions with no base register (bit 27 is set).
        """,

        23,
        4

    )


    BASE_REG_INVALID = Ia32BitFieldMember(
        "BASE_REG_INVALID",
        """
        @brief BaseReg invalid (0 = valid; 1 = invalid)

BaseReg invalid (0 = valid; 1 = invalid).
        """,

        27,
        1

    )


    INSTR = Ia32BitFieldMember(
        "INSTR",
        """
        @brief Instruction identity

0: SGDT

1: SIDT

2: LGDT

3: LIDT
        """,

        28,
        2

    )


class VmxVmexitInstructionInfoLdtrTrAccess(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
    """
    @brief VM-Exit Instruction-Information Field as Used for LLDT, LTR, SLDT, and STR

VM-Exit Instruction-Information Field as Used for LLDT, LTR, SLDT, and STR.
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super(VmxVmexitInstructionInfoLdtrTrAccess, self).__init__(value, byte_offset, byte_width, max_bytes=8)



    SCALING = Ia32BitFieldMember(
        "SCALING",
        """
        @brief Scaling

0: no scaling

1: scale by 2

2: scale by 4

3: scale by 8 (used only on processors that support Intel 64 architecture)

Undefined for instructions with no index register (bit 22 is set).
        """,

        0,
        2

    )


    REG_1 = Ia32BitFieldMember(
        "REG_1",
        """
        @brief Reg1. Undefined for memory instructions (bit 10 is clear)

Reg1. Undefined for memory instructions (bit 10 is clear).
        """,

        3,
        4

    )


    ADDRESS_SIZE = Ia32BitFieldMember(
        "ADDRESS_SIZE",
        """
        @brief Address size

0: 16-bit

1: 32-bit

2: 64-bit (used only on processors that support Intel 64 architecture)

Other values not used. Undefined for register instructions (bit 10 is set).
        """,

        7,
        3

    )


    MEM_REG = Ia32BitFieldMember(
        "MEM_REG",
        """
        @brief Mem/Reg (0 = memory; 1 = register)

Mem/Reg (0 = memory; 1 = register).
        """,

        10,
        1

    )


    SEGMENT_REGISTER = Ia32BitFieldMember(
        "SEGMENT_REGISTER",
        """
        @brief Segment register

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


    INDEX_REG = Ia32BitFieldMember(
        "INDEX_REG",
        """
        @brief General-purpose register. Undefined for register instructions (bit 10 is set) and for memory
instructions with no index register (bit 10 is clear and bit 22 is set)

General-purpose register. Undefined for register instructions (bit 10 is set) and for memory
instructions with no index register (bit 10 is clear and bit 22 is set).
        """,

        18,
        4

    )


    INDEX_REG_INVALID = Ia32BitFieldMember(
        "INDEX_REG_INVALID",
        """
        @brief IndexReg invalid (0 = valid; 1 = invalid). Undefined for register instructions (bit 10 is set)

IndexReg invalid (0 = valid; 1 = invalid). Undefined for register instructions (bit 10 is set).
        """,

        22,
        1

    )


    BASE_REG = Ia32BitFieldMember(
        "BASE_REG",
        """
        @brief BaseReg (encoded as IndexReg above).
Undefined for register instructions (bit 10 is set) and for memory instructions with no base register
(bit 10 is clear and bit 27 is set)

BaseReg (encoded as IndexReg above).
Undefined for register instructions (bit 10 is set) and for memory instructions with no base register
(bit 10 is clear and bit 27 is set).
        """,

        23,
        4

    )


    BASE_REG_INVALID = Ia32BitFieldMember(
        "BASE_REG_INVALID",
        """
        @brief BaseReg invalid (0 = valid; 1 = invalid). Undefined for register instructions (bit 10 is set)

BaseReg invalid (0 = valid; 1 = invalid). Undefined for register instructions (bit 10 is set).
        """,

        27,
        1

    )


    INSTR = Ia32BitFieldMember(
        "INSTR",
        """
        @brief Instruction identity

0: SLDT

1: STR

2: LLDT

3: LTR
        """,

        28,
        2

    )


class VmxVmexitInstructionInfoRdrandRdseed(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
    """
    @brief VM-Exit Instruction-Information Field as Used for RDRAND and RDSEED

VM-Exit Instruction-Information Field as Used for RDRAND and RDSEED.
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super(VmxVmexitInstructionInfoRdrandRdseed, self).__init__(value, byte_offset, byte_width, max_bytes=8)



    DEST_REGISTER = Ia32BitFieldMember(
        "DEST_REGISTER",
        """
        @brief Destination register

Destination register.
        """,

        3,
        4

    )


    OPERAND_SIZE = Ia32BitFieldMember(
        "OPERAND_SIZE",
        """
        @brief Operand size

0: 16-bit

1: 32-bit

2: 64-bit

The value 3 is not used.
        """,

        11,
        2

    )


class VmxVmexitInstructionInfoVmxAndXsaves(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
    """
    @brief VM-Exit Instruction-Information Field as Used for VMCLEAR, VMPTRLD, VMPTRST, VMXON, XRSTORS, and XSAVES

VM-Exit Instruction-Information Field as Used for VMCLEAR, VMPTRLD, VMPTRST, VMXON, XRSTORS, and XSAVES.
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super(VmxVmexitInstructionInfoVmxAndXsaves, self).__init__(value, byte_offset, byte_width, max_bytes=8)



    SCALING = Ia32BitFieldMember(
        "SCALING",
        """
        @brief Scaling

0: no scaling

1: scale by 2

2: scale by 4

3: scale by 8 (used only on processors that support Intel 64 architecture)

Undefined for instructions with no index register (bit 22 is set).
        """,

        0,
        2

    )


    ADDRESS_SIZE = Ia32BitFieldMember(
        "ADDRESS_SIZE",
        """
        @brief Address size

0: 16-bit

1: 32-bit

2: 64-bit (used only on processors that support Intel 64 architecture)

Other values not used.
        """,

        7,
        3

    )


    SEGMENT_REGISTER = Ia32BitFieldMember(
        "SEGMENT_REGISTER",
        """
        @brief Segment register

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


    INDEX_REG = Ia32BitFieldMember(
        "INDEX_REG",
        """
        @brief General-purpose register. Undefined for instructions with no index register (bit 22 is set)

General-purpose register. Undefined for instructions with no index register (bit 22 is set).
        """,

        18,
        4

    )


    INDEX_REG_INVALID = Ia32BitFieldMember(
        "INDEX_REG_INVALID",
        """
        @brief IndexReg invalid (0 = valid; 1 = invalid)

IndexReg invalid (0 = valid; 1 = invalid).
        """,

        22,
        1

    )


    BASE_REG = Ia32BitFieldMember(
        "BASE_REG",
        """
        @brief BaseReg (encoded as IndexReg above).
Undefined for memory instructions with no base register (bit 27 is set)

BaseReg (encoded as IndexReg above).
Undefined for memory instructions with no base register (bit 27 is set).
        """,

        23,
        4

    )


    BASE_REG_INVALID = Ia32BitFieldMember(
        "BASE_REG_INVALID",
        """
        @brief BaseReg invalid (0 = valid; 1 = invalid)

BaseReg invalid (0 = valid; 1 = invalid).
        """,

        27,
        1

    )


class VmxVmexitInstructionInfoVmreadVmwrite(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
    """
    @brief VM-Exit Instruction-Information Field as Used for VMREAD and VMWRITE

VM-Exit Instruction-Information Field as Used for VMREAD and VMWRITE.
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super(VmxVmexitInstructionInfoVmreadVmwrite, self).__init__(value, byte_offset, byte_width, max_bytes=8)



    SCALING = Ia32BitFieldMember(
        "SCALING",
        """
        @brief Scaling

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


    REG_1 = Ia32BitFieldMember(
        "REG_1",
        """
        @brief Reg1. Undefined for memory instructions (bit 10 is clear)

Reg1. Undefined for memory instructions (bit 10 is clear).
        """,

        3,
        4

    )


    ADDRESS_SIZE = Ia32BitFieldMember(
        "ADDRESS_SIZE",
        """
        @brief Address size

0: 16-bit

1: 32-bit

2: 64-bit (used only on processors that support Intel 64 architecture)

Other values not used. Undefined for register instructions (bit 10 is set).
        """,

        7,
        3

    )


    MEM_REG = Ia32BitFieldMember(
        "MEM_REG",
        """
        @brief Mem/Reg (0 = memory; 1 = register)

Mem/Reg (0 = memory; 1 = register).
        """,

        10,
        1

    )


    SEGMENT_REGISTER = Ia32BitFieldMember(
        "SEGMENT_REGISTER",
        """
        @brief Segment register

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


    INDEX_REG = Ia32BitFieldMember(
        "INDEX_REG",
        """
        @brief General-purpose register. Undefined for register instructions (bit 10 is set) and for
memory instructions with no index register (bit 10 is clear and bit 22 is set)

General-purpose register. Undefined for register instructions (bit 10 is set) and for
memory instructions with no index register (bit 10 is clear and bit 22 is set).
        """,

        18,
        4

    )


    INDEX_REG_INVALID = Ia32BitFieldMember(
        "INDEX_REG_INVALID",
        """
        @brief IndexReg invalid (0 = valid; 1 = invalid). Undefined for register instructions (bit 10 is set)

IndexReg invalid (0 = valid; 1 = invalid). Undefined for register instructions (bit 10 is set).
        """,

        22,
        1

    )


    BASE_REG = Ia32BitFieldMember(
        "BASE_REG",
        """
        @brief BaseReg (encoded as Reg1 above).
Undefined for register instructions (bit 10 is set) and for memory instructions with no base
register (bit 10 is clear and bit 27 is set)

BaseReg (encoded as Reg1 above).
Undefined for register instructions (bit 10 is set) and for memory instructions with no base
register (bit 10 is clear and bit 27 is set).
        """,

        23,
        4

    )


    BASE_REG_INVALID = Ia32BitFieldMember(
        "BASE_REG_INVALID",
        """
        @brief BaseReg invalid (0 = valid; 1 = invalid)

BaseReg invalid (0 = valid; 1 = invalid).
        """,

        27,
        1

    )


    REG_2 = Ia32BitFieldMember(
        "REG_2",
        """
        @brief Reg2 (same encoding as IndexReg above)

Reg2 (same encoding as IndexReg above).
        """,

        28,
        4

    )


class VmxSegmentAccessRights(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
    """
    @brief - The low 16 bits correspond to bits 23:8 of the upper 32 bits of a 64-bit segment descriptor. While bits
  19:16 of code-segment and data-segment descriptors correspond to the upper 4 bits of the segment
  limit, the corresponding bits (bits 11:8) are reserved in this VMCS field.

- Bit 16 indicates an unusable segment. Attempts to use such a segment fault except in 64-bit mode.
  In general, a segment register is unusable if it has been loaded with a null selector.

- Bits 31:17 are reserved

- The low 16 bits correspond to bits 23:8 of the upper 32 bits of a 64-bit segment descriptor. While bits
  19:16 of code-segment and data-segment descriptors correspond to the upper 4 bits of the segment
  limit, the corresponding bits (bits 11:8) are reserved in this VMCS field.

- Bit 16 indicates an unusable segment. Attempts to use such a segment fault except in 64-bit mode.
  In general, a segment register is unusable if it has been loaded with a null selector.

- Bits 31:17 are reserved.

@see SEGMENT_DESCRIPTOR_32

@see SEGMENT_DESCRIPTOR_64

@see XXX_ACCESS_RIGHTS fields of 32_BIT_GUEST_STATE_FIELDS
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super(VmxSegmentAccessRights, self).__init__(value, byte_offset, byte_width, max_bytes=4)



    TYPE = Ia32BitFieldMember(
        "TYPE",
        """
        @brief Segment type

Segment type.
        """,

        0,
        4

    )


    S_FLAG = Ia32BitFieldMember(
        "S_FLAG",
        """
        @brief S  Descriptor type (0 = system; 1 = code or data)

S  Descriptor type (0 = system; 1 = code or data).
        """,

        4,
        1

    )


    DPL = Ia32BitFieldMember(
        "DPL",
        """
        @brief DPL  Descriptor privilege level

DPL  Descriptor privilege level.
        """,

        5,
        2

    )


    P = Ia32BitFieldMember(
        "P",
        """
        @brief P  Segment present

P  Segment present.
        """,

        7,
        1

    )


    AVL = Ia32BitFieldMember(
        "AVL",
        """
        @brief AVL  Available for use by system software

AVL  Available for use by system software.
        """,

        12,
        1

    )


    L = Ia32BitFieldMember(
        "L",
        """
        @brief Reserved (except for CS). L  64-bit mode active (for CS only)

Reserved (except for CS). L  64-bit mode active (for CS only).
        """,

        13,
        1

    )


    DB = Ia32BitFieldMember(
        "DB",
        """
        @brief D/B  Default operation size (0 = 16-bit segment; 1 = 32-bit segment)

D/B  Default operation size (0 = 16-bit segment; 1 = 32-bit segment).
        """,

        14,
        1

    )


    G = Ia32BitFieldMember(
        "G",
        """
        @brief G  Granularity

G  Granularity.
        """,

        15,
        1

    )


    UNUSABLE = Ia32BitFieldMember(
        "UNUSABLE",
        """
        @brief Segment unusable (0 = usable; 1 = unusable)

Segment unusable (0 = usable; 1 = unusable).
        """,

        16,
        1

    )


class VmxInterruptibilityState(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
    """
    @brief The IA-32 architecture includes features that permit certain events to be
blocked for a period of time. This field contains information about such blocking

The IA-32 architecture includes features that permit certain events to be
blocked for a period of time. This field contains information about such blocking

@see INTERRUPTIBILITY_STATE of 32_BIT_GUEST_STATE_FIELDS
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super(VmxInterruptibilityState, self).__init__(value, byte_offset, byte_width, max_bytes=4)



    BLOCKING_BY_STI = Ia32BitFieldMember(
        "BLOCKING_BY_STI",
        """
        @brief Execution of STI with RFLAGS.IF = 0 blocks maskable interrupts on the instruction boundary
following its execution.1 Setting this bit indicates that this blocking is in effect

Execution of STI with RFLAGS.IF = 0 blocks maskable interrupts on the instruction boundary
following its execution.1 Setting this bit indicates that this blocking is in effect.

@see Vol2B[4(STISet Interrupt Flag)]
        """,

        0,
        1

    )


    BLOCKING_BY_MOV_SS = Ia32BitFieldMember(
        "BLOCKING_BY_MOV_SS",
        """
        @brief Execution of a MOV to SS or a POP to SS blocks or suppresses certain debug exceptions as well
as interrupts (maskable and nonmaskable) on the instruction boundary following its execution.
Setting this bit indicates that this blocking is in effect. This document uses the term blocking
by MOV SS, but it applies equally to POP SS

Execution of a MOV to SS or a POP to SS blocks or suppresses certain debug exceptions as well
as interrupts (maskable and nonmaskable) on the instruction boundary following its execution.
Setting this bit indicates that this blocking is in effect. This document uses the term blocking
by MOV SS, but it applies equally to POP SS.

@see Vol3A[6.8.3(Masking Exceptions and Interrupts When Switching Stacks)]
        """,

        1,
        1

    )


    BLOCKING_BY_SMI = Ia32BitFieldMember(
        "BLOCKING_BY_SMI",
        """
        @brief System-management interrupts (SMIs) are disabled while the processor is in system-management mode (SMM).
Setting this bit indicates that blocking of SMIs is in effect

System-management interrupts (SMIs) are disabled while the processor is in system-management mode (SMM).
Setting this bit indicates that blocking of SMIs is in effect.

@see Vol3C[34.2(System Management Interrupt (SMI))]
        """,

        2,
        1

    )


    BLOCKING_BY_NMI = Ia32BitFieldMember(
        "BLOCKING_BY_NMI",
        """
        @brief Delivery of a non-maskable interrupt (NMI) or a system-management interrupt (SMI) blocks
subsequent NMIs until the next execution of IRET. Setting this bit indicates that blocking of NMIs is
in effect. Clearing this bit does not imply that NMIs are not (temporarily) blocked for other
reasons.
If the virtual NMIs VM-execution control is 1, this bit does not control the
blocking of NMIs. Instead, it refers to virtual-NMI blocking (the fact that guest software is not
ready for an NMI)

Delivery of a non-maskable interrupt (NMI) or a system-management interrupt (SMI) blocks
subsequent NMIs until the next execution of IRET. Setting this bit indicates that blocking of NMIs is
in effect. Clearing this bit does not imply that NMIs are not (temporarily) blocked for other
reasons.
If the virtual NMIs VM-execution control is 1, this bit does not control the
blocking of NMIs. Instead, it refers to virtual-NMI blocking (the fact that guest software is not
ready for an NMI).

@see Vol3C[6.7.1(Handling Multiple NMIs)]

@see Vol3C[25.3(CHANGES TO INSTRUCTION BEHAVIOR IN VMX NON-ROOT OPERATION)]

@see Vol3C[24.6.1(Pin-Based VM-Execution Controls)]
        """,

        3,
        1

    )


    ENCLAVE_INTERRUPTION = Ia32BitFieldMember(
        "ENCLAVE_INTERRUPTION",
        """
        @brief A VM exit saves this bit as 1 to indicate that the VM exit was incident to enclave mode

A VM exit saves this bit as 1 to indicate that the VM exit was incident to enclave mode.
        """,

        4,
        1

    )


class VmxGuestActivityState:
    """
    

@see ACTIVITY_STATE of 32_BIT_GUEST_STATE_FIELDS
    """

    
      VMX_ACTIVE = 0x0
    
      VMX_HLT = 0x1
    
      VMX_SHUTDOWN = 0x2
    
      VMX_WAIT_FOR_SIPI = 0x3
    
class VmxVmexitReason(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
    """
    @brief Format of Exit Reason

Exit reason (32 bits). This field encodes the reason for the VM exit and has the structure.
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super(VmxVmexitReason, self).__init__(value, byte_offset, byte_width, max_bytes=4)



    BASIC_EXIT_REASON = Ia32BitFieldMember(
        "BASIC_EXIT_REASON",
        """
        @brief Provides basic information about the cause of the VM exit (if bit 31 is clear) or of the VM-entry
failure (if bit 31 is set)

Provides basic information about the cause of the VM exit (if bit 31 is clear) or of the VM-entry
failure (if bit 31 is set).
        """,

        0,
        16

    )


    ALWAYS0 = Ia32BitFieldMember(
        "ALWAYS0",
        """
        @brief Always cleared to 0

Always cleared to 0.
        """,

        16,
        1

    )


    RESERVED1 = Ia32BitFieldMember(
        "RESERVED1",
        """
        
        """,

        17,
        10

    )


    ENCLAVE_MODE = Ia32BitFieldMember(
        "ENCLAVE_MODE",
        """
        @brief A VM exit saves this bit as 1 to indicate that the VM exit was incident to enclave mode

A VM exit saves this bit as 1 to indicate that the VM exit was incident to enclave mode.
        """,

        27,
        1

    )


    PENDING_MTF_VM_EXIT = Ia32BitFieldMember(
        "PENDING_MTF_VM_EXIT",
        """
        @brief Pending MTF VM exit

Pending MTF VM exit.
        """,

        28,
        1

    )


    VM_EXIT_FROM_VMX_ROOT = Ia32BitFieldMember(
        "VM_EXIT_FROM_VMX_ROOT",
        """
        @brief VM exit from VMX root operation

VM exit from VMX root operation.
        """,

        29,
        1

    )


    RESERVED2 = Ia32BitFieldMember(
        "RESERVED2",
        """
        
        """,

        30,
        1

    )


    VM_ENTRY_FAILURE = Ia32BitFieldMember(
        "VM_ENTRY_FAILURE",
        """
        @brief VM-entry failure:

  - 0 = true VM exit

  - 1 = VM-entry failure

VM-entry failure:

  - 0 = true VM exit

  - 1 = VM-entry failure
        """,

        31,
        1

    )


class VmxIoBitmap(Ia32Struct):
    """"""
    class _MemberContainerIoA(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(VmxIoBitmap._MemberContainerIoA, self).__init__(value, byte_offset, byte_width, max_bytes=4096)
    
    
        value = Ia32BitFieldMember('value', 'value', 0, 32768)
    
    
    class _MemberContainerIoB(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(VmxIoBitmap._MemberContainerIoB, self).__init__(value, byte_offset, byte_width, max_bytes=4096)
    
    
        value = Ia32BitFieldMember('value', 'value', 0, 32768)
    
    
    _members = ["A","B",]

    def __init__(self, value):
        self._A = self._MemberContainerIoA(0, 0, 4096 )
        self._B = self._MemberContainerIoB(0, 4096, 4096 )
        super(VmxIoBitmap, self).__init__(value)


    @property
    def A(self):
        return self._A

    @A.setter
    def A(self, value):
        return self._A.set(value)

    @property
    def B(self):
        return self._B

    @B.setter
    def B(self, value):
        return self._B.set(value)


class VmxMsrBitmap(Ia32Struct):
    """"""
    class _MemberContainerRdmsrLow(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(VmxMsrBitmap._MemberContainerRdmsrLow, self).__init__(value, byte_offset, byte_width, max_bytes=1024)
    
    
        value = Ia32BitFieldMember('value', 'value', 0, 8192)
    
    
    class _MemberContainerRdmsrHigh(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(VmxMsrBitmap._MemberContainerRdmsrHigh, self).__init__(value, byte_offset, byte_width, max_bytes=1024)
    
    
        value = Ia32BitFieldMember('value', 'value', 0, 8192)
    
    
    class _MemberContainerWrmsrLow(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(VmxMsrBitmap._MemberContainerWrmsrLow, self).__init__(value, byte_offset, byte_width, max_bytes=1024)
    
    
        value = Ia32BitFieldMember('value', 'value', 0, 8192)
    
    
    class _MemberContainerWrmsrHigh(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(VmxMsrBitmap._MemberContainerWrmsrHigh, self).__init__(value, byte_offset, byte_width, max_bytes=1024)
    
    
        value = Ia32BitFieldMember('value', 'value', 0, 8192)
    
    
    _members = ["RDMSR_LOW","RDMSR_HIGH","WRMSR_LOW","WRMSR_HIGH",]

    def __init__(self, value):
        self._RDMSR_LOW = self._MemberContainerRdmsrLow(0, 0, 1024 )
        self._RDMSR_HIGH = self._MemberContainerRdmsrHigh(0, 1024, 1024 )
        self._WRMSR_LOW = self._MemberContainerWrmsrLow(0, 2048, 1024 )
        self._WRMSR_HIGH = self._MemberContainerWrmsrHigh(0, 3072, 1024 )
        super(VmxMsrBitmap, self).__init__(value)


    @property
    def RDMSR_LOW(self):
        return self._RDMSR_LOW

    @RDMSR_LOW.setter
    def RDMSR_LOW(self, value):
        return self._RDMSR_LOW.set(value)

    @property
    def RDMSR_HIGH(self):
        return self._RDMSR_HIGH

    @RDMSR_HIGH.setter
    def RDMSR_HIGH(self, value):
        return self._RDMSR_HIGH.set(value)

    @property
    def WRMSR_LOW(self):
        return self._WRMSR_LOW

    @WRMSR_LOW.setter
    def WRMSR_LOW(self, value):
        return self._WRMSR_LOW.set(value)

    @property
    def WRMSR_HIGH(self):
        return self._WRMSR_HIGH

    @WRMSR_HIGH.setter
    def WRMSR_HIGH(self, value):
        return self._WRMSR_HIGH.set(value)


