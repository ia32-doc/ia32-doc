from .doc import *

options_comment_subfields = {
    'short_description'         : True,
    'long_description'          : True,
    'note'                      : True,
    'access'                    : True,
    'remarks'                   : True,
    'see'                       : True,
    'reference'                 : True,
}

options_other_subfields = {
    'prefer_long_names'         : True,
    'prefer_alternative_names'  : True,
    # extra_empty_line (definition)?
    'name_letter_case'          : 'camel_case',  # [camel_case|snake_case|snake_case_upper]
}

options_subfields = { **options_comment_subfields, **options_other_subfields }


class DocProcessorOptions(object):
    def __init__(self, **kwargs):
        for category in DOC_TYPES:
            #
            # Create subfields for each option category, e.g.: group_short_description,
            # struct_note, ...
            #
            for subfield, subfield_default_value in options_subfields.items():
                setattr(self, f'{category}_{subfield}', subfield_default_value)

            #
            # Create common property getter for *_comments (e.g.: definition_comments),
            # which will simply return if all comment subfields are True or False.
            #
            def subfield_comments_getter(self_, category_=category):
                return all(
                    getattr(self_, f'{category_}_{comment_subfield_}')
                    for comment_subfield_, _ in options_comment_subfields.items()
                )

            #
            # Create common property setter for *_comments (e.g.: definition_comments),
            # which will simply set all comment subfields to desired value.
            #
            # Note that small hack is used with any() to run this expression as a comprehension.
            # Use of any is possible, because setattr() returns None.
            #
            def subfield_comments_setter(self_, value_, category_=category):
                any(
                    setattr(self_, f'{category_}_{comment_subfield_}', value_)
                    for comment_subfield_, _ in options_comment_subfields.items()
                )

            setattr(DocProcessorOptions, f'{category}_comments', property(subfield_comments_getter, subfield_comments_setter))

        #
        # Create common (global) property getter/setter for *_comments.
        #
        def comments_getter(self_):
            return all(
                getattr(self_, f'{category_}_comments')
                for category_ in DOC_TYPES
            )

        def comments_setter(self_, value_):
            any(
                setattr(self_, f'{category_}_comments', value_)
                for category_ in DOC_TYPES
            )

        setattr(DocProcessorOptions, f'comments', property(comments_getter, comments_setter))

        #
        # Create common property getter/setter for *_prefer_alternative_names.
        #
        def prefer_alternative_names_getter(self_):
            return all(
                getattr(self_, f'{category_}_prefer_alternative_names')
                for category_ in DOC_TYPES
            )

        def prefer_alternative_names_setter(self_, value_):
            any(
                setattr(self_, f'{category_}_prefer_alternative_names', value_)
                for category_ in DOC_TYPES
            )

        DocProcessorOptions.prefer_alternative_names = property(
            prefer_alternative_names_getter,
            prefer_alternative_names_setter
        )

        #
        # Create common property getter/setter for *_prefer_long_names.
        #
        def prefer_long_names_getter(self_):
            return all(
                getattr(self_, f'{category_}_prefer_long_names')
                for category_ in DOC_TYPES
            )

        def prefer_long_names_setter(self_, value_):
            any(
                setattr(self_, f'{category_}_prefer_long_names', value_)
                for category_ in DOC_TYPES
            )

        DocProcessorOptions.prefer_long_names = property(
            prefer_long_names_getter,
            prefer_long_names_setter
        )

        #
        # Additional options for individual categories.
        #
        # Group category.
        #
        self.group_defgroup = True

        #
        # Definition category.
        #
        self.definition_no_indent = True

        #
        # Bitfield field category.
        #
        self.bitfield_create_struct = True

        self.bitfield_field_long_description_with_bit_range = True
        self.bitfield_field_fill_with_reserved = True
        self.bitfield_field_reserved_prefix = 'Reserved'
        self.bitfield_field_flags_name = 'Flags'

        self.bitfield_field_with_define_bit = True
        self.bitfield_field_with_define_flag = True
        self.bitfield_field_with_define_mask = True
        self.bitfield_field_with_define_get = True

        self.bitfield_field_with_define_bit_suffix = '_BIT'
        self.bitfield_field_with_define_flag_suffix = '_FLAG'
        self.bitfield_field_with_define_mask_suffix = '_MASK'
        self.bitfield_field_with_define_get_macro_argument_name = '_'

        def bitfield_field_with_defines_getter(self_):
            return all([
                self_.bitfield_field_with_define_bit,
                self_.bitfield_field_with_define_flag,
                self_.bitfield_field_with_define_mask,
                self_.bitfield_field_with_define_get
            ])

        def bitfield_field_with_defines_setter(self_, value_):
            self_.bitfield_field_with_define_bit = value_
            self_.bitfield_field_with_define_flag = value_
            self_.bitfield_field_with_define_mask = value_
            self_.bitfield_field_with_define_get = value_

        DocProcessorOptions.bitfield_field_with_defines = property(
            bitfield_field_with_defines_getter,
            bitfield_field_with_defines_setter
        )

        #
        # Misc.
        #
        self.align = 60
        self.indent = 2
        self.brace_on_next_line = True  # Bitfield / struct.
        self.enum_as_define = False
        self.int_type_8  = 'UINT8'
        self.int_type_16 = 'UINT16'
        self.int_type_32 = 'UINT32'
        self.int_type_64 = 'UINT64'

        self.output_prepend = ''
        self.output_append = ''
        self.output_filename = 'out'

        #
        # Default letter cases.
        #
        self.group_name_letter_case = 'snake_case_upper'
        self.definition_name_letter_case = 'snake_case_upper'
        self.enum_name_letter_case = 'snake_case_upper'
        self.enum_field_name_letter_case = 'camel_case'
        self.struct_name_letter_case = 'snake_case_upper'
        self.struct_field_name_letter_case = 'camel_case'
        self.bitfield_name_letter_case = 'snake_case_upper'
        self.bitfield_field_name_letter_case = 'camel_case'

        if 'file' in kwargs:
            file = kwargs.pop('file')

            with open(file) as f:
                new_kwargs = yaml.load(f.read())

            #
            # Prefer original kwargs over config values.
            #
            new_kwargs.update(kwargs)
            kwargs = new_kwargs

        #
        # Apply options from arguments.
        #
        for option_name, option_value in kwargs.items():
            if not hasattr(self, option_name):
                raise Exception(f'{option_name} is not valid option!')

            setattr(self, option_name, option_value)


class DocProcessorOptionsStackPush(object):
    def __init__(self, ctx_stack: 'DocProcessorOptionsStack', new_ctx: DocProcessorOptions):
        self.ctx_stack = ctx_stack
        self.new_ctx = new_ctx

    def __enter__(self):
        self.ctx_stack.ctx_stack.append(self.ctx_stack.ctx)
        self.ctx_stack.ctx = self.new_ctx

    def __exit__(self, type, value, traceback):
        self.ctx_stack.ctx = self.ctx_stack.ctx_stack.pop()


class DocProcessorOptionsStack(object):
    def __init__(self):
        self.ctx = DocProcessorOptions()
        self.ctx_stack = []

    def push(self, new_ctx: DocProcessorOptions) -> DocProcessorOptionsStackPush:
        return DocProcessorOptionsStackPush(self, new_ctx)

    def __getattr__(self, item):
        return getattr(self.ctx, item)
