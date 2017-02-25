# -*- coding:utf-8 -*-
from marshmallow import (
    Schema,
    fields
)


class Person0(Schema):
    """original (no. 1)"""
    name = fields.String()


class Mix(Schema):
    """no. 2"""
    age = fields.Integer()


class Person(Person0, Mix):
    pass
