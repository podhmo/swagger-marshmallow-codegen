# -*- coding:utf-8 -*-
import logging
import sys
import dictknife
from .langhelpers import titleize, normalize
from .dispatcher import Pair, FormatDispatcher
from . import validate
logger = logging.getLogger(__name__)


class Accessor(object):
    def __init__(self):
        self.resolver = Resolver()

    def definitions(self, d):
        return d.get("definitions") or {}

    def properties(self, d):
        return d.get("properties") or {}

    def update_options_pre_properties(self, d, opts):
        for name in d.get("required") or []:
            opts[name]["required"] = True
        return opts

    def update_option_on_property(self, c, field, opts):
        if "description" in field:
            opts["description"] = field["description"]
        if self.resolver.has_many(field):
            logger.debug("    resolve: many=True")
            opts["many"] = True
        if "default" in field:
            logger.debug("    resolve: default=%r", field["default"])
            opts["missing"] = self.import_handler.handle_default_value(c, field["default"])  # xxx

        validators = self.resolver.resolve_validators_on_property(c, field)
        if validators:
            opts["validate"] = validators
        return opts

    @property
    def import_handler(self):
        return self.resolver.import_handler


class Resolver(object):
    def __init__(self):
        self.accessor = dictknife.Accessor()  # todo: rename
        self.dispatcher = FormatDispatcher()
        self.import_handler = ImportHandler()

    def has_ref(self, d):
        return "$ref" in d

    def has_schema(self, fulldata, d, cand=("object",), fullscan=True):
        typ = d.get("type", None)
        if typ in cand:
            return True
        if "properties" in d:
            return True
        if not self.has_ref(d):
            return False
        if not fullscan:
            return False
        _, definition = self.resolve_ref_definition(fulldata, d)
        return self.has_schema(fulldata, definition, fullscan=False)

    def has_nested(self, fulldata, d):
        if self.has_schema(fulldata, d, fullscan=False):
            return True
        return self.has_many(d) and self.has_schema(fulldata, d["items"])

    def has_many(self, d):
        return d.get("type") == "array" or "items" in d

    def resolve_normalized_name(self, name):
        return normalize(name)

    def resolve_schema_name(self, name):
        return titleize(name)

    def resolve_type_and_format(self, name, field, ignore_array=True):
        try:
            if self.has_many(field):
                return self.resolve_type_and_format(name, field["items"])
            typ = field["type"]
            format = field.get("format")
            return Pair(type=typ, format=format)
        except KeyError as e:
            logger.debug("%s is not found. name=%s", e.args[0], name)
            if "enum" in field:
                return Pair(type="string", format=None)
            if not field:
                return Pair(type="any", format=None)
            return Pair(type="object", format=None)

    def resolve_caller_name(self, c, field_name, field):
        pair = self.resolve_type_and_format(field_name, field)
        logger.debug("    resolve: type=%s, format=%s", pair.type, pair.format)

        path = self.dispatcher.dispatch(pair, field)
        if path is None:
            return None

        module, cls_name = path.rsplit(":", 1)
        if module == "marshmallow.fields":
            caller_name = "{}.{}".format("fields", cls_name)  # xxx:
        else:
            c.from_(module, cls_name)  # xxx
            caller_name = cls_name
        logger.debug("    resolve: field=%s", caller_name)
        return caller_name

    def resolve_ref_definition(self, fulldata, d, name=None, i=0, level=-1):
        # return schema_name, definition_dict
        # todo: support quoted "/"
        # on array
        if "items" in d:
            definition = d
            name, _ = self.resolve_ref_definition(fulldata, d["items"], name=name, i=i, level=level + 1)  # xxx
            return name, definition

        if "$ref" not in d:
            return self.resolve_schema_name(name), d
        if level == 0:
            return self.resolve_schema_name(name), d

        logger.debug("    resolve: %sref=%r", "  " * i, d["$ref"])

        path = d["$ref"][len("#/"):].split("/")
        name = path[-1]

        parent = self.accessor.maybe_access_container(fulldata, path)
        if parent is None:
            sys.stderr.write("\t{!r} is not found\n".format(d["$ref"]))
            return self.resolve_schema_name(name), d
        return self.resolve_ref_definition(fulldata, parent[name], name=name, i=i + 1, level=level - 1)

    def resolve_validators_on_property(self, c, field):
        validators = []

        def add(validator):
            logger.debug("    resolve: validator=%s", validator.__class__.__name__)
            return validators.append(self.import_handler.handle_validator(c, validator))

        # range
        if "minimum" in field or "maximum" in field:
            range_opts = {
                "min": field.get("minimum"),
                "exclusive_min": field.get("exclusiveMinimum", False),
                "max": field.get("maximum"),
                "exclusive_max": field.get("exclusiveMaximum", False),
            }
            add(validate.Range(**range_opts))
        if "minLength" in field or "maxLength" in field:
            length_opts = {
                "min": field.get("minLength"),
                "max": field.get("maxLength")
            }
            add(validate.Length(**length_opts))
        if "pattern" in field:
            regex_opts = {
                "regex": field["pattern"]
            }
            add(validate.Regexp(**regex_opts))
        if "enum" in field:
            enum_opts = {
                "choices": field["enum"]
            }
            add(validate.OneOf(**enum_opts))
        if "multipleOf" in field:
            multipleof_opts = {
                "n": field["multipleOf"]
            }
            add(validate.MultipleOf(**multipleof_opts))
        if "maxItems" in field or "minItems" in field:
            itemrange_opts = {
                "max": field.get("maxItems"),
                "min": field.get("minItems"),
            }
            add(validate.ItemsRange(**itemrange_opts))
        if field.get("uniqueItems", False):
            add(validate.Unique())
        return validators


class ImportHandler(object):
    def handle_validator(self, c, value):
        from marshmallow.validate import (
            Length,
            Regexp,
            OneOf,
        )
        from .validate import (
            Range,
            MultipleOf,
            Unique,
            ItemsRange
        )
        if isinstance(value, (Regexp)):
            c.import_("re")  # xxx
            c.from_("marshmallow.validate", value.__class__.__name__)
        elif isinstance(value, (Length, OneOf)):
            c.from_("marshmallow.validate", value.__class__.__name__)
        elif isinstance(value, (Range, MultipleOf, Unique, ItemsRange)):
            c.from_("swagger_marshmallow_codegen.validate", value.__class__.__name__)
        return _ReprWrapValidator(value)

    def handle_default_value(self, c, value):
        from datetime import (datetime, time, date)  # xxx
        from collections import OrderedDict  # xxx
        if isinstance(value, (time, date, datetime)):
            c.import_("datetime")
        elif isinstance(value, OrderedDict):
            c.from_("collections", "OrderedDict")
        return _ReprWrapDefault(value)


class _ReprWrap(object):
    def __init__(self, value):
        self.value = value

    def __getattr__(self, name):
        return getattr(self.value, name)

    @property
    def __class__(self):
        return self.value.__class__


class _ReprWrapValidator(_ReprWrap):
    def __repr__(self):
        return "{self.__class__.__name__}({args})".format(self=self, args=self.value._repr_args())


class _ReprWrapDefault(_ReprWrap):
    def __repr__(self):
        return "lambda: {self.value!r}".format(self=self)
