# -*- coding:utf-8 -*-
from prestring.python import Module, LazyFormat
from collections import defaultdict
from collections import OrderedDict
from .langhelpers import titlize


class Context(object):
    def __init__(self):
        self.m = Module()
        self.im = self.m.submodule()
        self.field_m = Module()


class Codegen(object):
    schema_class = "Schema"
    fields_module = "fields"

    def __init__(self, dispatcher, resolver):
        self.dispatcher = dispatcher
        self.resolver = resolver

    def write_header(self, c):
        c.im.stmt("# -*- coding:utf-8 -*-")

    def write_import_(self, c):
        c.im.from_("marshmallow", "Schema")
        c.im.from_("marshmallow", "fields")

    def write_schema(self, c, d):
        for name, definition in self.resolver.definitions(d).items():
            if not self.resolver.has_schema(definition):
                continue

            clsname = titlize(name)

            with c.m.class_(clsname, self.schema_class):
                opts = defaultdict(OrderedDict)
                self.resolver.update_options_pre_properties(definition, opts)

                for name, field in self.resolver.properties(definition).items():
                    if self.resolver.has_ref(field):
                        field = self.resolver.ref_original(d, field)

                    self.resolver.update_option_on_property(field, opts[name])

                    path = self.dispatcher.dispatch(self.resolver.type_and_format(field))
                    module, field_name = path.rsplit(":", 1)
                    # todo: import module
                    if module == "marshmallow.fields":
                        module = self.fields_module
                    kwargs = ", ".join(("{}={}".format(k, repr(v)) for k, v in (opts.get(name) or {}).items()))
                    c.m.stmt(LazyFormat("{} = {}.{}({})", name, module, field_name, kwargs))
            # print("@", name, definition)

    def codegen(self, d, ctx=None):
        c = ctx or Context()
        self.write_header(c)
        c.m.sep()
        self.write_import_(c)
        self.write_schema(c, d)
        return c.m
