from marshmallow import (
    Schema,
    fields,
)


class Person(Schema):
    name = fields.String(required=True)
    age = fields.Integer()
    memo = fields.Nested(lambda: Memo(), required=True)


class Memo(Schema):
    title = fields.String(required=True)
    content = fields.String(required=True)
