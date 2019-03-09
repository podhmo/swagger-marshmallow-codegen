from marshmallow import (
    Schema,
    fields
)


class Emojis(Schema):
    n100 = fields.String(dump_to='100', load_from='100')
    n1234 = fields.String(dump_to='1234', load_from='1234')
    n1 = fields.String(dump_to='1', load_from='1')
    x_1 = fields.String(dump_to='-1', load_from='-1')
    n8ball = fields.String(dump_to='8ball', load_from='8ball')
