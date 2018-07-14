class DocProcessorContext(object):
    def __init__(self,
                 definition_comments: bool=True,
                 definition_new_line: bool=True,
                 definition_no_indent: bool=True,
                 bitfield_field_comments: bool=True,
                 bitfield_field_with_definitions: bool=True,
                 prefer_alternative_names: bool=True):
        self.definition_comments = definition_comments
        self.definition_new_line = definition_new_line
        self.definition_no_indent = definition_no_indent
        self.bitfield_field_comments = bitfield_field_comments
        self.bitfield_field_with_definitions = bitfield_field_with_definitions
        self.prefer_alternative_names = prefer_alternative_names


class DocProcessorContextStackPush(object):
    def __init__(self, ctx_stack: 'DocProcessorContextStack', new_ctx: DocProcessorContext):
        self.ctx_stack = ctx_stack
        self.new_ctx = new_ctx

    def __enter__(self):
        self.ctx_stack.ctx_stack.append(self.ctx_stack.ctx)
        self.ctx_stack.ctx = self.new_ctx

    def __exit__(self, type, value, traceback):
        self.ctx_stack.ctx = self.ctx_stack.ctx_stack.pop()


class DocProcessorContextStack(object):
    def __init__(self):
        self.ctx = DocProcessorContext()
        self.ctx_stack = []

    def push(self, new_ctx) -> DocProcessorContextStackPush:
        return DocProcessorContextStackPush(self, new_ctx)

    def __getattr__(self, item):
        return getattr(self.ctx, item)

