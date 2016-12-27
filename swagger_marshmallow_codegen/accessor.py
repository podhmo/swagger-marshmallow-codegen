# -*- coding:utf-8 -*-
import logging
import sys
import json
import dictknife
from datetime import (datetime, time, date)  # xxx
from collections import OrderedDict  # xxx
from .langhelpers import titleize, normalize
from .dispatcher import Pair
from . import validate
logger = logging.getLogger(__name__)


class Accessor(object):
    def __init__(self):
        self.resolver = Resolver()

    def definitions(self, d):
        return d.get("definitions") or {}

    def properties(self, d):
        return d.get("properties") or {}

    def type_and_format(self, name, field, ignore_array=True):
        try:
            if self.resolver.has_many(field):
                return self.type_and_format(name, field["items"])
            typ = field["type"]
            format = field.get("format")
            logger.debug("type-and-format: name=%s type=%s, format=%s, field=%s", name, typ, format, lazy_json_dump(field))
            return Pair(type=typ, format=format)
        except KeyError as e:
            logger.debug("%s is not found. name=%s", e.args[0], name)
            if "enum" in field:
                return Pair(type="string", format=None)
            if not field:
                return Pair(type="any", format=None)
            return Pair(type="object", format=None)

    def update_options_pre_properties(self, d, opts):
        for name in d.get("required") or []:
            opts[name]["required"] = True
        return opts

    def update_option_on_property(self, c, field, opts):
        if "description" in field:
            opts["description"] = field["description"]
        if self.resolver.has_many(field):
            opts["many"] = True
        if "default" in field:
            # todo: import on datetime.datetime etc...
            self.attach_import(c, field["default"])
            opts["missing"] = field["default"]  # xxx

        validators = self.resolver.resolve_validators_on_property(c, field)
        if validators:
            opts["validate"] = validators
        return opts

    def attach_import(self, c, value):
        # xxx:
        if isinstance(value, (time, date, datetime)):
            c.im.import_("datetime")
        if isinstance(value, OrderedDict):
            c.im.from_("collections", "OrderedDict")


class _ReprWrap(object):
    def __init__(self, value, c, on_repr):
        self.value = value
        self.c = c
        self.on_repr = on_repr

    def __repr__(self):
        self.on_repr(self)
        return repr(self.value)

    def __getattr__(self, name):
        return getattr(self.value, name)

    @property
    def __class__(self):
        return self.value.__class__


class Resolver(object):
    def __init__(self):
        self.accessor = dictknife.Accessor()  # todo: rename

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
        schema_name = titleize(name)
        logger.debug("schema: %s", schema_name)
        return schema_name

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

        logger.debug("%sref: %r", "  " * i, d["$ref"])

        path = d["$ref"][len("#/"):].split("/")
        name = path[-1]

        parent = self.accessor.maybe_access_container(fulldata, path)
        if parent is None:
            sys.stderr.write("\t{!r} is not found\n".format(d["$ref"]))
            return self.resolve_schema_name(name), d
        return self.resolve_ref_definition(fulldata, parent[name], name=name, i=i + 1, level=level - 1)

    def resolve_validators_on_property(self, c, field):
        validators = []
        # range
        if "minimum" in field or "maximum" in field:
            range_opts = dict(c=c)
            range_opts["min"] = field.get("minimum")
            range_opts["exclusive_min"] = field.get("exclusiveMinimum", False)
            range_opts["max"] = field.get("maximum")
            range_opts["exclusive_max"] = field.get("exclusiveMaximum", False)
            validators.append(validate.RangeWithRepr(**range_opts))
        if "minLength" in field or "maxLength" in field:
            length_opts = dict(c=c)
            length_opts["min"] = field.get("minLength")
            length_opts["max"] = field.get("maxLength")
            validators.append(validate.LengthWithRepr(**length_opts))
        if "pattern" in field:
            regex_opts = dict(c=c)
            regex_opts["regex"] = field["pattern"]
            validators.append(validate.RegexpWithRepr(**regex_opts))
        if "enum" in field:
            enum_opts = dict(c=c)
            enum_opts["choices"] = field["enum"]
            validators.append(validate.OneOfWithRepr(**enum_opts))
        if "multipleOf" in field:
            multipleof_opts = dict(c=c)
            multipleof_opts["n"] = field["multipleOf"]
            validators.append(validate.MultipleOfWithRepr(**multipleof_opts))
        if "maxItems" in field or "minItems" in field:
            itemrange_opts = dict(c=c)
            itemrange_opts["max"] = field.get("maxItems")
            itemrange_opts["min"] = field.get("minItems")
            validators.append(validate.ItemsRangeWithRepr(**itemrange_opts))
        if field.get("uniqueItems", False):
            validators.append(validate.UniqueWithRepr(c=c))
        # xxx:
        for v in validators:
            repr(v)
        return validators


class LazyCallString(object):
    def __init__(self, call, *args, **kwargs):
        self.call = call
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        return self.call(*self.args, **self.kwargs)


def lazy_json_dump(s):
    return LazyCallString(json.dumps, s)
