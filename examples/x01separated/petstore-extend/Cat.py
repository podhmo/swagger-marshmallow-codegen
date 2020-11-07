# this is auto-generated by swagger-marshmallow-codegen
from __future__ import annotations
from marshmallow import (
    Schema,
    fields,
    INCLUDE,
)
from .Pet import Pet
from marshmallow.validate import OneOf


class Cat(Pet):
    """A representation of a cat"""
    huntingSkill = fields.String(required=True, description='The measured skill for hunting', validate=[OneOf(choices=['clueless', 'lazy', 'adventurous', 'aggressive'], labels=[])])

    class Meta:
        unknown = INCLUDE
