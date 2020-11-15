from marshmallow import (
    Schema,
    fields,
)


class Person(Schema):
    name = fields.String(required=True)
    age = fields.Integer()
    children = fields.List(fields.Nested(lambda: Person()))
    children2 = fields.List(fields.Nested(lambda: Person()))
    children3 = fields.List(fields.Nested(lambda: Person()))
    children4 = fields.List(fields.Nested(lambda: PersonChildren4Item()))


class PersonChildren4Item(Schema):
    pass


class PersonChildren4(PersonChildren4Item):
    def __init__(self, *args, **kwargs):
        kwargs['many'] = True
        super().__init__(*args, **kwargs)



class Children2(Person):
    def __init__(self, *args, **kwargs):
        kwargs['many'] = True
        super().__init__(*args, **kwargs)



class Children3(Person):
    def __init__(self, *args, **kwargs):
        kwargs['many'] = True
        super().__init__(*args, **kwargs)
