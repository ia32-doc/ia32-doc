from future.utils import with_metaclass
from utils.bit_field import *


__doc__ = """
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
    """Format of a 4-Level PML4 Entry (PML4E) that References a Page-Directory-Pointer Table."""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=8)


    
    P = BitFieldMember(
        "P",
        """
        Present; must be 1 to reference a page-directory-pointer table:
        Present; must be 1 to reference a page-directory-pointer table.
        """,
        0,
        1
    )

    
    RW = BitFieldMember(
        "RW",
        """
        Read/write; if 0, writes may not be allowed to the 512-GByte region controlled by this entry:
        Read/write; if 0, writes may not be allowed to the 512-GByte region controlled by this entry.
        """,
        1,
        1
    )

    
    US = BitFieldMember(
        "US",
        """
        User/supervisor; if 0, user-mode accesses are not allowed to the 512-GByte region controlled by this entry:
        User/supervisor; if 0, user-mode accesses are not allowed to the 512-GByte region controlled by this entry.
        """,
        2,
        1
    )

    
    PWT = BitFieldMember(
        "PWT",
        """
        Page-level write-through; indirectly determines the memory type used to access the page-directory-pointer table
referenced by this entry:
        Page-level write-through; indirectly determines the memory type used to access the page-directory-pointer table
referenced by this entry.
        """,
        3,
        1
    )

    
    PCD = BitFieldMember(
        "PCD",
        """
        Page-level cache disable; indirectly determines the memory type used to access the page-directory-pointer table
referenced by this entry:
        Page-level cache disable; indirectly determines the memory type used to access the page-directory-pointer table
referenced by this entry.
        """,
        4,
        1
    )

    
    A = BitFieldMember(
        "A",
        """
        Accessed; indicates whether this entry has been used for linear-address translation:
        Accessed; indicates whether this entry has been used for linear-address translation.
        """,
        5,
        1
    )

    
    RESERVED = BitFieldMember(
        "RESERVED",
        """
        Reserved (must be 0):
        Reserved (must be 0).
        """,
        7,
        1
    )

    
    IGNORED_1 = BitFieldMember(
        "IGNORED_1",
        """
        Ignored:
        Ignored.
        """,
        8,
        4
    )

    
    PFN = BitFieldMember(
        "PFN",
        """
        Physical address of 4-KByte aligned page-directory-pointer table referenced by this entry:
        Physical address of 4-KByte aligned page-directory-pointer table referenced by this entry.
        """,
        12,
        36
    )

    
    IGNORED_2 = BitFieldMember(
        "IGNORED_2",
        """
        Ignored:
        Ignored.
        """,
        52,
        11
    )

    
    XD = BitFieldMember(
        "XD",
        """
        If IA32_EFER.NXE = 1, execute-disable (if 1, instruction fetches are not allowed from the 512-GByte region
controlled by this entry); otherwise, reserved (must be 0):
        If IA32_EFER.NXE = 1, execute-disable (if 1, instruction fetches are not allowed from the 512-GByte region
controlled by this entry); otherwise, reserved (must be 0).
        """,
        63,
        1
    )

    

class Pdpte1gb64(with_metaclass(BitFieldMeta, BitField)):
    """Format of a 4-Level Page-Directory-Pointer-Table Entry (PDPTE) that Maps a 1-GByte Page."""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=8)


    
    P = BitFieldMember(
        "P",
        """
        Present; must be 1 to map a 1-GByte page:
        Present; must be 1 to map a 1-GByte page.
        """,
        0,
        1
    )

    
    RW = BitFieldMember(
        "RW",
        """
        Read/write; if 0, writes may not be allowed to the 1-GByte page referenced by this entry:
        Read/write; if 0, writes may not be allowed to the 1-GByte page referenced by this entry.
        """,
        1,
        1
    )

    
    US = BitFieldMember(
        "US",
        """
        User/supervisor; if 0, user-mode accesses are not allowed to the 1-GByte page referenced by this entry:
        User/supervisor; if 0, user-mode accesses are not allowed to the 1-GByte page referenced by this entry.
        """,
        2,
        1
    )

    
    PWT = BitFieldMember(
        "PWT",
        """
        Page-level write-through; indirectly determines the memory type used to access the 1-GByte page referenced by this
