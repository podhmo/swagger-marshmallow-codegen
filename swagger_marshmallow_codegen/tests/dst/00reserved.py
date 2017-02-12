# -*- coding:utf-8 -*-
from marshmallow import (
    Schema,
    fields
)


class Reserved(Schema):
    not_ = fields.Boolean(load_from="not", dump_to="not")
    as_ = fields.String(load_from="as", dump_to="as")
    in_ = fields.List(fields.String(), load_from="in", dump_to="in"))
    yield_ = fields.String(load_from="yield", dump_to="yield"))
