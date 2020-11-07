from __future__ import annotations
import logging
from functools import partial
from collections import namedtuple
from magicalimport import import_symbol

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
    Pair(type="string", format="date-time"): "marshmallow.fields:AwareDateTime",
    Pair(type="string", format="date"): "marshmallow.fields:Date",
    Pair(type="string", format="time"): "marshmallow.fields:Time",
    Pair(type="string", format="email"): "marshmallow.fields:Email",
    Pair(type="string", format="url"): "marshmallow.fields:URL",
    Pair(type="array", format=None): "marshmallow.fields:List",
    Pair(type="object", format=None): "marshmallow.fields:Nested",
    Pair(type="any", format=None): "marshmallow.fields:Field",
    Pair(type="file", format=None): "marshmallow.fields:Field",
}


class FormatDispatcher:
    type_map = TYPE_MAP

    @classmethod
    def override(cls, type_map):
        return partial(cls, type_map=type_map)

    @classmethod
    def load_def_map(cls, type_map):
        return {pair: import_symbol(path, cwd=True) for pair, path in type_map.items()}

    def __init__(self, type_map=None, use_def_map=True):
        self.type_map = type_map or self.__class__.type_map
        self.def_map = self.load_def_map(self.type_map) if use_def_map else {}

    def dispatch(self, pair, field):
        return self.type_map.get(pair) or self.type_map.get((pair[0], None))

    def handle_validator(self, c, value):
        return ReprWrapValidator(self.dispatch_validator(c, value))

    def dispatch_validator(self, c, value):
        from marshmallow.validate import Length, Regexp, OneOf
        from .validate import Range, MultipleOf, Unique, ItemsRange

        if isinstance(value, (Regexp)):
            c.import_("re")  # xxx
            c.from_("marshmallow.validate", value.__class__.__name__)
        elif isinstance(value, (Length, OneOf)):
            c.from_("marshmallow.validate", value.__class__.__name__)
        elif isinstance(value, (Range, MultipleOf, Unique, ItemsRange)):
            c.from_("swagger_marshmallow_codegen.validate", value.__class__.__name__)
        return value

    def handle_default(self, c, value, field):
        return ReprWrapDefault(self.dispatch_default(c, value, field))

    def dispatch_default(self, c, value, field):
        from datetime import datetime, time, date  # xxx
        from collections import OrderedDict  # xxx

        if isinstance(value, (time, date, datetime)):
            c.import_("datetime")
        elif isinstance(value, OrderedDict):
            c.from_("collections", "OrderedDict")
        return value


class ReprWrap:
    def __init__(self, value):
        self.value = value

    def __getattr__(self, name):
        return getattr(self.value, name)

    @property
    def __class__(self):
        return self.value.__class__


class ReprWrapValidator(ReprWrap):
    def __repr__(self):
        return "{self.__class__.__name__}({args})".format(
            self=self, args=self.value._repr_args()
        )


class ReprWrapDefault(ReprWrap):
    def __repr__(self):
        return "lambda: {self.value!r}".format(self=self)


class ReprWrapString(ReprWrap):
    def __repr__(self):
        return str(self.value)
