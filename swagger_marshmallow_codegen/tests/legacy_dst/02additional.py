from marshmallow import (
    Schema,
    fields,
)


class S(Schema):
    x = fields.Dict(keys=fields.String(), values=fields.Integer())
    y = fields.Dict(keys=fields.String(), values=fields.Integer())
    z = fields.Dict(keys=fields.String(), values=fields.Integer())
