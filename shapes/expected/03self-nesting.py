from marshmallow import (
    Schema,
    fields,
)


class Person(Schema):
    name = fields.String(required=True)
    age = fields.Integer()
    father = fields.Nested(lambda: Person())
    mother = fields.Nested(lambda: Person())
