from __future__ import annotations
from typing import List, Tuple

import os
import re
import sys
import yaml

from .text import DocTextCase

DOC_GROUP           = 'group'
DOC_DEFINITION      = 'definition'
DOC_ENUM            = 'enum'
DOC_ENUM_FIELD      = 'enum_field'
DOC_STRUCT          = 'struct'
DOC_STRUCT_FIELD    = 'struct_field'
DOC_BITFIELD        = 'bitfield'
DOC_BITFIELD_FIELD  = 'bitfield_field'

DOC_TYPES = [
    DOC_GROUP,
    DOC_DEFINITION,
    DOC_ENUM,
    DOC_ENUM_FIELD,
    DOC_STRUCT,
    DOC_STRUCT_FIELD,
    DOC_BITFIELD,
    DOC_BITFIELD_FIELD,
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
        if path in Doc.doc_cache:
            doc_list = Doc.doc_cache[path]
        else:
            print(f'Parsing "{path}"...', file=sys.stderr)
            doc_list = yaml.load(open(path, encoding='utf-8').read())

            for doc in doc_list:
                doc['path'] = path

            Doc.doc_cache[path] = doc_list

        return [ Doc.map_class(field, parent) for field in doc_list ]

    @staticmethod
    def map_class(doc: dict, parent: DocBase=None) -> DocBase:
        doc_base = DocBase(doc, parent)
        return globals()[f'Doc{DocTextCase.to_camel_case(doc_base.type)}'](doc, parent)


class DocBase(object):
    REQUIRED_NAME = True

    def __init__(self, doc: dict, parent: DocBase=None):
        self._doc = doc
        self._fields = []
        self._include = []

        self.parent = parent

        if 'fields' in doc:
            self._fields = [ Doc.map_class(field, self) for field in doc['fields'] ]

        if 'include' in doc:
            self._include = doc['include']

        self._do_include()

    def __repr__(self):
        return f'[{self.short_name} ({self.type})]'

    @property
    def short_name(self) -> str:
        return self._fix_name(self.short_name_raw)

    @property
    def long_name(self) -> str:
        return self._fix_name(self.long_name_raw)

    @property
    def alternative_name(self) -> str:
        if 'alternative_name' in self._doc:
            return self._make_name(self._doc['alternative_name'])

        return ''

    @property
    def short_name_raw(self) -> str:
        return self._make_name(self.short_name_standalone)

    @property
    def short_name_standalone(self) -> str:
        if 'short_name' in self._doc:
            return self._doc['short_name']
        elif 'name' in self._doc:
            return self._doc['name']
        elif 'name_with_suffix' in self._doc:
            if not self.parent:
                raise Exception('name_with_suffix without parent')
            return f'{self.parent.short_name}_{self._doc["name_with_suffix"]}'
        else:
            if self.REQUIRED_NAME:
                raise Exception('Field missing: short_name')
            else:
                return ''

    @property
    def long_name_raw(self) -> str:
        return self._make_name(self.long_name_standalone)

    @property
    def long_name_standalone(self) -> str:
        if 'long_name' in self._doc:
            return self._doc['long_name']
        elif 'name' in self._doc:
            return self._doc['name']
        elif 'name_with_suffix' in self._doc:
            if not self.parent:
                raise Exception('name_with_suffix without parent')
            return f'{self.parent.long_name}_{self._doc["name_with_suffix"]}'
        else:
            if self.REQUIRED_NAME:
                raise Exception('Field missing: long_name')
            else:
                return ''

    @property
    def short_description(self) -> str:
        return self.short_description_raw.rstrip().rstrip('.')

    @property
    def long_description(self) -> str:
        return self.long_description_raw.rstrip()

    @property
    def short_description_raw(self) -> str:
        if 'short_description' in self._doc:
            result = self._doc['short_description']
        elif 'description' in self._doc:
            result = self._doc['description']
        else:
            result = ''

        return self._fix_description(result)

    @property
    def long_description_raw(self) -> str:
        if 'long_description' in self._doc:
            result = self._doc['long_description']
        elif 'description' in self._doc:
            result = self._doc['description']
        else:
            result = ''

        return self._fix_description(result)

    @property
    def children_name_with_prefix(self) -> str:
        if 'children_name_with_prefix' in self._doc:
            if self._doc['children_name_with_prefix'] != '$':
                return self._doc['children_name_with_prefix']
            else:
                return self.short_name
        return ''

    @property
    def children_name_with_suffix(self) -> str:
        if 'children_name_with_suffix' in self._doc:
            if self._doc['children_name_with_suffix'] != '$':
                return self._doc['children_name_with_suffix']
            else:
                return self.short_name
        return ''

    @property
    def note(self) -> str:
        if 'note' in self._doc:
            return self._doc['note']
        return ''

    @property
    def access(self) -> str:
        if 'access' in self._doc:
            return self._doc['access']
        return ''

    @property
    def todo(self) -> str:
        if 'todo' in self._doc:
            return self._doc['todo']
        return ''

    @property
    def tag(self) -> str:
        if 'tag' in self._doc:
            return self._doc['tag']
        return ''

    @property
    def type(self) -> str:
        if 'type' not in self._doc:
            if self.parent:
                if self.parent.type == DOC_ENUM:
                    self._doc['type'] = DOC_ENUM_FIELD
                elif self.parent.type == DOC_STRUCT and 'size' in self._doc:
                    self._doc['type'] = DOC_STRUCT_FIELD
                elif self.parent.type == DOC_BITFIELD and 'bit' in self._doc:
                    self._doc['type'] = DOC_BITFIELD_FIELD
                else:
                    self._doc['type'] = DOC_DEFINITION
            else:
                self._doc['type'] = DOC_DEFINITION

        if 'type' in self._doc and self._doc['type'] in DOC_TYPES:
            return self._doc['type']
        else:
            raise Exception('Invalid type')

    @property
    def alternative_type(self) -> str:
        if 'alternative_type' in self._doc:
            return self._doc['alternative_type']
        return self.type

    @property
    def remarks(self) -> str:
        if 'remarks' in self._doc:
            return self._fix_description(self._doc['remarks'])
        return ''

    @property
    def see(self) -> str:
        if 'see' in self._doc:
            return self._doc['see']
        return ''

    @property
    def reference(self) -> str:
        if 'reference' in self._doc:
            return self._doc['reference']
        return ''

    @property
    def fields(self) -> List[DocBase]:
        return self._fields

    @property
    def include(self) -> List[str]:
        return self._include

    @property
    def path(self) -> str:
        return self._doc['path']

    def _make_name(self, name: str) -> str:
        candidate_types_for_affix = [ DOC_DEFINITION, DOC_GROUP, DOC_STRUCT, DOC_BITFIELD, DOC_ENUM, DOC_ENUM_FIELD ]
        if 'name_with_suffix' not in self._doc and self.type in candidate_types_for_affix:
            parent = self.parent

            while parent:
                if parent.children_name_with_prefix:
                    name = f'{parent.children_name_with_prefix}_{name}'

                if parent.children_name_with_suffix:
                    name = f'{name}_{parent.children_name_with_suffix}'

                parent = parent.parent

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
                doc_list = []  # raise Exception(f'Path {self.path} not found')

            for doc in doc_list:
                self._fields.append(doc)

    def _fix_name(self, name: str) -> str:
        result = name

        if self.type in ['group', 'struct', 'bitfield']:
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
        return self._doc['value']


class DocEnum(DocBase):
    def __init__(self, doc: dict, parent: DocBase=None):
        super().__init__(doc, parent)


class DocEnumField(DocBase):
    def __init__(self, doc: dict, parent: DocBase=None):
        super().__init__(doc, parent)

    @property
    def value(self) -> str:
        return self._doc['value']


class DocStruct(DocBase):
    def __init__(self, doc: dict, parent: DocBase=None):
        super().__init__(doc, parent)

    @property
    def size(self) -> int:
        if isinstance(self._doc['size'], int):
            return self._doc['size']
        return -1


class DocStructField(DocBase):
    def __init__(self, doc: dict, parent: DocBase=None):
        super().__init__(doc, parent)

    @property
    def size(self) -> int:
        if isinstance(self._doc['size'], str) and self._doc['size'] == '?':
            assert self.parent                      # Must have parent
            assert self.parent.fields[-1] == self   # Must be last element
            sum_of_previous_fields = sum(field.size for field in self.parent.fields[:-1])
            self._doc['size'] = self.parent.size - sum_of_previous_fields
        elif isinstance(self._doc['size'], int):
            pass
        else:
            raise Exception('Invalid size')

        return self._doc['size']


class DocBitfield(DocBase):
    REQUIRED_NAME = False

    def __init__(self, doc: dict, parent: DocBase=None):
        super().__init__(doc, parent)

    @property
    def size(self) -> int:
        return self._doc['size']


class DocBitfieldField(DocBase):
    def __init__(self, doc: dict, parent: DocBase=None):
        super().__init__(doc, parent)

    @property
    def bit(self) -> Tuple[int, int]:
        if isinstance(self._doc['bit'], int):
            bit_from, bit_to = self._doc['bit'], self._doc['bit'] + 1
        else:
            doc_bit = self._doc['bit']
            if 'MAXPHYADDR' in doc_bit:
                doc_bit = doc_bit.replace('(MAXPHYADDR-1)', f'{MAXPHYADDR - 1}')

            bit_from, bit_to = list(map(int, doc_bit.split('-')))
            bit_to += 1

        return bit_from, bit_to
