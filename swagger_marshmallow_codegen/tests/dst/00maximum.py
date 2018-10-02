from marshmallow import (
    Schema,
    fields,
)
from swagger_marshmallow_codegen.validate import (
    Range,
)


class X(Schema):
    n0 = fields.Number(validate=[Range(min=None, max=100, exclusive_min=False, exclusive_max=False)])
    n1 = fields.Number(validate=[Range(min=None, max=100, exclusive_min=False, exclusive_max=True)])
    n2 = fields.Number(validate=[Range(min=None, max=100, exclusive_min=False, exclusive_max=False)])
    m0 = fields.Number(validate=[Range(min=100, max=None, exclusive_min=False, exclusive_max=False)])
    m1 = fields.Number(validate=[Range(min=100, max=None, exclusive_min=True, exclusive_max=False)])
    m2 = fields.Number(validate=[Range(min=100, max=None, exclusive_min=False, exclusive_max=False)])
