from marshmallow import (
    Schema,
    fields
)
from marshmallow.validate import (
    OneOf
)
from swagger_marshmallow_codegen.validate import MultipleOf


class Person(Schema):
    name = fields.String(required=True)
    money = fields.Integer(validate=[OneOf(choices=[1, 5, 10, 50, 100, 500, 1000, 5000, 10000], labels=[])])
    deposit = fields.Integer(validate=[MultipleOf(n=10000)])
    color = fields.String(required=True, validate=[OneOf(choices=['R', 'G', 'B'], labels=[])])
