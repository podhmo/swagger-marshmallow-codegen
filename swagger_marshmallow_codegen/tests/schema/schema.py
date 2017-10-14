from marshmallow import (
    Schema,
    fields,
)


class Person(Schema):
    name = fields.String(required=True)
    age = fields.Integer(required=True)


class Group(Schema):
    name = fields.String(required=True)
    members = fields.List(fields.Nested('Person'), required=True)
