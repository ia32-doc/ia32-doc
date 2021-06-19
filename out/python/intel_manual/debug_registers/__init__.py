description = """
Eight debug registers control the debug
operation of the processor. These registers can be written to and read using the move to/from debug register form
of the MOV instruction. A debug register may be the source or destination operand for one of these instructions.

Debug registers are privileged resources; a MOV instruction that accesses these registers can only be executed in
real-address mode, in SMM or in protected mode at a CPL of 0. An attempt to read or write the debug registers
from any other privilege level generates a general-protection exception (\#GP).
The primary function of the debug registers is to set up and monitor from 1 to 4 breakpoints, numbered 0 though
3. For each breakpoint, the following information can be specified:

- The linear address where the breakpoint is to occur.

- The length of the breakpoint location: 1, 2, 4, or 8 bytes.

- The operation that must be performed at the address for a debug exception to be generated.

- Whether the breakpoint is enabled.

- Whether the breakpoint condition was present when the debug exception was generated.
"""

from .dr6 import *
from .dr7 import *



__all__ = [
    
        "dr6",
        "dr7",
]