from future.utils import with_metaclass
from utils.struct import *
from utils.bit_field import *


__doc__ = """
@brief 64-Bit (4-Level) Paging

A logical processor uses 4-level paging if CR0.PG = 1, CR4.PAE = 1, and IA32_EFER.LME = 1. With 4-level paging,
linear address are translated using a hierarchy of in-memory paging structures located using the contents of CR3.
4-level paging translates 48-bit linear addresses to 52-bit physical addresses. Although 52 bits corresponds to 4
PBytes, linear addresses are limited to 48 bits; at most 256 TBytes of linear-address space may be accessed at any
given time.

4-level paging uses a hierarchy of paging structures to produce a translation for a linear address. CR3 is used to
locate the first paging-structure, the PML4 table. Use of CR3 with 4-level paging depends on whether processcontext
identifiers (PCIDs) have been enabled by setting CR4.PCIDE.
"""


class Pml4e64(with_metaclass(BitFieldMeta, BitField)):
    """
    @brief Format of a 4-Level PML4 Entry (PML4E) that References a Page-Directory-Pointer Table

Format of a 4-Level PML4 Entry (PML4E) that References a Page-Directory-Pointer Table.
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super().__init__(value, byte_offset, byte_width, max_bytes=8)



    P = BitFieldMember(
        "P",
        """
        @brief Present; must be 1 to reference a page-directory-pointer table

Present; must be 1 to reference a page-directory-pointer table.
        """,

        0,
        1

    )


    RW = BitFieldMember(
        "RW",
        """
        @brief Read/write; if 0, writes may not be allowed to the 512-GByte region controlled by this entry

Read/write; if 0, writes may not be allowed to the 512-GByte region controlled by this entry.

@see Vol3A[4.6(Access Rights)]
        """,

        1,
        1

    )


    US = BitFieldMember(
        "US",
        """
        @brief User/supervisor; if 0, user-mode accesses are not allowed to the 512-GByte region controlled by this entry

User/supervisor; if 0, user-mode accesses are not allowed to the 512-GByte region controlled by this entry.

@see Vol3A[4.6(Access Rights)]
        """,

        2,
        1

    )


    PWT = BitFieldMember(
        "PWT",
        """
        @brief Page-level write-through; indirectly determines the memory type used to access the page-directory-pointer table
referenced by this entry

Page-level write-through; indirectly determines the memory type used to access the page-directory-pointer table
referenced by this entry.

@see Vol3A[4.9.2(Paging and Memory Typing When the PAT is Supported (Pentium III and More Recent Processor Families))]
        """,

        3,
        1

    )


    PCD = BitFieldMember(
        "PCD",
        """
        @brief Page-level cache disable; indirectly determines the memory type used to access the page-directory-pointer table
referenced by this entry

Page-level cache disable; indirectly determines the memory type used to access the page-directory-pointer table
referenced by this entry.

@see Vol3A[4.9.2(Paging and Memory Typing When the PAT is Supported (Pentium III and More Recent Processor Families))]
        """,

        4,
        1

    )


    A = BitFieldMember(
        "A",
        """
        @brief Accessed; indicates whether this entry has been used for linear-address translation

Accessed; indicates whether this entry has been used for linear-address translation.

@see Vol3A[4.8(Accessed and Dirty Flags)]
        """,

        5,
        1

    )


    RESERVED = BitFieldMember(
        "RESERVED",
        """
        @brief Reserved (must be 0)

Reserved (must be 0).
        """,

        7,
        1

    )


    IGNORED_1 = BitFieldMember(
        "IGNORED_1",
        """
        @brief Ignored

Ignored.
        """,

        8,
        4

    )


    PFN = BitFieldMember(
        "PFN",
        """
        @brief Physical address of 4-KByte aligned page-directory-pointer table referenced by this entry

Physical address of 4-KByte aligned page-directory-pointer table referenced by this entry.
        """,

        12,
        36

    )


    IGNORED_2 = BitFieldMember(
        "IGNORED_2",
        """
        @brief Ignored

