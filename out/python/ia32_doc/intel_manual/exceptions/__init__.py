from future.utils import with_metaclass
from utils.ia32_struct import *
from utils.ia32_bit_field import *


__doc__ = """
@brief Exceptions


"""


class ExceptionVector:
    """
    @brief Exceptions that can occur when the instruction is executed in protected mode.

Each exception is given a mnemonic that consists of a pound
sign (\#) followed by two letters and an optional error code in parentheses. For example, \#GP(0) denotes a general
protection exception with an error code of 0

Exceptions that can occur when the instruction is executed in protected mode.

Each exception is given a mnemonic that consists of a pound
sign (\#) followed by two letters and an optional error code in parentheses. For example, \#GP(0) denotes a general
protection exception with an error code of 0.
    """

    
      DE = 0x0
    
      DB = 0x1
    
      NMI = 0x2
    
      BP = 0x3
    
      OF = 0x4
    
      BR = 0x5
    
      UD = 0x6
    
      NM = 0x7
    
      DF = 0x8
    
      CO = 0x9
    
      TS = 0xa
    
      NP = 0xb
    
      SS = 0xc
    
      GP = 0xd
    
      PF = 0xe
    
      MF = 0x10
    
      AC = 0x11
    
      MC = 0x12
    
      XM = 0x13
    
      VE = 0x14
    
