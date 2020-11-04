from marshmallow import (
    Schema,
    fields,
)


class Person(Schema):
    name = fields.String(required=True)
    age = fields.Integer(required=True)
    data = fields.Dict(keys=fields.String(), values=fields.String())
