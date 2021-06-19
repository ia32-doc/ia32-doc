from future.utils import with_metaclass
from utils.bit_field import *


__doc__ = """
Every component of the VMCS is encoded by a 32-bit field that can be used by VMREAD and VMWRITE.
This enumerates all fields in the VMCS and their encodings. Fields are grouped by width (16-bit, 32-bit,
etc.) and type (guest-state, host-state, etc.).
"""
class VmcsComponentEncoding(with_metaclass(BitFieldMeta, BitField)):
    """"""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=2)


    
    ACCESS_TYPE = BitFieldMember(
        "ACCESS_TYPE",
        """
        Access type (0 = full; 1 = high); must be full for 16-bit, 32-bit, and natural-width fields:
        Access type (0 = full; 1 = high); must be full for 16-bit, 32-bit, and natural-width fields.
        """,
        0,
        1
    )

    
    INDEX = BitFieldMember(
        "INDEX",
        """
        Index:
        Index.
        """,
        1,
        9
    )

    
    TYPE = BitFieldMember(
        "TYPE",
        """
        Type:

0: control

1: VM-exit information

2: guest state

3: host state:
        Type:

0: control

1: VM-exit information

2: guest state

3: host state
        """,
        10,
        2
    )

    
    MUST_BE_ZERO = BitFieldMember(
        "MUST_BE_ZERO",
        """
        Reserved (must be 0):
        Reserved (must be 0).
        """,
        12,
        1
    )

    
    WIDTH = BitFieldMember(
        "WIDTH",
        """
        Width:

0: 16-bit

1: 64-bit

2: 32-bit

3: natural-width:
        Width:

0: 16-bit

1: 64-bit

2: 32-bit

3: natural-width
        """,
        13,
        2
    )

    

