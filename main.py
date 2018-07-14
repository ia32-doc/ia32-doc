from contextlib import redirect_stdout

from ia32doc.doc import Doc
from ia32doc.processor import DocProcessor


def main():
    processor = DocProcessor()

    doc_list = Doc.parse('yaml/Intel/index.yml')
    #doc_list = Doc.parse('yaml/Intel/CPUID/index.yml')
    #doc_list = Doc.parse('yaml/Intel/VMX/index.yml')

    with open('out/ia32.h', 'w') as f:
        with redirect_stdout(f):
            print(f'/** @file */')
            print(f'#pragma once')
            print(f'typedef unsigned char       UINT8;')
            print(f'typedef unsigned short      UINT16;')
            print(f'typedef unsigned int        UINT32;')
            print(f'typedef unsigned long long  UINT64;')
            print(f'')

            processor.process(doc_list)


if __name__ == '__main__':
    main()
