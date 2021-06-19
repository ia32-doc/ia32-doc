from future.utils import with_metaclass
from utils.bit_field import *


__doc__ = """

"""
CPUID_SIGNATURE = 0x0

class CpuidEax00(with_metaclass(BitFieldMeta, BitField)):
    """"""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=16)

    
    
    MAXCPUIDINPUT = BitFieldMember(
        "MAXCPUIDINPUT",
        """
        EAX:
        Maximum Input Value for Basic CPUID Information.
        """,
        0,
        32
        
    )

    
    VALUEGENU = BitFieldMember(
        "VALUEGENU",
        """
        EBX:
        Genu
        """,
        32,
        32
        
    )

    
    VALUENTEL = BitFieldMember(
        "VALUENTEL",
        """
        ECX:
        ntel
        """,
        64,
        32
        
    )

    
    VALUEINEI = BitFieldMember(
        "VALUEINEI",
        """
        EDX:
        ineI
        """,
        96,
        32
        
    )

    

CPUID_VERSION_INFO = 0x1

class CpuidEax01(with_metaclass(BitFieldMeta, BitField)):
    """"""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=0)

    
    

CPUID_CACHE_PARAMS = 0x4

class CpuidEax04(with_metaclass(BitFieldMeta, BitField)):
    """"""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=0)

    
    

CPUID_MONITOR_MWAIT = 0x5

class CpuidEax05(with_metaclass(BitFieldMeta, BitField)):
    """"""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=0)

    
    

CPUID_THERMAL_POWER_MANAGEMENT = 0x6

class CpuidEax06(with_metaclass(BitFieldMeta, BitField)):
    """"""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=0)

    
    

CPUID_STRUCTURED_EXTENDED_FEATURE_FLAGS = 0x7

class CpuidEax07(with_metaclass(BitFieldMeta, BitField)):
    """"""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=0)

    
    

CPUID_DIRECT_CACHE_ACCESS_INFO = 0x9

class CpuidEax09(with_metaclass(BitFieldMeta, BitField)):
    """"""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=0)

    
    

CPUID_ARCHITECTURAL_PERFORMANCE_MONITORING = 0xa

class CpuidEax0a(with_metaclass(BitFieldMeta, BitField)):
    """"""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=0)

    
    

CPUID_EXTENDED_TOPOLOGY = 0xb

class CpuidEax0b(with_metaclass(BitFieldMeta, BitField)):
    """"""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=0)

    
    

