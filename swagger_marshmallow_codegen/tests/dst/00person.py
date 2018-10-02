from marshmallow import (
    Schema,
    fields,
)


class Person(Schema):
    name = fields.String()
    age = fields.Integer()

