from future.utils import with_metaclass
from utils.bit_field import *


__doc__ = """
IA32_MTRR_PHYSMASK(0-9).
"""
class Ia32MtrrPhysmaskRegister(with_metaclass(BitFieldMeta, BitField)):
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

    
    VALID = BitFieldMember(
        "VALID",
        """
        Enables the register pair when set; disables register pair when clear:
        Enables the register pair when set; disables register pair when clear.
        """,
        11,
        1
    )

    
    PHYS_MASK = BitFieldMember(
        "PHYS_MASK",
        """
        Specifies a mask (24 bits if the maximum physical
address size is 36 bits, 28 bits if the maximum physical address size is 40 bits). The mask determines the range
of the region being mapped, according to the following relationships:

- Address_Within_Range AND PhysMask = PhysBase AND PhysMask

- This value is extended by 12 bits at the low end to form the mask value.

- The width of the PhysMask field depends on the maximum physical address size supported by the
processor.

CPUID.80000008H reports the maximum physical address size supported by the processor. If
CPUID.80000008H is not available, software may assume that the processor supports a 36-bit physical
address size:
        Specifies a mask (24 bits if the maximum physical
address size is 36 bits, 28 bits if the maximum physical address size is 40 bits). The mask determines the range
of the region being mapped, according to the following relationships:

- Address_Within_Range AND PhysMask = PhysBase AND PhysMask

- This value is extended by 12 bits at the low end to form the mask value.

- The width of the PhysMask field depends on the maximum physical address size supported by the
processor.

CPUID.80000008H reports the maximum physical address size supported by the processor. If
CPUID.80000008H is not available, software may assume that the processor supports a 36-bit physical
address size.
        """,
        12,
        36
    )

    

IA32_MTRR_PHYSMASK0 = 0x201

IA32_MTRR_PHYSMASK1 = 0x203

IA32_MTRR_PHYSMASK2 = 0x205

IA32_MTRR_PHYSMASK3 = 0x207

IA32_MTRR_PHYSMASK4 = 0x209

IA32_MTRR_PHYSMASK5 = 0x20b

IA32_MTRR_PHYSMASK6 = 0x20d

IA32_MTRR_PHYSMASK7 = 0x20f

IA32_MTRR_PHYSMASK8 = 0x211

IA32_MTRR_PHYSMASK9 = 0x213