entry:
        Page-level write-through; indirectly determines the memory type used to access the 1-GByte page referenced by this
entry.
        """,
        3,
        1
    )

    
    PCD = BitFieldMember(
        "PCD",
        """
        Page-level cache disable; indirectly determines the memory type used to access the 1-GByte page referenced by this
entry:
        Page-level cache disable; indirectly determines the memory type used to access the 1-GByte page referenced by this
entry.
        """,
        4,
        1
    )

    
    A = BitFieldMember(
        "A",
        """
        Accessed; indicates whether software has accessed the 1-GByte page referenced by this entry:
        Accessed; indicates whether software has accessed the 1-GByte page referenced by this entry.
        """,
        5,
        1
    )

    
    D = BitFieldMember(
        "D",
        """
        Dirty; indicates whether software has written to the 1-GByte page referenced by this entry:
        Dirty; indicates whether software has written to the 1-GByte page referenced by this entry.
        """,
        6,
        1
    )

    
    LARGE = BitFieldMember(
        "LARGE",
        """
        Page size; must be 1 (otherwise, this entry references a page directory):
        Page size; must be 1 (otherwise, this entry references a page directory).
        """,
        7,
        1
    )

    
    G = BitFieldMember(
        "G",
        """
        Global; if CR4.PGE = 1, determines whether the translation is global; ignored otherwise:
        Global; if CR4.PGE = 1, determines whether the translation is global; ignored otherwise.
        """,
        8,
        1
    )

    
    IGNORED_1 = BitFieldMember(
        "IGNORED_1",
        """
        Ignored:
        Ignored.
        """,
        9,
        3
    )

    
    PAT = BitFieldMember(
        "PAT",
        """
        Indirectly determines the memory type used to access the 1-GByte page referenced by this entry:
        Indirectly determines the memory type used to access the 1-GByte page referenced by this entry.
        """,
        12,
        1
    )

    
    PFN = BitFieldMember(
        "PFN",
        """
        Physical address of the 1-GByte page referenced by this entry:
        Physical address of the 1-GByte page referenced by this entry.
        """,
        30,
        18
    )

    
    IGNORED_2 = BitFieldMember(
        "IGNORED_2",
        """
        Ignored:
        Ignored.
        """,
        52,
        7
    )

    
    PROTECTION_KEY = BitFieldMember(
        "PROTECTION_KEY",
        """
        Protection key; if CR4.PKE = 1, determines the protection key of the page; ignored otherwise:
        Protection key; if CR4.PKE = 1, determines the protection key of the page; ignored otherwise.
        """,
        59,
        4
    )

    
    XD = BitFieldMember(
        "XD",
        """
        If IA32_EFER.NXE = 1, execute-disable (if 1, instruction fetches are not allowed from the 1-GByte page
controlled by this entry); otherwise, reserved (must be 0):
        If IA32_EFER.NXE = 1, execute-disable (if 1, instruction fetches are not allowed from the 1-GByte page
controlled by this entry); otherwise, reserved (must be 0).
        """,
        63,
        1
    )

    

class Pdpte64(with_metaclass(BitFieldMeta, BitField)):
    """Format of a 4-Level Page-Directory-Pointer-Table Entry (PDPTE) that References a Page Directory."""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=8)


    
    P = BitFieldMember(
        "P",
        """
        Present; must be 1 to reference a page directory:
        Present; must be 1 to reference a page directory.
        """,
        0,
        1
    )

    
    RW = BitFieldMember(
        "RW",
        """
        Read/write; if 0, writes may not be allowed to the 1-GByte region controlled by this entry:
        Read/write; if 0, writes may not be allowed to the 1-GByte region controlled by this entry.
        """,
        1,
        1
    )

    
    US = BitFieldMember(
        "US",
        """
        User/supervisor; if 0, user-mode accesses are not allowed to the 1-GByte region controlled by this entry:
        User/supervisor; if 0, user-mode accesses are not allowed to the 1-GByte region controlled by this entry.
        """,
        2,
        1
    )

    
    PWT = BitFieldMember(
        "PWT",
        """
        Page-level write-through; indirectly determines the memory type used to access the page directory referenced by
