from marshmallow import (
    Schema,
    fields,
    INCLUDE,
    RAISE,
)


class Person(Schema):
    name = fields.String(required=True)
    age = fields.Integer()


class Person_AdditionalProperties_True(Schema):
    name = fields.String(required=True)
    age = fields.Integer()

    class Meta:
        unknown = INCLUDE



class Person_AdditionalProperties_False(Schema):
    name = fields.String(required=True)
    age = fields.Integer()

    class Meta:
        unknown = RAISE
