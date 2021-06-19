from future.utils import with_metaclass
from utils.bit_field import *


__doc__ = """
Bits (64*n+63):(64*n) of the
SHA256 digest of the SIGSTRUCT.MODULUS for SGX Launch Enclave. On reset, the
default value is the digest of Intels signing key.
"""
IA32_SGXLEPUBKEYHASH0 = 0x8c

IA32_SGXLEPUBKEYHASH1 = 0x8d

IA32_SGXLEPUBKEYHASH2 = 0x8e

IA32_SGXLEPUBKEYHASH3 = 0x8f

IA32_SMM_MONITOR_CTL = 0x9b

class Ia32MsegHeader(with_metaclass(BitFieldMeta, BitField)):
    """"""

    

    def __init__(self, value):
        super().__init__(value, size_in_bytes=32)

    
    
    MSEG_HEADER_REVISION = BitFieldMember(
        "MSEG_HEADER_REVISION",
        """
        MSEG revision identifier:
        Different processors may use different MSEG revision identifiers.
These identifiers enable software to avoid using an MSEG header formatted for one processor on a
processor that uses a different format. Software can discover the MSEG revision identifier that a processor uses
by reading the VMX capability MSR IA32_VMX_MISC.
        """,
        0,
        32
        
    )

    
    MONITOR_FEATURES = BitFieldMember(
        "MONITOR_FEATURES",
        """
        SMM-transfer monitor features field:
        Bits 31:1 of this field are reserved and must be
zero. Bit 0 of the field is the IA-32e mode SMM feature bit. It indicates whether the logical processor will be
in IA-32e mode after the STM is activated.
        """,
        32,
        32
        
    )

    
    GDTR_LIMIT = BitFieldMember(
        "GDTR_LIMIT",
        """
        Fields that determine how processor state is loaded when the STM is activated.
SMM code should establish these fields so that activating of the STM invokes the STMs initialization
code:
        Fields that determine how processor state is loaded when the STM is activated.
SMM code should establish these fields so that activating of the STM invokes the STMs initialization
code.
        """,
        64,
        32
        
    )

    
    GDTR_BASE_OFFSET = BitFieldMember(
        "GDTR_BASE_OFFSET",
        """
        :
        
        """,
        96,
        32
        
    )

    
    CS_SELECTOR = BitFieldMember(
        "CS_SELECTOR",
        """
        :
        
        """,
        128,
        32
        
    )

    
    EIP_OFFSET = BitFieldMember(
        "EIP_OFFSET",
        """
        :
        
        """,
        160,
        32
        
    )

    
    ESP_OFFSET = BitFieldMember(
        "ESP_OFFSET",
        """
        :
        
        """,
        192,
        32
        
    )

    
    CR3_OFFSET = BitFieldMember(
        "CR3_OFFSET",
        """
        :
        
        """,
        224,
        32
        
    )

    

IA32_SMBASE = 0x9e