this entry:
        Page-level write-through; indirectly determines the memory type used to access the page directory referenced by
this entry.
        """,
        3,
        1
    )

    
    PCD = BitFieldMember(
        "PCD",
        """
        Page-level cache disable; indirectly determines the memory type used to access the page directory referenced by
this entry:
        Page-level cache disable; indirectly determines the memory type used to access the page directory referenced by
this entry.
        """,
        4,
        1
    )

    
    A = BitFieldMember(
        "A",
        """
        Accessed; indicates whether this entry has been used for linear-address translation:
        Accessed; indicates whether this entry has been used for linear-address translation.
        """,
        5,
        1
    )

    
    LARGE = BitFieldMember(
        "LARGE",
        """
        Page size; must be 0 (otherwise, this entry maps a 1-GByte page):
        Page size; must be 0 (otherwise, this entry maps a 1-GByte page).
        """,
        7,
        1
    )

    
    IGNORED_1 = BitFieldMember(
        "IGNORED_1",
        """
        Ignored:
        Ignored.
        """,
        8,
        4
    )

    
    PFN = BitFieldMember(
        "PFN",
        """
        Physical address of 4-KByte aligned page directory referenced by this entry:
        Physical address of 4-KByte aligned page directory referenced by this entry.
        """,
        12,
        36
    )

    
    IGNORED_2 = BitFieldMember(
        "IGNORED_2",
        """
        Ignored:
        Ignored.
        """,
        52,
        11
    )

    
    XD = BitFieldMember(
        "XD",
        """
        If IA32_EFER.NXE = 1, execute-disable (if 1, instruction fetches are not allowed from the 1-GByte region
controlled by this entry); otherwise, reserved (must be 0):
        If IA32_EFER.NXE = 1, execute-disable (if 1, instruction fetches are not allowed from the 1-GByte region
controlled by this entry); otherwise, reserved (must be 0).
        """,
        63,
        1
    )

    

class Pde2mb64(with_metaclass(BitFieldMeta, BitField)):
    """Format of a 4-Level Page-Directory Entry that Maps a 2-MByte Page."""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=8)


    
    P = BitFieldMember(
        "P",
        """
        Present; must be 1 to map a 2-MByte page:
        Present; must be 1 to map a 2-MByte page.
        """,
        0,
        1
    )

    
    RW = BitFieldMember(
        "RW",
        """
        Read/write; if 0, writes may not be allowed to the 2-MByte page referenced by this entry:
        Read/write; if 0, writes may not be allowed to the 2-MByte page referenced by this entry.
        """,
        1,
        1
    )

    
    US = BitFieldMember(
        "US",
        """
        User/supervisor; if 0, user-mode accesses are not allowed to the 2-MByte page referenced by this entry:
        User/supervisor; if 0, user-mode accesses are not allowed to the 2-MByte page referenced by this entry.
        """,
        2,
        1
    )

    
    PWT = BitFieldMember(
        "PWT",
        """
        Page-level write-through; indirectly determines the memory type used to access the 2-MByte page referenced by
this entry:
        Page-level write-through; indirectly determines the memory type used to access the 2-MByte page referenced by
