from future.utils import with_metaclass
from utils.bit_field import *


__doc__ = """

"""
class SegmentDescriptorRegister32(with_metaclass(BitFieldMeta, BitField)):
    """Pseudo-Descriptor Format (32-bit)."""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=6)

    
    
    LIMIT = BitFieldMember(
        "LIMIT",
        """
        Limit:
        Limit.
        """,
        0,
        16
        
    )

    
    BASE_ADDRESS = BitFieldMember(
        "BASE_ADDRESS",
        """
        Base Address:
        Base Address.
        """,
        16,
        32
        
    )

    

class SegmentDescriptorRegister64(with_metaclass(BitFieldMeta, BitField)):
    """Pseudo-Descriptor Format (64-bit)."""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=10)

    
    
    LIMIT = BitFieldMember(
        "LIMIT",
        """
        Limit:
        Limit.
        """,
        0,
        16
        
    )

    
    BASE = BitFieldMember(
        "BASE",
        """
        Base Address:
        Base Address.
        """,
        16,
        64
        
    )

    

class SegmentAccessRights(with_metaclass(BitFieldMeta, BitField)):
    """Segment access rights."""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=4)


    
    TYPE = BitFieldMember(
        "TYPE",
        """
        Type field:
        Indicates the segment or gate type and specifies the kinds of access that can be made to the
segment and the direction of growth. The interpretation of this field depends on whether the
descriptor type flag specifies an application (code or data) descriptor or a system descriptor. The
encoding of the type field is different for code, data, and system descriptors.
        """,
        8,
        4
    )

    
    S_FLAG = BitFieldMember(
        "S_FLAG",
        """
        S (descriptor type) flag:
        Specifies whether the segment descriptor is for a system segment (S flag is clear) or a code or data
segment (S flag is set).
        """,
        12,
        1
    )

    
    DPL = BitFieldMember(
        "DPL",
        """
        DPL (descriptor privilege level) field:
        Specifies the privilege level of the segment. The privilege level can range from 0 to 3, with 0 being
the most privileged level. The DPL is used to control access to the segment. See Section 5.5, Privilege
Levels, for a description of the relationship of the DPL to the CPL of the executing code
segment and the RPL of a segment selector.
        """,
        13,
        2
    )

    
    P = BitFieldMember(
        "P",
        """
        P (segment-present) flag:
        Indicates whether the segment is present in memory (set) or not present (clear). If this flag is clear,
the processor generates a segment-not-present exception (\#NP) when a segment selector that
points to the segment descriptor is loaded into a segment register. Memory management software
can use this flag to control which segments are actually loaded into physical memory at a given
time. It offers a control in addition to paging for managing virtual memory.
        """,
        15,
        1
    )

    
    AVAILABLE = BitFieldMember(
        "AVAILABLE",
        """
        Available bit:
        Bit 20 of the second doubleword of the segment descriptor is available for use by system software.
        """,
        20,
        1
    )

    
    L = BitFieldMember(
        "L",
        """
        L (64-bit code segment) flag:
        In IA-32e mode, bit 21 of the second doubleword of the segment descriptor indicates whether a
code segment contains native 64-bit code. A value of 1 indicates instructions in this code segment
are executed in 64-bit mode. A value of 0 indicates the instructions in this code segment are
executed in compatibility mode. If L-bit is set, then D-bit must be cleared. When not in IA-32e mode
or for non-code segments, bit 21 is reserved and should always be set to 0.
        """,
        21,
        1
    )

    
    DB = BitFieldMember(
        "DB",
        """
        D/B (default operation size/default stack pointer size and/or upper bound) flag:
        Performs different functions depending on whether the segment descriptor is an executable code
segment, an expand-down data segment, or a stack segment. (This flag should always be set to 1
for 32-bit code and data segments and to 0 for 16-bit code and data segments.)

- Executable code segment. The flag is called the D flag and it indicates the default length for
  effective addresses and operands referenced by instructions in the segment. If the flag is set,
  32-bit addresses and 32-bit or 8-bit operands are assumed; if it is clear, 16-bit addresses and
  16-bit or 8-bit operands are assumed.
  The instruction prefix 66H can be used to select an operand size other than the default, and the
  prefix 67H can be used select an address size other than the default.

- Stack segment (data segment pointed to by the SS register). The flag is called the B (big)
  flag and it specifies the size of the stack pointer used for implicit stack operations (such as
  pushes, pops, and calls). If the flag is set, a 32-bit stack pointer is used, which is stored in the
  32-bit ESP register; if the flag is clear, a 16-bit stack pointer is used, which is stored in the 16-
  bit SP register. If the stack segment is set up to be an expand-down data segment (described in
  the next paragraph), the B flag also specifies the upper bound of the stack segment.

- Expand-down data segment. The flag is called the B flag and it specifies the upper bound of
  the segment. If the flag is set, the upper bound is FFFFFFFFH (4 GBytes); if the flag is clear, the
  upper bound is FFFFH (64 KBytes).
        """,
        22,
        1
    )

    
    G = BitFieldMember(
        "G",
        """
        G (granularity) flag:
        Determines the scaling of the segment limit field. When the granularity flag is clear, the segment
limit is interpreted in byte units; when flag is set, the segment limit is interpreted in 4-KByte units.
(This flag does not affect the granularity of the base address; it is always byte granular.) When the
granularity flag is set, the twelve least significant bits of an offset are not tested when checking the
offset against the segment limit. For example, when the granularity flag is set, a limit of 0 results in
valid offsets from 0 to 4095.
        """,
        23,
        1
    )

    