Ignored.
        """,

        52,
        11

    )


    XD = BitFieldMember(
        "XD",
        """
        @brief If IA32_EFER.NXE = 1, execute-disable (if 1, instruction fetches are not allowed from the 512-GByte region
controlled by this entry); otherwise, reserved (must be 0)

If IA32_EFER.NXE = 1, execute-disable (if 1, instruction fetches are not allowed from the 512-GByte region
controlled by this entry); otherwise, reserved (must be 0).

@see Vol3A[4.6(Access Rights)]
        """,

        63,
        1

    )


class Pdpte1gb64(with_metaclass(BitFieldMeta, BitField)):
    """
    @brief Format of a 4-Level Page-Directory-Pointer-Table Entry (PDPTE) that Maps a 1-GByte Page

Format of a 4-Level Page-Directory-Pointer-Table Entry (PDPTE) that Maps a 1-GByte Page.
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super().__init__(value, byte_offset, byte_width, max_bytes=8)



    P = BitFieldMember(
        "P",
        """
        @brief Present; must be 1 to map a 1-GByte page

Present; must be 1 to map a 1-GByte page.
        """,

        0,
        1

    )


    RW = BitFieldMember(
        "RW",
        """
        @brief Read/write; if 0, writes may not be allowed to the 1-GByte page referenced by this entry

Read/write; if 0, writes may not be allowed to the 1-GByte page referenced by this entry.

@see Vol3A[4.6(Access Rights)]
        """,

        1,
        1

    )


    US = BitFieldMember(
        "US",
        """
        @brief User/supervisor; if 0, user-mode accesses are not allowed to the 1-GByte page referenced by this entry

User/supervisor; if 0, user-mode accesses are not allowed to the 1-GByte page referenced by this entry.

@see Vol3A[4.6(Access Rights)]
        """,

        2,
        1

    )


    PWT = BitFieldMember(
        "PWT",
        """
        @brief Page-level write-through; indirectly determines the memory type used to access the 1-GByte page referenced by this
entry

Page-level write-through; indirectly determines the memory type used to access the 1-GByte page referenced by this
entry.

@see Vol3A[4.9.2(Paging and Memory Typing When the PAT is Supported (Pentium III and More Recent Processor Families))]
        """,

        3,
        1

    )


    PCD = BitFieldMember(
        "PCD",
        """
        @brief Page-level cache disable; indirectly determines the memory type used to access the 1-GByte page referenced by this
entry

Page-level cache disable; indirectly determines the memory type used to access the 1-GByte page referenced by this
entry.

@see Vol3A[4.9.2(Paging and Memory Typing When the PAT is Supported (Pentium III and More Recent Processor Families))]
        """,

        4,
        1

    )


    A = BitFieldMember(
        "A",
        """
        @brief Accessed; indicates whether software has accessed the 1-GByte page referenced by this entry

Accessed; indicates whether software has accessed the 1-GByte page referenced by this entry.

@see Vol3A[4.8(Accessed and Dirty Flags)]
        """,

        5,
        1

    )


    D = BitFieldMember(
        "D",
        """
        @brief Dirty; indicates whether software has written to the 1-GByte page referenced by this entry

Dirty; indicates whether software has written to the 1-GByte page referenced by this entry.

@see Vol3A[4.8(Accessed and Dirty Flags)]
        """,

        6,
        1

    )


    LARGE = BitFieldMember(
        "LARGE",
        """
        @brief Page size; must be 1 (otherwise, this entry references a page directory)

Page size; must be 1 (otherwise, this entry references a page directory).
        """,

        7,
        1

    )


    G = BitFieldMember(
        "G",
        """
        @brief Global; if CR4.PGE = 1, determines whether the translation is global; ignored otherwise

Global; if CR4.PGE = 1, determines whether the translation is global; ignored otherwise.

@see Vol3A[4.10(Caching Translation Information)]
        """,

        8,
        1

    )


    IGNORED_1 = BitFieldMember(
        "IGNORED_1",
        """
        @brief Ignored

Ignored.
        """,

        9,
        3

    )


    PAT = BitFieldMember(
        "PAT",
        """
        @brief Indirectly determines the memory type used to access the 1-GByte page referenced by this entry

Indirectly determines the memory type used to access the 1-GByte page referenced by this entry.

@see Vol3A[4.9.2(Paging and Memory Typing When the PAT is Supported (Pentium III and More Recent Processor Families))]
        """,

        12,
        1

    )


    PFN = BitFieldMember(
        "PFN",
        """
        @brief Physical address of the 1-GByte page referenced by this entry

Physical address of the 1-GByte page referenced by this entry.
        """,

        30,
        18

    )


    IGNORED_2 = BitFieldMember(
        "IGNORED_2",
        """
        @brief Ignored

Ignored.
        """,

        52,
        7

    )


    PROTECTION_KEY = BitFieldMember(
        "PROTECTION_KEY",
        """
        @brief Protection key; if CR4.PKE = 1, determines the protection key of the page; ignored otherwise

Protection key; if CR4.PKE = 1, determines the protection key of the page; ignored otherwise.

@see Vol3A[4.6.2(Protection Keys)]
        """,

        59,
        4

    )


    XD = BitFieldMember(
        "XD",
        """
        @brief If IA32_EFER.NXE = 1, execute-disable (if 1, instruction fetches are not allowed from the 1-GByte page
controlled by this entry); otherwise, reserved (must be 0)

If IA32_EFER.NXE = 1, execute-disable (if 1, instruction fetches are not allowed from the 1-GByte page
controlled by this entry); otherwise, reserved (must be 0).

@see Vol3A[4.6(Access Rights)]
        """,

        63,
        1

    )


