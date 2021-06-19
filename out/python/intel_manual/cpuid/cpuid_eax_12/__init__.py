from future.utils import with_metaclass
from utils.bit_field import *


__doc__ = """
When CPUID executes with EAX set to 12H and ECX = 0H, the processor returns information about Intel SGX capabilities.

When CPUID executes with EAX set to 12H and ECX = 1H, the processor returns information about Intel SGX attributes.

When CPUID executes with EAX set to 12H and ECX = n (n > 1), the processor returns information about Intel SGX
Enclave Page Cache.
"""
CPUID_INTEL_SGX = 0x12

class CpuidEax12Ecx00(with_metaclass(BitFieldMeta, BitField)):
    """Intel SGX Capability Enumeration Leaf, sub-leaf 0 (EAX = 12H, ECX = 0)."""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=0)

    
    

class CpuidEax12Ecx01(with_metaclass(BitFieldMeta, BitField)):
    """Intel SGX Attributes Enumeration Leaf, sub-leaf 1 (EAX = 12H, ECX = 1)."""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=0)

    
    

class CpuidEax12Ecx02pSlt0(with_metaclass(BitFieldMeta, BitField)):
    """Intel SGX EPC Enumeration Leaf, sub-leaves (EAX = 12H, ECX = 2 or higher)."""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=0)

    
    

class CpuidEax12Ecx02pSlt1(with_metaclass(BitFieldMeta, BitField)):
    """Intel SGX EPC Enumeration Leaf, sub-leaves (EAX = 12H, ECX = 2 or higher)."""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=0)

    
    

