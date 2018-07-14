from __future__ import annotations
from typing import List, Tuple

import os
import re
import yaml

from .log import log

int_types_c = {
     8 : 'unsigned char',
    16 : 'unsigned short',
    32 : 'unsigned int',
    64 : 'unsigned long long',
}

int_types_cstdint = {
     8 : 'uint8_t',
    16 : 'uint16_t',
    32 : 'uint32_t',
    64 : 'uint64_t',
}

int_types_ms = {
     8 : 'UINT8',
    16 : 'UINT16',
    32 : 'UINT32',
    64 : 'UINT64',
}

int_types_ms2 = {
     8 : 'UCHAR',
    16 : 'USHORT',
    32 : 'ULONG',
    64 : 'ULONGLONG',
}

int_types = int_types_ms

DOC_VALID_TYPES = [
    'Group',
    'Definition',
    'Enum',
    'Struct',
    'StructField',
    'Bitfield',
    'BitfieldField',
]

'''
No processors supporting the Intel 64 architecture support more than 48 physical-address bits. Thus, no such processor can produce
a guest-physical address with more than 48 bits. An attempt to use such an address causes a page fault. An attempt to load
CR3 with such an address causes a general-protection fault. If PAE paging is being used, an attempt to load CR3 that would load a
PDPTE with such an address causes a general-protection fault.

(Vol3C[28.2.2(EPT Translation Mechanism)]
'''
MAXPHYADDR = 48


class Doc(object):
    doc_cache = { }

    @staticmethod
    def parse(path: str, parent: DocBase=None) -> List[DocBase]:
        log_message = f'Parsing "{path}"...' if not parent else \
                      f'Parsing "{path}" (included from "{parent.path}")...'

        if path in Doc.doc_cache:
            log_message += f'(cached)'
            log(log_message)

            doc_list = Doc.doc_cache[path]
        else:
            log(log_message)
            doc_list = yaml.load(open(path, encoding='utf-8').read())

            for doc in doc_list:
                doc['Path'] = path

            Doc.doc_cache[path] = doc_list

        return [ Doc.map_class(field, parent) for field in doc_list ]

    @staticmethod
    def map_class(doc: dict, parent: DocBase=None) -> DocBase:
        doc_base = DocBase(doc, parent)

        if doc_base.type == 'Group':
            #log(f'Processing group "{doc_base.short_name_standalone}"')
            return DocGroup(doc, parent)
        elif doc_base.type == 'Definition':
            return DocDefinition(doc, parent)
        elif doc_base.type == 'Struct':
            return DocStruct(doc, parent)
        elif doc_base.type == 'StructField':
            return DocStructField(doc, parent)
        elif doc_base.type == 'Bitfield':
            return DocBitfield(doc, parent)
        elif doc_base.type == 'BitfieldField':
            return DocBitfieldField(doc, parent)
        else:
            return doc_base


