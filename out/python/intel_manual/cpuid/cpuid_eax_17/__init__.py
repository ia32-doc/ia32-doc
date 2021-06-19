from future.utils import with_metaclass
from utils.bit_field import *


__doc__ = """
When CPUID executes with EAX set to 17H, the processor returns information about the System-On-Chip Vendor
Attribute Enumeration.
"""
CPUID_SOC_VENDOR = 0x17

class CpuidEax17Ecx00(with_metaclass(BitFieldMeta, BitField)):
    """System-On-Chip Vendor Attribute Enumeration Main Leaf (EAX = 17H, ECX = 0)."""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=0)

    
    

class CpuidEax17Ecx0103(with_metaclass(BitFieldMeta, BitField)):
    """System-On-Chip Vendor Attribute Enumeration Sub-leaf (EAX = 17H, ECX = 1..3)."""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=0)

    
    

class CpuidEax17EcxN(with_metaclass(BitFieldMeta, BitField)):
    """System-On-Chip Vendor Attribute Enumeration Sub-leaves (EAX = 17H, ECX > MaxSOCID_Index)."""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=0)

    
    

