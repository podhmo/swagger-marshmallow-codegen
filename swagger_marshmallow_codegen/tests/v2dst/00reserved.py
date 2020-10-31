from marshmallow import (
    Schema,
    fields,
)


class Reserved(Schema):
    not_ = fields.Boolean(data_key='not')
    as_ = fields.String(data_key='as')
    in_ = fields.List(fields.String(), data_key='in')
    yield_ = fields.String(data_key='yield')
