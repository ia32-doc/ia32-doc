from future.utils import with_metaclass
from utils.bit_field import *


__doc__ = """
A logical processor uses 32-bit paging if CR0.PG = 1 and CR4.PAE = 0. 32-bit paging translates 32-bit linear
addresses to 40-bit physical addresses. Although 40 bits corresponds to 1 TByte, linear addresses are limited to
32 bits; at most 4 GBytes of linear-address space may be accessed at any given time.

32-bit paging uses a hierarchy of paging structures to produce a translation for a linear address. CR3 is used to
locate the first paging-structure, the page directory.
32-bit paging may map linear addresses to either 4-KByte pages or 4-MByte pages.
"""
class Pde4mb32(with_metaclass(BitFieldMeta, BitField)):
    """Format of a 32-Bit Page-Directory Entry that Maps a 4-MByte Page."""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=4)


    
    P = BitFieldMember(
        "P",
        """
        Present; must be 1 to map a 4-MByte page:
        Present; must be 1 to map a 4-MByte page.
        """,
        0,
        1
    )

    
    RW = BitFieldMember(
        "RW",
        """
        Read/write; if 0, writes may not be allowed to the 4-MByte page referenced by this entry:
        Read/write; if 0, writes may not be allowed to the 4-MByte page referenced by this entry.
        """,
        1,
        1
    )

    
    US = BitFieldMember(
        "US",
        """
        User/supervisor; if 0, user-mode accesses are not allowed to the 4-MByte page referenced by this entry:
        User/supervisor; if 0, user-mode accesses are not allowed to the 4-MByte page referenced by this entry.
        """,
        2,
        1
    )

    
    PWT = BitFieldMember(
        "PWT",
        """
        Page-level write-through; indirectly determines the memory type used to access the 4-MByte page referenced by
this entry:
        Page-level write-through; indirectly determines the memory type used to access the 4-MByte page referenced by
this entry.
        """,
        3,
        1
    )

    
    PCD = BitFieldMember(
        "PCD",
        """
        Page-level cache disable; indirectly determines the memory type used to access the 4-MByte page referenced by
this entry:
        Page-level cache disable; indirectly determines the memory type used to access the 4-MByte page referenced by
this entry.
        """,
        4,
        1
    )

    
    A = BitFieldMember(
        "A",
        """
        Accessed; indicates whether software has accessed the 4-MByte page referenced by this entry:
        Accessed; indicates whether software has accessed the 4-MByte page referenced by this entry.
        """,
        5,
        1
    )

    
    D = BitFieldMember(
        "D",
        """
        Dirty; indicates whether software has written to the 4-MByte page referenced by this entry:
        Dirty; indicates whether software has written to the 4-MByte page referenced by this entry.
        """,
        6,
        1
    )

    
    LARGE = BitFieldMember(
        "LARGE",
        """
        Page size; must be 1 (otherwise, this entry references a page table):
        Page size; must be 1 (otherwise, this entry references a page table).
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
        Indirectly determines the memory type used to access the 4-MByte page referenced by this entry:
        Indirectly determines the memory type used to access the 4-MByte page referenced by this entry.
        """,
        12,
        1
    )

    
    PFN_LOW = BitFieldMember(
        "PFN_LOW",
        """
        Bits (M1):32 of physical address of the 4-MByte page referenced by this entry:
        Bits (M1):32 of physical address of the 4-MByte page referenced by this entry.
        """,
        13,
        8
    )

    
    PFN_HIGH = BitFieldMember(
        "PFN_HIGH",
        """
        Bits 31:22 of physical address of the 4-MByte page referenced by this entry:
        Bits 31:22 of physical address of the 4-MByte page referenced by this entry.
        """,
        22,
        10
    )

    

class Pde32(with_metaclass(BitFieldMeta, BitField)):
    """Format of a 32-Bit Page-Directory Entry that References a Page Table."""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=4)


    
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
        Read/write; if 0, writes may not be allowed to the 4-MByte region controlled by this entry:
        Read/write; if 0, writes may not be allowed to the 4-MByte region controlled by this entry.
        """,
        1,
        1
    )

    
    US = BitFieldMember(
        "US",
        """
        User/supervisor; if 0, user-mode accesses are not allowed to the 4-MByte region controlled by this entry:
        User/supervisor; if 0, user-mode accesses are not allowed to the 4-MByte region controlled by this entry.
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

    
    IGNORED_1 = BitFieldMember(
        "IGNORED_1",
        """
        Ignored:
        Ignored.
        """,
        6,
        1
    )

    
    LARGE = BitFieldMember(
        "LARGE",
        """
        If CR4.PSE = 1, must be 0 (otherwise, this entry maps a 4-MByte page); otherwise, ignored:
        If CR4.PSE = 1, must be 0 (otherwise, this entry maps a 4-MByte page); otherwise, ignored.
        """,
        7,
        1
    )

    
    IGNORED_2 = BitFieldMember(
        "IGNORED_2",
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
        20
    )

    

class Pte32(with_metaclass(BitFieldMeta, BitField)):
    """Format of a 32-Bit Page-Table Entry that Maps a 4-KByte Page."""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=4)


    
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
        Physical address of 4-KByte aligned page table referenced by this entry:
        Physical address of 4-KByte aligned page table referenced by this entry.
        """,
        12,
        20
    )

    

class PtEntry32(with_metaclass(BitFieldMeta, BitField)):
    """Format of a common Page-Table Entry."""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=4)


    
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
        20
    )

    

