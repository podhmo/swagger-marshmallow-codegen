from marshmallow import (
    Schema,
    fields,
)


class Person(Schema):
    name = fields.String(required=True, description='name of something')
    age = fields.Integer(description='age')
    father = fields.Nested(lambda: Father())
    mother = fields.Nested(lambda: Mother())
    skills = fields.List(fields.Nested(lambda: Skill()))


class Father(Person):
    pass


class Mother(Person):
    pass


class Skill(Schema):
    name = fields.String(required=True)
