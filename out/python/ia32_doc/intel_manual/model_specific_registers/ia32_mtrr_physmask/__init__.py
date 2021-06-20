from future.utils import with_metaclass
from utils.struct import *
from utils.bit_field import *


__doc__ = """
@brief IA32_MTRR_PHYSMASK(n)

IA32_MTRR_PHYSMASK(0-9).

@see Vol3A[11.11.2.3(Variable Range MTRRs)]
"""


class Ia32MtrrPhysmaskRegister(with_metaclass(BitFieldMeta, BitField)):
    """
    
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super(Ia32MtrrPhysmaskRegister, self).__init__(value, byte_offset, byte_width, max_bytes=8)



    TYPE = BitFieldMember(
        "TYPE",
        """
        @brief Specifies the memory type for the range

Specifies the memory type for the range.
        """,

        0,
        8

    )


    VALID = BitFieldMember(
        "VALID",
        """
        @brief Enables the register pair when set; disables register pair when clear

Enables the register pair when set; disables register pair when clear.
        """,

        11,
        1

    )


    PHYS_MASK = BitFieldMember(
        "PHYS_MASK",
        """
        @brief Specifies a mask (24 bits if the maximum physical
address size is 36 bits, 28 bits if the maximum physical address size is 40 bits). The mask determines the range
of the region being mapped, according to the following relationships:

- Address_Within_Range AND PhysMask = PhysBase AND PhysMask

- This value is extended by 12 bits at the low end to form the mask value.

- The width of the PhysMask field depends on the maximum physical address size supported by the
processor.

CPUID.80000008H reports the maximum physical address size supported by the processor. If
CPUID.80000008H is not available, software may assume that the processor supports a 36-bit physical
address size

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

@see Vol3A[11.11.3(Example Base and Mask Calculations)]
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


