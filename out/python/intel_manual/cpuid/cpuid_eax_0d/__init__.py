from future.utils import with_metaclass
from utils.bit_field import *


__doc__ = """
When CPUID executes with EAX set to 0DH and ECX = 0, the processor returns information about the bit-vector
representation of all processor state extensions that are supported in the processor and storage size requirements
of the XSAVE/XRSTOR area.

When CPUID executes with EAX set to 0DH and ECX = n (n > 1, and is a valid sub-leaf index), the processor returns
information about the size and offset of each processor extended state save area within the XSAVE/XRSTOR area.
Software can use the forward-extendable technique depicted below to query the valid sub-leaves
and obtain size and offset information for each processor extended state save area:

<pre>
For i = 2 to 62 // sub-leaf 1 is reserved
  IF (CPUID.(EAX=0DH, ECX=0):VECTOR[i] = 1) // VECTOR is the 64-bit value of EDX:EAX
    Execute CPUID.(EAX=0DH, ECX = i) to examine size and offset for sub-leaf i;
  FI;
</pre>
"""
CPUID_EXTENDED_STATE = 0xd

class CpuidEax0dEcx00(with_metaclass(BitFieldMeta, BitField)):
    """Processor Extended State Enumeration Main Leaf (EAX = 0DH, ECX = 0)."""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=0)

    
    

class CpuidEax0dEcx01(with_metaclass(BitFieldMeta, BitField)):
    """Direct Cache Access Information Leaf."""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=0)

    
    

class CpuidEax0dEcxN(with_metaclass(BitFieldMeta, BitField)):
    """Processor Extended State Enumeration Sub-leaves (EAX = 0DH, ECX = n, n > 1)."""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=0)

    
    

