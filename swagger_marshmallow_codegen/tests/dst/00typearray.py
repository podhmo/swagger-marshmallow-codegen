# -*- coding:utf-8 -*-
from marshmallow import (
    Schema,
    fields
)


class Foo(Schema):
    value0 = fields.String()
    value1 = fields.String(allow_none=True)
    value2 = fields.String(allow_none=True)
    value3 = fields.String()
    value4 = fields.Integer()
