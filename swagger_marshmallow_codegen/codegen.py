# -*- coding:utf-8 -*-
import re
import logging
from functools import partial
from prestring.python import Module, LazyFormat, LazyKeywords
from dictknife import deepequal
from collections import defaultdict
from collections import OrderedDict
from collections import namedtuple
from .langhelpers import LazyCallString, titleize


logger = logging.getLogger(__name__)
PathInfo = namedtuple("PathInfo", "matchdict, GET, POST, json_body")


class Context(object):
    def __init__(self, m=None, im=None):
        self.m = m or Module(import_unique=True)
        self.im = im or self.m.submodule()

    def from_(self, module, name):
        logger.debug("      import: module=%s, name=%s", module, name)
        self.im.from_(module, name)

    def import_(self, module):
        logger.debug("      import: module=%s", module)
        self.im.import_(module)

    def create_child(self):
        return self.__class__(self.m.submodule(), self.im)


class CodegenError(Exception):
    pass


class SchemaWriter(object):
    def __init__(self, accessor, schema_class):
        self.accessor = accessor
        self.schema_class = schema_class
        self.arrived = set()

    @property
    def resolver(self):
        return self.accessor.resolver

    def write_field_one(self, c, d, schema_name, definition, name, field, opts):
        field_class_name = None
        if self.resolver.has_ref(field):
            field_class_name, field = self.resolver.resolve_ref_definition(d, field, level=1)
            if field_class_name == schema_name and deepequal(field, definition):
                field_class_name = "self"

            # finding original definition
            if self.resolver.has_ref(field):
                ref_name, field = self.resolver.resolve_ref_definition(d, field)
                if ref_name is None:
                    raise CodegenError("ref: %r is not found", field["$ref"])

        logger.debug("      field: %s", lazy_json_dump(field))
        self.accessor.update_option_on_property(c, field, opts)
        caller_name = self.accessor.resolver.resolve_caller_name(c, name, field)
        if caller_name is None:
            raise CodegenError("matched field class is not found. name=%r, schema=%r", name, schema_name)

        normalized_name = self.resolver.resolve_normalized_name(name)
        if normalized_name != name:
            opts["dump_to"] = opts["load_from"] = name

        kwargs = LazyKeywordsRepr(opts)

        if self.resolver.has_nested(d, field) and field_class_name:
            logger.debug("      nested: %s, %s", caller_name, field_class_name)
            if opts:
                kwargs = LazyFormat(", {}", kwargs)
            value = LazyFormat("{}({!r}{})", caller_name, field_class_name, kwargs)
        else:
            if caller_name == "fields.Nested":
                caller_name = "fields.Field"
            # field
            value = LazyFormat("{}({})", caller_name, kwargs)
        if opts.pop("many", False):
            value = LazyFormat("fields.List({})", value)
        logger.info("  write field: write %s, field=%s", name, caller_name)
        c.m.stmt(LazyFormat("{} = {}", normalized_name, value))

    def write_field_many(self, c, d, schema_name, definition, field_name, field, opts):
        opts["many"] = True
        field = field["items"]
        return self.write_field_one(c, d, schema_name, definition, field_name, field, opts)

    def write_schema(self, c, d, clsname, definition, force=False):
        if not force and clsname in self.arrived:
            return
        self.arrived.add(clsname)
        base_classes = [self.schema_class]

        if self.resolver.has_ref(definition):
            ref_name, ref_definition = self.resolver.resolve_ref_definition(d, definition)
            if ref_name is None:
                raise CodegenError("$ref %r is not found", definition["$ref"])
            else:
                self.write_schema(c, d, ref_name, ref_definition)
                base_classes = [ref_name]
        elif self.resolver.has_allof(definition):
            ref_list, definition = self.resolver.resolve_allof_definition(d, definition)
            if ref_list:
                base_classes = []
                for ref_name, ref_definition in ref_list:
                    if ref_name is None:
                        raise CodegenError("$ref %r is not found", ref_definition)  # xxx
                    else:
                        self.write_schema(c, d, ref_name, ref_definition)
                        base_classes.append(ref_name)

        with c.m.class_(clsname, *base_classes):
            if "description" in definition:
                c.m.stmt('"""{}"""'.format(definition["description"]))
            opts = defaultdict(OrderedDict)
            self.accessor.update_options_pre_properties(definition, opts)

            properties = self.accessor.properties(definition)
            if not properties:
                c.m.stmt("pass")
            else:
                for name, field in properties.items():
                    name = str(name)
                    if self.resolver.has_many(field):
                        self.write_field_many(c, d, clsname, definition, name, field, opts[name])
                    else:
                        self.write_field_one(c, d, clsname, definition, name, field, opts[name])


