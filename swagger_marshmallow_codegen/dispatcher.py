# -*- coding:utf-8 -*-
import logging
from collections import namedtuple
from .langhelpers import load_function
logger = logging.getLogger(__name__)


Pair = namedtuple("Pair", "type,format")

# TODO: correct mapping

# http://apispec.readthedocs.io/en/latest/_modules/apispec/ext/marshmallow/swagger.html
TYPE_MAP = {
    Pair(type="integer", format="int32"): "marshmallow.fields:Integer",
    Pair(type="number", format=None): "marshmallow.fields:Number",
    Pair(type="number", format="float"): "marshmallow.fields:Float",
    Pair(type="number", format="decimal"): "marshmallow.fields:Decimal",  # not matched
    Pair(type="number", format="integer"): "marshmallow.fields:Integer",
    Pair(type="integer", format=None): "marshmallow.fields:Integer",  # swagger
    Pair(type="string", format=None): "marshmallow.fields:String",
    Pair(type="boolean", format=None): "marshmallow.fields:Boolean",
    Pair(type="string", format="uuid"): "marshmallow.fields:UUID",
    Pair(type="string", format="date-time"): "swagger_marshmallow_codegen.fields:DateTime",
    Pair(type="string", format="date"): "swagger_marshmallow_codegen.fields:Date",
    Pair(type="string", format="time"): "swagger_marshmallow_codegen.fields:Time",
    Pair(type="string", format="email"): "marshmallow.fields:Email",
    Pair(type="string", format="url"): "marshmallow.fields:URL",

    Pair(type="object", format=None): "marshmallow.fields:Nested",
    Pair(type="any", format=None): "marshmallow.fields:Field",
}


class FormatDispatcher(object):
    path_map = TYPE_MAP
    def_map = None  # singleton

    @classmethod
    def load_def_map(cls, path_map):
        return {pair: load_function(path) for pair, path in path_map.items()}

    def __init__(self):
        if self.__class__.def_map is None:
            self.__class__.load_def_map(self.__class__.path_map)

    def dispatch(self, pair, field):
        if pair.type == "object" and len(field) <= 1:
            return "marshmallow.fields:Field"
        return self.path_map.get(pair) or self.path_map.get((pair[0], None))