class Pdpte64(with_metaclass(BitFieldMeta, BitField)):
    """
    @brief Format of a 4-Level Page-Directory-Pointer-Table Entry (PDPTE) that References a Page Directory

Format of a 4-Level Page-Directory-Pointer-Table Entry (PDPTE) that References a Page Directory.
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super().__init__(value, byte_offset, byte_width, max_bytes=8)



    P = BitFieldMember(
        "P",
        """
        @brief Present; must be 1 to reference a page directory

Present; must be 1 to reference a page directory.
        """,

        0,
        1

    )


    RW = BitFieldMember(
        "RW",
        """
        @brief Read/write; if 0, writes may not be allowed to the 1-GByte region controlled by this entry

Read/write; if 0, writes may not be allowed to the 1-GByte region controlled by this entry.

@see Vol3A[4.6(Access Rights)]
        """,

        1,
        1

    )


    US = BitFieldMember(
        "US",
        """
        @brief User/supervisor; if 0, user-mode accesses are not allowed to the 1-GByte region controlled by this entry

User/supervisor; if 0, user-mode accesses are not allowed to the 1-GByte region controlled by this entry.

@see Vol3A[4.6(Access Rights)]
        """,

        2,
        1

    )


    PWT = BitFieldMember(
        "PWT",
        """
        @brief Page-level write-through; indirectly determines the memory type used to access the page directory referenced by
this entry

Page-level write-through; indirectly determines the memory type used to access the page directory referenced by
this entry.

@see Vol3A[4.9.2(Paging and Memory Typing When the PAT is Supported (Pentium III and More Recent Processor Families))]
        """,

        3,
        1

    )


    PCD = BitFieldMember(
        "PCD",
        """
        @brief Page-level cache disable; indirectly determines the memory type used to access the page directory referenced by
this entry

Page-level cache disable; indirectly determines the memory type used to access the page directory referenced by
this entry.

@see Vol3A[4.9.2(Paging and Memory Typing When the PAT is Supported (Pentium III and More Recent Processor Families))]
        """,

        4,
        1

    )


    A = BitFieldMember(
        "A",
        """
        @brief Accessed; indicates whether this entry has been used for linear-address translation

Accessed; indicates whether this entry has been used for linear-address translation.

@see Vol3A[4.8(Accessed and Dirty Flags)]
        """,

        5,
        1

    )


    LARGE = BitFieldMember(
        "LARGE",
        """
        @brief Page size; must be 0 (otherwise, this entry maps a 1-GByte page)

