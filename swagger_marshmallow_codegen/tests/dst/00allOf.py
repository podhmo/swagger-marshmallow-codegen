from marshmallow.validate import OneOf
from swagger_marshmallow_codegen.validate import Range
class Pet(Schema):
    name = fields.String(required=True)
    petType = fields.String(required=True)


class Cat(Pet):
    huntingSkill = fields.String(required=True, description='The measured skill for hunting', missing=lambda: 'lazy', validate=[OneOf(choices=['clueless', 'lazy', 'adventurous', 'aggressive'], labels=[])])


class Dog(Pet):
    packSize = fields.Integer(required=True, description='the size of the pack the dog is from', missing=lambda: 0, validate=[Range(min=0, max=None, exclusive_min=False, exclusive_max=False)])
