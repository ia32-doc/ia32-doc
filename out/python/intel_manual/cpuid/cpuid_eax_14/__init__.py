from future.utils import with_metaclass
from utils.bit_field import *


__doc__ = """
When CPUID executes with EAX set to 14H and ECX = 0H, the processor returns information about Intel Processor
Trace extensions.

When CPUID executes with EAX set to 14H and ECX = n (n > 0 and less than the number of non-zero bits in
CPUID.(EAX=14H, ECX= 0H).EAX), the processor returns information about packet generation in Intel Processor
Trace.
"""
CPUID_INTEL_PROCESSOR_TRACE = 0x14

class CpuidEax14Ecx00(with_metaclass(BitFieldMeta, BitField)):
    """Intel Processor Trace Enumeration Main Leaf (EAX = 14H, ECX = 0)."""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=0)

    
    

class CpuidEax14Ecx01(with_metaclass(BitFieldMeta, BitField)):
    """Intel Processor Trace Enumeration Sub-leaf (EAX = 14H, ECX = 1)."""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=0)

    
    

CPUID_TIME_STAMP_COUNTER = 0x15

class CpuidEax15(with_metaclass(BitFieldMeta, BitField)):
    """"""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=0)

    
    

CPUID_PROCESSOR_FREQUENCY = 0x16

class CpuidEax16(with_metaclass(BitFieldMeta, BitField)):
    """"""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=0)

    
    

