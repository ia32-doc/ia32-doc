from future.utils import with_metaclass
from ia32_python.utils.ia32_struct import *
from ia32_python.utils.ia32_bit_field import *


__doc__ = """
@brief Code- and Data-Segment Descriptor Types

When the S (descriptor type) flag in a segment descriptor is set, the descriptor is for either a code or a data
segment. The highest order bit of the type field (bit 11 of the second double word of the segment descriptor) then
determines whether the descriptor is for a data segment (clear) or a code segment (set).
For data segments, the three low-order bits of the type field (bits 8, 9, and 10) are interpreted as accessed (A),
write-enable (W), and expansion-direction (E). See Table 3-1 for a description of the encoding of the bits in the
type field for code and data segments. Data segments can be read-only or read/write segments, depending on the
setting of the write-enable bit.
"""


SEGMENT_DESCRIPTOR_TYPE_DATA_R = 0x0


SEGMENT_DESCRIPTOR_TYPE_DATA_RA = 0x1


SEGMENT_DESCRIPTOR_TYPE_DATA_RW = 0x2


SEGMENT_DESCRIPTOR_TYPE_DATA_RWA = 0x3


SEGMENT_DESCRIPTOR_TYPE_DATA_RE = 0x4


SEGMENT_DESCRIPTOR_TYPE_DATA_REA = 0x5


SEGMENT_DESCRIPTOR_TYPE_DATA_RWE = 0x6


SEGMENT_DESCRIPTOR_TYPE_DATA_RWEA = 0x7


SEGMENT_DESCRIPTOR_TYPE_CODE_E = 0x8


SEGMENT_DESCRIPTOR_TYPE_CODE_EA = 0x9


SEGMENT_DESCRIPTOR_TYPE_CODE_ER = 0xa


SEGMENT_DESCRIPTOR_TYPE_CODE_ERA = 0xb


SEGMENT_DESCRIPTOR_TYPE_CODE_EC = 0xc


SEGMENT_DESCRIPTOR_TYPE_CODE_ECA = 0xd


SEGMENT_DESCRIPTOR_TYPE_CODE_ERC = 0xe


SEGMENT_DESCRIPTOR_TYPE_CODE_ERCA = 0xf


