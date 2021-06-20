from future.utils import with_metaclass
from ia32_python.utils.ia32_struct import *
from ia32_python.utils.ia32_bit_field import *


__doc__ = """
@brief System Descriptor Types

When the S (descriptor type) flag in a segment descriptor is clear, the descriptor type is a system descriptor. The
processor recognizes the following types of system descriptors:

- Local descriptor-table (LDT) segment descriptor.

- Task-state segment (TSS) descriptor.

- Call-gate descriptor.

- Interrupt-gate descriptor.

- Trap-gate descriptor.

- Task-gate descriptor.

These descriptor types fall into two categories: system-segment descriptors and gate descriptors. Systemsegment
descriptors point to system segments (LDT and TSS segments). Gate descriptors are in themselves
gates, which hold pointers to procedure entry points in code segments (call, interrupt, and trap gates) or which
hold segment selectors for TSSs (task gates).
"""


SEGMENT_DESCRIPTOR_TYPE_RESERVED_1 = 0x0


SEGMENT_DESCRIPTOR_TYPE_TSS_16_AVAILABLE = 0x1


SEGMENT_DESCRIPTOR_TYPE_LDT = 0x2


SEGMENT_DESCRIPTOR_TYPE_TSS_16_BUSY = 0x3


SEGMENT_DESCRIPTOR_TYPE_CALL_GATE_16 = 0x4


SEGMENT_DESCRIPTOR_TYPE_TASK_GATE = 0x5


SEGMENT_DESCRIPTOR_TYPE_INTERRUPT_GATE_16 = 0x6


SEGMENT_DESCRIPTOR_TYPE_TRAP_GATE_16 = 0x7


SEGMENT_DESCRIPTOR_TYPE_RESERVED_2 = 0x8


SEGMENT_DESCRIPTOR_TYPE_TSS_AVAILABLE = 0x9


SEGMENT_DESCRIPTOR_TYPE_RESERVED_3 = 0xa


SEGMENT_DESCRIPTOR_TYPE_TSS_BUSY = 0xb


SEGMENT_DESCRIPTOR_TYPE_CALL_GATE = 0xc


SEGMENT_DESCRIPTOR_TYPE_RESERVED_4 = 0xd


SEGMENT_DESCRIPTOR_TYPE_INTERRUPT_GATE = 0xe


SEGMENT_DESCRIPTOR_TYPE_TRAP_GATE = 0xf


class SegmentSelector(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
    """
    @brief A segment selector is a 16-bit identifier for a segment. It does not point directly to the segment,
but instead points to the segment descriptor that defines the segment

A segment selector is a 16-bit identifier for a segment. It does not point directly to the segment,
but instead points to the segment descriptor that defines the segment.
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super(SegmentSelector, self).__init__(value, byte_offset, byte_width, max_bytes=2)



    RPL = Ia32BitFieldMember(
        "RPL",
        """
        @brief Specifies the privilege level of the selector. The privilege level can range from 0 to
3, with 0 being the most privileged level

Specifies the privilege level of the selector. The privilege level can range from 0 to
3, with 0 being the most privileged level.

@see Vol3A[5.5(Privilege Levels)]
        """,

        0,
        2

    )


    TI = Ia32BitFieldMember(
        "TI",
        """
        @brief Specifies the descriptor table to use: clearing this flag selects the GDT; setting this flag
selects the current LDT

Specifies the descriptor table to use: clearing this flag selects the GDT; setting this flag
selects the current LDT.
        """,

        2,
        1

    )


    INDEX = Ia32BitFieldMember(
        "INDEX",
        """
        @brief Selects one of 8192 descriptors in the GDT or LDT. The processor multiplies
the index value by 8 (the number of bytes in a segment descriptor) and adds the result to the base
address of the GDT or LDT (from the GDTR or LDTR register, respectively)

Selects one of 8192 descriptors in the GDT or LDT. The processor multiplies
the index value by 8 (the number of bytes in a segment descriptor) and adds the result to the base
address of the GDT or LDT (from the GDTR or LDTR register, respectively).
        """,

        3,
        13

    )


