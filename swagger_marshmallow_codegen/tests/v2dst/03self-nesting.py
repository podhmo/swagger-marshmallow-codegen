from marshmallow import (
    Schema,
    fields,
)


class Person(Schema):
    name = fields.String(required=True)
    age = fields.Integer()
    father = fields.Field(lambda: Person)
    mother = fields.Field(lambda: Person)
