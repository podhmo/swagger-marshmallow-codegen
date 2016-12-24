# -*- coding:utf-8 -*-
import logging
import sys
import json
import dictknife
from .dispatcher import Pair
logger = logging.getLogger(__name__)


class Resolver(object):
    def __init__(self):
        self.accessor = dictknife.Accessor()

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

    def has_ref(self, d):
        return "$ref" in d

    def has_schema(self, d):
        return d.get("type", None) in ("array", "object", None)

    def ref_original(self, fulldata, d, i=0):
        # todo: support quoted "/"
        if "$ref" not in d:
            return d
        logger.debug("%sref: %r", "  " * i, d["$ref"])
        path = d["$ref"][len("#/"):].split("/")
        parent = self.accessor.maybe_access_container(fulldata, path)
        if parent is None:
            sys.stderr.write("\t{!r} is not found\n".format(d["$ref"]))
            return d
        return self.ref_original(fulldata, parent[path[-1]], i=i + 1)


class LazyCallString(object):
    def __init__(self, call, *args, **kwargs):
        self.call = call
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        return self.call(*self.args, **self.kwargs)


def lazy_json_dump(s):
    return LazyCallString(json.dumps, s)
