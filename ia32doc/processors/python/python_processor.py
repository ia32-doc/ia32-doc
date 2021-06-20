import jinja2
import humps
import os
import shutil
from ia32doc.processors.base import DocProcessor
from ia32doc.doc import DocGroup,\
    DocEnum,\
    DocBitfield,\
    DocStruct,\
    DocDefinition


class DocPythonProcessor(DocProcessor):
    def __init__(self, out_dir):
        super().__init__()
        directory = os.path.split(__file__)[0]
        self._templates_dir = os.path.join(directory, 'python-templates')
        self._out_dir = out_dir
        self._package_dir = os.path.join(out_dir, "ia32_doc")
        print("Output dir: {}".format(os.path.abspath(self._out_dir)))
        os.makedirs(self._out_dir, exist_ok=True)

        # Copy utils directory to the outer module
        dst_utils_dir = os.path.join(self._package_dir, 'utils')
        src_utils_dir = os.path.join(directory, 'utils')
        shutil.rmtree(dst_utils_dir, ignore_errors=True)
        shutil.copytree(src_utils_dir, dst_utils_dir)

        # Copy additional files to the outer module
        src_additional_dir = os.path.join(directory, 'additional-files')
        for file in os.listdir(src_additional_dir):
            if os.path.isdir(file):
                shutil.copytree(
                    os.path.join(src_additional_dir, file),
                    os.path.join(out_dir, file)
                )
            else:
                shutil.copy2(
                    os.path.join(src_additional_dir, file),
                    os.path.join(out_dir, file)
                )

        self._current_group_file = None

    def _get_template(self, template_name: str) -> jinja2.Template:
        try:
            template_path = os.path.join(self._templates_dir, template_name)
            content = open(template_path, 'r').read()
            return jinja2.Template(content, keep_trailing_newline=True)
        except (FileNotFoundError, OSError) as e:
            raise jinja2.TemplateError(e)

    def _generate_gemplate(self, doc, template_name, ident=0, name_prefix='', **kwargs):
        template = self._get_template(template_name)

        def get_description(document):
            description = []

            if document.short_description != '':
                description.append("@brief " + document.short_description)
            description.append(document.long_description)
            if document.see != '':
                see_list = []
                if isinstance(document.see, str):
                    see_list.append(document.see)
                elif isinstance(document.see, list):
                    see_list = document.see
                else:
                    raise RuntimeError("Unsupported type!")
                description.extend("@see " + reference for reference in see_list)
            # strip non-ascii characters from the description
            description_str = \
                "\n\n".join(description).encode('ascii', 'ignore').decode('ascii')
            return description_str

        def class_name(document):
            if document.long_name_raw != '':
                return humps.pascalize(document.long_name_raw.lower())
            else:
                # TODO: aviod collisions
                return "Dummy"

        content = template.render(
            doc=doc,
            get_description=get_description,
            class_name=class_name,
            humps=humps,
            hex=hex,
            zip=zip,
            hasattr=hasattr,
            name_prefix=name_prefix,
            **kwargs
        )
        content = '\n'.join('    ' * ident + line for line in content.splitlines())
        return content

    def _append_template_to_group(self, doc, template_name, ident=0, name_prefix='', **kwargs):
        content = \
            self._generate_gemplate(doc, template_name, ident, name_prefix, **kwargs)
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
        return "{} = {}\n".format(doc.short_name, value)

    def process_group(self, doc: DocGroup) -> None:
        # Create a package for the given group
        init_file_path = os.path.join(
            self._package_dir,
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
            "from utils.struct import *\n"
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
        struct_members = [
            f for
            f in
            doc.fields if
            'struct_field' == f.type or 'bitfield' == f.type
        ]

        # Render bitfield for each struct member
        member_containers = [
            self._generate_gemplate(
                member,
                "bitfield.j2",
                ident=1,
                name_prefix='_MemberContainer',
                struct_members=struct_members,
            ) for
            member in
            struct_members
        ]

        definitions = [
            self._create_definition(f) for
            f in
            doc.fields if
            'definitions' == doc.type
        ]

        self._append_template_to_group(
            doc,
            "struct.j2",
            struct_members=struct_members,
            member_containers=member_containers,
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
