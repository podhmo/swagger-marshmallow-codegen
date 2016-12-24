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

    def type_and_format(self, field):
        typ = field["type"]
        format = field.get("format")
        logger.debug("type-and-format: type=%s, format=%s, field=%s", typ, format, lazy_json_dump(field))
        return Pair(type=typ, format=format)

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
        return titlize(name)

    def resolve_ref_definition(self, fulldata, d, name=None, i=0):
        # return schema_name, definition_dict
        # todo: support quoted "/"
        if "$ref" not in d:
            return name, d
        logger.debug("%sref: %r", "  " * i, d["$ref"])

        path = d["$ref"][len("#/"):].split("/")
        name = path[-1]

        parent = self.accessor.maybe_access_container(fulldata, path)
        if parent is None:
            sys.stderr.write("\t{!r} is not found\n".format(d["$ref"]))
            return name, d
        return self.resolve_ref_definition(fulldata, parent[name], name=self.resolve_schema_name(name), i=i + 1)


class LazyCallString(object):
    def __init__(self, call, *args, **kwargs):
        self.call = call
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        return self.call(*self.args, **self.kwargs)


def lazy_json_dump(s):
    return LazyCallString(json.dumps, s)
