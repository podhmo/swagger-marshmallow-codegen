# this is auto-generated by swagger-marshmallow-codegen
from __future__ import annotations
from swagger_marshmallow_codegen.schema.legacy import (
    LegacySchema,
    AdditionalPropertiesSchema,
)
from marshmallow import fields


class Score(AdditionalPropertiesSchema):
    name = fields.String(required=True)

    class Meta:
        additional_field = fields.Integer()
