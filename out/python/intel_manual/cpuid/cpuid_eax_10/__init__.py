from future.utils import with_metaclass
from utils.bit_field import *


__doc__ = """
When CPUID executes with EAX set to 10H and ECX = 0, the processor returns information about the bit-vector
representation of QoS Enforcement resource types that are supported in the processor. Each bit, starting from bit
1, corresponds to a specific resource type if the bit is set. The bit position corresponds to the sub-leaf index (or
ResID) that software must use to query QoS enforcement capability available for that type.

When CPUID executes with EAX set to 10H and ECX = n (n >= 1, and is a valid ResID), the processor returns information
about available classes of service and range of QoS mask MSRs that software can use to configure each
class of services using capability bit masks in the QoS Mask registers, IA32_resourceType_Mask_n.
"""
CPUID_INTEL_RDT_ALLOCATION = 0x10

class CpuidEax10Ecx00(with_metaclass(BitFieldMeta, BitField)):
    """Intel Resource Director Technology (Intel RDT) Allocation Enumeration Sub-leaf (EAX = 10H, ECX = 0)."""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=0)

    
    

class CpuidEax10Ecx01(with_metaclass(BitFieldMeta, BitField)):
    """L3 Cache Allocation Technology Enumeration Sub-leaf (EAX = 10H, ECX = ResID = 1)."""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=0)

    
    

class CpuidEax10Ecx02(with_metaclass(BitFieldMeta, BitField)):
    """L2 Cache Allocation Technology Enumeration Sub-leaf (EAX = 10H, ECX = ResID = 2)."""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=0)

    
    

class CpuidEax10Ecx03(with_metaclass(BitFieldMeta, BitField)):
    """Memory Bandwidth Allocation Enumeration Sub-leaf (EAX = 10H, ECX = ResID = 3)."""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=0)

    
    

