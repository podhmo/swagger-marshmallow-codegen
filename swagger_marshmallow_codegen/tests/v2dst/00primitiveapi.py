from marshmallow import (
    Schema,
    fields
)
from swagger_marshmallow_codegen.schema import (
    PrimitiveValueSchema
)


class IntsInput:
    class Get:
        pass

    class Post:
        class Body(PrimitiveValueSchema):
            class schema_class(Schema):
                value = fields.List(fields.Integer())





class IntsOutput:
    class Get200(PrimitiveValueSchema):
        class schema_class(Schema):
            value = fields.List(fields.Integer())
