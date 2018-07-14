# IA32-doc

IA32-doc is a project which aims to put as many definitions from the _Intel Manual_
into machine-processable format (in this case: **yaml**).

### Why?

Because such thing, as far as I know, does not exist. You can try to cherry-pick definitions
from [Linux source code][linux-source], [ReactOS][reactos-source],
[VirtualBox source code][virtualbox-source] or [EDK-II source code][edk-ii-source],
but you can expect limited set of definitions which are often poorly documented as a bonus.

### What is this good for?

**[For this](out/ia32.h)**. For your hobby OS. For your hobby hypervisor. For your experiments
with APIC, various MSRs, SGX, performance counters, you name it.

### FAQ

##### Are there definitions for 32-bit or 64-bit CPU?
Hopefully, both.

##### Are there definitions for AMD-specific stuff?
No, just Intel-specific stuff.

##### What sources did you use?
Mainly: _Intel® 64 and IA-32 architectures software developer’s manual combined volumes: 1, 2A, 2B, 2C, 2D, 3A, 3B, 3C, 3D,
and 4 **(May 2018)**_.

I've also took inspiration of various names/descriptions from other projects (VirtualBox, TianoCore).

##### Is any other output than C-header available?
No. Although, it shouldn't be that hard to extend the Python code to generate source code
in other programming languages.

##### What Python packages do I need?
Just **PyYAML**. And Python >= 3.7.

##### Who is going to maintain it?
Nobody. Maybe miracle happens and someone (or group of people) decide to fork this repo and maintain
it. Don't expect me to keep up with each release of Intel Manual, though. Although I may add
whatever I'm interested into at any moment.

##### What's in there?
Look into [yaml/Intel](yaml/Intel) directory. Currently there are transcribed:
- Control registers (CR0, CR3, CR4, CR8)
- CPUID for every EAX/ECX function found in current Intel Manual
- MSRs (Model Specific Registers)
- Segment descriptors (GDT/LDT/IDT/TSS)
- VMX-related definitions (VMCS)
- APIC
- EFLAGS

##### I don't like the use of UINT*/CamelCase/Doxygen, what should I do?
To change naming of integers, use `int_types` in [ia32doc/doc.py](ia32doc/doc.py).

To change anything related to the output file, you have to modify [`DocProcessor` class](ia32doc/processor.py).
I agree that application with command-line switches for this purpose would be awesome.

##### I'd like to add new yaml definitions, what should I do?
Look at [yaml/template.yml](yaml/template.yml) to better understand the format.
Also, by looking at other yaml files, you should get the idea.

### Notes and remarks
- First of all - at the end of the day, **you should ALWAYS consult the holy Intel Manual anyway**.
  Unconditionally. Seriously, once you get past _Hello world_ and decide to write your OS or hypervisor,
  there is no way you'll succeed without reading Intel Manual.
- There may be errors, typos, copy-paste errors in these _yaml_ transcriptions.
- I'm aware that there is lot of stuff missing here. I've mainly tried to transcribe what I personally
  desired.

### TODO
- ? OriginalNames - preserve case-sensitivity (BIOS, x2APIC, ToPA, ...)
- ? Add final Reserved field to bitfields
- ? Possibility to split into multiple .h
- ?? Add doxygen main page
- ??? Add AMD
- Find what else is missing
- Fix 32/64 bitfields for MSR registers
- Add possibility for bitfields to have both UINT32/UINT64 members
- EPT/PAGE_TABLEs

### License

All the code in this repository is open-source under the MIT license. see the **LICENSE.txt** file in this repository.


If you find this project interesting, you can buy me a coffee

```
  BTC 12hwTTPYDbkVqsfpGjrsVa7WpShvQn24ro
  LTC LLDVqnBEMS8Tv7ZF1otcy56HDhkXVVFJDH
```

   [linux-source]: <https://elixir.bootlin.com/linux/latest/source/arch/x86/include/asm/msr-index.h>
   [virtualbox-source]: <https://www.virtualbox.org/svn/vbox/trunk/include/iprt/x86.h>
   [edk-ii-source]: <https://github.com/tianocore/edk2/blob/master/UefiCpuPkg/Include/Register/ArchitecturalMsr.h>
   [reactos-source]: <https://doxygen.reactos.org/d9/d7c/ndk_2amd64_2ketypes_8h.html>
