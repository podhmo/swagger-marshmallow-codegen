from marshmallow import (
    Schema,
    fields,
)


class Stat(Schema):
    days = fields.List(fields.Integer())
    days2 = fields.List(fields.Integer())
    total = fields.Integer()
    week = fields.Integer()
