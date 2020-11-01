from marshmallow import (
    Schema,
    fields,
)
from swagger_marshmallow_codegen.schema import PrimitiveValueSchema


class MyInt(PrimitiveValueSchema):
    class schema_class(Schema):
        value = fields.Integer()
