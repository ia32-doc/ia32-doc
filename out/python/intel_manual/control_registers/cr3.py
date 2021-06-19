from utils.bit_field import BitField

class Cr3(BitField):
    """"""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=8)

    _FIELDS = ["PWT","PCD","PD_PHYS_ADDR",]

    
    @property
    def PWT(self):
        """
        Page-level Write-Through
        Controls the memory type used to access the first paging
structure of the current paging-structure hierarchy. This bit is not used if paging is disabled,
with PAE paging, or with 4-level paging if CR4.PCIDE=1.
        """
        return self[3:4]

    @PWT.setter
    def PWT(self, value):
        self[3:4] = value
    
    @property
    def PCD(self):
        """
        Page-level Cache Disable
        Controls the memory type used to access the first paging
structure of the current paging-structure hierarchy. This bit is not used if paging is disabled,
with PAE paging, or with 4-level paging2 if CR4.PCIDE=1.
        """
        return self[4:5]

    @PCD.setter
    def PCD(self, value):
        self[4:5] = value
    
    @property
    def PD_PHYS_ADDR(self):
        """
        Address of page directory
        Physical address of the 4-KByte aligned page directory (32-bit paging) or PML4 table (64-bit paging)
used for linear-address translation.
        """
        return self[12:48]

    @PD_PHYS_ADDR.setter
    def PD_PHYS_ADDR(self, value):
        self[12:48] = value
    