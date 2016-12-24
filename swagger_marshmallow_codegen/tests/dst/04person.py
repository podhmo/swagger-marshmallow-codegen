class Person(Schema):
    name = fields.String(required=True, description='name of something')
    age = fields.Integer(description='age')
    father = fields.Nested('self')
    mother = fields.Nested('self')
    skills = fields.Nested('Skill', many=True)


class Skill(Schema):
    name = fields.String(required=True)
