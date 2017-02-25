# -*- coding:utf-8 -*-
from marshmallow import (
    Schema,
    fields
)


class Message(Schema):
    message = fields.String(required=True, missing=lambda: 'Hello, Adam!')
