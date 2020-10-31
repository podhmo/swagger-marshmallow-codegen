from marshmallow import (
    Schema,
    fields
)
from swagger_marshmallow_codegen.validate import (
    Range
)


class X(Schema):
    n0 = fields.Number(validate=[Range(min=None, max=100, min_inclusive=True, max_inclusive=True)])
    n1 = fields.Number(validate=[Range(min=None, max=100, min_inclusive=True, max_inclusive=False)])
    n2 = fields.Number(validate=[Range(min=None, max=100, min_inclusive=True, max_inclusive=True)])
    m0 = fields.Number(validate=[Range(min=100, max=None, min_inclusive=True, max_inclusive=True)])
    m1 = fields.Number(validate=[Range(min=100, max=None, min_inclusive=False, max_inclusive=True)])
    m2 = fields.Number(validate=[Range(min=100, max=None, min_inclusive=True, max_inclusive=True)])
