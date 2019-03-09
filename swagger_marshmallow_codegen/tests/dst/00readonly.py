from marshmallow import (
    Schema,
    fields
)


class Foo(Schema):
    value0 = fields.String()
    value1 = fields.String()
    value2 = fields.String(dump_only=True)
