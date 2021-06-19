from future.utils import with_metaclass
from utils.bit_field import *


__doc__ = """
Capability Reporting Register of Pin-Based VM-Execution Flex Controls,
Primary Processor-Based VM-Execution Flex Controls,
VM-Exit Flex Controls and VM-Entry Flex Controls.
"""
IA32_VMX_TRUE_PINBASED_CTLS = 0x48d

IA32_VMX_TRUE_PROCBASED_CTLS = 0x48e

IA32_VMX_TRUE_EXIT_CTLS = 0x48f

IA32_VMX_TRUE_ENTRY_CTLS = 0x490

class Ia32VmxTrueCtlsRegister(with_metaclass(BitFieldMeta, BitField)):
    """"""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=8)


    
    ALLOWED_0_SETTINGS = BitFieldMember(
        "ALLOWED_0_SETTINGS",
        """
        Indicate the allowed 0-settings of these controls. VM entry allows control X to be 0 if
bit X in the MSR is cleared to 0; if bit X in the MSR is set to 1, VM entry fails if
control X is 0:
        Indicate the allowed 0-settings of these controls. VM entry allows control X to be 0 if
bit X in the MSR is cleared to 0; if bit X in the MSR is set to 1, VM entry fails if
control X is 0.
        """,
        0,
        32
    )

    
    ALLOWED_1_SETTINGS = BitFieldMember(
        "ALLOWED_1_SETTINGS",
        """
        Indicate the allowed 1-settings of these controls. VM entry allows control X to be 1 if bit 32+X in
the MSR is set to 1; if bit 32+X in the MSR is cleared to 0, VM entry fails if control X is 1:
        Indicate the allowed 1-settings of these controls. VM entry allows control X to be 1 if bit 32+X in
the MSR is set to 1; if bit 32+X in the MSR is cleared to 0, VM entry fails if control X is 1.
        """,
        32,
        32
    )

    

IA32_VMX_VMFUNC = 0x491