this entry.
        """,
        3,
        1
    )

    
    PCD = BitFieldMember(
        "PCD",
        """
        Page-level cache disable; indirectly determines the memory type used to access the 2-MByte page referenced by
this entry:
        Page-level cache disable; indirectly determines the memory type used to access the 2-MByte page referenced by
this entry.
        """,
        4,
        1
    )

    
    A = BitFieldMember(
        "A",
        """
        Accessed; indicates whether software has accessed the 2-MByte page referenced by this entry:
        Accessed; indicates whether software has accessed the 2-MByte page referenced by this entry.
        """,
        5,
        1
    )

    
    D = BitFieldMember(
        "D",
        """
        Dirty; indicates whether software has written to the 2-MByte page referenced by this entry:
        Dirty; indicates whether software has written to the 2-MByte page referenced by this entry.
        """,
        6,
        1
    )

    
    LARGE = BitFieldMember(
        "LARGE",
        """
        Page size; must be 1 (otherwise, this entry references a page directory):
        Page size; must be 1 (otherwise, this entry references a page directory).
        """,
        7,
        1
    )

    
    G = BitFieldMember(
        "G",
        """
        Global; if CR4.PGE = 1, determines whether the translation is global; ignored otherwise:
        Global; if CR4.PGE = 1, determines whether the translation is global; ignored otherwise.
        """,
        8,
        1
    )

    
    IGNORED_1 = BitFieldMember(
        "IGNORED_1",
        """
        Ignored:
        Ignored.
        """,
        9,
        3
    )

    
    PAT = BitFieldMember(
        "PAT",
        """
        Indirectly determines the memory type used to access the 2-MByte page referenced by this entry:
        Indirectly determines the memory type used to access the 2-MByte page referenced by this entry.
        """,
        12,
        1
    )

    
    PFN = BitFieldMember(
        "PFN",
        """
        Physical address of the 2-MByte page referenced by this entry:
        Physical address of the 2-MByte page referenced by this entry.
        """,
        21,
        27
    )

    
    IGNORED_2 = BitFieldMember(
        "IGNORED_2",
        """
        Ignored:
        Ignored.
        """,
        52,
        7
    )

    
    PROTECTION_KEY = BitFieldMember(
        "PROTECTION_KEY",
        """
        Protection key; if CR4.PKE = 1, determines the protection key of the page; ignored otherwise:
        Protection key; if CR4.PKE = 1, determines the protection key of the page; ignored otherwise.
        """,
        59,
        4
    )

    
    XD = BitFieldMember(
        "XD",
        """
        If IA32_EFER.NXE = 1, execute-disable (if 1, instruction fetches are not allowed from the 2-MByte page
controlled by this entry); otherwise, reserved (must be 0):
        If IA32_EFER.NXE = 1, execute-disable (if 1, instruction fetches are not allowed from the 2-MByte page
controlled by this entry); otherwise, reserved (must be 0).
        """,
        63,
        1
    )

    

class Pde64(with_metaclass(BitFieldMeta, BitField)):
    """Format of a 4-Level Page-Directory Entry that References a Page Table."""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=8)


    
    P = BitFieldMember(
        "P",
        """
        Present; must be 1 to reference a page table:
        Present; must be 1 to reference a page table.
        """,
        0,
        1
    )

    
    RW = BitFieldMember(
        "RW",
        """
        Read/write; if 0, writes may not be allowed to the 2-MByte region controlled by this entry:
        Read/write; if 0, writes may not be allowed to the 2-MByte region controlled by this entry.
        """,
        1,
        1
    )

    
    US = BitFieldMember(
        "US",
        """
        User/supervisor; if 0, user-mode accesses are not allowed to the 2-MByte region controlled by this entry:
        User/supervisor; if 0, user-mode accesses are not allowed to the 2-MByte region controlled by this entry.
        """,
        2,
        1
    )

    
    PWT = BitFieldMember(
        "PWT",
        """
        Page-level write-through; indirectly determines the memory type used to access the page table referenced by this
