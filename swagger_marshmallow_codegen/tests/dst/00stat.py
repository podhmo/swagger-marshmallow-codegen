class Stat(Schema):
    days = fields.Integer(many=True)
    days2 = fields.Integer(many=True)
    total = fields.Integer()
    week = fields.Integer()
