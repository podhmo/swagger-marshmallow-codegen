from marshmallow import (
    Schema,
    fields,
)


class Wrap(Schema):
    empties = fields.List(fields.Nested(lambda: WrapEmptiesItem()))


class WrapEmptiesItem(Schema):
    pass
