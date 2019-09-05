import keyword
import logging
from collections import namedtuple
from functools import partial
from prestring import PreString
from prestring.python import Module
from prestring.utils import LazyFormat, LazyKeywordsRepr
from dictknife import deepequal, deepmerge
from collections import defaultdict
from collections import OrderedDict
from .langhelpers import LazyCallString, titleize, clsname_from_path

logger = logging.getLogger(__name__)
NAME_MARKER = "x-marshmallow-name"


class Context:
    def __init__(self, m=None, im=None):
        self.m = m or Module(import_unique=True)
        self.im = im or self.m.submodule()

    def from_(self, module, name):
        logger.debug("      import: module=%s, name=%s", module, name)
        self.im.from_(module, name)

    def import_(self, module):
        logger.debug("      import: module=%s", module)
        self.im.import_(module)

    def new_child(self):
        return self.__class__(self.m.submodule(newline=False), self.im)


class CodegenError(Exception):
    pass


class SchemaWriter:
    extra_schema_module = "swagger_marshmallow_codegen.schema"

    def __init__(self, accessor, schema_class, *, extra_schema_module=None):
        self.accessor = accessor
        self.schema_class = schema_class
        self.arrived = set()
        self.extra_schema_module = (
            extra_schema_module or self.__class__.extra_schema_module
        )

    @classmethod
    def override(cls, extra_schema_module):
        return partial(cls, extra_schema_module=extra_schema_module)

    @property
    def resolver(self):
        return self.accessor.resolver

    def write_field_one(
        self, c, d, schema_name, definition, name, field, opts, wrap=None
    ):
        field_class_name = None
        if self.resolver.has_ref(field):
            field_class_name, field = self.resolver.resolve_ref_definition(
                d, field, level=1
            )
            if field_class_name == schema_name and deepequal(field, definition):
                field_class_name = "self"

            if self.resolver.has_many(field):
                return self.write_field_many(
                    c, d, field_class_name, definition, name, field, opts
                )

            # finding original definition
            if self.resolver.has_ref(field):
                ref_name, field = self.resolver.resolve_ref_definition(d, field)
                if self.resolver.has_many(field):
                    return self.write_field_many(
                        c, d, field_class_name, definition, name, field, opts
                    )
                if ref_name is None:
                    raise CodegenError("ref: %r is not found", field["$ref"])

        logger.debug("      field: %s", lazy_json_dump(field))
        self.accessor.update_option_on_property(c, field, opts)
        caller_name = self.accessor.resolver.resolve_caller_name(c, name, field)
        if caller_name is None:
            raise CodegenError(
                "matched field class is not found. name=%r, schema=%r",
                name,
                schema_name,
            )

        normalized_name = self.resolver.resolve_normalized_name(name)
        if normalized_name != name:
            opts["data_key"] = name
        if keyword.iskeyword(normalized_name) or normalized_name == "fields":
            opts["data_key"] = normalized_name
            normalized_name = normalized_name + "_"

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
        logger.info("  write field: write %s, field=%s", name, caller_name)
        if wrap is not None:
            value = wrap(value)
        c.m.stmt(LazyFormat("{} = {}", normalized_name, value))

    def write_field_many(self, c, d, schema_name, definition, name, field, opts):
        self.accessor.update_option_on_property(c, field, opts)
        opts.pop("many", None)

        caller_name = self.accessor.resolver.resolve_caller_name(c, name, field)
        if caller_name is None:
            raise CodegenError(
                "matched field class is not found. name=%r, schema=%r",
                name,
                schema_name,
            )

        normalized_name = self.resolver.resolve_normalized_name(name)
        if normalized_name != name:
            opts["data_key"] = name
        if keyword.iskeyword(normalized_name) or normalized_name == "fields":
            opts["data_key"] = normalized_name
            normalized_name = normalized_name + "_"

        def wrap(value, opts=opts):
            if opts:
                return LazyFormat(
                    "{}({}, {})", caller_name, value, LazyKeywordsRepr(opts)
                )
            else:
                return LazyFormat("{}({})", caller_name, value)

        field = field["items"]
        return self.write_field_one(
            c,
            d,
            schema_name,
            definition,
            normalized_name,
            field,
            OrderedDict(),
            wrap=wrap,
        )

    def write_primitive_schema(self, c, d, clsname, definition, many=False):
        c.im.from_(self.extra_schema_module, "PrimitiveValueSchema")
        with c.m.class_(clsname, "PrimitiveValueSchema"):
            with c.m.class_("schema_class", self.schema_class):
                if many or self.resolver.has_many(definition):
                    definition["type"] = "array"
                    self.write_field_many(c, d, clsname, {}, "value", definition, {})
                else:
                    self.write_field_one(c, d, clsname, {}, "value", definition, {})

    def write_schema(
        self, c, d, clsname, definition, force=False, meta_writer=None, many=False
    ):
        if not force and clsname in self.arrived:
            return
        self.arrived.add(clsname)
        base_classes = [self.schema_class]
        if self.resolver.has_ref(definition):
            ref_name, ref_definition = self.resolver.resolve_ref_definition(
                d, definition
            )
            if ref_name is None:
                raise CodegenError("$ref %r is not found", definition["$ref"])
            elif "items" in ref_definition:
                # work around
                many = True
                items = ref_definition["items"]
                if self.resolver.has_ref(items):
                    _, items = self.resolver.resolve_ref_definition(
                        d, ref_definition["items"]
                    )
                if not self.resolver.has_schema(d, items):
                    return self.write_primitive_schema(
                        c, d, clsname, ref_definition, many=many
                    )
                else:
                    self.write_schema(c, d, ref_name, items)
                    base_classes = [ref_name]
            else:
                if not self.resolver.has_schema(d, ref_definition):
                    return self.write_primitive_schema(
                        c, d, clsname, ref_definition, many=many
                    )
                self.write_schema(c, d, ref_name, ref_definition)
                base_classes = [ref_name]
        elif self.resolver.has_allof(definition):
            ref_list, ref_definition = self.resolver.resolve_allof_definition(
                d, definition
            )
            definition = deepmerge(ref_definition, definition)
            if ref_list:
                base_classes = []
                for ref_name, ref_definition in ref_list:
                    if ref_name is None:
                        raise CodegenError(
                            "$ref %r is not found", ref_definition
                        )  # xxx
                    else:
                        self.write_schema(c, d, ref_name, ref_definition)
                        base_classes.append(ref_name)

        # supporting additional properties
        if (
            "additionalProperties" in definition
            and base_classes[0] == self.schema_class
        ):
            c.from_(self.extra_schema_module, "AdditionalPropertiesSchema")
            base_classes[0] = "AdditionalPropertiesSchema"

        if "properties" not in definition and (
            "object" != definition.get("type", "object") and "items" not in definition
        ):
            return self.write_primitive_schema(c, d, clsname, definition, many=many)

        if "items" in definition:
            many = True
            if not self.resolver.has_ref(definition["items"]):
                return self.write_primitive_schema(c, d, clsname, definition, many=many)
            else:
                ref_name, ref_definition = self.resolver.resolve_ref_definition(
                    d, definition["items"]
                )
                if ref_name is None:
                    return self.write_primitive_schema(
                        c, d, clsname, definition, many=many
                    )
                else:
                    self.write_schema(c, d, ref_name, ref_definition)
                    base_classes = [ref_name]

        with c.m.class_(clsname, bases=base_classes):
            if "description" in definition:
                c.m.stmt('"""{}"""'.format(definition["description"]))

            if meta_writer is not None:
                meta_writer(c.m)

            if many or self.resolver.has_many(definition):
                with c.m.def_("__init__", "self", "*args", "**kwargs"):
                    c.m.stmt("kwargs['many'] = True")
                    c.m.stmt("super().__init__(*args, **kwargs)")

            opts = defaultdict(OrderedDict)
            self.accessor.update_options_pre_properties(definition, opts)

            properties = self.accessor.properties(definition)
            need_pass_statement = False
            if not properties and not many:
                need_pass_statement = True
            else:
                for name, field in properties.items():
                    name = str(name)
                    if self.resolver.has_many(field):
                        self.write_field_many(
                            c, d, clsname, definition, name, field, opts[name]
                        )
                    else:
                        self.write_field_one(
                            c, d, clsname, definition, name, field, opts[name]
                        )

            # supporting additional properties
            subdef = definition.get("additionalProperties")
            if subdef and hasattr(subdef, "keys"):
                need_pass_statement = False
                c.m.sep()
                subdef = definition["additionalProperties"]
                with c.m.class_("Meta"):
                    if self.resolver.has_ref(subdef):
                        ref_name, _ = self.resolver.resolve_ref_definition(d, subdef)
                        if ref_name is None:
                            raise CodegenError("$ref %r is not found", subdef["$ref"])
                        self.write_field_one(
                            c,
                            d,
                            ref_name,
                            {},
                            "additional_field",
                            subdef,
                            OrderedDict(),
                        )
                    elif self.resolver.has_many(subdef):
                        self.write_field_many(
                            c, d, "", subdef, "additional_field", subdef, OrderedDict()
                        )
                    else:
                        self.write_field_one(
                            c, d, "", subdef, "additional_field", subdef, OrderedDict()
                        )

            if need_pass_statement:
                c.m.stmt("pass")


