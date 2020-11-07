# this is auto-generated by swagger-marshmallow-codegen
from __future__ import annotations
from marshmallow import (
    Schema,
    fields,
    INCLUDE,
)


class Shop(Schema):
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    description = fields.Nested(lambda: ShopDescription())

    class Meta:
        unknown = INCLUDE



class ShopDescription(Schema):
    content = fields.String()
    position = fields.String()

    class Meta:
        unknown = INCLUDE
