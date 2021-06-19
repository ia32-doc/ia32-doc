from utils.bit_field import BitField

class Cr8(BitField):
    """"""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=8)

    _FIELDS = ["TPL","RESERVED",]

    
    @property
    def TPL(self):
        """
        Task Priority Level
        This sets the threshold value corresponding to the highestpriority
interrupt to be blocked. A value of 0 means all interrupts are enabled. This field is available in 64-
bit mode. A value of 15 means all interrupts will be disabled.
        """
        return self[0:4]

    @TPL.setter
    def TPL(self, value):
        self[0:4] = value
    
    @property
    def RESERVED(self):
        """
        Reserved
        Reserved and must be written with zeros. Failure to do this causes a general-protection exception.
        """
        return self[4:64]

    @RESERVED.setter
    def RESERVED(self, value):
        self[4:64] = value
    