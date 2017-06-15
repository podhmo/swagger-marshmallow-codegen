from marshmallow import (
    Schema,
    fields
)
from swagger_marshmallow_codegen.schema import (
    PrimitiveValueSchema
)


class IntsInput(object):
    class Post(object):
        class Body(PrimitiveValueSchema):
            class schema_class(Schema):
                value = fields.List(fields.Integer())





class IntsOutput(object):
    class Get200(PrimitiveValueSchema):
        class schema_class(Schema):
            value = fields.List(fields.Integer())
