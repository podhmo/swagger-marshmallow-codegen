class Person(Schema):
    name = fields.String(required=True, description='name of something')
    age = fields.Integer(description='age')
