from future.utils import with_metaclass
from utils.bit_field import *


__doc__ = """
The processor allows any area of system memory to be cached in the L1, L2, and L3 caches. In individual pages or
regions of system memory, it allows the type of caching (also called memory type) to be specified.
"""
MEMORY_TYPE_UC = 0x0

MEMORY_TYPE_WC = 0x1

MEMORY_TYPE_WT = 0x4

MEMORY_TYPE_WP = 0x5

MEMORY_TYPE_WB = 0x6

MEMORY_TYPE_UC_MINUS = 0x7

MEMORY_TYPE_INVALID = 0xff

