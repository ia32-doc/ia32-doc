import jinja2
import humps
import os
import shutil
from ia32doc.processors.base import DocProcessor
from ia32doc.doc import DocGroup,\
    DocEnum,\
    DocEnumField,\
    DocBitfield,\
    DocStruct,\
    DocDefinition,\
    DocStructField,\
    DocBitfieldField


class DocPythonProcessor(DocProcessor):
    def __init__(self):
        super().__init__()
        directory = os.path.split(__file__)[0]
        self._templates_dir = os.path.join(directory, 'python-templates')
        self._out_dir = os.path.join('out', 'python')
        os.makedirs(self._out_dir, exist_ok=True)
        dst_utils_dir = os.path.join(self._out_dir, 'utils')
        src_utils_dir = os.path.join(directory, 'utils')
        shutil.rmtree(dst_utils_dir, ignore_errors=True)
        shutil.copytree(src_utils_dir, dst_utils_dir)

    def _get_template(self, template_name: str) -> jinja2.Template:
        try:
            template_path = os.path.join(self._templates_dir, template_name)
            content = open(template_path, 'r').read()
            return jinja2.Template(content)
        except (FileNotFoundError, OSError) as e:
            raise jinja2.TemplateError(e)

    def _render_template_to_file(self, doc, template_name, output_path):
        full_output_path = os.path.join(self._out_dir, output_path)
        # Create directories if not exists
        directories = os.path.split(full_output_path)[0]
        os.makedirs(directories, exist_ok=True)
        with open(full_output_path, 'w') as output_file:
            template = self._get_template(template_name)
            # strip non-ascii characters from the description
            description = \
                doc.long_description.encode('ascii', 'ignore').decode('ascii')
            content = template.render(
                doc=doc,
                strip_description=lambda d: d.encode('ascii', 'ignore').decode('ascii'),
                humps=humps,
            )
            output_file.write(content)

    @staticmethod
    def _get_parent_directory(doc):
        directories = ['']
        while doc.parent is not None:
            directories.insert(0, doc.parent.short_name.lower())
            doc = doc.parent

        return os.path.join(*directories)

    def process_group(self, doc: DocGroup) -> None:
        # Create a package for the given group
        init_file_path = os.path.join(
            self._get_parent_directory(doc),
            doc.short_name.lower(),
            "__init__.py"
        )
        description = doc.long_description
        fields = list(map(lambda f: f.short_name.lower(), doc.fields))
        self._render_template_to_file(
            doc,
            "group.j2",
            init_file_path,
        )
        self.process(doc.fields)

    def process_enum(self, doc: DocEnum) -> None:
        breakpoint()
        name = humps.pascalize(doc.short_name.lower())
        description = doc.long_description
        fields = doc.fields
        enum_file_path = name
        self._render_template_to_file(
            doc,
            "enum.j2",
            enum_file_path,
        )

    def process_enum_field(self, doc: DocEnumField) -> None:
        breakpoint()

    def process_struct(self, doc: DocStruct) -> None:
        breakpoint()

    def process_struct_field(self, doc: DocStructField) -> None:
        breakpoint()

    def process_definition(self, doc: DocDefinition) -> None:
        breakpoint()

    def process_bitfield(self, doc: DocBitfield) -> None:
        name = humps.pascalize(doc.short_name.lower())
        description = doc.long_description
        fields = doc.fields
        bitfield_file_path = os.path.join(
            self._get_parent_directory(doc),
            doc.short_name.lower() + '.py'
        )
        self._render_template_to_file(
            doc,
            "bitfield.j2",
            bitfield_file_path,
        )

    def process_bitfield_field(self, doc: DocBitfieldField) -> None:
        breakpoint()