import datetime
from collections import OrderedDict
class X(Schema):
    string = fields.String(missing='default')
    integer = fields.Integer(missing=10)
    boolean = fields.Boolean(missing=True)
    datetime = fields.DateTime(missing=datetime.datetime(2000, 1, 1, 1, 1, 1))
    object = fields.Nested('XObject', missing=OrderedDict([('name', 'foo'), ('age', 20)]))
    array = fields.Integer(many=True, missing=[1, 2, 3])


class XObject(Schema):
    name = fields.String(missing='foo')
    age = fields.Integer(missing=20)
