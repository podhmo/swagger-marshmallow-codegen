# this is auto-generated by swagger-marshmallow-codegen
from __future__ import annotations
from marshmallow import (
    Schema,
    fields,
    INCLUDE,
)
from marshmallow.validate import OneOf
from ._lazy import _usePet
from .Pet import Pet


class Cat(Pet):
    """A representation of a cat"""
    huntingSkill = fields.String(required=True, description='The measured skill for hunting', validate=[OneOf(choices=['clueless', 'lazy', 'adventurous', 'aggressive'], labels=[])])

    class Meta:
        unknown = INCLUDE
