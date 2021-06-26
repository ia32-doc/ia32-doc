from future.utils import with_metaclass
from ia32_python.utils.ia32_struct import *
from ia32_python.utils.ia32_enum import *
from ia32_python.utils.ia32_bit_field import *


__doc__ = """
@brief Paging structures entry counts

Paging structures entry counts.
"""


PML4_ENTRY_COUNT_64 = 0x200


PDPTE_ENTRY_COUNT_64 = 0x200


PDE_ENTRY_COUNT_64 = 0x200


PTE_ENTRY_COUNT_64 = 0x200


