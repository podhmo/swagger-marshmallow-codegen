class X(Schema):
    string = fields.String(default='default')
    integer = fields.Integer(default=10)
    boolean = fields.Boolean(default=True)
    datetime = fields.DateTime(default=datetime.datetime(2000, 1, 1, 1, 1, 1))
    object = fields.Nested('XObject')
    array = fields.Integer(many=True)


class XObject(Schema):
    name = fields.String(default='foo')
    age = fields.Integer(default=20)
