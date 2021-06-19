from future.utils import with_metaclass
from utils.bit_field import *


__doc__ = """
IA32_MTRR_PHYSBASE(0-9).
"""
class Ia32MtrrPhysbaseRegister(with_metaclass(BitFieldMeta, BitField)):
    """"""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=8)


    
    TYPE = BitFieldMember(
        "TYPE",
        """
        Specifies the memory type for the range:
        Specifies the memory type for the range.
        """,
        0,
        8
    )

    
    PHYS_BASE = BitFieldMember(
        "PHYS_BASE",
        """
        Specifies the base address of the address range.
This 24-bit value, in the case where MAXPHYADDR is 36 bits, is extended by 12 bits at the low end to form the
base address (this automatically aligns the address on a 4-KByte boundary):
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

