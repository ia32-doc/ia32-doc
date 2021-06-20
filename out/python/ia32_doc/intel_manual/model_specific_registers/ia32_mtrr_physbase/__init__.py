from future.utils import with_metaclass
from utils.ia32_struct import *
from utils.ia32_bit_field import *


__doc__ = """
@brief IA32_MTRR_PHYSBASE(n)

IA32_MTRR_PHYSBASE(0-9).

@see Vol3A[11.11.2.3(Variable Range MTRRs)]
"""


class Ia32MtrrPhysbaseRegister(with_metaclass(Ia32BitFieldMeta, Ia32BitField)):
    """
    
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super(Ia32MtrrPhysbaseRegister, self).__init__(value, byte_offset, byte_width, max_bytes=8)



    TYPE = Ia32BitFieldMember(
        "TYPE",
        """
        @brief Specifies the memory type for the range

Specifies the memory type for the range.
        """,

        0,
        8

    )


    PHYS_BASE = Ia32BitFieldMember(
        "PHYS_BASE",
        """
        @brief Specifies the base address of the address range.
This 24-bit value, in the case where MAXPHYADDR is 36 bits, is extended by 12 bits at the low end to form the
base address (this automatically aligns the address on a 4-KByte boundary)

Specifies the base address of the address range.
This 24-bit value, in the case where MAXPHYADDR is 36 bits, is extended by 12 bits at the low end to form the
base address (this automatically aligns the address on a 4-KByte boundary).
        """,

        12,
        36

    )


IA32_MTRR_PHYSBASE0 = 0x200


IA32_MTRR_PHYSBASE1 = 0x202


IA32_MTRR_PHYSBASE2 = 0x204


IA32_MTRR_PHYSBASE3 = 0x206


IA32_MTRR_PHYSBASE4 = 0x208


IA32_MTRR_PHYSBASE5 = 0x20a


IA32_MTRR_PHYSBASE6 = 0x20c


IA32_MTRR_PHYSBASE7 = 0x20e


IA32_MTRR_PHYSBASE8 = 0x210


IA32_MTRR_PHYSBASE9 = 0x212