Page size; must be 0 (otherwise, this entry maps a 1-GByte page).
        """,

        7,
        1

    )


    IGNORED_1 = BitFieldMember(
        "IGNORED_1",
        """
        @brief Ignored

Ignored.
        """,

        8,
        4

    )


    PFN = BitFieldMember(
        "PFN",
        """
        @brief Physical address of 4-KByte aligned page directory referenced by this entry

Physical address of 4-KByte aligned page directory referenced by this entry.
        """,

        12,
        36

    )


    IGNORED_2 = BitFieldMember(
        "IGNORED_2",
        """
        @brief Ignored

Ignored.
        """,

        52,
        11

    )


    XD = BitFieldMember(
        "XD",
        """
        @brief If IA32_EFER.NXE = 1, execute-disable (if 1, instruction fetches are not allowed from the 1-GByte region
controlled by this entry); otherwise, reserved (must be 0)

If IA32_EFER.NXE = 1, execute-disable (if 1, instruction fetches are not allowed from the 1-GByte region
controlled by this entry); otherwise, reserved (must be 0).

@see Vol3A[4.6(Access Rights)]
        """,

        63,
        1

    )


class Pde2mb64(with_metaclass(BitFieldMeta, BitField)):
    """
    @brief Format of a 4-Level Page-Directory Entry that Maps a 2-MByte Page

Format of a 4-Level Page-Directory Entry that Maps a 2-MByte Page.
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super().__init__(value, byte_offset, byte_width, max_bytes=8)



    P = BitFieldMember(
        "P",
        """
        @brief Present; must be 1 to map a 2-MByte page

Present; must be 1 to map a 2-MByte page.
        """,

        0,
        1

    )


    RW = BitFieldMember(
        "RW",
        """
        @brief Read/write; if 0, writes may not be allowed to the 2-MByte page referenced by this entry

Read/write; if 0, writes may not be allowed to the 2-MByte page referenced by this entry.

@see Vol3A[4.6(Access Rights)]
        """,

        1,
        1

    )


    US = BitFieldMember(
        "US",
        """
        @brief User/supervisor; if 0, user-mode accesses are not allowed to the 2-MByte page referenced by this entry

User/supervisor; if 0, user-mode accesses are not allowed to the 2-MByte page referenced by this entry.

@see Vol3A[4.6(Access Rights)]
        """,

        2,
        1

    )


    PWT = BitFieldMember(
        "PWT",
        """
        @brief Page-level write-through; indirectly determines the memory type used to access the 2-MByte page referenced by
this entry

Page-level write-through; indirectly determines the memory type used to access the 2-MByte page referenced by
this entry.

@see Vol3A[4.9.2(Paging and Memory Typing When the PAT is Supported (Pentium III and More Recent Processor Families))]
        """,

        3,
        1

    )


    PCD = BitFieldMember(
        "PCD",
        """
        @brief Page-level cache disable; indirectly determines the memory type used to access the 2-MByte page referenced by
this entry

Page-level cache disable; indirectly determines the memory type used to access the 2-MByte page referenced by
this entry.

@see Vol3A[4.9.2(Paging and Memory Typing When the PAT is Supported (Pentium III and More Recent Processor Families))]
        """,

        4,
        1

    )


    A = BitFieldMember(
        "A",
        """
        @brief Accessed; indicates whether software has accessed the 2-MByte page referenced by this entry

Accessed; indicates whether software has accessed the 2-MByte page referenced by this entry.

@see Vol3A[4.8(Accessed and Dirty Flags)]
        """,

        5,
        1

    )


    D = BitFieldMember(
        "D",
        """
        @brief Dirty; indicates whether software has written to the 2-MByte page referenced by this entry

Dirty; indicates whether software has written to the 2-MByte page referenced by this entry.

@see Vol3A[4.8(Accessed and Dirty Flags)]
        """,

        6,
        1

    )


    LARGE = BitFieldMember(
        "LARGE",
        """
        @brief Page size; must be 1 (otherwise, this entry references a page directory)

Page size; must be 1 (otherwise, this entry references a page directory).
        """,

        7,
        1

    )


    G = BitFieldMember(
        "G",
        """
        @brief Global; if CR4.PGE = 1, determines whether the translation is global; ignored otherwise

Global; if CR4.PGE = 1, determines whether the translation is global; ignored otherwise.

@see Vol3A[4.10(Caching Translation Information)]
        """,

        8,
        1

    )


    IGNORED_1 = BitFieldMember(
        "IGNORED_1",
        """
        @brief Ignored

Ignored.
        """,

        9,
        3

    )


    PAT = BitFieldMember(
        "PAT",
        """
        @brief Indirectly determines the memory type used to access the 2-MByte page referenced by this entry

Indirectly determines the memory type used to access the 2-MByte page referenced by this entry.

@see Vol3A[4.9.2(Paging and Memory Typing When the PAT is Supported (Pentium III and More Recent Processor Families))]
        """,

        12,
        1

    )


    PFN = BitFieldMember(
        "PFN",
        """
        @brief Physical address of the 2-MByte page referenced by this entry

Physical address of the 2-MByte page referenced by this entry.
        """,

        21,
        27

    )


    IGNORED_2 = BitFieldMember(
        "IGNORED_2",
        """
        @brief Ignored

Ignored.
        """,

        52,
        7

    )


    PROTECTION_KEY = BitFieldMember(
        "PROTECTION_KEY",
        """
        @brief Protection key; if CR4.PKE = 1, determines the protection key of the page; ignored otherwise

Protection key; if CR4.PKE = 1, determines the protection key of the page; ignored otherwise.

@see Vol3A[4.6.2(Protection Keys)]
        """,

        59,
        4

    )


    XD = BitFieldMember(
        "XD",
        """
        @brief If IA32_EFER.NXE = 1, execute-disable (if 1, instruction fetches are not allowed from the 2-MByte page
controlled by this entry); otherwise, reserved (must be 0)

If IA32_EFER.NXE = 1, execute-disable (if 1, instruction fetches are not allowed from the 2-MByte page
controlled by this entry); otherwise, reserved (must be 0).

@see Vol3A[4.6(Access Rights)]
        """,

        63,
        1

    )