class ExceptionErrorCode(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
    """
    @brief When an exception condition is related to a specific segment selector or IDT vector, the processor pushes an error
code onto the stack of the exception handler (whether it is a procedure or task). The error code resembles a segment
selector; however, instead of a TI flag and RPL field, the error code contains 3 different flags

When an exception condition is related to a specific segment selector or IDT vector, the processor pushes an error
code onto the stack of the exception handler (whether it is a procedure or task). The error code resembles a segment
selector; however, instead of a TI flag and RPL field, the error code contains 3 different flags.
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super(ExceptionErrorCode, self).__init__(value, byte_offset, byte_width, max_bytes=4)



    EXT = Ia32BitFieldMember(
        "EXT",
        """
        @brief When set, indicates that the exception occurred during delivery of an
event external to the program, such as an interrupt or an earlier exception. The bit is cleared if the
exception occurred during delivery of a software interrupt (INT n, INT3, or INTO)

When set, indicates that the exception occurred during delivery of an
event external to the program, such as an interrupt or an earlier exception. The bit is cleared if the
exception occurred during delivery of a software interrupt (INT n, INT3, or INTO).
        """,

        0,
        1

    )


    IDT = Ia32BitFieldMember(
        "IDT",
        """
        @brief When set, indicates that the index portion of the error code refers
to a gate descriptor in the IDT; when clear, indicates that the index refers to a descriptor in the GDT
or the current LDT

When set, indicates that the index portion of the error code refers
to a gate descriptor in the IDT; when clear, indicates that the index refers to a descriptor in the GDT
or the current LDT.
        """,

        1,
        1

    )


    TI = Ia32BitFieldMember(
        "TI",
        """
        @brief Only used when the IDT flag is clear. When set, the TI flag indicates that the
index portion of the error code refers to a segment or gate descriptor in the LDT; when clear, it indicates
that the index refers to a descriptor in the current GDT

Only used when the IDT flag is clear. When set, the TI flag indicates that the
index portion of the error code refers to a segment or gate descriptor in the LDT; when clear, it indicates
that the index refers to a descriptor in the current GDT.
        """,

        2,
        1

    )


    INDEX = Ia32BitFieldMember(
        "INDEX",
        """
        @brief The segment selector index field provides an index into the IDT, GDT, or current LDT to the segment or gate
selector being referenced by the error code. In some cases the error code is null (all bits are clear except possibly
EXT). A null error code indicates that the error was not caused by a reference to a specific segment or that a null
segment selector was referenced in an operation

The segment selector index field provides an index into the IDT, GDT, or current LDT to the segment or gate
selector being referenced by the error code. In some cases the error code is null (all bits are clear except possibly
EXT). A null error code indicates that the error was not caused by a reference to a specific segment or that a null
segment selector was referenced in an operation.
        """,

        3,
        13

    )


class PageFaultException(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
    """
    @brief Page fault exception

Page fault exception.
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super(PageFaultException, self).__init__(value, byte_offset, byte_width, max_bytes=4)



    P = Ia32BitFieldMember(
        "P",
        """
        @brief This flag is 0 if there is no translation for the linear address because the P flag was 0 in one of the pagingstructure
entries used to translate that address

This flag is 0 if there is no translation for the linear address because the P flag was 0 in one of the pagingstructure
entries used to translate that address.
        """,

        0,
        1

    )


    W = Ia32BitFieldMember(
        "W",
        """
        @brief If the access causing the page-fault exception was a write, this flag is 1; otherwise, it is 0. This flag describes
the access causing the page-fault exception, not the access rights specified by paging

If the access causing the page-fault exception was a write, this flag is 1; otherwise, it is 0. This flag describes
the access causing the page-fault exception, not the access rights specified by paging.
        """,

        1,
        1

    )


    U = Ia32BitFieldMember(
        "U",
        """
        @brief If a user-mode access caused the page-fault exception, this flag is 1; it is 0 if a supervisor-mode access did so.
This flag describes the access causing the page-fault exception, not the access rights specified by paging

If a user-mode access caused the page-fault exception, this flag is 1; it is 0 if a supervisor-mode access did so.
This flag describes the access causing the page-fault exception, not the access rights specified by paging.

@see Vol3A[4.6(ACCESS RIGHTS)]
        """,

        2,
        1

    )


    RSVD = Ia32BitFieldMember(
        "RSVD",
        """
        @brief This flag is 1 if there is no translation for the linear address because a reserved bit was set in one of the pagingstructure
entries used to translate that address. (Because reserved bits are not checked in a paging-structure
entry whose P flag is 0, bit 3 of the error code can be set only if bit 0 is also set).
Bits reserved in the paging-structure entries are reserved for future functionality. Software developers should
be aware that such bits may be used in the future and that a paging-structure entry that causes a page-fault
exception on one processor might not do so in the future

This flag is 1 if there is no translation for the linear address because a reserved bit was set in one of the pagingstructure
entries used to translate that address. (Because reserved bits are not checked in a paging-structure
entry whose P flag is 0, bit 3 of the error code can be set only if bit 0 is also set).
Bits reserved in the paging-structure entries are reserved for future functionality. Software developers should
be aware that such bits may be used in the future and that a paging-structure entry that causes a page-fault
exception on one processor might not do so in the future.
        """,

        3,
        1

    )


    I = Ia32BitFieldMember(
        "I",
        """
        @brief This flag is 1 if (1) the access causing the page-fault exception was an instruction fetch; and (2) either
(a) CR4.SMEP = 1; or (b) both (i) CR4.PAE = 1 (either PAE paging or 4-level paging is in use); and
(ii) IA32_EFER.NXE = 1. Otherwise, the flag is 0. This flag describes the access causing the page-fault
exception, not the access rights specified by paging

This flag is 1 if (1) the access causing the page-fault exception was an instruction fetch; and (2) either
(a) CR4.SMEP = 1; or (b) both (i) CR4.PAE = 1 (either PAE paging or 4-level paging is in use); and
(ii) IA32_EFER.NXE = 1. Otherwise, the flag is 0. This flag describes the access causing the page-fault
exception, not the access rights specified by paging.
        """,

        4,
        1

    )


    PK = Ia32BitFieldMember(
        "PK",
        """
        @brief This flag is 1 if (1) IA32_EFER.LMA = CR4.PKE = 1; (2) the access causing the page-fault exception was a data
access; (3) the linear address was a user-mode address with protection key i; and (5) the PKRU register
is such that either (a) ADi = 1; or (b) the following all hold: (i) WDi = 1; (ii) the access is a write
access; and (iii) either CR0.WP = 1 or the access causing the page-fault exception was a user-mode access

This flag is 1 if (1) IA32_EFER.LMA = CR4.PKE = 1; (2) the access causing the page-fault exception was a data
access; (3) the linear address was a user-mode address with protection key i; and (5) the PKRU register
is such that either (a) ADi = 1; or (b) the following all hold: (i) WDi = 1; (ii) the access is a write
access; and (iii) either CR0.WP = 1 or the access causing the page-fault exception was a user-mode access.

@see Vol3A[4.6.2(Protection Keys)]
        """,

        5,
        1

    )


    SGX = Ia32BitFieldMember(
        "SGX",
        """
        @brief This flag is 1 if the exception is unrelated to paging and resulted from violation of SGX-specific access-control
requirements. Because such a violation can occur only if there is no ordinary page fault, this flag is set only if
the P flag (bit 0) is 1 and the RSVD flag (bit 3) and the PK flag (bit 5) are both 0

This flag is 1 if the exception is unrelated to paging and resulted from violation of SGX-specific access-control
requirements. Because such a violation can occur only if there is no ordinary page fault, this flag is set only if
the P flag (bit 0) is 1 and the RSVD flag (bit 3) and the PK flag (bit 5) are both 0.
        """,

        15,
        1

    )


