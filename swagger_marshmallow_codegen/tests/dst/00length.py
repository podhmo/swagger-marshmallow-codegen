from marshmallow.validate import(
    Length
)
class X(Schema):
    s0 = fields.String()
    s1 = fields.String(validate=[Length(min=None, max=10)])
    s2 = fields.String(validate=[Length(min=5, max=None)])
    s3 = fields.String(validate=[Length(min=5, max=10)])