class Pde64(with_metaclass(BitFieldMeta, BitField)):
    """
    @brief Format of a 4-Level Page-Directory Entry that References a Page Table

Format of a 4-Level Page-Directory Entry that References a Page Table.
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super().__init__(value, byte_offset, byte_width, max_bytes=8)



    P = BitFieldMember(
        "P",
        """
        @brief Present; must be 1 to reference a page table

Present; must be 1 to reference a page table.
        """,

        0,
        1

    )


    RW = BitFieldMember(
        "RW",
        """
        @brief Read/write; if 0, writes may not be allowed to the 2-MByte region controlled by this entry

Read/write; if 0, writes may not be allowed to the 2-MByte region controlled by this entry.

@see Vol3A[4.6(Access Rights)]
        """,

        1,
        1

    )


    US = BitFieldMember(
        "US",
        """
        @brief User/supervisor; if 0, user-mode accesses are not allowed to the 2-MByte region controlled by this entry

User/supervisor; if 0, user-mode accesses are not allowed to the 2-MByte region controlled by this entry.

@see Vol3A[4.6(Access Rights)]
        """,

        2,
        1

    )


    PWT = BitFieldMember(
        "PWT",
        """
        @brief Page-level write-through; indirectly determines the memory type used to access the page table referenced by this
entry

Page-level write-through; indirectly determines the memory type used to access the page table referenced by this
entry.

@see Vol3A[4.9.2(Paging and Memory Typing When the PAT is Supported (Pentium III and More Recent Processor Families))]
        """,

        3,
        1

    )


    PCD = BitFieldMember(
        "PCD",
        """
        @brief Page-level cache disable; indirectly determines the memory type used to access the page table referenced by this
entry

Page-level cache disable; indirectly determines the memory type used to access the page table referenced by this
entry.

@see Vol3A[4.9.2(Paging and Memory Typing When the PAT is Supported (Pentium III and More Recent Processor Families))]
        """,

        4,
        1

    )


    A = BitFieldMember(
        "A",
        """
        @brief Accessed; indicates whether this entry has been used for linear-address translation

