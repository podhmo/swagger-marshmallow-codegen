from marshmallow import (
    Schema,
    fields,
)


class Person(Schema):
    name = fields.String(required=True, description='name of something')
    age = fields.Integer(description='age')
    father = fields.Nested(lambda: Person())
    mother = fields.Nested(lambda: Person())
    skills = fields.List(fields.Nested(lambda: Skill()))


class Skill(Schema):
    name = fields.String(required=True)
