from marshmallow import (
    Schema,
    fields
)
from swagger_marshmallow_codegen.schema import (
    AdditionalPropertiesSchema
)


class Box(AdditionalPropertiesSchema):
    name = fields.String()

    class Meta:
        additional_field = fields.Integer()



class Box2(AdditionalPropertiesSchema):
    name = fields.String()

    class Meta:
        additional_field = fields.Nested('Box')



class Box3(AdditionalPropertiesSchema):
    name = fields.String()

    class Meta:
        additional_field = fields.String()



class Box4(Schema):
    box = fields.Nested('Box4Box')


class Box4Box(AdditionalPropertiesSchema):

    class Meta:
        additional_field = fields.String()
