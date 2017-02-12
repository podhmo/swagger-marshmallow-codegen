# -*- coding:utf-8 -*-
from marshmallow import (
    Schema,
    fields
)


class Wrap(Schema):
    empties = fields.List(fields.Nested('WrapEmptiesItem'))


class WrapEmptiesItem(Schema):
    pass
