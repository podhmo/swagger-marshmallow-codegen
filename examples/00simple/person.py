# -*- coding:utf-8 -*-
from marshmallow import (
    Schema,
    fields
)


class Person(Schema):
    name = fields.String(required=True)
    age = fields.Integer()
