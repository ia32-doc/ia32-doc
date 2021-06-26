from future.utils import with_metaclass
from ia32_python.utils.ia32_struct import *
from ia32_python.utils.ia32_enum import *
from ia32_python.utils.ia32_bit_field import *


__doc__ = """
@brief EPT Entry counts

EPT Entry counts.
"""


EPML4_ENTRY_COUNT = 0x200


EPDPTE_ENTRY_COUNT = 0x200


EPDE_ENTRY_COUNT = 0x200


EPTE_ENTRY_COUNT = 0x200


class InveptType(with_metaclass(Ia32EnumMeta, Ia32Enum)):
    """
    
    """


    INVEPT_SINGLE_CONTEXT = Ia32EnumField(
        "INVEPT_SINGLE_CONTEXT",
        0x1,
        """@brief If the INVEPT type is 1, the logical processor invalidates all guest-physical mappings and
combined mappings associated with the EP4TA specified in the INVEPT descriptor. Combined mappings for
that EP4TA are invalidated for all VPIDs and all PCIDs. (The instruction may invalidate mappings associated
with other EP4TAs.)

If the INVEPT type is 1, the logical processor invalidates all guest-physical mappings and
combined mappings associated with the EP4TA specified in the INVEPT descriptor. Combined mappings for
that EP4TA are invalidated for all VPIDs and all PCIDs. (The instruction may invalidate mappings associated
with other EP4TAs.)""",
   )

    INVEPT_ALL_CONTEXT = Ia32EnumField(
        "INVEPT_ALL_CONTEXT",
        0x2,
        """@brief If the INVEPT type is 2, the logical processor invalidates guest-physical mappings and
combined mappings associated with all EP4TAs (and, for combined mappings, for all VPIDs and PCIDs)

If the INVEPT type is 2, the logical processor invalidates guest-physical mappings and
combined mappings associated with all EP4TAs (and, for combined mappings, for all VPIDs and PCIDs).""",
   )

class InvvpidType(with_metaclass(Ia32EnumMeta, Ia32Enum)):
    """
    
    """


    INVVPID_INDIVIDUAL_ADDRESS = Ia32EnumField(
        "INVVPID_INDIVIDUAL_ADDRESS",
        0x0,
        """@brief If the INVVPID type is 0, the logical processor invalidates linear mappings and
combined mappings associated with the VPID specified in the INVVPID descriptor and that would be used
to translate the linear address specified in of the INVVPID descriptor. Linear mappings and combined
mappings for that VPID and linear address are invalidated for all PCIDs and, for combined mappings, all
EP4TAs. (The instruction may also invalidate mappings associated with other VPIDs and for other linear
addresses)

If the INVVPID type is 0, the logical processor invalidates linear mappings and
combined mappings associated with the VPID specified in the INVVPID descriptor and that would be used
to translate the linear address specified in of the INVVPID descriptor. Linear mappings and combined
mappings for that VPID and linear address are invalidated for all PCIDs and, for combined mappings, all
EP4TAs. (The instruction may also invalidate mappings associated with other VPIDs and for other linear
addresses).""",
   )

    INVVPID_SINGLE_CONTEXT = Ia32EnumField(
        "INVVPID_SINGLE_CONTEXT",
        0x1,
        """@brief If the INVVPID type is 1, the logical processor invalidates all linear mappings and
combined mappings associated with the VPID specified in the INVVPID descriptor. Linear mappings and
combined mappings for that VPID are invalidated for all PCIDs and, for combined mappings, all EP4TAs.
(The instruction may also invalidate mappings associated with other VPIDs)

If the INVVPID type is 1, the logical processor invalidates all linear mappings and
combined mappings associated with the VPID specified in the INVVPID descriptor. Linear mappings and
combined mappings for that VPID are invalidated for all PCIDs and, for combined mappings, all EP4TAs.
(The instruction may also invalidate mappings associated with other VPIDs).""",
   )

    INVVPID_ALL_CONTEXT = Ia32EnumField(
        "INVVPID_ALL_CONTEXT",
        0x2,
        """@brief If the INVVPID type is 2, the logical processor invalidates linear mappings and combined
mappings associated with all VPIDs except VPID 0000H and with all PCIDs. (The instruction may also
invalidate linear mappings with VPID 0000H.) Combined mappings are invalidated for all EP4TAs

If the INVVPID type is 2, the logical processor invalidates linear mappings and combined
mappings associated with all VPIDs except VPID 0000H and with all PCIDs. (The instruction may also
invalidate linear mappings with VPID 0000H.) Combined mappings are invalidated for all EP4TAs.""",
   )

    INVVPID_SINGLE_CONTEXT_RETAINING_GLOBALS = Ia32EnumField(
        "INVVPID_SINGLE_CONTEXT_RETAINING_GLOBALS",
        0x3,
        """@brief If the INVVPID type is 3, the logical processor invalidates linear
mappings and combined mappings associated with the VPID specified in the INVVPID descriptor. Linear
mappings and combined mappings for that VPID are invalidated for all PCIDs and, for combined mappings,
all EP4TAs. The logical processor is not required to invalidate information that was used for global translations
(although it may do so). (The instruction may also invalidate mappings associated with other VPIDs)

If the INVVPID type is 3, the logical processor invalidates linear
mappings and combined mappings associated with the VPID specified in the INVVPID descriptor. Linear
mappings and combined mappings for that VPID are invalidated for all PCIDs and, for combined mappings,
all EP4TAs. The logical processor is not required to invalidate information that was used for global translations
(although it may do so). (The instruction may also invalidate mappings associated with other VPIDs).

@see Vol3C[4.10(Caching Translation Information)]""",
   )

