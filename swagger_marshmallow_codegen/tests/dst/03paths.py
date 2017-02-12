# -*- coding:utf-8 -*-
from marshmallow import (
    Schema,
    fields
)
from marshmallow.validate import (
    Length,
    Regexp
)
from swagger_marshmallow_codegen.schema import (
    PrimitiveValueSchema
)
import re


class Label(Schema):
    color = fields.String(validate=[Length(min=6, max=6, equal=None)])
    name = fields.String()
    url = fields.String()


class IssuedLabelsInput(object):
    class Delete(object):
        """
        Remove all labels from an issue.
        """

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            number = fields.Integer(description='Number of issue.')


    class Get(object):
        """
        List labels on an issue.
        """

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            number = fields.Integer(description='Number of issue.')


    class Post(object):
        """
        Add labels to an issue.
        """

        class Body(PrimitiveValueSchema):
            v = fields.String(validate=[Regexp(regex=re.compile('.+@.+'))])

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            number = fields.Integer(description='Number of issue.')


    class Put(object):
        """
        Replace all labels for an issue.
        Sending an empty array ([]) will remove all Labels from the Issue.
        """

        class Body(PrimitiveValueSchema):
            v = fields.String(validate=[Regexp(regex=re.compile('.+@.+'))])

        class Header(Schema):
            X_GitHub_Media_Type = fields.String(description='You can check the current version of media type in responses.\n', dump_to='X-GitHub-Media-Type', load_from='X-GitHub-Media-Type')
            Accept = fields.String(description='Is used to set specified media type.')
            X_RateLimit_Limit = fields.Integer(dump_to='X-RateLimit-Limit', load_from='X-RateLimit-Limit')
            X_RateLimit_Remaining = fields.Integer(dump_to='X-RateLimit-Remaining', load_from='X-RateLimit-Remaining')
            X_RateLimit_Reset = fields.Integer(dump_to='X-RateLimit-Reset', load_from='X-RateLimit-Reset')
            X_GitHub_Request_Id = fields.Integer(dump_to='X-GitHub-Request-Id', load_from='X-GitHub-Request-Id')

        class Path(Schema):
            owner = fields.String(description='Name of repository owner.')
            repo = fields.String(description='Name of repository.')
            number = fields.Integer(description='Number of issue.')




class IssuedLabelsOutput(object):
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
