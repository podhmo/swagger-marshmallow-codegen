from marshmallow import (
    Schema,
    fields,
)
from marshmallow.validate import (
    Length,
    Regexp,
)
from swagger_marshmallow_codegen.schema import PrimitiveValueSchema
import re


class Label(Schema):
    color = fields.String(validate=[Length(min=6, max=6, equal=None)])
    name = fields.String()
    url = fields.String()


class IssuedLabelsInput:
    class Delete:
        """
        Remove all labels from an issue.
        """

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(data_key='X-GitHub-Media-Type', description='You can check the current version of media type in responses.\n')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(data_key='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(data_key='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(data_key='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(data_key='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(required=True, description='Name of repository owner.')
            repo = fields.String(required=True, description='Name of repository.')
            number = fields.Integer(required=True, description='Number of issue.')


    class Get:
        """
        List labels on an issue.
        """

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(data_key='X-GitHub-Media-Type', description='You can check the current version of media type in responses.\n')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(data_key='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(data_key='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(data_key='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(data_key='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(required=True, description='Name of repository owner.')
            repo = fields.String(required=True, description='Name of repository.')
            number = fields.Integer(required=True, description='Number of issue.')


    class Post:
        """
        Add labels to an issue.
        """

        class Body(PrimitiveValueSchema):
            class schema_class(Schema):
                value = fields.List(fields.String(validate=[Regexp(regex=re.compile('.+@.+'))]))


        class Header(Schema):
            X_GitHub_Media_Type = fields.String(data_key='X-GitHub-Media-Type', description='You can check the current version of media type in responses.\n')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(data_key='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(data_key='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(data_key='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(data_key='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(required=True, description='Name of repository owner.')
            repo = fields.String(required=True, description='Name of repository.')
            number = fields.Integer(required=True, description='Number of issue.')


    class Put:
        """
        Replace all labels for an issue.
        Sending an empty array ([]) will remove all Labels from the Issue.
        """

        class Body(PrimitiveValueSchema):
            class schema_class(Schema):
                value = fields.List(fields.String(validate=[Regexp(regex=re.compile('.+@.+'))]))


        class Header(Schema):
            X_GitHub_Media_Type = fields.String(data_key='X-GitHub-Media-Type', description='You can check the current version of media type in responses.\n')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(data_key='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(data_key='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(data_key='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(data_key='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(required=True, description='Name of repository owner.')
            repo = fields.String(required=True, description='Name of repository.')
            number = fields.Integer(required=True, description='Number of issue.')




class IssuedLabelsOutput:
    class Get200(Label):
        """OK"""
        def __init__(self, *args, **kwargs):
            kwargs['many'] = True
            super().__init__(*args, **kwargs)


    class Post201(Label):
        """Created"""
        pass

    class Put201(Label):
        """Created"""
        pass
