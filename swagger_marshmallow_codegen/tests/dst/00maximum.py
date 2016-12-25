from swagger_marshmallow_codegen import(
    validate
)
class X(Schema):
    n0 = fields.Number(validate=[validate.Range(min=None, max=100, exclusive_max=False, exclusive_min=False)])
    n1 = fields.Number(validate=[validate.Range(min=None, max=100, exclusive_max=True, exclusive_min=False)])
    n2 = fields.Number(validate=[validate.Range(min=None, max=100, exclusive_max=False, exclusive_min=False)])
    m0 = fields.Number(validate=[validate.Range(min=100, max=None, exclusive_max=False, exclusive_min=False)])
    m1 = fields.Number(validate=[validate.Range(min=100, max=None, exclusive_max=False, exclusive_min=True)])
    m2 = fields.Number(validate=[validate.Range(min=100, max=None, exclusive_max=False, exclusive_min=False)])