class DocBase(object):
    def __init__(self, doc: dict, parent: DocBase=None):
        self._doc = doc
        self._parent = parent
        self._fields = []
        self._include = []
        
        if 'Fields' in doc:
            self._fields = [ Doc.map_class(field, self) for field in doc['Fields'] ]

        if 'Include' in doc:
            self._include = doc['Include']

        self._do_include()

    @property
    def short_name(self) -> str:
        return self._fix_name(self.short_name_raw)

    @property
    def long_name(self) -> str:
        return self._fix_name(self.long_name_raw)

    @property
    def alternative_name(self) -> str:
        if 'AlternativeName' in self._doc:
            return self._make_name(self._doc['AlternativeName'])

        return ''

    @property
    def short_name_raw(self) -> str:
        return self._make_name(self.short_name_standalone)

    @property
    def short_name_standalone(self) -> str:
        if 'ShortName' in self._doc:
            return self._doc['ShortName']
        elif 'Name' in self._doc:
            return self._doc['Name']
        elif 'NameWithPostfix' in self._doc:
            if not self._parent:
                raise Exception('NameWithPostfix without parent')
            return f'{self._parent.short_name}_{self._doc["NameWithPostfix"]}'
        else:
            raise Exception('Field missing: short_name')

    @property
    def long_name_raw(self) -> str:
        return self._make_name(self.long_name_standalone)

    @property
    def long_name_standalone(self) -> str:
        if 'LongName' in self._doc:
            return self._doc['LongName']
        elif 'Name' in self._doc:
            return self._doc['Name']
        elif 'NameWithPostfix' in self._doc:
            if not self._parent:
                raise Exception('NameWithPostfix without parent')
            return f'{self._parent.long_name}_{self._doc["NameWithPostfix"]}'
        else:
            raise Exception('Field missing: long_name')

    @property
    def short_description(self) -> str:
        if 'ShortDescription' in self._doc:
            result = self._doc['ShortDescription']
        elif 'Description' in self._doc:
            result = self._doc['Description']
        else:
            result = ''

        return self._fix_description(result)

    @property
    def long_description(self) -> str:
        if 'LongDescription' in self._doc:
            result = self._doc['LongDescription']
        elif 'Description' in self._doc:
            result = self._doc['Description']
        else:
            result = ''

        return self._fix_description(result)

    @property
    def children_name_with_prefix(self) -> str:
        if 'ChildrenNameWithPrefix' in self._doc:
            if self._doc['ChildrenNameWithPrefix'] != '$':
                return self._doc['ChildrenNameWithPrefix']
            else:
                return self.short_name
        return ''

    @property
    def children_name_with_postfix(self) -> str:
        if 'ChildrenNameWithPostfix' in self._doc:
            if self._doc['ChildrenNameWithPostfix'] != '$':
                return self._doc['ChildrenNameWithPostfix']
            else:
                return self.short_name
        return ''

    @property
    def note(self) -> str:
        if 'Note' in self._doc:
            return self._doc['Note']
        return ''

    @property
    def access(self) -> str:
        if 'Access' in self._doc:
            return self._doc['Access']
        return ''

    @property
    def todo(self) -> str:
        if 'Todo' in self._doc:
            return self._doc['Todo']
        return ''

    @property
    def tag(self) -> str:
        if 'Tag' in self._doc:
            return self._doc['Tag']
        return ''

    @property
    def type(self) -> str:
        if 'Type' not in self._doc:
            if self._parent:
                if self._parent.type == 'Struct':
                    self._doc['Type'] = 'StructField'
                elif self._parent.type == 'Bitfield':
                    self._doc['Type'] = 'BitfieldField'
                else:
                    self._doc['Type'] = 'Definition'
            else:
                self._doc['Type'] = 'Definition'

        if 'Type' in self._doc and self._doc['Type'] in DOC_VALID_TYPES:
            return self._doc['Type']
        else:
            raise Exception('Invalid type')

    @property
    def alternative_type(self) -> str:
        if 'AlternativeType' in self._doc:
            return self._doc['AlternativeType']
        return self.type

    @property
    def remarks(self) -> str:
        if 'Remarks' in self._doc:
            return self._fix_description(self._doc['Remarks'])
        return ''

    @property
    def see_also(self) -> str:
        if 'SeeAlso' in self._doc:
            return self._doc['SeeAlso']
        return ''

    @property
    def reference(self) -> str:
        if 'Reference' in self._doc:
            return self._doc['Reference']
        return ''

    @property
    def fields(self) -> List[DocBase]:
        return self._fields

    @property
    def include(self) -> List[str]:
        return self._include

    @property
    def path(self) -> str:
        return self._doc['Path']

    def _make_name(self, name: str) -> str:
        if self.type in ['Definition', 'Struct', 'Bitfield']:
            parent = self._parent

            while parent:
                if parent.children_name_with_prefix:
                    name = f'{parent.children_name_with_prefix}_{name}'

                if parent.children_name_with_postfix:
                    name = f'{name}_{parent.children_name_with_postfix}'

                parent = parent._parent

        return name

    def _do_include(self) -> None:
        for include in self._include:
            file_path = os.path.join(os.path.dirname(self.path), include + '.yml')
            dir_path = os.path.join(os.path.dirname(self.path), include, 'index.yml')

            if os.path.isfile(file_path):
                doc_list = Doc.parse(file_path, self)
            elif os.path.isfile(dir_path):
                doc_list = Doc.parse(dir_path, self)
            else:
                doc_list = []

            for doc in doc_list:
                self._fields.append(doc)

    def _fix_name(self, name: str) -> str:
        result = name

        if self.type in ['Group', 'Struct', 'Bitfield']:
            #
            # Remove everything between '(' and ')' characters.
            #
            result = re.sub(r'\([^)]*\)', '', result)

            #
            # Remove all consecutive '_' characters.
            #
            result = re.sub(r'[_]{2,}', '_', result)
        else:
            #
            # Replace every occurence of (xXxX) with uppercase XXXX.
            #
            result = re.sub(r'\(([^)]*)\)', r'\1', result)
            result = result.upper()

        return result

    @staticmethod
    def _fix_description(description: str) -> str:
        result = description

        #
        # Escape '#' characters (which do not start with '-').
        # '-#' are numbered lists.
        #
        result = re.sub(r'([^-])#', r'\1\#', result)

        return result


class DocGroup(DocBase):
    def __init__(self, doc: dict, parent: DocBase=None):
        super().__init__(doc, parent)


class DocDefinition(DocBase):
    def __init__(self, doc: dict, parent: DocBase=None):
        super().__init__(doc, parent)

    @property
    def value(self) -> str:
        try:
            return self._doc['Value']
        except:
            pass


class DocStruct(DocBase):
    def __init__(self, doc: dict, parent: DocBase=None):
        super().__init__(doc, parent)


class DocStructField(DocBase):
    def __init__(self, doc: dict, parent: DocBase=None):
        super().__init__(doc, parent)

    @property
    def size(self) -> int:
        return self._doc['Size']

    @property
    def size_type(self) -> str:
        return int_types[self.size]


class DocBitfield(DocBase):
    def __init__(self, doc: dict, parent: DocBase=None):
        super().__init__(doc, parent)

    @property
    def size_min(self):
        if isinstance(self._doc['Size'], int):
            return self._doc['Size']
        else:
            return self._doc['Size'][0]

    @property
    def size_max(self):
        if isinstance(self._doc['Size'], int):
            return self._doc['Size']
        else:
            return self._doc['Size'][1]

    @property
    def size(self) -> int:
        return self.size_max

    @property
    def size_type_min(self) -> str:
        return int_types[self.size_min]

    @property
    def size_type_max(self) -> str:
        return int_types[self.size_max]

    @property
    def size_type(self) -> str:
        return int_types[self.size]


class DocBitfieldField(DocBase):
    def __init__(self, doc: dict, parent: DocBase=None):
        super().__init__(doc, parent)

    @property
    def bit(self) -> Tuple[int, int]:
        if isinstance(self._doc['Bit'], int):
            bit_from, bit_to = self._doc['Bit'], self._doc['Bit'] + 1
        else:
            doc_bit = self._doc['Bit']
            if 'MAXPHYADDR' in doc_bit:
                doc_bit = doc_bit.replace('(MAXPHYADDR-1)', f'{MAXPHYADDR - 1}')

            bit_from, bit_to = list(map(int, doc_bit.split('-')))
            bit_to += 1

        return bit_from, bit_to


