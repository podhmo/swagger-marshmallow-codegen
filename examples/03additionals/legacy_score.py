# -*- coding:utf-8 -*-
# this is auto-generated by swagger-marshmallow-codegen
from swagger_marshmallow_codegen.schema.legacy import (
    AdditionalPropertiesSchema,
    LegacySchema
)
from marshmallow import fields


class Score(AdditionalPropertiesSchema):
    name = fields.String(required=True)

    class Meta:
        additional_field = fields.Integer()
