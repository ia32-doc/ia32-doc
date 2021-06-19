from future.utils import with_metaclass
from utils.bit_field import *


__doc__ = """
When CPUID executes with EAX set to 18H, the processor returns information about the Deterministic Address
Translation Parameters.
"""
CPUID_DETERMINISTIC_ADDRESS_TRANSLATION_PARAMETERS = 0x18

class CpuidEax18Ecx00(with_metaclass(BitFieldMeta, BitField)):
    """Deterministic Address Translation Parameters Main Leaf (EAX = 18H, ECX = 0)."""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=0)

    
    

class CpuidEax18Ecx01p(with_metaclass(BitFieldMeta, BitField)):
    """Deterministic Address Translation Parameters Sub-leaf (EAX = 18H, ECX  1)."""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=0)

    
    

CPUID_EXTENDED_FUNCTION = 0x80000000

class CpuidEax80000000(with_metaclass(BitFieldMeta, BitField)):
    """"""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=0)

    
    

CPUID_EXTENDED_CPU_SIGNATURE = 0x80000001

class CpuidEax80000001(with_metaclass(BitFieldMeta, BitField)):
    """"""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=0)

    
    

CPUID_BRAND_STRING1 = 0x80000002

CPUID_BRAND_STRING2 = 0x80000003

CPUID_BRAND_STRING3 = 0x80000004

class CpuidEax80000002(with_metaclass(BitFieldMeta, BitField)):
    """"""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=0)

    
    

class CpuidEax80000003(with_metaclass(BitFieldMeta, BitField)):
    """Extended Function CPUID Information."""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=0)

    
    

class CpuidEax80000004(with_metaclass(BitFieldMeta, BitField)):
    """Extended Function CPUID Information."""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=0)

    
    

class CpuidEax80000005(with_metaclass(BitFieldMeta, BitField)):
    """Extended Function CPUID Information."""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=0)

    
    

CPUID_EXTENDED_CACHE_INFO = 0x80000006

class CpuidEax80000006(with_metaclass(BitFieldMeta, BitField)):
    """"""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=0)

    
    

CPUID_EXTENDED_TIME_STAMP_COUNTER = 0x80000007

class CpuidEax80000007(with_metaclass(BitFieldMeta, BitField)):
    """"""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=0)

    
    