class DefinitionsSchemaWriter(object):
    def __init__(self, accessor, schema_writer):
        self.accessor = accessor
        self.schema_writer = schema_writer

    @property
    def resolver(self):
        return self.accessor.resolver

    def write(self, c, d):
        for schema_name, definition in self.accessor.definitions(d):

            if not self.resolver.has_schema(d, definition):
                logger.info("write schema: skip %s", schema_name)
                continue

            clsname = self.resolver.resolve_schema_name(schema_name)
            logger.info("write schema: write %s", schema_name)
            self.schema_writer.write_schema(c, d, clsname, definition)


class PathsSchemaWriter(object):
    def __init__(self, accessor, schema_writer):
        self.accessor = accessor
        self.schema_writer = schema_writer
        self.separate_rx = re.compile("[/_]")
        self.ignore_rx = re.compile("[^0-9a-zA-Z_]+")

    @property
    def resolver(self):
        return self.accessor.resolver

    def write(self, c, d):
        for path, methods in self.accessor.paths(d):
            path_separated = self.separate_rx.split(path.lstrip("/"))  # xxx:
            clsname = "".join(titleize(self.ignore_rx.sub("", name)) for name in path_separated)
            sc = c.create_child()
            with sc.m.class_(clsname + "Input"):
                for method, definition in self.accessor.methods(methods):
                    ssc = sc.create_child()
                    with ssc.m.class_(titleize(method)):
                        path_info = self.build_path_info(d, definition)
                        if path_info.matchdict:
                            clsname = "Path"
                            self.schema_writer.write_schema(ssc, d, clsname, {"properties": path_info.matchdict}, force=True)
                        if path_info.GET:
                            clsname = "GET"
                            self.schema_writer.write_schema(ssc, d, clsname, {"properties": path_info.GET}, force=True)
                        if path_info.POST:
                            clsname = "POST"
                            self.schema_writer.write_schema(ssc, d, clsname, {"properties": path_info.POST}, force=True)
                        if path_info.json_body:
                            clsname = "Body"
                            definition = next(iter(path_info.json_body.values()))["schema"]
                            self.schema_writer.write_schema(ssc, d, clsname, definition, force=True)

    def build_path_info(self, fulldata, d):
        info = defaultdict(OrderedDict)
        for p in self.accessor.parameters(d):
            if self.resolver.has_ref(p):
                _, p = self.resolver.resolve_ref_definition(fulldata, p)
            info[p.get("in")][p.get("name")] = p
        return PathInfo(
            matchdict=(info.get("path") or {}),
            GET=(info.get("query") or {}),
            POST=(info.get("forData") or {}),
            json_body=(info.get("body") or {}),
        )


class Codegen(object):
    schema_class_path = "marshmallow:Schema"

    @classmethod
    def override(cls, schema_class_path):
        return partial(cls, schema_class_path=schema_class_path)

    def __init__(self, accessor, schema_class_path=None):
        self.accessor = accessor
        self.schema_class_path = schema_class_path or self.__class__.schema_class_path
        self.schema_class = self.schema_class_path.rsplit(":", 1)[-1]

    @property
    def resolver(self):
        return self.accessor.resolver

    def write_header(self, c):
        c.im.stmt("# -*- coding:utf-8 -*-")

    def write_import_(self, c):
        c.from_(*self.schema_class_path.rsplit(":", 1))
        c.from_("marshmallow", "fields")

    def write_body(self, c, d):
        sw = SchemaWriter(self.accessor, self.schema_class)
        DefinitionsSchemaWriter(self.accessor, sw).write(c, d)
        PathsSchemaWriter(self.accessor, sw).write(c, d)

    def codegen(self, d, ctx=None):
        c = ctx or Context()
        self.write_header(c)
        c.m.sep()
        self.write_import_(c)
        self.write_body(c, d)
        return c.m


class LazyKeywordsRepr(LazyKeywords):
    def _string(self):
        return ", ".join(["{}={}".format(str(k), repr(v)) for k, v in self.kwargs.items()])


def lazy_json_dump(s):
    import json
    return LazyCallString(json.dumps, s)
