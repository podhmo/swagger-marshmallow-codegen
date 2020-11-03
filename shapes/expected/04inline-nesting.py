from marshmallow import (
    Schema,
    fields,
)


class Person(Schema):
    age = fields.Integer()
    memo = fields.Nested(lambda: PersonMemo(), required=True)
    name = fields.String(required=True)


class PersonMemo(Schema):
    content = fields.String(required=True)
    title = fields.String(required=True)
