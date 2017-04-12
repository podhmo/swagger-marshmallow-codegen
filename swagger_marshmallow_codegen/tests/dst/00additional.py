from marshmallow import (
    Schema,
    fields
)
from swagger_marshmallow_codegen.schema import (
    AdditionalPropertiesSchema
)


class Box(AdditionalPropertiesSchema):
    name = fields.String()

    class Meta(object):
        additional_field = fields.Integer()



class Box2(AdditionalPropertiesSchema):
    name = fields.String()

    class Meta(object):
        additional_field = fields.Nested('Box')



class Box3(AdditionalPropertiesSchema):
    name = fields.String()

    class Meta(object):
        additional_field = fields.String()
