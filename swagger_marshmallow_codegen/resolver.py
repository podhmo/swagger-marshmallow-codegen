# -*- coding:utf-8 -*-
import logging
import json
from .dispatcher import Pair
logger = logging.getLogger(__name__)


class Resolver(object):
    def resolve_definitions(self, d):
        return d.get("definitions") or {}

    def resolve_properties(self, d):
        return d.get("properties") or {}

    def resolve_type_and_format(self, field):
        typ = field["type"]
        format = field.get("format")
        logger.debug("dispatch type=%s, format=%s, field=%s", typ, format, lazy_json_dump(field))
        return Pair(type=typ, format=format)

    def resolve_options_pre_properties(self, d, opts):
        for name in d.get("required") or []:
            opts[name]["required"] = True
        return opts


class LazyCallString(object):
    def __init__(self, call, *args, **kwargs):
        self.call = call
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        return self.call(*self.args, **self.kwargs)


def lazy_json_dump(s):
    return LazyCallString(json.dumps, s)
