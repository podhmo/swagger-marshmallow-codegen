from marshmallow import (
    Schema,
    fields,
)
from marshmallow.validate import OneOf


class Member(Schema):
    name = fields.String()
    color = fields.String(validate=[OneOf(choices=['r', 'g', 'b'], labels=[])])
    xs = fields.List(fields.String(validate=[OneOf(choices=['x', 'y', 'z'], labels=[])]))