class DefinitionsSchemaWriter:
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


class PathsSchemaWriter:
    OVERRIDE_NAME_MARKER = NAME_MARKER

    def __init__(self, accessor, schema_writer):
        self.accessor = accessor
        self.schema_writer = schema_writer

    @property
    def resolver(self):
        return self.accessor.resolver

    def get_lazy_clsname(self, path):
        return PreString(clsname_from_path(path))

    def write(self, c, d):
        for path, methods in self.accessor.paths(d):
            sc = c.new_child()
            found = False
            lazy_clsname = self.get_lazy_clsname(path)
            with sc.m.class_(LazyFormat("{}Input", lazy_clsname)):
                toplevel_parameters = self.accessor.parameters(methods)
                if self.OVERRIDE_NAME_MARKER in methods:
                    lazy_clsname.pop()
                    lazy_clsname.append(methods[self.OVERRIDE_NAME_MARKER])
                for method, definition in self.accessor.methods(methods):
                    ssc = sc.new_child()
                    with ssc.m.class_(titleize(method)):
                        if "summary" in definition or "description" in definition:
                            ssc.m.stmt('"""')
                            if "summary" in definition:
                                for line in (
                                    definition["summary"].rstrip("\n").split("\n")
                                ):
                                    ssc.m.stmt(line)
                            elif "description" in definition:
                                for line in (
                                    definition["description"].rstrip("\n").split("\n")
                                ):
                                    ssc.m.stmt(line)
                            ssc.m.stmt('"""')
                            ssc.m.stmt("")

                        path_info = self.build_path_info(
                            d, toplevel_parameters, self.accessor.parameters(definition)
                        )
                        for section, properties in sorted(path_info.info.items()):
                            if section is None:
                                continue
                            clsname = titleize(section)
                            if section == "body":
                                definition = next(iter(properties.values()))["schema"]
                                self.schema_writer.write_schema(
                                    ssc, d, clsname, definition, force=True
                                )
                            else:
                                definition = {
                                    "properties": properties,
                                    "required": path_info.required[section],
                                }
                                self.schema_writer.write_schema(
                                    ssc, d, clsname, definition, force=True
                                )
                        if path_info and not path_info.info:
                            ssc.m.stmt("pass")

                    if not path_info:
                        ssc.m.clear()
                    found = found or bool(path_info)
            if not found:
                sc.m.clear()

    PathInfo = namedtuple("PathInfo", "info, required")

    def build_path_info(self, fulldata, *paramaters_set):
        info = defaultdict(OrderedDict)
        required = defaultdict(list)
        for parameters in paramaters_set:
            for p in parameters:
                if self.resolver.has_ref(p):
                    _, p = self.resolver.resolve_ref_definition(fulldata, p)
                name = p.get("name")
                section = p.get("in")
                info[section][name] = p
                if p.get("required"):
                    required[section].append(name)
        return self.PathInfo(info=info, required=required)


