from marshmallow import (
    Schema,
    fields,
)
import datetime
from swagger_marshmallow_codegen.fields import DateTime


class X(Schema):
    string = fields.String(missing=lambda: 'default')
    integer = fields.Integer(missing=lambda: 10)
    boolean = fields.Boolean(missing=lambda: True)
    datetime = DateTime(missing=lambda: datetime.datetime(2000, 1, 1, 1, 1, 1))
    object = fields.Nested('XObject', missing=lambda: {'name': 'foo', 'age': 20})
    array = fields.List(fields.Integer(), missing=lambda: [1, 2, 3])


class XObject(Schema):
    name = fields.String(missing=lambda: 'foo')
    age = fields.Integer(missing=lambda: 20)
