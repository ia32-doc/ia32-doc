from future.utils import with_metaclass
from utils.struct import *
from utils.bit_field import *


__doc__ = """
@brief IA32_MC(i)_CTL2

MSR to enable/disable CMCI capability for bank n.

@see Vol3B[15.3.2.5(IA32_MCi_CTL2 MSRs)]
"""


IA32_MC0_CTL2 = 0x280


IA32_MC1_CTL2 = 0x281


IA32_MC2_CTL2 = 0x282


IA32_MC3_CTL2 = 0x283


IA32_MC4_CTL2 = 0x284


IA32_MC5_CTL2 = 0x285


IA32_MC6_CTL2 = 0x286


IA32_MC7_CTL2 = 0x287


IA32_MC8_CTL2 = 0x288


IA32_MC9_CTL2 = 0x289


IA32_MC10_CTL2 = 0x28a


IA32_MC11_CTL2 = 0x28b


IA32_MC12_CTL2 = 0x28c


IA32_MC13_CTL2 = 0x28d


IA32_MC14_CTL2 = 0x28e


IA32_MC15_CTL2 = 0x28f


IA32_MC16_CTL2 = 0x290


IA32_MC17_CTL2 = 0x291


IA32_MC18_CTL2 = 0x292


IA32_MC19_CTL2 = 0x293


IA32_MC20_CTL2 = 0x294


IA32_MC21_CTL2 = 0x295


IA32_MC22_CTL2 = 0x296


IA32_MC23_CTL2 = 0x297


IA32_MC24_CTL2 = 0x298


IA32_MC25_CTL2 = 0x299


IA32_MC26_CTL2 = 0x29a


IA32_MC27_CTL2 = 0x29b


IA32_MC28_CTL2 = 0x29c


IA32_MC29_CTL2 = 0x29d


IA32_MC30_CTL2 = 0x29e


IA32_MC31_CTL2 = 0x29f


class Ia32McCtl2Register(with_metaclass(BitFieldMeta, BitField)):
    """
    
    """
    def __init__(self, value=0, byte_offset=None, byte_width=None):
        super().__init__(value, byte_offset, byte_width, max_bytes=8)



    CORRECTED_ERROR_COUNT_THRESHOLD = BitFieldMember(
        "CORRECTED_ERROR_COUNT_THRESHOLD",
        """
        @brief Corrected error count threshold

Corrected error count threshold.
        """,

        0,
        15

    )


    CMCI_EN = BitFieldMember(
        "CMCI_EN",
        """
        @brief CMCI_EN

CMCI_EN.
        """,

        30,
        1

    )


IA32_MTRR_DEF_TYPE = 0x2ff


