# -*- coding:utf-8 -*-
from marshmallow import (
    Schema,
    fields
)


class Person0(Schema):
    """original (no. 1)"""
    name = fields.String()


class Person(Person0):
    """no. 4"""
    age = fields.Integer()