entry:
        Page-level write-through; indirectly determines the memory type used to access the page table referenced by this
entry.
        """,
        3,
        1
    )

    
    PCD = BitFieldMember(
        "PCD",
        """
        Page-level cache disable; indirectly determines the memory type used to access the page table referenced by this
entry:
        Page-level cache disable; indirectly determines the memory type used to access the page table referenced by this
entry.
        """,
        4,
        1
    )

    
    A = BitFieldMember(
        "A",
        """
        Accessed; indicates whether this entry has been used for linear-address translation:
        Accessed; indicates whether this entry has been used for linear-address translation.
        """,
        5,
        1
    )

    
    LARGE = BitFieldMember(
        "LARGE",
        """
        Page size; must be 0 (otherwise, this entry maps a 2-MByte page):
        Page size; must be 0 (otherwise, this entry maps a 2-MByte page).
        """,
        7,
        1
    )

    
    IGNORED_1 = BitFieldMember(
        "IGNORED_1",
        """
        Ignored:
        Ignored.
        """,
        8,
        4
    )

    
    PFN = BitFieldMember(
        "PFN",
        """
        Physical address of 4-KByte aligned page table referenced by this entry:
        Physical address of 4-KByte aligned page table referenced by this entry.
        """,
        12,
        36
    )

    
    IGNORED_2 = BitFieldMember(
        "IGNORED_2",
        """
        Ignored:
        Ignored.
        """,
        52,
        11
    )

    
    XD = BitFieldMember(
        "XD",
        """
        If IA32_EFER.NXE = 1, execute-disable (if 1, instruction fetches are not allowed from the 2-MByte region
controlled by this entry); otherwise, reserved (must be 0):
        If IA32_EFER.NXE = 1, execute-disable (if 1, instruction fetches are not allowed from the 2-MByte region
controlled by this entry); otherwise, reserved (must be 0).
        """,
        63,
        1
    )

    

class Pte64(with_metaclass(BitFieldMeta, BitField)):
    """Format of a 4-Level Page-Table Entry that Maps a 4-KByte Page."""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=8)


    
    P = BitFieldMember(
        "P",
        """
        Present; must be 1 to map a 4-KByte page:
        Present; must be 1 to map a 4-KByte page.
        """,
        0,
        1
    )

    
    RW = BitFieldMember(
        "RW",
        """
        Read/write; if 0, writes may not be allowed to the 4-KByte page referenced by this entry:
        Read/write; if 0, writes may not be allowed to the 4-KByte page referenced by this entry.
        """,
        1,
        1
    )

    
    US = BitFieldMember(
        "US",
        """
        User/supervisor; if 0, user-mode accesses are not allowed to the 4-KByte page referenced by this entry:
        User/supervisor; if 0, user-mode accesses are not allowed to the 4-KByte page referenced by this entry.
        """,
        2,
        1
    )

    
    PWT = BitFieldMember(
        "PWT",
        """
        Page-level write-through; indirectly determines the memory type used to access the 4-KByte page referenced by
this entry:
        Page-level write-through; indirectly determines the memory type used to access the 4-KByte page referenced by
this entry.
        """,
        3,
        1
    )

    
    PCD = BitFieldMember(
        "PCD",
        """
        Page-level cache disable; indirectly determines the memory type used to access the 4-KByte page referenced by this
entry:
        Page-level cache disable; indirectly determines the memory type used to access the 4-KByte page referenced by this
