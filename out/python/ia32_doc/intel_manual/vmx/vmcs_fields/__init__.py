from future.utils import with_metaclass
from utils.ia32_struct import *
from utils.ia32_bit_field import *


__doc__ = """
@brief VMCS (VM Control Structure)

Every component of the VMCS is encoded by a 32-bit field that can be used by VMREAD and VMWRITE.
This enumerates all fields in the VMCS and their encodings. Fields are grouped by width (16-bit, 32-bit,
etc.) and type (guest-state, host-state, etc.).
"""


class VmcsComponentEncoding(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
    """
    
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super(VmcsComponentEncoding, self).__init__(value, byte_offset, byte_width, max_bytes=2)



    ACCESS_TYPE = Ia32BitFieldMember(
        "ACCESS_TYPE",
        """
        @brief Access type (0 = full; 1 = high); must be full for 16-bit, 32-bit, and natural-width fields

Access type (0 = full; 1 = high); must be full for 16-bit, 32-bit, and natural-width fields.
        """,

        0,
        1

    )


    INDEX = Ia32BitFieldMember(
        "INDEX",
        """
        @brief Index

Index.
        """,

        1,
        9

    )


    TYPE = Ia32BitFieldMember(
        "TYPE",
        """
        @brief Type:

0: control

1: VM-exit information

2: guest state

3: host state

Type:

0: control

1: VM-exit information

2: guest state

3: host state
        """,

        10,
        2

    )


    MUST_BE_ZERO = Ia32BitFieldMember(
        "MUST_BE_ZERO",
        """
        @brief Reserved (must be 0)

Reserved (must be 0).
        """,

        12,
        1

    )


    WIDTH = Ia32BitFieldMember(
        "WIDTH",
        """
        @brief Width:

0: 16-bit

1: 64-bit

2: 32-bit

3: natural-width

Width:

0: 16-bit

1: 64-bit

2: 32-bit

3: natural-width
        """,

        13,
        2

    )


