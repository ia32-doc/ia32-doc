from .doc import *
from .processor_ctx import DocProcessorContextStack


class DocIndent(object):
    def __init__(self):
        self.indent = 0

    def __enter__(self):
        self.indent += 2

    def __exit__(self, type, value, traceback):
        self.indent -= 2

    def __str__(self):
        return ' ' * self.indent

    def __call__(self, text, indent_only=True):
        indent = ' ' * (self.indent - text) \
                 if len(text) < self.indent \
                 else ' '

        return indent if indent_only else f'{text}{indent}'


class DocProcessorBase(object):
    def __init__(self):
        self.indent = DocIndent()
        self.ctx = DocProcessorContextStack()
        self.last_new_line_count = 0

    def print(self, text: str) -> None:
        if text:
            for line in text.splitlines():
                if line:
                    if line.startswith('#') and self.ctx.definition_no_indent and self.indent.indent > 0:
                        keyword = re.match(r'(#\w*)\s*(.*)', line).group(1)
                        line = re.sub(r'(#\w*)\s*(.*)', rf'\1{self.indent(keyword)}\2', line)
                        print(f'{self._fix_text(line)}')
                    else:
                        print(f'{self.indent}{self._fix_text(line)}')

                    self.last_new_line_count = 0
                else:
                    #
                    # Empty line? Just print new line.
                    #
                    print()
                    self.last_new_line_count += 1
        else:
            #
            # Empty text? Just print new line.
            #
            print()
            self.last_new_line_count += 1

    def process(self, doc_list: List[DocBase]) -> None:
        for doc in doc_list:
            if doc.type == 'Group':
                self.process_group(doc)
            elif isinstance(doc, DocDefinition):
                self.process_definition(doc)
            elif isinstance(doc, DocStruct):
                self.process_struct(doc)
            elif isinstance(doc, DocBitfield):
                self.process_bitfield(doc)

    def process_group(self, doc: DocBase) -> None:
        pass

    def process_definition(self, doc: DocDefinition) -> None:
        pass

    def process_bitfield(self, doc: DocBitfield) -> None:
        pass

    def process_bitfield_field(self, doc: DocBitfield, field: DocBitfieldField,
                               bit_position: int, reserved_count: int) -> Tuple[int, int]:
        pass

    def process_struct(self, doc: DocStruct) -> None:
        pass

    def process_struct_field(self, doc: DocStructField) -> None:
        pass

    @staticmethod
    def _fix_text(text: str) -> str:
        text = text.replace('“', '"')
        text = text.replace('”', '"')
        text = text.replace('—', '-')
        text = text.replace('–', '-')
        text = text.replace('®', '(R)')
        text = text.replace('’', '\'')
        text = text.replace('•', '*')
        text = text.replace('≥', '>=')
        text = text.replace('™', '(TM)')
        text = text.replace('←', '<-')

        return text
