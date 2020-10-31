from marshmallow import (
    Schema,
    fields,
)


class Emojis(Schema):
    n100 = fields.String(data_key='100')
    n1234 = fields.String(data_key='1234')
    n1 = fields.String(data_key='1')
    x_1 = fields.String(data_key='-1')
    n8ball = fields.String(data_key='8ball')
