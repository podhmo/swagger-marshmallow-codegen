from swagger_marshmallow_codegen import(
    validate
)
class A(Schema):
    nums = fields.List(fields.Integer(validate=[validate.ItemsRange(min=1, max=10), validate.Unique()]))