class SegmentDescriptor32(with_metaclass(BitFieldMeta, BitField)):
    """A segment descriptor is a data structure in a GDT or LDT that provides the processor with the size and location of
a segment, as well as access control and status information. Segment descriptors are typically created by
compilers, linkers, loaders, or the operating system or executive, but not application programs."""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=4)

    
    
    LIMIT_LOW = BitFieldMember(
        "LIMIT_LOW",
        """
        Segment limit field (15:00):
        Specifies the size of the segment. The processor puts together the two segment limit fields to form
a 20-bit value. The processor interprets the segment limit in one of two ways, depending on the
setting of the G (granularity) flag:

- If the granularity flag is clear, the segment size can range from 1 byte to 1 MByte, in byte increments.

- If the granularity flag is set, the segment size can range from 4 KBytes to 4 GBytes, in 4-KByte
  increments.

The processor uses the segment limit in two different ways, depending on whether the segment is
an expand-up or an expand-down segment. For expand-up segments, the offset
in a logical address can range from 0 to the segment limit. Offsets greater than the segment limit
generate general-protection exceptions (\#GP, for all segments other than SS) or stack-fault exceptions
(\#SS for the SS segment). For expand-down segments, the segment limit has the reverse
function; the offset can range from the segment limit plus 1 to FFFFFFFFH or FFFFH, depending on
the setting of the B flag. Offsets less than or equal to the segment limit generate general-protection
exceptions or stack-fault exceptions. Decreasing the value in the segment limit field for an expanddown
segment allocates new memory at the bottom of the segment's address space, rather than at
the top. IA-32 architecture stacks always grow downwards, making this mechanism convenient for
expandable stacks.
        """,
        0,
        16
        
    )

    
    BASE_LOW = BitFieldMember(
        "BASE_LOW",
        """
        Base address field (15:00):
        Defines the location of byte 0 of the segment within the 4-GByte linear address space. The
processor puts together the three base address fields to form a single 32-bit value. Segment base
addresses should be aligned to 16-byte boundaries. Although 16-byte alignment is not required,
this alignment allows programs to maximize performance by aligning code and data on 16-byte
boundaries.
        """,
        16,
        16
        
    )

    

class SegmentDescriptor64(with_metaclass(BitFieldMeta, BitField)):
    """A segment descriptor is a data structure in a GDT or LDT that provides the processor with the size and location of
a segment, as well as access control and status information. Segment descriptors are typically created by
compilers, linkers, loaders, or the operating system or executive, but not application programs."""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=12)

    
    
    LIMIT_LOW = BitFieldMember(
        "LIMIT_LOW",
        """
        Segment limit field (15:00):
        Specifies the size of the segment. The processor puts together the two segment limit fields to form
a 20-bit value. The processor interprets the segment limit in one of two ways, depending on the
setting of the G (granularity) flag:

- If the granularity flag is clear, the segment size can range from 1 byte to 1 MByte, in byte increments.

- If the granularity flag is set, the segment size can range from 4 KBytes to 4 GBytes, in 4-KByte
  increments.

The processor uses the segment limit in two different ways, depending on whether the segment is
an expand-up or an expand-down segment. For expand-up segments, the offset
in a logical address can range from 0 to the segment limit. Offsets greater than the segment limit
generate general-protection exceptions (\#GP, for all segments other than SS) or stack-fault exceptions
(\#SS for the SS segment). For expand-down segments, the segment limit has the reverse
function; the offset can range from the segment limit plus 1 to FFFFFFFFH or FFFFH, depending on
the setting of the B flag. Offsets less than or equal to the segment limit generate general-protection
exceptions or stack-fault exceptions. Decreasing the value in the segment limit field for an expanddown
segment allocates new memory at the bottom of the segment's address space, rather than at
the top. IA-32 architecture stacks always grow downwards, making this mechanism convenient for
expandable stacks.
        """,
        0,
        16
        
    )

    
    BASE_LOW = BitFieldMember(
        "BASE_LOW",
        """
        Base address field (15:00):
        Defines the location of byte 0 of the segment within the 4-GByte linear address space. The
processor puts together the three base address fields to form a single 32-bit value. Segment base
addresses should be aligned to 16-byte boundaries. Although 16-byte alignment is not required,
this alignment allows programs to maximize performance by aligning code and data on 16-byte
boundaries.
        """,
        16,
        16
        
    )

    
    BASE_UPPER = BitFieldMember(
        "BASE_UPPER",
        """
        Base address field (32:63); see description of $BASE_LOW for more details:
        Base address field (32:63); see description of $BASE_LOW for more details.
        """,
        32,
        32
        
    )

    
    MUST_BE_ZERO = BitFieldMember(
        "MUST_BE_ZERO",
        """
        Base address field (32:63); see description of $BASE_LOW for more details:
        Base address field (32:63); see description of $BASE_LOW for more details.
        """,
        64,
        32
        
    )

    

SEGMENT_DESCRIPTOR_TYPE_SYSTEM = 0x0

SEGMENT_DESCRIPTOR_TYPE_CODE_OR_DATA = 0x1

