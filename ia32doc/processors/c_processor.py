from typing import Union, Tuple

from .base import DocProcessor

from ..doc import DocBase, DocGroup, DocDefinition, DocEnum, DocEnumField,\
                  DocBitfield, DocBitfieldField, DocStruct, DocStructField
from ..doc import DOC_DEFINITION, DOC_STRUCT, DOC_BITFIELD, DOC_STRUCT_FIELD, DOC_ENUM_FIELD
from ..text import DocText


class DocCProcessor(DocProcessor):
    def __init__(self):
        super().__init__()

        #
        # Nesting level of union/struct typedefs.
        #
        self._typedef_nesting = 0

        #
        # Bitfield position of last bitfield field.
        #
        self._bitfield_position = None

        #
        # Number of "Reserved" bitfield fields in current bitfield.
        #
        self._bitfield_reserved_count = None

        #
        # Make C++ code.
        #
        self._output_cpp = False

    def process_group(self, doc: DocGroup) -> None:
        if self.opt.group_comments and doc.long_description or self.opt.group_defgroup:
            self.print(f'/**')
            self.print_details(doc)

            if self.opt.group_defgroup:
                self.print(f' * @{{')
            self.print(f' */')

        self.process(doc.fields)

        if self.opt.group_defgroup:
            self.print(f'/**')
            self.print(f' * @}}')
            self.print(f' */')

        self.print(f'')

    def process_definition(self, doc: DocDefinition) -> None:
        #
        # We need to set "override_name_letter_case" explicitly,
        # because this method is also shared for DocEnumField.
        #
        name = self.make_name(doc, override_name_letter_case=self.opt.definition_name_letter_case)

        if self.opt.definition_comments and doc.long_description:
            #
            # Do not print empty line for the first element.
            #
            if next(filter(lambda field: isinstance(field, DocDefinition), doc.parent.fields)) != doc:
                self.print(f'')
            self.print(f'/**')
            self.print_details(doc)
            self.print(f' */')

        align = self.opt.align if self.opt.definition_no_indent else \
                self.align_indent_adjusted

        value = f'0x{doc.value:08X}' if isinstance(doc.value, int) else \
                f'{doc.value}'

        self.print(f'#define {name:<{align}} {value}')

        self.process(doc.fields)

    def process_enum(self, doc: DocEnum) -> None:
        if self.opt.enum_as_define:
            if self.opt.enum_comments and doc.long_description:
                self.print(f'/**')
                self.print_details(doc)

                #
                # Create defgroup for this group of definitions (enum).
                #
                if self.opt.group_defgroup:
                    self.print(f' * @{{')
                self.print(f' */')

            for field in doc.fields:
                assert field.type in [ DOC_DEFINITION, DOC_ENUM_FIELD ]
                definition_field: DocDefinition = field

                #
                # DocDefinition and DocEnumField has the same interface,
                # so it can be hacked this way.
                #
                self.process_definition(definition_field)

            if self.opt.group_defgroup:
                self.print(f'/**')
                self.print(f' * @}}')
                self.print(f' */')
        else:
            self._typedef_nesting += 1

            if self.opt.enum_comments and doc.long_description:
                self.print(f'/**')
                self.print_details(doc, treat_description_as_short=True)
                self.print(f' */')

            optional_curly_brace = ' {' if not self.opt.brace_on_next_line else ''
            optional_typedef = ''
            optional_name_begin = ''
            optional_name_end = ''

            if self._output_cpp:
                optional_name_begin = f' {self.make_name(doc)}'
            else:
                optional_typedef = 'typedef ' if self._typedef_nesting == 1 else ''
                optional_name_end = f' {self.make_name(doc)}'

            self.print(f'{optional_typedef}enum{optional_name_begin}{optional_curly_brace}')
            if self.opt.brace_on_next_line:
                self.print(f'{{')

            with self.indent:
                for field in doc.fields:
                    assert field.type in [ DOC_DEFINITION, DOC_ENUM_FIELD ]
                    getattr(self, f'process_{field.type}')(field)

            if self._typedef_nesting == 1:
                self.print(f'}}{optional_name_end};')
            else:
                name = self.make_name(
                    doc,
                    standalone=True,
                    override_name_letter_case=self.opt.enum_field_name_letter_case
                )
                self.print(f'}} {name};')

            self._typedef_nesting -= 1

        self.print(f'')

    def process_enum_field(self, doc: DocEnumField) -> None:
        name = self.make_name(doc)

        if self.opt.enum_field_comments and doc.long_description:
            #
            # Do not print empty line for the first element.
            #
            if next(filter(lambda field: isinstance(field, DocEnumField), doc.parent.fields)) != doc:
                self.print(f'')
            self.print(f'/**')
            self.print_details(doc)
            self.print(f' */')

        value = f'0x{doc.value:08X}'

        self.print(f'{name:<{self.opt.align}} = {value},')

        self.process(doc.fields)

    def process_struct(self, doc: DocStruct) -> None:
        self._typedef_nesting += 1

        if self.opt.struct_comments and doc.long_description:
            self.print(f'/**')
            self.print_details(doc, treat_description_as_short=True)
            self.print(f' */')

        if doc.tag == 'Packed':
            self.print(f'#pragma pack(push, 1)')

        has_name = doc.short_name or doc.long_name
        optional_curly_brace = ' {' if not self.opt.brace_on_next_line else ''
        optional_typedef = ''
        optional_name_begin = ''
        optional_name_end = ''

        if self._output_cpp:
            optional_name_begin = f' {self.make_name(doc)}'
        else:
            optional_typedef = 'typedef ' if self._typedef_nesting == 1 else ''
            optional_name_end = f' {self.make_name(doc)}'

        self.print(f'{optional_typedef}struct{optional_name_begin}{optional_curly_brace}')
        if self.opt.brace_on_next_line:
            self.print(f'{{')

        with self.indent:
            for field in doc.fields:
                assert field.type in [ DOC_STRUCT, DOC_BITFIELD, DOC_STRUCT_FIELD ]

                if isinstance(field, DocBitfield) and not self.opt.bitfield_create_struct:
                    self.print(f'{self.make_size_type(field.size)[0]} {self.make_name(field, standalone=True)};')
                else:
                    getattr(self, f'process_{field.type}')(field)

        if self._typedef_nesting == 1:
            assert has_name
            self.print(f'}}{optional_name_end};')
        else:
            if has_name:
                name = self.make_name(
                    doc,
                    standalone=True,
                    override_name_letter_case=self.opt.struct_field_name_letter_case
                )
                self.print(f'}} {name};')
            else:
                self.print(f'}};')

        if doc.tag == 'Packed':
            self.print(f'#pragma pack(pop)')

        self.print(f'')

        self._typedef_nesting -= 1

    def process_struct_field(self, doc: DocStructField) -> None:
        if self.opt.struct_field_comments and doc.long_description:
            #
            # Do not print empty line for the first element.
            #
            if next(iter(doc.parent.fields)) != doc:
                self.print(f'')
            self.print(f'/**')
            self.print_details(doc)
            self.print(f' */')

        size_type, size_type_array = self.make_size_type(doc.size)
        self.print(f'{size_type} {self.make_name(doc)}{size_type_array};')

        if doc.fields:
            self.print(f'')
            self.process(doc.fields)

    def process_bitfield(self, doc: DocBitfield) -> None:
        if self.opt.bitfield_create_struct:
            self._typedef_nesting += 1

            if self.opt.bitfield_comments and doc.long_description:
                self.print(f'/**')
                self.print_details(doc, treat_description_as_short=True)
                self.print(f' */')

            has_name = doc.short_name or doc.long_name
            optional_curly_brace = ' {' if not self.opt.brace_on_next_line else ''
            optional_typedef = ''
            optional_name_begin = ''
            optional_name_end = ''

            #
            # Bitfields at root level MUST have name.
            #
            if self._typedef_nesting == 1:
                assert has_name

            if self._output_cpp:
                optional_name_begin = f' {self.make_name(doc)}'
            else:
                optional_typedef = 'typedef ' if self._typedef_nesting == 1 else ''
                optional_name_end = f' {self.make_name(doc)}'

            #
            # Create union (only for named bitfields).
            #
            if has_name:
                self.print(f'{optional_typedef}union{optional_name_begin}{optional_curly_brace}')
                if self.opt.brace_on_next_line:
                    self.print(f'{{')
            else:
                #
                # If the bitfield is unnamed, do not double-indent the struct.
                #
                self.indent.indent_next = 0

            with self.indent:
                self.print(f'struct{optional_curly_brace}')
                if self.opt.brace_on_next_line:
                    self.print(f'{{')

                with self.indent:
                    assert self._bitfield_position is None
                    assert self._bitfield_reserved_count is None
                    self._bitfield_position = 0
                    self._bitfield_reserved_count = 0

                    last_field = None
                    for field in doc.fields:
                        if isinstance(field, DocBitfieldField):
                            self.process_bitfield_field(field)
                            last_field = field

                    #
                    # Check if we have to create last "Reserved" field.
                    #
                    last_bit_from, last_bit_to = last_field.bit
                    if last_bit_to < doc.size and self.opt.bitfield_field_fill_with_reserved:
                        self._bitfield_reserved_count += 1
                        bit_length = doc.size - self._bitfield_position
                        long_name = f'{self.opt.bitfield_field_reserved_prefix}{self._bitfield_reserved_count}'
                        self.print(
                            f'{self.make_size_type(doc.size)[0]} {long_name:<{self.align_indent_adjusted}}: '
                            f'{bit_length};'
                        )

                    self._bitfield_position = None
                    self._bitfield_reserved_count = None

                self.print(f'}};')

                #
                # Print "Flags" member (only for named bitfields).
                #
                if has_name:
                    self.print(f'')
                    self.print(f'{self.make_size_type(doc.size)[0]} {self.opt.bitfield_field_flags_name};')

            #
            # End of the union (only for named bitfields).
            #
            if has_name:
                if self._typedef_nesting == 1:
                    self.print(f'}}{optional_name_end};')
                else:
                    name = self.make_name(
                        doc,
                        standalone=True,
                        override_name_letter_case=self.opt.bitfield_field_name_letter_case
                    )
                    self.print(f'}} {name};')

            self._typedef_nesting -= 1
        else:
            #
            # Do not create unions.
            #
            for field in doc.fields:
                if isinstance(field, DocBitfieldField):
                    self.process_bitfield_field(field)

        self.print(f'')

    def process_bitfield_field(self, doc: DocBitfieldField) -> None:
        bit_from, bit_to = doc.bit

        if self.opt.bitfield_create_struct:
            #
            # Handle "Reserved" fields.
            #
            if bit_from > self._bitfield_position:
                self._bitfield_reserved_count += 1

                bit_length = bit_from - self._bitfield_position
                long_name = f'{self.opt.bitfield_field_reserved_prefix}{self._bitfield_reserved_count}'
                self.print(
                    f'{self.make_size_type(doc.parent.size)[0]} {long_name:<{self.align_indent_adjusted}}: '
                    f'{bit_length};'
                )
                self._bitfield_position = bit_from

            #
            # Print bit-field.
            #
            bit_length = bit_to - self._bitfield_position
            if self.opt.bitfield_field_comments and doc.long_description:
                if self._bitfield_position > 0:
                    self.print(f'')

                self.print(f'/**')
                self.print_details(doc)
                self.print(f' */')

            self.print(
                f'{self.make_size_type(doc.parent.size)[0]} {self.make_name(doc):<{self.align_indent_adjusted}}: '
                f'{bit_length};'
            )

        #
        # Print definitions for fields.
        #
        bit_shift = bit_to - bit_from

        #
        # Print definitions only for NAMED bitfields.
        #
        if doc.parent.short_name or doc.parent.long_name:
            bitfield_field_with_define_any = any([
                self.opt.bitfield_field_with_define_bit,
                self.opt.bitfield_field_with_define_flag,
                self.opt.bitfield_field_with_define_mask,
                self.opt.bitfield_field_with_define_get
            ])

            if bitfield_field_with_define_any:
                part1 = self.make_name(doc.parent, override_name_letter_case=self.opt.definition_name_letter_case)
                part2 = self.make_name(doc, override_name_letter_case=self.opt.definition_name_letter_case)
                align = self.opt.align if self.opt.definition_no_indent else \
                        self.align_indent_adjusted

                #
                # !!! INCREDIBLY UGLY HACK !!!
                # Remove _REGISTER suffix.
                #
                if 'name_with_suffix' in doc.parent._doc:
                    part1 = part1[0:(len(part1) - len(doc.parent._doc['name_with_suffix']) - 1)]

            if self.opt.bitfield_field_with_define_bit:
                definition = f'{part1}_{part2}{self.opt.bitfield_field_with_define_bit_suffix}'
                self.print(f'#define {definition:<{align}} {bit_from}')

            if self.opt.bitfield_field_with_define_flag:
                definition = f'{part1}_{part2}{self.opt.bitfield_field_with_define_flag_suffix}'
                self.print(f'#define {definition:<{align}} 0x{(((1 << bit_shift) - 1) << bit_from):02X}')

            if self.opt.bitfield_field_with_define_mask:
                definition = f'{part1}_{part2}{self.opt.bitfield_field_with_define_mask_suffix}'
                self.print(f'#define {definition:<{align}} 0x{((1 << bit_shift) - 1):02X}')

            if self.opt.bitfield_field_with_define_get:
                definition = f'{part1}_{part2}({self.opt.bitfield_field_with_define_get_macro_argument_name})'
                self.print(
                    f'#define {definition:<{align}} '
                    f'((({self.opt.bitfield_field_with_define_get_macro_argument_name}) >> {bit_from}) & '
                    f'0x{((1 << bit_shift) - 1):02X})'
                )

        self._bitfield_position = bit_to

        self.process(doc.fields)

    def process_struct(self, doc: DocStruct) -> None:
        self._typedef_nesting += 1

        if self.opt.struct_comments and doc.long_description:
            self.print(f'/**')
            self.print_details(doc, treat_description_as_short=True)
            self.print(f' */')

        if doc.tag == 'Packed':
            self.print(f'#pragma pack(push, 1)')

        has_name = doc.short_name or doc.long_name
        optional_curly_brace = ' {' if not self.opt.brace_on_next_line else ''
        optional_typedef = 'typedef ' if self._typedef_nesting == 1 else ''

        self.print(f'{optional_typedef}struct{optional_curly_brace}')
        if self.opt.brace_on_next_line:
            self.print(f'{{')

        with self.indent:
            for field in doc.fields:
                assert field.type in [ DOC_DEFINITION, DOC_STRUCT, DOC_BITFIELD, DOC_STRUCT_FIELD ]

                if isinstance(field, DocBitfield) and not self.opt.bitfield_create_struct:
                    self.print(f'{self.make_size_type(field.size)[0]} {self.make_name(field, standalone=True)};')
                else:
                    getattr(self, f'process_{field.type}')(field)

        if self._typedef_nesting == 1:
            assert has_name
            self.print(f'}} {self.make_name(doc)};')
        else:
            if has_name:
                name = self.make_name(
                    doc,
                    standalone=True,
                    override_name_letter_case=self.opt.struct_field_name_letter_case
                )
                self.print(f'}} {name};')
            else:
                self.print(f'}};')

        if doc.tag == 'Packed':
            self.print(f'#pragma pack(pop)')

        self.print(f'')

        self._typedef_nesting -= 1

    def process_struct_field(self, doc: DocStructField) -> None:
        if self.opt.struct_field_comments and doc.long_description:
            #
            # Do not print empty line for the first element.
            #
            if next(iter(doc.parent.fields)) != doc:
                self.print(f'')
            self.print(f'/**')
            self.print_details(doc)
            self.print(f' */')

        size_type, size_type_array = self.make_size_type(doc.size)
        self.print(f'{size_type} {self.make_name(doc)}{size_type_array};')

        if doc.fields:
            self.print(f'')
            self.process(doc.fields)

    #                                                                                                                  #
    # ================================================================================================================ #
    #                                                                                                                  #

    def print_details(self, doc: DocBase, treat_description_as_short=False) -> None:
        #
        # Handle group-related comments.
        # ------------------------------
        #
        print_defgroup = False
        if isinstance(doc, DocGroup):
            print_defgroup = self.opt.group_defgroup

            if print_defgroup and doc.short_name:
                group_id   = self.make_name(doc, long=False, raw=True)
                group_name = self.make_multiline_comment(doc.short_description, '          ')

                self.print(f' * @defgroup {group_id} \\')
                self.print(f' * {group_name}')

        #
        # Handle short/long descriptions.
        # -------------------------------
        #
        print_short_description = getattr(self.opt, f'{doc.type}_short_description') and doc.short_description
        print_long_description = getattr(self.opt, f'{doc.type}_long_description') and doc.long_description
        print_access = getattr(self.opt, f'{doc.type}_access') and doc.access

        if doc.short_description_raw == doc.long_description_raw:
            if treat_description_as_short:
                print_long_description = False
            else:
                print_short_description = False

        #
        # Do not print @brief when @defgroup has been printed.
        #
        if print_short_description and not print_defgroup:
            access = f' <b>({doc.access})</b>' if print_access else ''
            short_description = self.make_multiline_comment(doc.short_description, '@brief ')
            self.print(f' * {short_description}{access}')

        if print_long_description:
            #
            # Delimit short_description and long_description with empty line.
            # Delimit @defgroup and long_description with empty line.
            #
            if print_short_description or print_defgroup:
                self.print(f' *')

            if isinstance(doc, DocBitfieldField) and self.opt.bitfield_field_long_description_with_bit_range:
                bit_from, bit_to = doc.bit
                bit_to -= 1

                bit = f'[Bit {bit_from}] ' if bit_from == bit_to else \
                      f'[Bits {bit_to}:{bit_from}] '

                long_description = self.make_multiline_comment(f'{bit}{doc.long_description}')
            else:
                long_description = self.make_multiline_comment(doc.long_description)

            self.print(f' * {long_description}')

        #
        # Handle detailed comments.
        # -------------------------
        #
        print_note      = getattr(self.opt, f'{doc.type}_note') and doc.note
        print_remarks   = getattr(self.opt, f'{doc.type}_remarks') and doc.remarks
        print_see       = getattr(self.opt, f'{doc.type}_see') and doc.see
        print_reference = getattr(self.opt, f'{doc.type}_reference') and doc.reference

        #
        # Delimit description (above) from details with empty line.
        #
        if any([print_note, print_remarks, print_see, print_reference]):
            self.print(f' *')

        if print_note:
            note = self.make_multiline_comment(doc.note, '@note ')
            self.print(f' * {note}')

        if print_remarks:
            remarks = self.make_multiline_comment(doc.remarks, '@remarks ')
            self.print(f' * {remarks}')

        #
        # see and reference can be either list (of strings) or string.
        #
        if print_see:
            if isinstance(doc.see, list):
                for see in doc.see:
                    self.print(f' * @see {see}')
            else:
                self.print(f' * @see {doc.see}')

        if print_reference:
            if isinstance(doc.reference, list):
                for reference in doc.reference:
                    self.print(f' * @see {reference} (reference)')
            else:
                self.print(f' * @see {doc.reference} (reference)')

    def make_name(self, doc: DocBase,
                  long: bool=None, raw: bool=False, standalone: bool=False,
                  override_name_letter_case: str=None) -> str:
        assert not (raw and standalone)  # invalid combination

        if long is None:
            long = getattr(self.opt, f'{doc.type}_prefer_long_names')

        if getattr(self.opt, f'{doc.type}_prefer_alternative_names') and doc.alternative_name:
            result = doc.alternative_name
        else:
            if raw:
                result = doc.long_name_raw if long else doc.short_name_raw
            elif standalone:
                result = doc.long_name_standalone if long else doc.short_name_standalone
            else:
                result = doc.long_name if long else doc.short_name

        if override_name_letter_case is not None:
            letter_case = override_name_letter_case
        else:
            letter_case = getattr(self.opt, f'{doc.type}_name_letter_case')

        return DocText.convert_case(result, letter_case)

    def make_size_type(self, size) -> Union[str, Tuple[str, str]]:
        try:
            if size in [ 8, 16, 32, 64 ]:
                return getattr(self.opt, f'int_type_{size}'), ''
            elif size % 8 == 0:
                size_in_bytes = size // 8
                return self.opt.int_type_8, f'[{size_in_bytes}]'
            else:
                raise Exception('Cannot represent size as type')
        except:
            import sys
            print(size, file=sys.stderr)
            raise

    @staticmethod
    def make_multiline_comment(text: str, prefix: str='', indent: int=1) -> str:
        #
        # Compute indent from the prefix (if provided).
        #
        if prefix:
            indent = len(prefix) + 1    # + 1 space ' * {...}'
                                        # ~~~~~~~~~~~~ ^ here
            text = prefix + text

        indent_text = ' ' * indent
        lines = DocText.wrap(text, 120)

        result = lines[0]

        if len(lines) > 1:
            result += f'\n'
            result += f'\n'.join([ f' *{indent_text}{line}' for line in lines[1:] ])

        return result

    @property
    def align_indent_adjusted(self) -> int:
        return max(0, self.opt.align - self.indent.indent)