class ResponsesSchemaWriter:
    OVERRIDE_NAME_MARKER = NAME_MARKER

    def __init__(self, accessor, schema_writer):
        self.accessor = accessor
        self.schema_writer = schema_writer

    @property
    def resolver(self):
        return self.accessor.resolver

    # todo: move
    def get_lazy_clsname(self, path):
        return PreString(clsname_from_path(path))

    def write(self, c, d):
        for path, methods in self.accessor.paths(d):
            lazy_clsname = self.get_lazy_clsname(path)
            sc = c.new_child()
            found = False
            with sc.m.class_(LazyFormat("{}Output", lazy_clsname)):
                if self.OVERRIDE_NAME_MARKER in methods:
                    lazy_clsname.pop()
                    lazy_clsname.append(methods[self.OVERRIDE_NAME_MARKER])
                for method, definition in self.accessor.methods(methods):
                    for status, definition in self.accessor.responses(definition):
                        if self.resolver.has_ref(definition):
                            _, definition = self.resolver.resolve_ref_definition(
                                d, definition
                            )
                        if "schema" in definition:
                            found = True
                            clsname = titleize(method) + status
                            schema_definition = definition["schema"]

                            def meta(m):
                                if "description" in definition:
                                    m.stmt('"""{}"""'.format(definition["description"]))

                            self.schema_writer.write_schema(
                                sc,
                                d,
                                clsname,
                                schema_definition,
                                force=True,
                                meta_writer=meta,
                            )
            if not found:
                sc.m.clear()