entry.
        """,
        4,
        1
    )

    
    A = BitFieldMember(
        "A",
        """
        Accessed; indicates whether software has accessed the 4-KByte page referenced by this entry:
        Accessed; indicates whether software has accessed the 4-KByte page referenced by this entry.
        """,
        5,
        1
    )

    
    D = BitFieldMember(
        "D",
        """
        Dirty; indicates whether software has written to the 4-KByte page referenced by this entry:
        Dirty; indicates whether software has written to the 4-KByte page referenced by this entry.
        """,
        6,
        1
    )

    
    PAT = BitFieldMember(
        "PAT",
        """
        Indirectly determines the memory type used to access the 4-KByte page referenced by this entry:
        Indirectly determines the memory type used to access the 4-KByte page referenced by this entry.
        """,
        7,
        1
    )

    
    G = BitFieldMember(
        "G",
        """
        Global; if CR4.PGE = 1, determines whether the translation is global; ignored otherwise:
        Global; if CR4.PGE = 1, determines whether the translation is global; ignored otherwise.
        """,
        8,
        1
    )

    
    IGNORED_1 = BitFieldMember(
        "IGNORED_1",
        """
        Ignored:
        Ignored.
        """,
        9,
        3
    )

    
    PFN = BitFieldMember(
        "PFN",
        """
        Physical address of the 4-KByte page referenced by this entry:
        Physical address of the 4-KByte page referenced by this entry.
        """,
        12,
        36
    )

    
    IGNORED_2 = BitFieldMember(
        "IGNORED_2",
        """
        Ignored:
        Ignored.
        """,
        52,
        7
    )

    
    PROTECTION_KEY = BitFieldMember(
        "PROTECTION_KEY",
        """
        Protection key; if CR4.PKE = 1, determines the protection key of the page; ignored otherwise:
        Protection key; if CR4.PKE = 1, determines the protection key of the page; ignored otherwise.
        """,
        59,
        4
    )

    
    XD = BitFieldMember(
        "XD",
        """
        If IA32_EFER.NXE = 1, execute-disable (if 1, instruction fetches are not allowed from the 1-GByte page
controlled by this entry); otherwise, reserved (must be 0):
        If IA32_EFER.NXE = 1, execute-disable (if 1, instruction fetches are not allowed from the 1-GByte page
controlled by this entry); otherwise, reserved (must be 0).
        """,
        63,
        1
    )

    

class PtEntry64(with_metaclass(BitFieldMeta, BitField)):
    """Format of a common Page-Table Entry."""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=8)


    
    P = BitFieldMember(
        "P",
        """
        :
        
        """,
        0,
        1
    )

    
    RW = BitFieldMember(
        "RW",
        """
        :
        
        """,
        1,
        1
    )

    
    US = BitFieldMember(
        "US",
        """
        :
        
        """,
        2,
        1
    )

    
    PWT = BitFieldMember(
        "PWT",
        """
        :
        
        """,
        3,
        1
    )

    
    PCD = BitFieldMember(
        "PCD",
        """
        :
        
        """,
        4,
        1
    )

    
    A = BitFieldMember(
        "A",
        """
        :
        
        """,
        5,
        1
    )

    
    D = BitFieldMember(
        "D",
        """
        :
        
        """,
        6,
        1
    )

    
    LARGE = BitFieldMember(
        "LARGE",
        """
        :
        
        """,
        7,
        1
    )

    
    G = BitFieldMember(
        "G",
        """
        :
        
        """,
        8,
        1
    )

    
    IGNORED_1 = BitFieldMember(
        "IGNORED_1",
        """
        Ignored:
        Ignored.
        """,
        9,
        3
    )

    
    PFN = BitFieldMember(
        "PFN",
        """
        Physical address of the 4-KByte page referenced by this entry:
        Physical address of the 4-KByte page referenced by this entry.
        """,
        12,
        36
    )

    
    IGNORED_2 = BitFieldMember(
        "IGNORED_2",
        """
        Ignored:
        Ignored.
        """,
        52,
        7
    )

    
    PROTECTION_KEY = BitFieldMember(
        "PROTECTION_KEY",
        """
        :
        
        """,
        59,
        4
    )

    
    XD = BitFieldMember(
        "XD",
        """
        :
        
        """,
        63,
        1
    )

    

