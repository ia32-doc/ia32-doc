from future.utils import with_metaclass
from ia32_python.utils.ia32_struct import *
from ia32_python.utils.ia32_enum import *
from ia32_python.utils.ia32_bit_field import *


__doc__ = """
@brief Segment descriptors


"""


class SegmentDescriptorRegister32(Ia32Struct):
    """@brief Pseudo-Descriptor Format (32-bit)

Pseudo-Descriptor Format (32-bit)."""
    class _MemberContainerLimit(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        @brief Limit
    
    Limit.
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(SegmentDescriptorRegister32._MemberContainerLimit, self).__init__(value, byte_offset, byte_width, max_bytes=2)
    
    
        value = Ia32BitFieldMember('value', 'value', 0, 16)
    
    
    class _MemberContainerBaseAddress(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        @brief Base Address
    
    Base Address.
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(SegmentDescriptorRegister32._MemberContainerBaseAddress, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
        value = Ia32BitFieldMember('value', 'value', 0, 32)
    
    
    _members = ["LIMIT","BASE_ADDRESS",]

    def __init__(self, value):
        self._LIMIT = self._MemberContainerLimit(0, 0, 2 )
        self._BASE_ADDRESS = self._MemberContainerBaseAddress(0, 2, 4 )
        super(SegmentDescriptorRegister32, self).__init__(value)


    @property
    def LIMIT(self):
        return self._LIMIT

    @LIMIT.setter
    def LIMIT(self, value):
        return self._LIMIT.set(value)

    @property
    def BASE_ADDRESS(self):
        return self._BASE_ADDRESS

    @BASE_ADDRESS.setter
    def BASE_ADDRESS(self, value):
        return self._BASE_ADDRESS.set(value)


class SegmentDescriptorRegister64(Ia32Struct):
    """@brief Pseudo-Descriptor Format (64-bit)

Pseudo-Descriptor Format (64-bit)."""
    class _MemberContainerLimit(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        @brief Limit
    
    Limit.
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(SegmentDescriptorRegister64._MemberContainerLimit, self).__init__(value, byte_offset, byte_width, max_bytes=2)
    
    
        value = Ia32BitFieldMember('value', 'value', 0, 16)
    
    
    class _MemberContainerBaseAddress(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        @brief Base Address
    
    Base Address.
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(SegmentDescriptorRegister64._MemberContainerBaseAddress, self).__init__(value, byte_offset, byte_width, max_bytes=8)
    
    
        value = Ia32BitFieldMember('value', 'value', 0, 64)
    
    
    _members = ["LIMIT","BASE",]

    def __init__(self, value):
        self._LIMIT = self._MemberContainerLimit(0, 0, 2 )
        self._BASE = self._MemberContainerBaseAddress(0, 2, 8 )
        super(SegmentDescriptorRegister64, self).__init__(value)


    @property
    def LIMIT(self):
        return self._LIMIT

    @LIMIT.setter
    def LIMIT(self, value):
        return self._LIMIT.set(value)

    @property
    def BASE(self):
        return self._BASE

    @BASE.setter
    def BASE(self, value):
        return self._BASE.set(value)


class SegmentAccessRights(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
    """
    @brief Segment access rights

Segment access rights.
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super(SegmentAccessRights, self).__init__(value, byte_offset, byte_width, max_bytes=4)



    TYPE = Ia32BitFieldMember(
        "TYPE",
        """
        @brief Type field

Indicates the segment or gate type and specifies the kinds of access that can be made to the
segment and the direction of growth. The interpretation of this field depends on whether the
descriptor type flag specifies an application (code or data) descriptor or a system descriptor. The
encoding of the type field is different for code, data, and system descriptors.

@see Vol3A[3.4.5.1(Code- and Data-Segment Descriptor Types)]
        """,

        8,
        4

    )


    S_FLAG = Ia32BitFieldMember(
        "S_FLAG",
        """
        @brief S (descriptor type) flag

Specifies whether the segment descriptor is for a system segment (S flag is clear) or a code or data
segment (S flag is set).
        """,

        12,
        1

    )


    DPL = Ia32BitFieldMember(
        "DPL",
        """
        @brief DPL (descriptor privilege level) field

Specifies the privilege level of the segment. The privilege level can range from 0 to 3, with 0 being
the most privileged level. The DPL is used to control access to the segment. See Section 5.5, Privilege
Levels, for a description of the relationship of the DPL to the CPL of the executing code
segment and the RPL of a segment selector.
        """,

        13,
        2

    )


    P = Ia32BitFieldMember(
        "P",
        """
        @brief P (segment-present) flag

Indicates whether the segment is present in memory (set) or not present (clear). If this flag is clear,
the processor generates a segment-not-present exception (\#NP) when a segment selector that
points to the segment descriptor is loaded into a segment register. Memory management software
can use this flag to control which segments are actually loaded into physical memory at a given
time. It offers a control in addition to paging for managing virtual memory.
        """,

        15,
        1

    )


    AVAILABLE = Ia32BitFieldMember(
        "AVAILABLE",
        """
        @brief Available bit

Bit 20 of the second doubleword of the segment descriptor is available for use by system software.
        """,

        20,
        1

    )


    L = Ia32BitFieldMember(
        "L",
        """
        @brief L (64-bit code segment) flag

In IA-32e mode, bit 21 of the second doubleword of the segment descriptor indicates whether a
code segment contains native 64-bit code. A value of 1 indicates instructions in this code segment
are executed in 64-bit mode. A value of 0 indicates the instructions in this code segment are
executed in compatibility mode. If L-bit is set, then D-bit must be cleared. When not in IA-32e mode
or for non-code segments, bit 21 is reserved and should always be set to 0.
        """,

        21,
        1

    )


    DB = Ia32BitFieldMember(
        "DB",
        """
        @brief D/B (default operation size/default stack pointer size and/or upper bound) flag

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


    G = Ia32BitFieldMember(
        "G",
        """
        @brief G (granularity) flag

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


class SegmentDescriptor32(Ia32Struct):
    """@brief General Segment Descriptor (32-bit)

A segment descriptor is a data structure in a GDT or LDT that provides the processor with the size and location of
a segment, as well as access control and status information. Segment descriptors are typically created by
compilers, linkers, loaders, or the operating system or executive, but not application programs.

@see Vol3A[5.2(FIELDS AND FLAGS USED FOR SEGMENT-LEVEL AND PAGE-LEVEL PROTECTION)]

@see Vol3A[5.2.1(Code-Segment Descriptor in 64-bit Mode)]

@see Vol3A[5.8.3(Call Gates)]

@see Vol3A[6.11(IDT DESCRIPTORS)]

@see Vol3A[6.14.1(64-Bit Mode IDT)]

@see Vol3A[7.2.2(TSS Descriptor)]

@see Vol3A[7.2.3(TSS Descriptor in 64-bit mode)]

@see Vol3A[7.2.5(Task-Gate Descriptor)]"""
    class _MemberContainerSegmentLimitLow(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        @brief Segment limit field (15:00)
    
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
    
    @see Vol3A[3.4.5.1(Code- and Data-Segment Descriptor Types)]
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(SegmentDescriptor32._MemberContainerSegmentLimitLow, self).__init__(value, byte_offset, byte_width, max_bytes=2)
    
    
        value = Ia32BitFieldMember('value', 'value', 0, 16)
    
    
    class _MemberContainerBaseAddressLow(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        @brief Base address field (15:00)
    
    Defines the location of byte 0 of the segment within the 4-GByte linear address space. The
    processor puts together the three base address fields to form a single 32-bit value. Segment base
    addresses should be aligned to 16-byte boundaries. Although 16-byte alignment is not required,
    this alignment allows programs to maximize performance by aligning code and data on 16-byte
    boundaries.
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(SegmentDescriptor32._MemberContainerBaseAddressLow, self).__init__(value, byte_offset, byte_width, max_bytes=2)
    
    
        value = Ia32BitFieldMember('value', 'value', 0, 16)
    
    
    class _MemberContainerSegment_(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        @brief Segment descriptor fields
    
    Segment descriptor fields.
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(SegmentDescriptor32._MemberContainerSegment_, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        BASE_MIDDLE = Ia32BitFieldMember(
            "BASE_MIDDLE",
            """
            @brief Base address field (23:16); see description of $BASE_LOW for more details
    
    Base address field (23:16); see description of $BASE_LOW for more details.
            """,
    
            0,
            8
    
        )
    
    
        TYPE = Ia32BitFieldMember(
            "TYPE",
            """
            @brief Type field
    
    Indicates the segment or gate type and specifies the kinds of access that can be made to the
    segment and the direction of growth. The interpretation of this field depends on whether the
    descriptor type flag specifies an application (code or data) descriptor or a system descriptor. The
    encoding of the type field is different for code, data, and system descriptors.
    
    @see Vol3A[3.4.5.1(Code- and Data-Segment Descriptor Types)]
            """,
    
            8,
            4
    
        )
    
    
        S_FLAG = Ia32BitFieldMember(
            "S_FLAG",
            """
            @brief S (descriptor type) flag
    
    Specifies whether the segment descriptor is for a system segment (S flag is clear) or a code or data
    segment (S flag is set).
            """,
    
            12,
            1
    
        )
    
    
        DPL = Ia32BitFieldMember(
            "DPL",
            """
            @brief DPL (descriptor privilege level) field
    
    Specifies the privilege level of the segment. The privilege level can range from 0 to 3, with 0 being
    the most privileged level. The DPL is used to control access to the segment. See Section 5.5, Privilege
    Levels, for a description of the relationship of the DPL to the CPL of the executing code
    segment and the RPL of a segment selector.
            """,
    
            13,
            2
    
        )
    
    
        P = Ia32BitFieldMember(
            "P",
            """
            @brief P (segment-present) flag
    
    Indicates whether the segment is present in memory (set) or not present (clear). If this flag is clear,
    the processor generates a segment-not-present exception (\#NP) when a segment selector that
    points to the segment descriptor is loaded into a segment register. Memory management software
    can use this flag to control which segments are actually loaded into physical memory at a given
    time. It offers a control in addition to paging for managing virtual memory.
            """,
    
            15,
            1
    
        )
    
    
        LIMIT_HIGH = Ia32BitFieldMember(
            "LIMIT_HIGH",
            """
            @brief Segment limit field (19:16); see description of $LIMIT_LOW for more details
    
    Segment limit field (19:16); see description of $LIMIT_LOW for more details.
            """,
    
            16,
            4
    
        )
    
    
        AVL = Ia32BitFieldMember(
            "AVL",
            """
            @brief Available bit
    
    Bit 20 of the second doubleword of the segment descriptor is available for use by system software.
            """,
    
            20,
            1
    
        )
    
    
        L = Ia32BitFieldMember(
            "L",
            """
            @brief L (64-bit code segment) flag
    
    In IA-32e mode, bit 21 of the second doubleword of the segment descriptor indicates whether a
    code segment contains native 64-bit code. A value of 1 indicates instructions in this code segment
    are executed in 64-bit mode. A value of 0 indicates the instructions in this code segment are
    executed in compatibility mode. If L-bit is set, then D-bit must be cleared. When not in IA-32e mode
    or for non-code segments, bit 21 is reserved and should always be set to 0.
            """,
    
            21,
            1
    
        )
    
    
        DB = Ia32BitFieldMember(
            "DB",
            """
            @brief D/B (default operation size/default stack pointer size and/or upper bound) flag
    
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
    
    
        G = Ia32BitFieldMember(
            "G",
            """
            @brief G (granularity) flag
    
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
    
    
        BASE_HIGH = Ia32BitFieldMember(
            "BASE_HIGH",
            """
            @brief Base address field (31:24); see description of $BASE_LOW for more details
    
    Base address field (31:24); see description of $BASE_LOW for more details.
            """,
    
            24,
            8
    
        )
    
    
    
    _members = ["LIMIT_LOW","BASE_LOW","SEGMENT_",]

    def __init__(self, value):
        self._LIMIT_LOW = self._MemberContainerSegmentLimitLow(0, 0, 2 )
        self._BASE_LOW = self._MemberContainerBaseAddressLow(0, 2, 2 )
        self._SEGMENT_ = self._MemberContainerSegment_(0, 4, 4 )
        super(SegmentDescriptor32, self).__init__(value)


    @property
    def LIMIT_LOW(self):
        return self._LIMIT_LOW

    @LIMIT_LOW.setter
    def LIMIT_LOW(self, value):
        return self._LIMIT_LOW.set(value)

    @property
    def BASE_LOW(self):
        return self._BASE_LOW

    @BASE_LOW.setter
    def BASE_LOW(self, value):
        return self._BASE_LOW.set(value)

    @property
    def SEGMENT_(self):
        return self._SEGMENT_

    @SEGMENT_.setter
    def SEGMENT_(self, value):
        return self._SEGMENT_.set(value)


class SegmentDescriptor64(Ia32Struct):
    """@brief General Segment Descriptor (64-bit)

A segment descriptor is a data structure in a GDT or LDT that provides the processor with the size and location of
a segment, as well as access control and status information. Segment descriptors are typically created by
compilers, linkers, loaders, or the operating system or executive, but not application programs."""
    class _MemberContainerSegmentLimitLow(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        @brief Segment limit field (15:00)
    
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
    
    @see Vol3A[3.4.5.1(Code- and Data-Segment Descriptor Types)]
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(SegmentDescriptor64._MemberContainerSegmentLimitLow, self).__init__(value, byte_offset, byte_width, max_bytes=2)
    
    
        value = Ia32BitFieldMember('value', 'value', 0, 16)
    
    
    class _MemberContainerBaseAddressLow(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        @brief Base address field (15:00)
    
    Defines the location of byte 0 of the segment within the 4-GByte linear address space. The
    processor puts together the three base address fields to form a single 32-bit value. Segment base
    addresses should be aligned to 16-byte boundaries. Although 16-byte alignment is not required,
    this alignment allows programs to maximize performance by aligning code and data on 16-byte
    boundaries.
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(SegmentDescriptor64._MemberContainerBaseAddressLow, self).__init__(value, byte_offset, byte_width, max_bytes=2)
    
    
        value = Ia32BitFieldMember('value', 'value', 0, 16)
    
    
    class _MemberContainerSegment_(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        @brief Segment descriptor fields
    
    Segment descriptor fields.
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(SegmentDescriptor64._MemberContainerSegment_, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        BASE_MIDDLE = Ia32BitFieldMember(
            "BASE_MIDDLE",
            """
            @brief Base address field (23:16); see description of $BASE_LOW for more details
    
    Base address field (23:16); see description of $BASE_LOW for more details.
            """,
    
            0,
            8
    
        )
    
    
        TYPE = Ia32BitFieldMember(
            "TYPE",
            """
            @brief Type field
    
    Indicates the segment or gate type and specifies the kinds of access that can be made to the
    segment and the direction of growth. The interpretation of this field depends on whether the
    descriptor type flag specifies an application (code or data) descriptor or a system descriptor. The
    encoding of the type field is different for code, data, and system descriptors.
    
    @see Vol3A[3.4.5.1(Code- and Data-Segment Descriptor Types)]
            """,
    
            8,
            4
    
        )
    
    
        S_FLAG = Ia32BitFieldMember(
            "S_FLAG",
            """
            @brief S (descriptor type) flag
    
    Specifies whether the segment descriptor is for a system segment (S flag is clear) or a code or data
    segment (S flag is set).
            """,
    
            12,
            1
    
        )
    
    
        DPL = Ia32BitFieldMember(
            "DPL",
            """
            @brief DPL (descriptor privilege level) field
    
    Specifies the privilege level of the segment. The privilege level can range from 0 to 3, with 0 being
    the most privileged level. The DPL is used to control access to the segment. See Section 5.5, Privilege
    Levels, for a description of the relationship of the DPL to the CPL of the executing code
    segment and the RPL of a segment selector.
            """,
    
            13,
            2
    
        )
    
    
        P = Ia32BitFieldMember(
            "P",
            """
            @brief P (segment-present) flag
    
    Indicates whether the segment is present in memory (set) or not present (clear). If this flag is clear,
    the processor generates a segment-not-present exception (\#NP) when a segment selector that
    points to the segment descriptor is loaded into a segment register. Memory management software
    can use this flag to control which segments are actually loaded into physical memory at a given
    time. It offers a control in addition to paging for managing virtual memory.
            """,
    
            15,
            1
    
        )
    
    
        LIMIT_HIGH = Ia32BitFieldMember(
            "LIMIT_HIGH",
            """
            @brief Segment limit field (19:16); see description of $LIMIT_LOW for more details
    
    Segment limit field (19:16); see description of $LIMIT_LOW for more details.
            """,
    
            16,
            4
    
        )
    
    
        AVAILABLE = Ia32BitFieldMember(
            "AVAILABLE",
            """
            @brief Available bit
    
    Bit 20 of the second doubleword of the segment descriptor is available for use by system software.
            """,
    
            20,
            1
    
        )
    
    
        L = Ia32BitFieldMember(
            "L",
            """
            @brief L (64-bit code segment) flag
    
    In IA-32e mode, bit 21 of the second doubleword of the segment descriptor indicates whether a
    code segment contains native 64-bit code. A value of 1 indicates instructions in this code segment
    are executed in 64-bit mode. A value of 0 indicates the instructions in this code segment are
    executed in compatibility mode. If L-bit is set, then D-bit must be cleared. When not in IA-32e mode
    or for non-code segments, bit 21 is reserved and should always be set to 0.
            """,
    
            21,
            1
    
        )
    
    
        DB = Ia32BitFieldMember(
            "DB",
            """
            @brief D/B (default operation size/default stack pointer size and/or upper bound) flag
    
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
    
    
        G = Ia32BitFieldMember(
            "G",
            """
            @brief G (granularity) flag
    
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
    
    
        BASE_HIGH = Ia32BitFieldMember(
            "BASE_HIGH",
            """
            @brief Base address field (31:24); see description of $BASE_LOW for more details
    
    Base address field (31:24); see description of $BASE_LOW for more details.
            """,
    
            24,
            8
    
        )
    
    
    
    class _MemberContainerBaseAddressUpper(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        @brief Base address field (32:63); see description of $BASE_LOW for more details
    
    Base address field (32:63); see description of $BASE_LOW for more details.
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(SegmentDescriptor64._MemberContainerBaseAddressUpper, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
        value = Ia32BitFieldMember('value', 'value', 0, 32)
    
    
    class _MemberContainerMustBeZero(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        @brief Base address field (32:63); see description of $BASE_LOW for more details
    
    Base address field (32:63); see description of $BASE_LOW for more details.
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(SegmentDescriptor64._MemberContainerMustBeZero, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
        value = Ia32BitFieldMember('value', 'value', 0, 32)
    
    
    _members = ["LIMIT_LOW","BASE_LOW","SEGMENT_","BASE_UPPER","MUST_BE_ZERO",]

    def __init__(self, value):
        self._LIMIT_LOW = self._MemberContainerSegmentLimitLow(0, 0, 2 )
        self._BASE_LOW = self._MemberContainerBaseAddressLow(0, 2, 2 )
        self._SEGMENT_ = self._MemberContainerSegment_(0, 4, 4 )
        self._BASE_UPPER = self._MemberContainerBaseAddressUpper(0, 8, 4 )
        self._MUST_BE_ZERO = self._MemberContainerMustBeZero(0, 12, 4 )
        super(SegmentDescriptor64, self).__init__(value)


    @property
    def LIMIT_LOW(self):
        return self._LIMIT_LOW

    @LIMIT_LOW.setter
    def LIMIT_LOW(self, value):
        return self._LIMIT_LOW.set(value)

    @property
    def BASE_LOW(self):
        return self._BASE_LOW

    @BASE_LOW.setter
    def BASE_LOW(self, value):
        return self._BASE_LOW.set(value)

    @property
    def SEGMENT_(self):
        return self._SEGMENT_

    @SEGMENT_.setter
    def SEGMENT_(self, value):
        return self._SEGMENT_.set(value)

    @property
    def BASE_UPPER(self):
        return self._BASE_UPPER

    @BASE_UPPER.setter
    def BASE_UPPER(self, value):
        return self._BASE_UPPER.set(value)

    @property
    def MUST_BE_ZERO(self):
        return self._MUST_BE_ZERO

    @MUST_BE_ZERO.setter
    def MUST_BE_ZERO(self, value):
        return self._MUST_BE_ZERO.set(value)


SEGMENT_DESCRIPTOR_TYPE_SYSTEM = 0x0


SEGMENT_DESCRIPTOR_TYPE_CODE_OR_DATA = 0x1


