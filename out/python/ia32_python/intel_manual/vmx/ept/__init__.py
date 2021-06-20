from future.utils import with_metaclass
from ia32_python.utils.ia32_struct import *
from ia32_python.utils.ia32_bit_field import *


__doc__ = """
@brief The extended page-table mechanism

The extended page-table mechanism (EPT) is a feature that can be used to support the virtualization of physical
memory. When EPT is in use, certain addresses that would normally be treated as physical addresses (and used to
access memory) are instead treated as guest-physical addresses. Guest-physical addresses are translated by
traversing a set of EPT paging structures to produce physical addresses that are used to access memory.
"""


class EptPointer(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
    """
    @brief Extended-Page-Table Pointer (EPTP)

The extended-page-table pointer (EPTP) contains the address of the base of EPT PML4 table,
as well as other EPT configuration information.

@see Vol3C[28.2.2(EPT Translation Mechanism]
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super(EptPointer, self).__init__(value, byte_offset, byte_width, max_bytes=8)



    TYPE = Ia32BitFieldMember(
        "TYPE",
        """
        @brief EPT paging-structure memory type:

- 0 = Uncacheable (UC)

- 6 = Write-back (WB)

Other values are reserved

EPT paging-structure memory type:

- 0 = Uncacheable (UC)

- 6 = Write-back (WB)

Other values are reserved.

@see Vol3C[28.2.6(EPT and memory Typing)]
        """,

        0,
        3

    )


    PAGE_WALK_LENGTH = Ia32BitFieldMember(
        "PAGE_WALK_LENGTH",
        """
        @brief This value is 1 less than the EPT page-walk length

This value is 1 less than the EPT page-walk length.

@see Vol3C[28.2.6(EPT and memory Typing)]
        """,

        3,
        3

    )


    ENABLE_ACCESS_AND_DIRTY_FLAGS = Ia32BitFieldMember(
        "ENABLE_ACCESS_AND_DIRTY_FLAGS",
        """
        @brief Setting this control to 1 enables accessed and dirty flags for EPT

Setting this control to 1 enables accessed and dirty flags for EPT.

@see Vol3C[28.2.4(Accessed and Dirty Flags for EPT)]
        """,

        6,
        1

    )


    PFN = Ia32BitFieldMember(
        "PFN",
        """
        @brief Bits N1:12 of the physical address of the 4-KByte aligned EPT PML4 table

Bits N1:12 of the physical address of the 4-KByte aligned EPT PML4 table.
        """,

        12,
        36

    )


class EptPml4(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
    """
    @brief Format of an EPT PML4 Entry (PML4E) that References an EPT Page-Directory-Pointer Table

A 4-KByte naturally aligned EPT PML4 table is located at the physical address specified in bits 51:12 of the
extended-page-table pointer (EPTP), a VM-execution control field. An EPT
PML4 table comprises 512 64-bit entries (EPT PML4Es). An EPT PML4E is selected using the physical address
defined as follows:

- Bits 63:52 are all 0.

- Bits 51:12 are from the EPTP.

- Bits 11:3 are bits 47:39 of the guest-physical address.

- Bits 2:0 are all 0.

Because an EPT PML4E is identified using bits 47:39 of the guest-physical address, it controls access to a 512-
GByte region of the guest-physical-address space.

@see Vol3C[24.6.11(Extended-Page-Table Pointer (EPTP)]
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super(EptPml4, self).__init__(value, byte_offset, byte_width, max_bytes=8)



    READ = Ia32BitFieldMember(
        "READ",
        """
        @brief Read access; indicates whether reads are allowed from the 512-GByte region controlled by this entry

Read access; indicates whether reads are allowed from the 512-GByte region controlled by this entry.
        """,

        0,
        1

    )


    WRITE = Ia32BitFieldMember(
        "WRITE",
        """
        @brief Write access; indicates whether writes are allowed from the 512-GByte region controlled by this entry

Write access; indicates whether writes are allowed from the 512-GByte region controlled by this entry.
        """,

        1,
        1

    )


    EXECUTE = Ia32BitFieldMember(
        "EXECUTE",
        """
        @brief If the mode-based execute control for EPT VM-execution control is 0, execute access; indicates whether instruction
fetches are allowed from the 512-GByte region controlled by this entry.

If that control is 1, execute access for supervisor-mode linear addresses; indicates whether instruction fetches are
allowed from supervisor-mode linear addresses in the 512-GByte region controlled by this entry

If the mode-based execute control for EPT VM-execution control is 0, execute access; indicates whether instruction
fetches are allowed from the 512-GByte region controlled by this entry.

If that control is 1, execute access for supervisor-mode linear addresses; indicates whether instruction fetches are
allowed from supervisor-mode linear addresses in the 512-GByte region controlled by this entry.
        """,

        2,
        1

    )


    ACCESSED = Ia32BitFieldMember(
        "ACCESSED",
        """
        @brief If bit 6 of EPTP is 1, accessed flag for EPT; indicates whether software has accessed the 512-GByte region
controlled by this entry. Ignored if bit 6 of EPTP is 0

If bit 6 of EPTP is 1, accessed flag for EPT; indicates whether software has accessed the 512-GByte region
controlled by this entry. Ignored if bit 6 of EPTP is 0.

@see Vol3C[28.2.4(Accessed and Dirty Flags for EPT)]
        """,

        8,
        1

    )


    USER_MODE_EXECUTE = Ia32BitFieldMember(
        "USER_MODE_EXECUTE",
        """
        @brief Execute access for user-mode linear addresses. If the mode-based execute control for EPT VM-execution control is
1, indicates whether instruction fetches are allowed from user-mode linear addresses in the 512-GByte region
controlled by this entry. If that control is 0, this bit is ignored

Execute access for user-mode linear addresses. If the mode-based execute control for EPT VM-execution control is
1, indicates whether instruction fetches are allowed from user-mode linear addresses in the 512-GByte region
controlled by this entry. If that control is 0, this bit is ignored.
        """,

        10,
        1

    )


    PFN = Ia32BitFieldMember(
        "PFN",
        """
        @brief Physical address of 4-KByte aligned EPT page-directory-pointer table referenced by this entry

Physical address of 4-KByte aligned EPT page-directory-pointer table referenced by this entry.
        """,

        12,
        36

    )


class Epdpte1gb(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
    """
    @brief Format of an EPT Page-Directory-Pointer-Table Entry (PDPTE) that Maps a 1-GByte Page

Format of an EPT Page-Directory-Pointer-Table Entry (PDPTE) that Maps a 1-GByte Page.
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super(Epdpte1gb, self).__init__(value, byte_offset, byte_width, max_bytes=8)



    READ = Ia32BitFieldMember(
        "READ",
        """
        @brief Read access; indicates whether reads are allowed from the 1-GByte page referenced by this entry

Read access; indicates whether reads are allowed from the 1-GByte page referenced by this entry.
        """,

        0,
        1

    )


    WRITE = Ia32BitFieldMember(
        "WRITE",
        """
        @brief Write access; indicates whether writes are allowed from the 1-GByte page referenced by this entry

Write access; indicates whether writes are allowed from the 1-GByte page referenced by this entry.
        """,

        1,
        1

    )


    EXECUTE = Ia32BitFieldMember(
        "EXECUTE",
        """
        @brief If the mode-based execute control for EPT VM-execution control is 0, execute access; indicates whether
instruction fetches are allowed from the 1-GByte page controlled by this entry.

If that control is 1, execute access for supervisor-mode linear addresses; indicates whether instruction fetches are
allowed from supervisor-mode linear addresses in the 1-GByte page controlled by this entry

If the mode-based execute control for EPT VM-execution control is 0, execute access; indicates whether
instruction fetches are allowed from the 1-GByte page controlled by this entry.

If that control is 1, execute access for supervisor-mode linear addresses; indicates whether instruction fetches are
allowed from supervisor-mode linear addresses in the 1-GByte page controlled by this entry.
        """,

        2,
        1

    )


    TYPE = Ia32BitFieldMember(
        "TYPE",
        """
        @brief EPT memory type for this 1-GByte page

EPT memory type for this 1-GByte page.

@see Vol3C[28.2.6(EPT and memory Typing)]
        """,

        3,
        3

    )


    IGNORE_PAT = Ia32BitFieldMember(
        "IGNORE_PAT",
        """
        @brief Ignore PAT memory type for this 1-GByte page

Ignore PAT memory type for this 1-GByte page.

@see Vol3C[28.2.6(EPT and memory Typing)]
        """,

        6,
        1

    )


    LARGE = Ia32BitFieldMember(
        "LARGE",
        """
        @brief Must be 1 (otherwise, this entry references an EPT page directory)

Must be 1 (otherwise, this entry references an EPT page directory).
        """,

        7,
        1

    )


    ACCESSED = Ia32BitFieldMember(
        "ACCESSED",
        """
        @brief If bit 6 of EPTP is 1, accessed flag for EPT; indicates whether software has accessed the 1-GByte page referenced
by this entry. Ignored if bit 6 of EPTP is 0

If bit 6 of EPTP is 1, accessed flag for EPT; indicates whether software has accessed the 1-GByte page referenced
by this entry. Ignored if bit 6 of EPTP is 0.

@see Vol3C[28.2.4(Accessed and Dirty Flags for EPT)]
        """,

        8,
        1

    )


    DIRTY = Ia32BitFieldMember(
        "DIRTY",
        """
        @brief If bit 6 of EPTP is 1, dirty flag for EPT; indicates whether software has written to the 1-GByte page referenced by
this entry. Ignored if bit 6 of EPTP is 0

If bit 6 of EPTP is 1, dirty flag for EPT; indicates whether software has written to the 1-GByte page referenced by
this entry. Ignored if bit 6 of EPTP is 0.

@see Vol3C[28.2.4(Accessed and Dirty Flags for EPT)]
        """,

        9,
        1

    )


    USER_MODE_EXECUTE = Ia32BitFieldMember(
        "USER_MODE_EXECUTE",
        """
        @brief Execute access for user-mode linear addresses. If the mode-based execute control for EPT VM-execution control is
1, indicates whether instruction fetches are allowed from user-mode linear addresses in the 1-GByte page controlled
by this entry. If that control is 0, this bit is ignored

Execute access for user-mode linear addresses. If the mode-based execute control for EPT VM-execution control is
1, indicates whether instruction fetches are allowed from user-mode linear addresses in the 1-GByte page controlled
by this entry. If that control is 0, this bit is ignored.
        """,

        10,
        1

    )


    PFN = Ia32BitFieldMember(
        "PFN",
        """
        @brief Physical address of 4-KByte aligned EPT page-directory-pointer table referenced by this entry

Physical address of 4-KByte aligned EPT page-directory-pointer table referenced by this entry.
        """,

        30,
        18

    )


    SUPPRESS_VE = Ia32BitFieldMember(
        "SUPPRESS_VE",
        """
        @brief Suppress \#VE. If the EPT-violation \#VE VM-execution control is 1, EPT violations caused by accesses to this page
are convertible to virtualization exceptions only if this bit is 0. If EPT-violation \#VE VMexecution
control is 0, this bit is ignored

Suppress \#VE. If the EPT-violation \#VE VM-execution control is 1, EPT violations caused by accesses to this page
are convertible to virtualization exceptions only if this bit is 0. If EPT-violation \#VE VMexecution
control is 0, this bit is ignored.

@see Vol3C[25.5.6.1(Convertible EPT Violations)]
        """,

        63,
        1

    )


class Epdpte(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
    """
    @brief Format of an EPT Page-Directory-Pointer-Table Entry (PDPTE) that References an EPT Page Directory

Format of an EPT Page-Directory-Pointer-Table Entry (PDPTE) that References an EPT Page Directory.
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super(Epdpte, self).__init__(value, byte_offset, byte_width, max_bytes=8)



    READ = Ia32BitFieldMember(
        "READ",
        """
        @brief Read access; indicates whether reads are allowed from the 1-GByte region controlled by this entry

Read access; indicates whether reads are allowed from the 1-GByte region controlled by this entry.
        """,

        0,
        1

    )


    WRITE = Ia32BitFieldMember(
        "WRITE",
        """
        @brief Write access; indicates whether writes are allowed from the 1-GByte region controlled by this entry

Write access; indicates whether writes are allowed from the 1-GByte region controlled by this entry.
        """,

        1,
        1

    )


    EXECUTE = Ia32BitFieldMember(
        "EXECUTE",
        """
        @brief If the mode-based execute control for EPT VM-execution control is 0, execute access; indicates whether instruction
fetches are allowed from the 1-GByte region controlled by this entry.

If that control is 1, execute access for supervisor-mode linear addresses; indicates whether instruction fetches are
allowed from supervisor-mode linear addresses in the 1-GByte region controlled by this entry

If the mode-based execute control for EPT VM-execution control is 0, execute access; indicates whether instruction
fetches are allowed from the 1-GByte region controlled by this entry.

If that control is 1, execute access for supervisor-mode linear addresses; indicates whether instruction fetches are
allowed from supervisor-mode linear addresses in the 1-GByte region controlled by this entry.
        """,

        2,
        1

    )


    ACCESSED = Ia32BitFieldMember(
        "ACCESSED",
        """
        @brief If bit 6 of EPTP is 1, accessed flag for EPT; indicates whether software has accessed the 1-GByte region controlled
by this entry. Ignored if bit 6 of EPTP is 0

If bit 6 of EPTP is 1, accessed flag for EPT; indicates whether software has accessed the 1-GByte region controlled
by this entry. Ignored if bit 6 of EPTP is 0.

@see Vol3C[28.2.4(Accessed and Dirty Flags for EPT)]
        """,

        8,
        1

    )


    USER_MODE_EXECUTE = Ia32BitFieldMember(
        "USER_MODE_EXECUTE",
        """
        @brief Execute access for user-mode linear addresses. If the mode-based execute control for EPT VM-execution control is
1, indicates whether instruction fetches are allowed from user-mode linear addresses in the 1-GByte region
controlled by this entry. If that control is 0, this bit is ignored

Execute access for user-mode linear addresses. If the mode-based execute control for EPT VM-execution control is
1, indicates whether instruction fetches are allowed from user-mode linear addresses in the 1-GByte region
controlled by this entry. If that control is 0, this bit is ignored.
        """,

        10,
        1

    )


    PFN = Ia32BitFieldMember(
        "PFN",
        """
        @brief Physical address of 4-KByte aligned EPT page-directory-pointer table referenced by this entry

Physical address of 4-KByte aligned EPT page-directory-pointer table referenced by this entry.
        """,

        12,
        36

    )


class Epde2mb(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
    """
    @brief Format of an EPT Page-Directory Entry (PDE) that Maps a 2-MByte Page

Format of an EPT Page-Directory Entry (PDE) that Maps a 2-MByte Page.
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super(Epde2mb, self).__init__(value, byte_offset, byte_width, max_bytes=8)



    READ = Ia32BitFieldMember(
        "READ",
        """
        @brief Read access; indicates whether reads are allowed from the 2-MByte page referenced by this entry

Read access; indicates whether reads are allowed from the 2-MByte page referenced by this entry.
        """,

        0,
        1

    )


    WRITE = Ia32BitFieldMember(
        "WRITE",
        """
        @brief Write access; indicates whether writes are allowed from the 2-MByte page referenced by this entry

Write access; indicates whether writes are allowed from the 2-MByte page referenced by this entry.
        """,

        1,
        1

    )


    EXECUTE = Ia32BitFieldMember(
        "EXECUTE",
        """
        @brief If the mode-based execute control for EPT VM-execution control is 0, execute access; indicates whether instruction
fetches are allowed from the 2-MByte page controlled by this entry.

If that control is 1, execute access for supervisor-mode linear addresses; indicates whether instruction fetches are
allowed from supervisor-mode linear addresses in the 2-MByte page controlled by this entry

If the mode-based execute control for EPT VM-execution control is 0, execute access; indicates whether instruction
fetches are allowed from the 2-MByte page controlled by this entry.

If that control is 1, execute access for supervisor-mode linear addresses; indicates whether instruction fetches are
allowed from supervisor-mode linear addresses in the 2-MByte page controlled by this entry.
        """,

        2,
        1

    )


    TYPE = Ia32BitFieldMember(
        "TYPE",
        """
        @brief EPT memory type for this 2-MByte page

EPT memory type for this 2-MByte page.

@see Vol3C[28.2.6(EPT and memory Typing)]
        """,

        3,
        3

    )


    IGNORE_PAT = Ia32BitFieldMember(
        "IGNORE_PAT",
        """
        @brief Ignore PAT memory type for this 2-MByte page

Ignore PAT memory type for this 2-MByte page.

@see Vol3C[28.2.6(EPT and memory Typing)]
        """,

        6,
        1

    )


    LARGE = Ia32BitFieldMember(
        "LARGE",
        """
        @brief Must be 1 (otherwise, this entry references an EPT page table)

Must be 1 (otherwise, this entry references an EPT page table).
        """,

        7,
        1

    )


    ACCESSED = Ia32BitFieldMember(
        "ACCESSED",
        """
        @brief If bit 6 of EPTP is 1, accessed flag for EPT; indicates whether software has accessed the 2-MByte page referenced
by this entry. Ignored if bit 6 of EPTP is 0

If bit 6 of EPTP is 1, accessed flag for EPT; indicates whether software has accessed the 2-MByte page referenced
by this entry. Ignored if bit 6 of EPTP is 0.

@see Vol3C[28.2.4(Accessed and Dirty Flags for EPT)]
        """,

        8,
        1

    )


    DIRTY = Ia32BitFieldMember(
        "DIRTY",
        """
        @brief If bit 6 of EPTP is 1, dirty flag for EPT; indicates whether software has written to the 2-MByte page referenced by
this entry. Ignored if bit 6 of EPTP is 0

If bit 6 of EPTP is 1, dirty flag for EPT; indicates whether software has written to the 2-MByte page referenced by
this entry. Ignored if bit 6 of EPTP is 0.

@see Vol3C[28.2.4(Accessed and Dirty Flags for EPT)]
        """,

        9,
        1

    )


    USER_MODE_EXECUTE = Ia32BitFieldMember(
        "USER_MODE_EXECUTE",
        """
        @brief Execute access for user-mode linear addresses. If the mode-based execute control for EPT VM-execution control is
1, indicates whether instruction fetches are allowed from user-mode linear addresses in the 2-MByte page controlled
by this entry. If that control is 0, this bit is ignored

Execute access for user-mode linear addresses. If the mode-based execute control for EPT VM-execution control is
1, indicates whether instruction fetches are allowed from user-mode linear addresses in the 2-MByte page controlled
by this entry. If that control is 0, this bit is ignored.
        """,

        10,
        1

    )


    PFN = Ia32BitFieldMember(
        "PFN",
        """
        @brief Physical address of 4-KByte aligned EPT page-directory-pointer table referenced by this entry

Physical address of 4-KByte aligned EPT page-directory-pointer table referenced by this entry.
        """,

        21,
        27

    )


    SUPPRESS_VE = Ia32BitFieldMember(
        "SUPPRESS_VE",
        """
        @brief Suppress \#VE. If the EPT-violation \#VE VM-execution control is 1, EPT violations caused by accesses to this page
are convertible to virtualization exceptions only if this bit is 0. If EPT-violation \#VE VMexecution
control is 0, this bit is ignored

Suppress \#VE. If the EPT-violation \#VE VM-execution control is 1, EPT violations caused by accesses to this page
are convertible to virtualization exceptions only if this bit is 0. If EPT-violation \#VE VMexecution
control is 0, this bit is ignored.

@see Vol3C[25.5.6.1(Convertible EPT Violations)]
        """,

        63,
        1

    )


class Epde(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
    """
    @brief Format of an EPT Page-Directory Entry (PDE) that References an EPT Page Table

Format of an EPT Page-Directory Entry (PDE) that References an EPT Page Table.
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super(Epde, self).__init__(value, byte_offset, byte_width, max_bytes=8)



    READ = Ia32BitFieldMember(
        "READ",
        """
        @brief Read access; indicates whether reads are allowed from the 2-MByte region controlled by this entry

Read access; indicates whether reads are allowed from the 2-MByte region controlled by this entry.
        """,

        0,
        1

    )


    WRITE = Ia32BitFieldMember(
        "WRITE",
        """
        @brief Write access; indicates whether writes are allowed from the 2-MByte region controlled by this entry

Write access; indicates whether writes are allowed from the 2-MByte region controlled by this entry.
        """,

        1,
        1

    )


    EXECUTE = Ia32BitFieldMember(
        "EXECUTE",
        """
        @brief If the mode-based execute control for EPT VM-execution control is 0, execute access; indicates whether instruction
fetches are allowed from the 2-MByte region controlled by this entry.

If that control is 1, execute access for supervisor-mode linear addresses; indicates whether instruction fetches are
allowed from supervisor-mode linear addresses in the 2-MByte region controlled by this entry

If the mode-based execute control for EPT VM-execution control is 0, execute access; indicates whether instruction
fetches are allowed from the 2-MByte region controlled by this entry.

If that control is 1, execute access for supervisor-mode linear addresses; indicates whether instruction fetches are
allowed from supervisor-mode linear addresses in the 2-MByte region controlled by this entry.
        """,

        2,
        1

    )


    ACCESSED = Ia32BitFieldMember(
        "ACCESSED",
        """
        @brief If bit 6 of EPTP is 1, accessed flag for EPT; indicates whether software has accessed the 2-MByte region controlled
by this entry. Ignored if bit 6 of EPTP is 0

If bit 6 of EPTP is 1, accessed flag for EPT; indicates whether software has accessed the 2-MByte region controlled
by this entry. Ignored if bit 6 of EPTP is 0.

@see Vol3C[28.2.4(Accessed and Dirty Flags for EPT)]
        """,

        8,
        1

    )


    USER_MODE_EXECUTE = Ia32BitFieldMember(
        "USER_MODE_EXECUTE",
        """
        @brief Execute access for user-mode linear addresses. If the mode-based execute control for EPT VM-execution control is
1, indicates whether instruction fetches are allowed from user-mode linear addresses in the 2-MByte region
controlled by this entry. If that control is 0, this bit is ignored

Execute access for user-mode linear addresses. If the mode-based execute control for EPT VM-execution control is
1, indicates whether instruction fetches are allowed from user-mode linear addresses in the 2-MByte region
controlled by this entry. If that control is 0, this bit is ignored.
        """,

        10,
        1

    )


    PFN = Ia32BitFieldMember(
        "PFN",
        """
        @brief Physical address of 4-KByte aligned EPT page table referenced by this entry

Physical address of 4-KByte aligned EPT page table referenced by this entry.
        """,

        12,
        36

    )


class Epte(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
    """
    @brief Format of an EPT Page-Table Entry that Maps a 4-KByte Page

Format of an EPT Page-Table Entry that Maps a 4-KByte Page.
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super(Epte, self).__init__(value, byte_offset, byte_width, max_bytes=8)



    READ = Ia32BitFieldMember(
        "READ",
        """
        @brief Read access; indicates whether reads are allowed from the 4-KByte page referenced by this entry

Read access; indicates whether reads are allowed from the 4-KByte page referenced by this entry.
        """,

        0,
        1

    )


    WRITE = Ia32BitFieldMember(
        "WRITE",
        """
        @brief Write access; indicates whether writes are allowed from the 4-KByte page referenced by this entry

Write access; indicates whether writes are allowed from the 4-KByte page referenced by this entry.
        """,

        1,
        1

    )


    EXECUTE = Ia32BitFieldMember(
        "EXECUTE",
        """
        @brief If the mode-based execute control for EPT VM-execution control is 0, execute access; indicates whether
instruction fetches are allowed from the 4-KByte page controlled by this entry.

If that control is 1, execute access for supervisor-mode linear addresses; indicates whether instruction fetches are
allowed from supervisor-mode linear addresses in the 4-KByte page controlled by this entry

If the mode-based execute control for EPT VM-execution control is 0, execute access; indicates whether
instruction fetches are allowed from the 4-KByte page controlled by this entry.

If that control is 1, execute access for supervisor-mode linear addresses; indicates whether instruction fetches are
allowed from supervisor-mode linear addresses in the 4-KByte page controlled by this entry.
        """,

        2,
        1

    )


    TYPE = Ia32BitFieldMember(
        "TYPE",
        """
        @brief EPT memory type for this 4-KByte page

EPT memory type for this 4-KByte page.

@see Vol3C[28.2.6(EPT and memory Typing)]
        """,

        3,
        3

    )


    IGNORE_PAT = Ia32BitFieldMember(
        "IGNORE_PAT",
        """
        @brief Ignore PAT memory type for this 4-KByte page

Ignore PAT memory type for this 4-KByte page.

@see Vol3C[28.2.6(EPT and memory Typing)]
        """,

        6,
        1

    )


    ACCESSED = Ia32BitFieldMember(
        "ACCESSED",
        """
        @brief If bit 6 of EPTP is 1, accessed flag for EPT; indicates whether software has accessed the 4-KByte page referenced
by this entry. Ignored if bit 6 of EPTP is 0

If bit 6 of EPTP is 1, accessed flag for EPT; indicates whether software has accessed the 4-KByte page referenced
by this entry. Ignored if bit 6 of EPTP is 0.

@see Vol3C[28.2.4(Accessed and Dirty Flags for EPT)]
        """,

        8,
        1

    )


    DIRTY = Ia32BitFieldMember(
        "DIRTY",
        """
        @brief If bit 6 of EPTP is 1, dirty flag for EPT; indicates whether software has written to the 4-KByte page referenced by
this entry. Ignored if bit 6 of EPTP is 0

If bit 6 of EPTP is 1, dirty flag for EPT; indicates whether software has written to the 4-KByte page referenced by
this entry. Ignored if bit 6 of EPTP is 0.

@see Vol3C[28.2.4(Accessed and Dirty Flags for EPT)]
        """,

        9,
        1

    )


    USER_MODE_EXECUTE = Ia32BitFieldMember(
        "USER_MODE_EXECUTE",
        """
        @brief Execute access for user-mode linear addresses. If the mode-based execute control for EPT VM-execution control is
1, indicates whether instruction fetches are allowed from user-mode linear addresses in the 4-KByte page controlled
by this entry. If that control is 0, this bit is ignored

Execute access for user-mode linear addresses. If the mode-based execute control for EPT VM-execution control is
1, indicates whether instruction fetches are allowed from user-mode linear addresses in the 4-KByte page controlled
by this entry. If that control is 0, this bit is ignored.
        """,

        10,
        1

    )


    PFN = Ia32BitFieldMember(
        "PFN",
        """
        @brief Physical address of the 4-KByte page referenced by this entry

Physical address of the 4-KByte page referenced by this entry.
        """,

        12,
        36

    )


    SUPPRESS_VE = Ia32BitFieldMember(
        "SUPPRESS_VE",
        """
        @brief Suppress \#VE. If the EPT-violation \#VE VM-execution control is 1, EPT violations caused by accesses to this page
are convertible to virtualization exceptions only if this bit is 0. If EPT-violation \#VE VMexecution
control is 0, this bit is ignored

Suppress \#VE. If the EPT-violation \#VE VM-execution control is 1, EPT violations caused by accesses to this page
are convertible to virtualization exceptions only if this bit is 0. If EPT-violation \#VE VMexecution
control is 0, this bit is ignored.

@see Vol3C[25.5.6.1(Convertible EPT Violations)]
        """,

        63,
        1

    )


class EptEntry(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
    """
    @brief Format of a common EPT Entry

Format of a common EPT Entry.
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super(EptEntry, self).__init__(value, byte_offset, byte_width, max_bytes=8)



    READ = Ia32BitFieldMember(
        "READ",
        """
        
        """,

        0,
        1

    )


    WRITE = Ia32BitFieldMember(
        "WRITE",
        """
        
        """,

        1,
        1

    )


    EXECUTE = Ia32BitFieldMember(
        "EXECUTE",
        """
        
        """,

        2,
        1

    )


    TYPE = Ia32BitFieldMember(
        "TYPE",
        """
        
        """,

        3,
        3

    )


    IGNORE_PAT = Ia32BitFieldMember(
        "IGNORE_PAT",
        """
        
        """,

        6,
        1

    )


    LARGE = Ia32BitFieldMember(
        "LARGE",
        """
        
        """,

        7,
        1

    )


    ACCESSED = Ia32BitFieldMember(
        "ACCESSED",
        """
        
        """,

        8,
        1

    )


    DIRTY = Ia32BitFieldMember(
        "DIRTY",
        """
        
        """,

        9,
        1

    )


    USER_MODE_EXECUTE = Ia32BitFieldMember(
        "USER_MODE_EXECUTE",
        """
        
        """,

        10,
        1

    )


    PFN = Ia32BitFieldMember(
        "PFN",
        """
        
        """,

        12,
        36

    )


    SUPPRESS_VE = Ia32BitFieldMember(
        "SUPPRESS_VE",
        """
        
        """,

        63,
        1

    )