Accessed; indicates whether this entry has been used for linear-address translation.

@see Vol3A[4.8(Accessed and Dirty Flags)]
        """,

        5,
        1

    )


    LARGE = BitFieldMember(
        "LARGE",
        """
        @brief Page size; must be 0 (otherwise, this entry maps a 2-MByte page)

Page size; must be 0 (otherwise, this entry maps a 2-MByte page).
        """,

        7,
        1

    )


    IGNORED_1 = BitFieldMember(
        "IGNORED_1",
        """
        @brief Ignored

Ignored.
        """,

        8,
        4

    )


    PFN = BitFieldMember(
        "PFN",
        """
        @brief Physical address of 4-KByte aligned page table referenced by this entry

Physical address of 4-KByte aligned page table referenced by this entry.
        """,

        12,
        36

    )


    IGNORED_2 = BitFieldMember(
        "IGNORED_2",
        """
        @brief Ignored

Ignored.
        """,

        52,
        11

    )


    XD = BitFieldMember(
        "XD",
        """
        @brief If IA32_EFER.NXE = 1, execute-disable (if 1, instruction fetches are not allowed from the 2-MByte region
controlled by this entry); otherwise, reserved (must be 0)

If IA32_EFER.NXE = 1, execute-disable (if 1, instruction fetches are not allowed from the 2-MByte region
controlled by this entry); otherwise, reserved (must be 0).

@see Vol3A[4.6(Access Rights)]
        """,

        63,
        1

    )


class Pte64(with_metaclass(BitFieldMeta, BitField)):
    """
    @brief Format of a 4-Level Page-Table Entry that Maps a 4-KByte Page

Format of a 4-Level Page-Table Entry that Maps a 4-KByte Page.
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super().__init__(value, byte_offset, byte_width, max_bytes=8)



    P = BitFieldMember(
        "P",
        """
        @brief Present; must be 1 to map a 4-KByte page

Present; must be 1 to map a 4-KByte page.
        """,

        0,
        1

    )


    RW = BitFieldMember(
        "RW",
        """
        @brief Read/write; if 0, writes may not be allowed to the 4-KByte page referenced by this entry

Read/write; if 0, writes may not be allowed to the 4-KByte page referenced by this entry.

@see Vol3A[4.6(Access Rights)]
        """,

        1,
        1

    )


    US = BitFieldMember(
        "US",
        """
        @brief User/supervisor; if 0, user-mode accesses are not allowed to the 4-KByte page referenced by this entry

User/supervisor; if 0, user-mode accesses are not allowed to the 4-KByte page referenced by this entry.

@see Vol3A[4.6(Access Rights)]
        """,

        2,
        1

    )


    PWT = BitFieldMember(
        "PWT",
        """
        @brief Page-level write-through; indirectly determines the memory type used to access the 4-KByte page referenced by
this entry

Page-level write-through; indirectly determines the memory type used to access the 4-KByte page referenced by
this entry.

@see Vol3A[4.9.2(Paging and Memory Typing When the PAT is Supported (Pentium III and More Recent Processor Families))]
        """,

        3,
        1

    )


    PCD = BitFieldMember(
        "PCD",
        """
        @brief Page-level cache disable; indirectly determines the memory type used to access the 4-KByte page referenced by this
entry

Page-level cache disable; indirectly determines the memory type used to access the 4-KByte page referenced by this
entry.

@see Vol3A[4.9.2(Paging and Memory Typing When the PAT is Supported (Pentium III and More Recent Processor Families))]
        """,

        4,
        1

    )


    A = BitFieldMember(
        "A",
        """
        @brief Accessed; indicates whether software has accessed the 4-KByte page referenced by this entry

Accessed; indicates whether software has accessed the 4-KByte page referenced by this entry.

@see Vol3A[4.8(Accessed and Dirty Flags)]
        """,

        5,
        1

    )


    D = BitFieldMember(
        "D",
        """
        @brief Dirty; indicates whether software has written to the 4-KByte page referenced by this entry

Dirty; indicates whether software has written to the 4-KByte page referenced by this entry.

@see Vol3A[4.8(Accessed and Dirty Flags)]
        """,

        6,
        1

    )


    PAT = BitFieldMember(
        "PAT",
        """
        @brief Indirectly determines the memory type used to access the 4-KByte page referenced by this entry

Indirectly determines the memory type used to access the 4-KByte page referenced by this entry.

@see Vol3A[4.9.2(Paging and Memory Typing When the PAT is Supported (Pentium III and More Recent Processor Families))]
        """,

        7,
        1

    )


    G = BitFieldMember(
        "G",
        """
        @brief Global; if CR4.PGE = 1, determines whether the translation is global; ignored otherwise

Global; if CR4.PGE = 1, determines whether the translation is global; ignored otherwise.

@see Vol3A[4.10(Caching Translation Information)]
        """,

        8,
        1

    )


    IGNORED_1 = BitFieldMember(
        "IGNORED_1",
        """
        @brief Ignored

Ignored.
        """,

        9,
        3

    )


    PFN = BitFieldMember(
        "PFN",
        """
        @brief Physical address of the 4-KByte page referenced by this entry

Physical address of the 4-KByte page referenced by this entry.
        """,

        12,
        36

    )


    IGNORED_2 = BitFieldMember(
        "IGNORED_2",
        """
        @brief Ignored

Ignored.
        """,

        52,
        7

    )


    PROTECTION_KEY = BitFieldMember(
        "PROTECTION_KEY",
        """
        @brief Protection key; if CR4.PKE = 1, determines the protection key of the page; ignored otherwise

Protection key; if CR4.PKE = 1, determines the protection key of the page; ignored otherwise.

@see Vol3A[4.6.2(Protection Keys)]
        """,

        59,
        4

    )


    XD = BitFieldMember(
        "XD",
        """
        @brief If IA32_EFER.NXE = 1, execute-disable (if 1, instruction fetches are not allowed from the 1-GByte page
controlled by this entry); otherwise, reserved (must be 0)

If IA32_EFER.NXE = 1, execute-disable (if 1, instruction fetches are not allowed from the 1-GByte page
controlled by this entry); otherwise, reserved (must be 0).

@see Vol3A[4.6(Access Rights)]
        """,

        63,
        1

    )


