from marshmallow import (
    Schema,
    fields
)
from marshmallow.validate import OneOf
from swagger_marshmallow_codegen.validate import Range


class Pet(Schema):
    name = fields.String(required=True)
    petType = fields.String(required=True)


class Cat(Pet):
    """A representation of a cat"""
    huntingSkill = fields.String(required=True, description='The measured skill for hunting', validate=[OneOf(choices=['clueless', 'lazy', 'adventurous', 'aggressive'], labels=[])])


class Dog(Pet):
    """A representation of a dog"""
    packSize = fields.Integer(required=True, description='the size of the pack the dog is from', validate=[Range(min=0, max=None, exclusive_min=False, exclusive_max=False)])