class InveptDescriptor(Ia32Struct):
    """"""
    class _MemberContainerEptPointer(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(InveptDescriptor._MemberContainerEptPointer, self).__init__(value, byte_offset, byte_width, max_bytes=8)
    
    
        value = Ia32BitFieldMember('value', 'value', 0, 64)
    
    
    class _MemberContainerReserved(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        @brief Must be zero
    
    Must be zero.
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(InveptDescriptor._MemberContainerReserved, self).__init__(value, byte_offset, byte_width, max_bytes=8)
    
    
        value = Ia32BitFieldMember('value', 'value', 0, 64)
    
    
    _members = ["EPTP","RESERVED",]

    def __init__(self, value):
        self._EPTP = self._MemberContainerEptPointer(0, 0, 8 )
        self._RESERVED = self._MemberContainerReserved(0, 8, 8 )
        super(InveptDescriptor, self).__init__(value)


    @property
    def EPTP(self):
        return self._EPTP

    @EPTP.setter
    def EPTP(self, value):
        return self._EPTP.set(value)

    @property
    def RESERVED(self):
        return self._RESERVED

    @RESERVED.setter
    def RESERVED(self, value):
        return self._RESERVED.set(value)


class InvvpidDescriptor(Ia32Struct):
    """"""
    class _MemberContainerVpid(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(InvvpidDescriptor._MemberContainerVpid, self).__init__(value, byte_offset, byte_width, max_bytes=2)
    
    
        value = Ia32BitFieldMember('value', 'value', 0, 16)
    
    
    class _MemberContainerReserved1(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        @brief Must be zero
    
    Must be zero.
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(InvvpidDescriptor._MemberContainerReserved1, self).__init__(value, byte_offset, byte_width, max_bytes=2)
    
    
        value = Ia32BitFieldMember('value', 'value', 0, 16)
    
    
    class _MemberContainerReserved2(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        @brief Must be zero
    
    Must be zero.
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(InvvpidDescriptor._MemberContainerReserved2, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
        value = Ia32BitFieldMember('value', 'value', 0, 32)
    
    
    class _MemberContainerLinearAddress(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(InvvpidDescriptor._MemberContainerLinearAddress, self).__init__(value, byte_offset, byte_width, max_bytes=8)
    
    
        value = Ia32BitFieldMember('value', 'value', 0, 64)
    
    
    _members = ["VPID","RESERVED1","RESERVED2","LINEAR_ADDRESS",]

    def __init__(self, value):
        self._VPID = self._MemberContainerVpid(0, 0, 2 )
        self._RESERVED1 = self._MemberContainerReserved1(0, 2, 2 )
        self._RESERVED2 = self._MemberContainerReserved2(0, 4, 4 )
        self._LINEAR_ADDRESS = self._MemberContainerLinearAddress(0, 8, 8 )
        super(InvvpidDescriptor, self).__init__(value)


    @property
    def VPID(self):
        return self._VPID

    @VPID.setter
    def VPID(self, value):
        return self._VPID.set(value)

    @property
    def RESERVED1(self):
        return self._RESERVED1

    @RESERVED1.setter
    def RESERVED1(self, value):
        return self._RESERVED1.set(value)

    @property
    def RESERVED2(self):
        return self._RESERVED2

    @RESERVED2.setter
    def RESERVED2(self, value):
        return self._RESERVED2.set(value)

    @property
    def LINEAR_ADDRESS(self):
        return self._LINEAR_ADDRESS

    @LINEAR_ADDRESS.setter
    def LINEAR_ADDRESS(self, value):
        return self._LINEAR_ADDRESS.set(value)


class Vmcs(Ia32Struct):
    """@brief Format of the VMCS Region

A logical processor uses virtual-machine control data structures (VMCSs) while it is in VMX operation. These
manage transitions into and out of VMX non-root operation (VM entries and VM exits) as well as processor behavior
in VMX non-root operation. This structure is manipulated by the new instructions VMCLEAR, VMPTRLD, VMREAD,
and VMWRITE.

A VMCS region comprises up to 4-KBytes. The exact size is implementation specific and can be determined
by consulting the VMX capability MSR IA32_VMX_BASIC."""
    class _MemberContainerEmpty(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(Vmcs._MemberContainerEmpty, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        REVISION_ID = Ia32BitFieldMember(
            "REVISION_ID",
            """
            @brief VMCS revision identifier
    
    Processors that maintain VMCS data in different formats (see below) use different VMCS revision identifiers.
    These identifiers enable software to avoid using a VMCS region formatted for one processor on a processor
    that uses a different format.
    
    Software should write the VMCS revision identifier to the VMCS region before using that region for a VMCS. The
    VMCS revision identifier is never written by the processor; VMPTRLD fails if its operand references a VMCS region
    whose VMCS revision identifier differs from that used by the processor.
    
    Software can discover the VMCS revision identifier that a processor uses by reading the VMX capability
    MSR IA32_VMX_BASIC.
    
    @see Vol3C[24.6.2(Processor-Based VM-Execution Controls)]
    
    @see Vol3D[A.1(BASIC VMX INFORMATION)]
            """,
    
            0,
            31
    
        )
    
    
        SHADOW_VMCS_INDICATOR = Ia32BitFieldMember(
            "SHADOW_VMCS_INDICATOR",
            """
            @brief Shadow-VMCS indicator
    
    Software should clear or set the shadow-VMCS indicator depending on whether the VMCS is to be an ordinary
    VMCS or a shadow VMCS. VMPTRLD fails if the shadow-VMCS indicator is set and the processor does not support
    the 1-setting of the "VMCS shadowing" VM-execution control. Software can discover support for this setting
    by reading the VMX capability MSR IA32_VMX_PROCBASED_CTLS2.
    
    @see Vol3C[24.10(VMCS TYPES ORDINARY AND SHADOW)]
            """,
    
            31,
            1
    
        )
    
    
    
    class _MemberContainerAbortIndicator(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        @brief VMX-abort indicator
    
    The contents of these bits do not
    control processor operation in any way. A logical processor writes a non-zero value into these bits if a VMX abort
    occurs. Software may also write into this field.
    
    @see Vol3D[27.7(VMX Aborts)]
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(Vmcs._MemberContainerAbortIndicator, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
        value = Ia32BitFieldMember('value', 'value', 0, 32)
    
    
    class _MemberContainerData(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        @brief VMCS data (implementation-specific format)
    
    These parts of the VMCS control VMX non-root operation and the VMX transitions.
    
    The format of these data is implementation-specific. To ensure proper behavior in VMX operation,
    software should maintain the VMCS region and related structures in writeback cacheable memory. Future
    implementations may allow or require a different memory type. Software should consult the VMX capability MSR
    IA32_VMX_BASIC.
    
    @see Vol3C[24.11.4(Software Access to Related Structures)]
    
    @see Vol3D[A.1(BASIC VMX INFORMATION)]
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(Vmcs._MemberContainerData, self).__init__(value, byte_offset, byte_width, max_bytes=4088)
    
    
        value = Ia32BitFieldMember('value', 'value', 0, 32704)
    
    
    _members = ["EMPTY","ABORT_INDICATOR","DATA",]

    def __init__(self, value):
        self._EMPTY = self._MemberContainerEmpty(0, 0, 4 )
        self._ABORT_INDICATOR = self._MemberContainerAbortIndicator(0, 4, 4 )
        self._DATA = self._MemberContainerData(0, 8, 4088 )
        super(Vmcs, self).__init__(value)


    @property
    def EMPTY(self):
        return self._EMPTY

    @EMPTY.setter
    def EMPTY(self, value):
        return self._EMPTY.set(value)

    @property
    def ABORT_INDICATOR(self):
        return self._ABORT_INDICATOR

    @ABORT_INDICATOR.setter
    def ABORT_INDICATOR(self, value):
        return self._ABORT_INDICATOR.set(value)

    @property
    def DATA(self):
        return self._DATA

    @DATA.setter
    def DATA(self, value):
        return self._DATA.set(value)


class Vmxon(Ia32Struct):
    """@brief Format of the VMXON Region

Before executing VMXON, software allocates a region of memory that the logical processor uses to support
VMX operation. This region is called the VMXON region.

A VMXON region comprises up to 4-KBytes. The exact size is implementation specific and can be determined
by consulting the VMX capability MSR IA32_VMX_BASIC."""
    class _MemberContainerEmpty(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(Vmxon._MemberContainerEmpty, self).__init__(value, byte_offset, byte_width, max_bytes=4)
    
    
    
        REVISION_ID = Ia32BitFieldMember(
            "REVISION_ID",
            """
            @brief VMCS revision identifier
    
    Before executing VMXON, software should write the VMCS revision identifier to the VMXON region.
    (Specifically, it should write the 31-bit VMCS revision identifier to bits 30:0 of the first 4 bytes of
    the VMXON region; bit 31 should be cleared to 0.)
    
    @see VMCS
    
    @see Vol3C[24.2(FORMAT OF THE VMCS REGION)]
    
    @see Vol3C[24.11.5(VMXON Region)]
            """,
    
            0,
            31
    
        )
    
    
        MUST_BE_ZERO = Ia32BitFieldMember(
            "MUST_BE_ZERO",
            """
            @brief Bit 31 is always 0
    
    Bit 31 is always 0.
            """,
    
            31,
            1
    
        )
    
    
    
    class _MemberContainerData(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
        """
        @brief VMXON data (implementation-specific format)
    
    The format of these data is implementation-specific. To ensure proper behavior in VMX operation,
    software should not access or modify the VMXON region of a logical processor between execution of VMXON and
    VMXOFF on that logical processor. Doing otherwise may lead to unpredictable behavior.
    
    @see Vol3C[24.11.4(Software Access to Related Structures)]
    
    @see Vol3D[A.1(BASIC VMX INFORMATION)]
        """
        def __init__(self, value=0, byte_offset=None, byte_width=None):
            super(Vmxon._MemberContainerData, self).__init__(value, byte_offset, byte_width, max_bytes=4092)
    
    
        value = Ia32BitFieldMember('value', 'value', 0, 32736)
    
    
    _members = ["EMPTY","DATA",]

    def __init__(self, value):
        self._EMPTY = self._MemberContainerEmpty(0, 0, 4 )
        self._DATA = self._MemberContainerData(0, 4, 4092 )
        super(Vmxon, self).__init__(value)


    @property
    def EMPTY(self):
        return self._EMPTY

    @EMPTY.setter
    def EMPTY(self, value):
        return self._EMPTY.set(value)

    @property
    def DATA(self):
        return self._DATA

    @DATA.setter
    def DATA(self, value):
        return self._DATA.set(value)