class Codegen:
    schema_class_path = "marshmallow:Schema"
    schema_writer_factory = SchemaWriter

    @classmethod
    def override(cls, *, schema_class_path=None, schema_writer_factory=None):
        return partial(
            cls,
            schema_class_path=schema_class_path,
            schema_writer_factory=schema_writer_factory,
        )

    def __init__(self, accessor, *, schema_class_path=None, schema_writer_factory=None):
        self.accessor = accessor
        self.schema_class_path = schema_class_path or self.__class__.schema_class_path
        self.schema_writer_factory = (
            schema_writer_factory or self.__class__.schema_writer_factory
        )
        self.schema_class = self.schema_class_path.rsplit(":", 1)[-1]

    @property
    def resolver(self):
        return self.accessor.resolver

    def write_header(self, c, test):
        if not test:
            c.im.stmt("# -*- coding:utf-8 -*-")
            c.im.stmt("# this is auto-generated by swagger-marshmallow-codegen")

    def write_import_(self, c):
        c.from_(*self.schema_class_path.rsplit(":", 1))
        c.from_("marshmallow", "fields")

    def write_body(self, c, d, targets):
        sw = self.schema_writer_factory(self.accessor, self.schema_class)
        if targets.get("schema", False):
            DefinitionsSchemaWriter(self.accessor, sw).write(c.new_child(), d)
        if targets.get("input", False):
            PathsSchemaWriter(self.accessor, sw).write(c.new_child(), d)
        if targets.get("output", False):
            ResponsesSchemaWriter(self.accessor, sw).write(c.new_child(), d)

    def codegen(self, d, targets, ctx=None, test=False):
        c = ctx or Context()
        self.write_header(c, test=test)
        c.m.sep()
        self.write_import_(c)
        self.write_body(c, d, targets)
        return c.m


def lazy_json_dump(s):
    import json

    return LazyCallString(json.dumps, s)
