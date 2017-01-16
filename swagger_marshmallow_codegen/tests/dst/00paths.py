# -*- coding:utf-8 -*-
from marshmallow import (
    Schema,
    fields
)
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
        """Get all pets"""

        class Query(Schema):
            animal_type = fields.String(validate=[Regexp(regex=re.compile('^[a-zA-Z0-9]*$'))])
            limit = fields.Integer(missing=lambda: 100, validate=[Range(min=0, max=None, exclusive_min=False, exclusive_max=False)])




class PetsPetIdInput(object):
    class Get(object):
        """Get a single pet"""

        class Path(Schema):
            pet_id = fields.String(description="Pet's Unique identifier", validate=[Regexp(regex=re.compile('^[a-zA-Z0-9-]+$'))])


    class Put(object):
        """Create or update a pet"""

        class Body(Pet):
            pass

        class Path(Schema):
            pet_id = fields.String(description="Pet's Unique identifier", validate=[Regexp(regex=re.compile('^[a-zA-Z0-9-]+$'))])


    class Delete(object):
        """Remove a pet"""

        class Path(Schema):
            pet_id = fields.String(description="Pet's Unique identifier", validate=[Regexp(regex=re.compile('^[a-zA-Z0-9-]+$'))])




class PetsOutput(object):
    class Get200(Pet):
        """Return pets"""

        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class PetsPetIdOutput(object):
    class Get200(Pet):
        """Return pet"""
        pass
