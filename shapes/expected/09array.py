from marshmallow import (
    Schema,
    fields,
)
from swagger_marshmallow_codegen.schema import PrimitiveValueSchema


class Person(Schema):
    name = fields.String(required=True)
    age = fields.Integer()
    children = fields.List(fields.Nested(lambda: Person()))
    children2 = fields.List(fields.Nested(lambda: Person()))
    children3 = fields.List(fields.Nested(lambda: Person()))
    children4 = fields.List(fields.Nested(lambda: PersonChildren4Item()))
    Nchildren = fields.List(fields.List(fields.Nested(lambda: Person())))
    Nchildren2 = fields.List(fields.List(fields.Nested(lambda: Person())))
    Nchildren3 = fields.List(fields.List(fields.Nested(lambda: Person())))
    Nchildren4 = fields.List(fields.List(fields.Nested(lambda: Person())))
    Nchildren5 = fields.List(fields.List(fields.Nested(lambda: PersonNchildren5ItemItem())))


class PersonNchildren5ItemItem(PersonNchildren5ItemItem):
    def __init__(self, *args, **kwargs):
        kwargs['many'] = True
        super().__init__(*args, **kwargs)



class PersonNchildren5(PersonNchildren5ItemItem):
    def __init__(self, *args, **kwargs):
        kwargs['many'] = True
        super().__init__(*args, **kwargs)



class PersonNchildren5Item(PersonNchildren5ItemItem):
    def __init__(self, *args, **kwargs):
        kwargs['many'] = True
        super().__init__(*args, **kwargs)



class PersonNchildren(PrimitiveValueSchema):
    class schema_class(Schema):
        value = fields.List(fields.List(fields.Nested(lambda: Person())))



class PersonChildren4Item(Schema):
    name = fields.String()
    age = fields.Integer()
    children = fields.List(fields.Nested(lambda: Person()))


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



class NChildren2(PrimitiveValueSchema):
    class schema_class(Schema):
        value = fields.List(fields.List(fields.Nested(lambda: Person())))



class NChildren3(Person):
    def __init__(self, *args, **kwargs):
        kwargs['many'] = True
        super().__init__(*args, **kwargs)



class NChildren4(PrimitiveValueSchema):
    class schema_class(Schema):
        value = fields.List(fields.List(fields.Nested(lambda: Person())))
