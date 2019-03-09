from marshmallow import (
    Schema,
    fields
)


class Reserved(Schema):
    not_ = fields.Boolean(dump_to='not', load_from='not')
    as_ = fields.String(dump_to='as', load_from='as')
    in_ = fields.List(fields.String(), dump_to='in', load_from='in')
    yield_ = fields.String(dump_to='yield', load_from='yield')
