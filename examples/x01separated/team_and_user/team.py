# this is auto-generated by swagger-marshmallow-codegen
from __future__ import annotations
from marshmallow import (
    Schema,
    fields,
    INCLUDE,
)
from ._lazy import _useUser


class Team(Schema):
    members = fields.List(fields.Nested(_useUser))
    name = fields.String()

    class Meta:
        unknown = INCLUDE
