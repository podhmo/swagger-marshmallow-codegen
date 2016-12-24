# -*- coding:utf-8 -*-
import logging
from prestring.python import Module, LazyFormat
from dictknife import deepequal
from collections import defaultdict
from collections import OrderedDict
logger = logging.getLogger(__name__)


class Context(object):
    def __init__(self):
        self.m = Module()
        self.im = self.m.submodule()
        self.field_m = Module()


class Codegen(object):
    schema_class = "Schema"
    fields_module = "fields"

    def __init__(self, dispatcher, accessor):
        self.dispatcher = dispatcher
        self.accessor = accessor

    def write_header(self, c):
        c.im.stmt("# -*- coding:utf-8 -*-")

    def write_import_(self, c):
        c.im.from_("marshmallow", "Schema")
        c.im.from_("marshmallow", "fields")

    def write_schema(self, c, d):
        for schema_name, definition in self.accessor.definitions(d).items():
            if not self.accessor.resolver.has_schema(definition):
                continue

            clsname = self.accessor.resolver.resolve_schema_name(schema_name)

            with c.m.class_(clsname, self.schema_class):
                opts = defaultdict(OrderedDict)
                self.accessor.update_options_pre_properties(definition, opts)

                for name, field in self.accessor.properties(definition).items():
                    if self.accessor.resolver.has_many(field):
                        self.write_field_many(c, d, schema_name, definition, name, field, opts[name])
                    else:
                        self.write_field_one(c, d, schema_name, definition, name, field, opts[name])

    def write_field_one(self, c, d, schema_name, definition, name, field, opts):
        field_name = name
        if self.accessor.resolver.has_ref(field):
            ref_name, field = self.accessor.resolver.resolve_ref_definition(d, field)
            if ref_name is None:
                logger.info("ref: %r is not found", field["$ref"])
                return
            field_name = ref_name
            if field_name == schema_name and deepequal(field, definition):
                field_name = "self"

        self.accessor.update_option_on_property(field, opts)

        path = self.dispatcher.dispatch(self.accessor.type_and_format(field))
        kwargs = ", ".join(("{}={}".format(k, repr(v)) for k, v in opts.items()))
        if self.accessor.resolver.has_schema(field):
            field_class_name = field_name
            module, field_name = path.rsplit(":", 1)
            # todo: import module
            if module == "marshmallow.fields":
                module = self.fields_module
            c.m.stmt(LazyFormat("{} = {}.{}({!r}, {})", name, module, field_name, field_class_name, kwargs))
        else:
            # field
            module, field_name = path.rsplit(":", 1)
            # todo: import module
            if module == "marshmallow.fields":
                module = self.fields_module
            c.m.stmt(LazyFormat("{} = {}.{}({})", name, module, field_name, kwargs))

    def write_field_many(self, c, d, schema_name, definition, field_name, field, opts):
        opts["many"] = True
        field = field["items"]
        return self.write_field_one(c, d, schema_name, definition, field_name, field, opts)

    def codegen(self, d, ctx=None):
        c = ctx or Context()
        self.write_header(c)
        c.m.sep()
        self.write_import_(c)
        self.write_schema(c, d)
        return c.m
