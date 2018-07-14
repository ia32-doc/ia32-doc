from .doc import *
from .processor_base import DocProcessorBase
from .text_wrapper import wrap


class DocProcessor(DocProcessorBase):
    #
    # Public methods.
    # ===============
    #

    def __init__(self):
        super().__init__()
        self._align_const = 60
        self._typedef_nesting = 0

    def process_group(self, doc: DocBase) -> None:
        group_id = self._make_short_name(doc, True)
        group_name = self._make_multiline_comment(self._make_short_description(doc), '          ')

        if doc.long_description:
            group_details = self._make_multiline_comment(self._make_long_description(doc))

        self.print(f'/**')
        self.print(f' * @defgroup {group_id} \\')
        self.print(f' * {group_name}')

        if doc.long_description:
            self.print(f' *')
            self.print(f' * {group_details}')

        self._print_details(doc)
        self.print(f' * @{{')
        self.print(f' */')

        self.process(doc.fields)

        self.print(f'/**')
        self.print(f' * @}}')
        self.print(f' */')

        self.print(f'')

    def process_definition(self, doc: DocDefinition) -> None:
        definition_name = self._make_long_name(doc)
        definition_description_printed = False

        if self.ctx.definition_comments and doc.long_description:
            definition_brief = self._make_multiline_comment(self._make_long_description(doc), '@brief ')
            definition_access = f' <b>({doc.access})</b>' if doc.access else ''

            self.print(f'/**')
            self.print(f' * {definition_brief}{definition_access}')
            self.print(f' */')

            definition_description_printed = True

        if isinstance(doc.value, int):
            self.print(f'#define {definition_name:<{self._align_const}} 0x{doc.value:08X}')
        else:
            self.print(f'#define {definition_name:<{self._align_const}} {doc.value}')

        if self.ctx.definition_new_line:
            if definition_description_printed:
                self.print(f'')

        self.process(doc.fields)

    def process_bitfield(self, doc: DocBitfield) -> None:
        self._typedef_nesting += 1

        self._print_doc(doc)

        if self._typedef_nesting == 1:
            self.print(f'typedef union')
        else:
            self.print(f'union')

        self.print(f'{{')

        with self.indent:
            self.print(f'struct')
            self.print(f'{{')

            with self.indent:
                bit_position = 0
                reserved_count = 0

                for field in doc.fields:
                    if isinstance(field, DocBitfieldField):
                        bit_position, reserved_count = self.process_bitfield_field(
                            doc, field, bit_position, reserved_count
                            )

            self.print(f'}};')
            self.print(f'')

            #
            # Print "Flags" member.
            #
            if doc.size_min != doc.size_max:
                self.print(f'{doc.size_type_min} Flags{doc.size_min};')
                self.print(f'{doc.size_type_max} Flags{doc.size_max};')
            else:
                self.print(f'{doc.size_type} Flags;')

        if self._typedef_nesting == 1:
            self.print(f'}} {self._make_long_name(doc)};')
        else:
            self.print(f'}} {self._fix_case(self._make_long_name(doc, standalone=True))};')

        self.print(f'')

        self._typedef_nesting -= 1

        self.process(doc.fields)

    def process_bitfield_field(
            self, doc: DocBitfield, field: DocBitfieldField, bit_position: int, reserved_count: int
            ) -> Tuple[int, int]:
        bit_from, bit_to = field.bit

        #
        # Handle "Reserved" fields.
        #
        if bit_from > bit_position:
            reserved_count += 1

            bit_length = bit_from - bit_position
            field_long_name = f'Reserved{reserved_count}'
            self.print(f'{doc.size_type} {self._fix_case(field_long_name):<{self._align}}: {bit_length};')
            bit_position = bit_from

        #
        # Print bit-field.
        #
        bit_length = bit_to - bit_position
        if self.ctx.bitfield_field_comments and field.long_description:
            if bit_position > 0:
                self.print(f'')

            if field.short_description == field.long_description:
                field_description = self._make_multiline_comment(self._make_long_description(field))

                self.print(f'/**')
                self.print(f' * {field_description}')
                self.print(f' */')
            else:
                field_short_description = self._make_multiline_comment(self._make_short_description(field), '@brief ')
                field_long_description = self._make_multiline_comment(self._make_long_description(field))
                field_access = f' <b>({field.access})</b>' if field.access else ''

                self.print(f'/**')
                self.print(f' * {field_short_description}{field_access}')
                self.print(f' *')
                self.print(f' * {field_long_description}')
                self._print_details(field)
                self.print(f' */')

        self.print(f'{doc.size_type} {self._fix_case(self._make_long_name(field)):<{self._align}}: {bit_length};')

        #
        # Print definitions for fields.
        #
        if self.ctx.bitfield_field_with_definitions:
            bit_shift = bit_to - bit_from
            macro_arg_name = '_'

            definition_bit = f'{self._make_long_name(doc)}_{self._make_long_name(field)}_BIT'
            self.print(f'#define {definition_bit:<{self._align_const}} {bit_from}')

            # _SIZE/_MASK?
            definition_size = f'{self._make_long_name(doc)}_{self._make_long_name(field)}_MASK'
            self.print(f'#define {definition_size:<{self._align_const}} 0x{((1 << bit_shift) - 1):02X}')

            definition = f'{self._make_long_name(doc)}_{self._make_long_name(field)}({macro_arg_name})'
            self.print(f'#define {definition:<{self._align_const}} ((({macro_arg_name}) >> {bit_from}) '
                       f'& 0x{((1 << bit_shift) - 1):02X})')

        bit_position = bit_to

        self.process(doc.fields)

        return bit_position, reserved_count

    def process_struct(self, doc: DocStruct) -> None:
        self._typedef_nesting += 1

        self._print_doc(doc)

        if doc.tag == 'Packed':
            self.print(f'#include <pshpack1.h>')

        if self._typedef_nesting == 1:
            self.print(f'typedef struct')
        else:
            self.print(f'struct')

        self.print(f'{{')

        with self.indent:
            field_number = 0

            for field in doc.fields:
                if isinstance(field, DocStruct):
                    self.process_struct(field)
                elif isinstance(field, DocBitfield):
                    self.process_bitfield(field)
                elif isinstance(field, DocStructField):
                    self.process_struct_field(field)
                else:
                    raise Exception('Invalid field type')

                field_number += 1

        if self._typedef_nesting == 1:
            self.print(f'}} {self._make_long_name(doc)};')
        else:
            self.print(f'}} {self._fix_case(self._make_long_name(doc, standalone=True))};')

        if doc.tag == 'Packed':
            self.print(f'#include <poppack.h>')

        self.print(f'')

        # self.process(doc.fields)

        self._typedef_nesting -= 1

    def process_struct_field(self, doc: DocStructField) -> None:
        self.print(f'{doc.size_type} {self._fix_case(self._make_long_name(doc))};')

        if doc.fields:
            self.print(f'')
            self.process(doc.fields)

    #
    # Private methods.
    # ================
    #

    def _fix_case(self, text: str) -> str:
        return ''.join(e.title() for e in text.split('_'))

    def _print_doc(self, doc: DocBase) -> None:
        if doc.short_description:
            doc_brief = self._make_multiline_comment(self._make_short_description(doc), '@brief ')

            self.print(f'/**')
            self.print(f' * {doc_brief}')

            if doc.long_description != doc.short_description:
                doc_details = self._make_multiline_comment(self._make_long_description(doc))

                self.print(f' *')
                self.print(f' * {doc_details}')

            self.print(f' */')

    def _print_details(self, doc: DocBase) -> None:
        if doc.note or doc.remarks or doc.see_also or doc.reference:
            self.print(f' *')

        if doc.note:
            doc_note = self._make_multiline_comment(doc.note, '@note ')
            self.print(f' * {doc_note}')

        if doc.remarks:
            doc_remarks = self._make_multiline_comment(doc.remarks, '@remarks ')
            self.print(f' * {doc_remarks}')

        if doc.see_also:
            if isinstance(doc.see_also, list):
                for see_also in doc.see_also:
                    self.print(f' * @see {see_also}')
            else:
                self.print(f' * @see {doc.see_also}')

        if doc.reference:
            self.print(f' * @see {doc.reference} (reference)')

    def _make_short_name(self, doc: DocBase, raw: bool=False, standalone: bool=False) -> str:
        if self.ctx.prefer_alternative_names and doc.alternative_name:
            result = doc.alternative_name
        else:
            if raw:
                result = doc.short_name_raw
            elif standalone:
                result = doc.short_name_standalone
            else:
                result = doc.short_name

        return result

    def _make_long_name(self, doc: DocBase, raw: bool=False, standalone: bool=False) -> str:
        if self.ctx.prefer_alternative_names and doc.alternative_name:
            result = doc.alternative_name
        else:
            if raw:
                result = doc.long_name_raw
            elif standalone:
                result = doc.long_name_standalone
            else:
                result = doc.long_name

        return result

    def _make_short_description(self, doc: DocBase) -> str:
        return doc.short_description.rstrip().rstrip('.')

    def _make_long_description(self, doc: DocBase) -> str:
        return doc.long_description.rstrip()

    def _make_multiline_comment(self, text: str, prefix: str='', indent: int=1) -> str:
        #
        # Compute indent from the prefix (if provided).
        #
        if prefix:
            indent = len(prefix) + 1    # + 1 space ' * {...}'
                                        # ~~~~~~~~~~~~ ^ here
            text = prefix + text

        indent_text = ' ' * indent
        lines = wrap(text, 120)

        result = lines[0]

        if len(lines) > 1:
            result += f'\n'
            result += f'\n'.join([ f' *{indent_text}{line}' for line in lines[1:] ])

        return result

    #
    # Private properties.
    # ===================
    #

    @property
    def _align(self):
        return self._align_const - self.indent.indent
