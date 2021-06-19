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
    def __init__(self, out_dir):
        super().__init__()
        directory = os.path.split(__file__)[0]
        self._templates_dir = os.path.join(directory, 'python-templates')
        self._out_dir = out_dir
        print("Output dir: {}".format(os.path.abspath(self._out_dir)))
        os.makedirs(self._out_dir, exist_ok=True)

        # Copy utils directory to the outer module
        dst_utils_dir = os.path.join(self._out_dir, 'utils')
        src_utils_dir = os.path.join(directory, 'utils')
        shutil.rmtree(dst_utils_dir, ignore_errors=True)
        shutil.copytree(src_utils_dir, dst_utils_dir)

        self._current_group_file = None

    def _get_template(self, template_name: str) -> jinja2.Template:
        try:
            template_path = os.path.join(self._templates_dir, template_name)
            content = open(template_path, 'r').read()
            return jinja2.Template(content)
        except (FileNotFoundError, OSError) as e:
            raise jinja2.TemplateError(e)

    def _append_template_to_group(self, doc, template_name, **kwargs):
        template = self._get_template(template_name)
        # strip non-ascii characters from the description
        content = template.render(
            doc=doc,
            strip_description=lambda d: d.encode('ascii', 'ignore').decode('ascii'),
            humps=humps,
            hex=hex,
            **kwargs
        )
        self._current_group_file.write(content)

    @staticmethod
    def _get_parent_directory(doc):
        directories = ['']
        while doc.parent is not None:
            directories.insert(0, doc.parent.short_name.lower())
            doc = doc.parent

        return os.path.join(*directories)

    @staticmethod
    def _create_definition(doc):
        value = doc.value
        if isinstance(value, int):
            value = hex(value)
        return "{} = {}".format(doc.short_name, value)

    def process_group(self, doc: DocGroup) -> None:
        # Create a package for the given group
        init_file_path = os.path.join(
            self._out_dir,
            self._get_parent_directory(doc),
            doc.short_name.lower(),
            "__init__.py"
        )

        if self._current_group_file is not None:
            self._current_group_file.close()

        # Create directories that do not exists
        directories = os.path.split(init_file_path)[0]
        os.makedirs(directories, exist_ok=True)
        self._current_group_file = open(init_file_path, "w")

        # Include utils
        self._current_group_file.write(
            "from future.utils import with_metaclass\n"
            "from utils.bit_field import *\n\n\n"
        )

        self._append_template_to_group(
            doc,
            "group.j2",
        )
        self.process(doc.fields)

    def process_enum(self, doc: DocEnum) -> None:
        self._append_template_to_group(
            doc,
            "enum.j2",
        )

    def process_struct(self, doc: DocStruct) -> None:
        struct_fields = [f for f in doc.fields if 'struct_field' == f.type]
        definitions = [
            self._create_definition(f) for
            f in
            doc.fields if
            'definitions' == doc.type
        ]
        total_size = sum(map(lambda f: f.size, struct_fields))
        self._append_template_to_group(
            doc,
            "struct.j2",
            total_size=total_size,
            struct_fields=struct_fields,
            definitions=definitions,
        )

    def process_definition(self, doc: DocDefinition) -> None:
        definition = self._create_definition(doc)
        self._current_group_file.write(definition + "\n\n")

    def process_bitfield(self, doc: DocBitfield) -> None:
        self._append_template_to_group(
            doc,
            "bitfield.j2",
        )
