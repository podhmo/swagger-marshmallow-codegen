from marshmallow import (
    Schema,
    fields
)
from marshmallow.validate import (
    Length,
    Regexp
)
import re
from swagger_marshmallow_codegen.validate import Range


class Pet(Schema):
    id = fields.String(description='Unique identifier', dump_only=True)
    name = fields.String(required=True, description="Pet's name", validate=[Length(min=1, max=100, equal=None)])
    animal_type = fields.String(required=True, description='Kind of animal', validate=[Length(min=1, max=None, equal=None)])
    tags = fields.Field(description='Custom tags')
    created = fields.DateTime(description='Creation time', dump_only=True)


class PetsInput:
    class Get:
        """
        Get all pets
        """

        class Query(Schema):
            animal_type = fields.String(validate=[Regexp(regex=re.compile('^[a-zA-Z0-9]*$'))])
            limit = fields.Integer(missing=lambda: 100, validate=[Range(min=0, max=None, exclusive_min=False, exclusive_max=False)])




class PetsPetIdInput:
    class Get:
        """
        Get a single pet
        """

        class Path(Schema):
            pet_id = fields.String(required=True, description="Pet's Unique identifier", validate=[Regexp(regex=re.compile('^[a-zA-Z0-9-]+$'))])


    class Put:
        """
        Create or update a pet
        """

        class Body(Pet):
            pass

        class Path(Schema):
            pet_id = fields.String(required=True, description="Pet's Unique identifier", validate=[Regexp(regex=re.compile('^[a-zA-Z0-9-]+$'))])


    class Delete:
        """
        Remove a pet
        """

        class Path(Schema):
            pet_id = fields.String(required=True, description="Pet's Unique identifier", validate=[Regexp(regex=re.compile('^[a-zA-Z0-9-]+$'))])




class PetsOutput:
    class Get200(Pet):
        """Return pets"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)




class PetsPetIdOutput:
    class Get200(Pet):
        """Return pet"""
        pass
