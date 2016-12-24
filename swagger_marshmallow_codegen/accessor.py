# -*- coding:utf-8 -*-
import logging
import sys
import json
import dictknife
from .langhelpers import titlize
from .dispatcher import Pair
logger = logging.getLogger(__name__)


class Accessor(object):
    def __init__(self):
        self.resolver = Resolver()

    def definitions(self, d):
        return d.get("definitions") or {}

    def properties(self, d):
        return d.get("properties") or {}

    def type_and_format(self, name, field):
        try:
            typ = field["type"]
            format = field.get("format")
            logger.debug("type-and-format: name=%s type=%s, format=%s, field=%s", name, typ, format, lazy_json_dump(field))
            return Pair(type=typ, format=format)
        except KeyError as e:
            logger.debug("%s is not found. name=%s", e.args[0], name)
            if "enum" in field:
                return Pair(type="string", format=None)
            return Pair(type="object", format=None)

    def update_options_pre_properties(self, d, opts):
        for name in d.get("required") or []:
            opts[name]["required"] = True
        return opts

    def update_option_on_property(self, field, opts):
        if "description" in field:
            opts["description"] = field["description"]
        return opts


class Resolver(object):
    def __init__(self):
        self.accessor = dictknife.Accessor()  # todo: rename

    def has_ref(self, d):
        return "$ref" in d

    def has_schema(self, d):
        return d.get("type", None) in ("array", "object", None)

    def has_many(self, d):
        return d.get("type") == "array"

    def resolve_schema_name(self, name):
        schema_name = titlize(name)
        logger.debug("schema: %s", schema_name)
        return schema_name

    def resolve_ref_definition(self, fulldata, d, name=None, i=0, level=-1):
        # return schema_name, definition_dict
        # todo: support quoted "/"
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


class LazyCallString(object):
    def __init__(self, call, *args, **kwargs):
        self.call = call
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        return self.call(*self.args, **self.kwargs)


def lazy_json_dump(s):
    return LazyCallString(json.dumps, s)
