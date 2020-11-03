from marshmallow import (
    Schema,
    fields,
)
import datetime
from collections import OrderedDict


class X(Schema):
    string = fields.String(missing=lambda: 'default')
    integer = fields.Integer(missing=lambda: 10)
    boolean = fields.Boolean(missing=lambda: True)
    datetime = fields.AwareDateTime(missing=lambda: datetime.datetime(2000, 1, 1, 1, 1, 1, tzinfo=datetime.timezone.utc))
    object = fields.Nested(lambda: XObject(), missing=lambda: OrderedDict([('name', 'foo'), ('age', 20)]))
    array = fields.List(fields.Integer(), missing=lambda: [1, 2, 3])


class XObject(Schema):
    name = fields.String(missing=lambda: 'foo')
    age = fields.Integer(missing=lambda: 20)