class PtEntry64(with_metaclass(BitFieldMeta, BitField)):
    """
    @brief Format of a common Page-Table Entry

Format of a common Page-Table Entry.
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super().__init__(value, byte_offset, byte_width, max_bytes=8)



    P = BitFieldMember(
        "P",
        """
        
        """,

        0,
        1

    )


    RW = BitFieldMember(
        "RW",
        """
        
        """,

        1,
        1

    )


    US = BitFieldMember(
        "US",
        """
        
        """,

        2,
        1

    )


    PWT = BitFieldMember(
        "PWT",
        """
        
        """,

        3,
        1

    )


    PCD = BitFieldMember(
        "PCD",
        """
        
        """,

        4,
        1

    )


    A = BitFieldMember(
        "A",
        """
        
        """,

        5,
        1

    )


    D = BitFieldMember(
        "D",
        """
        
        """,

        6,
        1

    )


    LARGE = BitFieldMember(
        "LARGE",
        """
        
        """,

        7,
        1

    )


    G = BitFieldMember(
        "G",
        """
        
        """,

        8,
        1

    )


    IGNORED_1 = BitFieldMember(
        "IGNORED_1",
        """
        @brief Ignored

Ignored.
        """,

        9,
        3

    )


    PFN = BitFieldMember(
        "PFN",
        """
        @brief Physical address of the 4-KByte page referenced by this entry

Physical address of the 4-KByte page referenced by this entry.
        """,

        12,
        36

    )


    IGNORED_2 = BitFieldMember(
        "IGNORED_2",
        """
        @brief Ignored

Ignored.
        """,

        52,
        7

    )


    PROTECTION_KEY = BitFieldMember(
        "PROTECTION_KEY",
        """
        
        """,

        59,
        4

    )


    XD = BitFieldMember(
        "XD",
        """
        
        """,

        63,
        1

    )


