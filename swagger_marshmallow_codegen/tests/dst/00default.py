import datetime
from collections import OrderedDict
class X(Schema):
    string = fields.String(default='default')
    integer = fields.Integer(default=10)
    boolean = fields.Boolean(default=True)
    datetime = fields.DateTime(default=datetime.datetime(2000, 1, 1, 1, 1, 1))
    object = fields.Nested('XObject', default=OrderedDict([('name', 'foo'), ('age', 20)]))
    array = fields.Integer(many=True, default=[1, 2, 3])


class XObject(Schema):
    name = fields.String(default='foo')
    age = fields.Integer(default=20)
