from marshmallow.validate import (
    Length,
    Regexp
)
from swagger_marshmallow_codegen.fields import DateTime
import re
from swagger_marshmallow_codegen.validate import Range
class Pet(Schema):
    id = fields.String(description='Unique identifier', dump_only=True)
    name = fields.String(required=True, description="Pet's name", validate=[Length(min=1, max=100, equal=None)])
    animal_type = fields.String(required=True, description='Kind of animal', validate=[Length(min=1, max=None, equal=None)])
    tags = fields.Field(description='Custom tags')
    created = DateTime(description='Creation time', dump_only=True)


class PetsInput(object):
    class Get(object):
        class GET(Schema):
            animal_type = fields.String(validate=[Regexp(regex=re.compile('^[a-zA-Z0-9]*$'))])
            limit = fields.Integer(missing=lambda: 100, validate=[Range(min=0, max=None, exclusive_min=False, exclusive_max=False)])




class PetsPetIdInput(object):
    class Get(object):
        class Path(Schema):
            pet_id = fields.String(description="Pet's Unique identifier", validate=[Regexp(regex=re.compile('^[a-zA-Z0-9-]+$'))])


    class Put(object):
        class Path(Schema):
            pet_id = fields.String(description="Pet's Unique identifier", validate=[Regexp(regex=re.compile('^[a-zA-Z0-9-]+$'))])

        class Body(Pet):
            pass


    class Delete(object):
        class Path(Schema):
            pet_id = fields.String(description="Pet's Unique identifier", validate=[Regexp(regex=re.compile('^[a-zA-Z0-9-]+$'))])
