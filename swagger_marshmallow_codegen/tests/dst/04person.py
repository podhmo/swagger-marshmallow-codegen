# -*- coding:utf-8 -*-
from marshmallow import (
    Schema,
    fields
)


class Person(Schema):
    name = fields.String(required=True, description='name of something')
    age = fields.Integer(description='age')
    father = fields.Nested('self')
    mother = fields.Nested('self')
    skills = fields.List(fields.Nested('Skill', ))


class Skill(Schema):
    name = fields.String(required=True)
