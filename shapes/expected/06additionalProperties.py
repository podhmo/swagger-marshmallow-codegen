from marshmallow import (
    Schema,
    fields,
)
from swagger_marshmallow_codegen.schema import (
    AdditionalPropertiesSchema,
    PrimitiveValueSchema,
)


class Box(AdditionalPropertiesSchema):
    name = fields.String(required=True)

    class Meta:
        additional_field = fields.Integer()



class Value(PrimitiveValueSchema):
    class schema_class(Schema):
        value = fields.Integer()
