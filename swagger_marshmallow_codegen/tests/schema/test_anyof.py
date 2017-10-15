import unittest
from testmarker import mark
from collections import namedtuple


@mark.anyof
class LoadTests(unittest.TestCase):
    def _getTargetClass(self):
        from .schema import Person, Group
        from swagger_marshmallow_codegen.schema import AnyOfSchema

        class S(AnyOfSchema):
            class Meta:
                schema_classes = (Person, Group)

        return S

    def test_many_false(self):
        from marshmallow import UnmarshalResult
        S = self._getTargetClass()
        C = namedtuple("C", "data, expected, msg")
        candidates = [
            C(
                msg="person missing",
                data=dict(age="10"),
                expected=UnmarshalResult(
                    data=dict(age=10),
                    errors=dict(_schema=["not matched, any of ['Person', 'Group']"])
                ),
            ),
            C(
                msg="person ok",
                data=dict(name="foo", age="10"),
                expected=UnmarshalResult(data=dict(name="foo", age=10), errors={})
            ),
            C(
                msg="group ok",
                data=dict(name="A", members=[]),
                expected=UnmarshalResult(data=dict(name="A", members=[]), errors={}),
            ),
            C(
                msg="group ok2",
                data=dict(name="A", members=[dict(name="foo", age="10")]),
                expected=UnmarshalResult(
                    data=dict(name="A", members=[dict(name="foo", age=10)]), errors={}
                ),
            ),
            C(
                msg="both",
                data=dict(age="10", name="A", members=[]),
                expected=UnmarshalResult(
                    data=dict(age=10, name="A", members=[]),
                    errors={},
                ),
            ),
        ]
        for c in candidates:
            with self.subTest(msg=c.msg):
                s = S()
                got = s.load(c.data)
                self.assertEqual(got.errors, c.expected.errors)
                self.assertEqual(got.data, c.expected.data)

    def test_many_true(self):
        from marshmallow import UnmarshalResult
        S = self._getTargetClass()
        C = namedtuple("C", "data, expected, msg")
        candidates = [
            C(
                msg="person missing",
                data=[dict(age="10")],
                expected=UnmarshalResult(
                    data=[dict(age=10)],
                    errors={0: dict(_schema=["not matched, any of ['Person', 'Group']"])}
                ),
            ),
            C(
                msg="person ok",
                data=[dict(name="foo", age="10")],
                expected=UnmarshalResult(data=[dict(name="foo", age=10)], errors={})
            ),
            C(
                msg="group ok",
                data=[dict(name="A", members=[])],
                expected=UnmarshalResult(data=[dict(name="A", members=[])], errors={}),
            ),
            C(
                msg="group ok2",
                data=[dict(name="A", members=[dict(name="foo", age="10")])],
                expected=UnmarshalResult(
                    data=[dict(name="A", members=[dict(name="foo", age=10)])], errors={}
                ),
            ),
            C(
                msg="both",
                data=[dict(age="10", name="A", members=[])],
                expected=UnmarshalResult(
                    data=[dict(age=10, name="A", members=[])],
                    errors={},
                ),
            ),
            C(
                msg="ng items[1]",
                data=[dict(name="foo", age="10"),
                      dict(name="bar"),
                      dict(name="boo", age="10")],
                expected=UnmarshalResult(
                    data=[dict(name="foo", age=10),
                          dict(name="bar"),
                          dict(name="boo", age=10)],
                    errors={1: {
                        '_schema': ["not matched, any of ['Person', 'Group']"]
                    }},
                ),
            )
        ]
        for c in candidates:
            with self.subTest(msg=c.msg):
                s = S()
                got = s.load(c.data, many=True)
                self.assertEqual(got.errors, c.expected.errors)
                self.assertEqual(got.data, c.expected.data)

    def test_nested(self):
        from marshmallow import UnmarshalResult, fields, Schema

        class S(Schema):
            target = fields.Nested(self._getTargetClass())

        C = namedtuple("C", "data, expected, msg")
        candidates = [
            C(
                msg="person missing",
                data=dict(target=dict(age="10")),
                expected=UnmarshalResult(
                    data=dict(target=dict(age=10)),
                    errors=dict(target=dict(_schema=["not matched, any of ['Person', 'Group']"]))
                ),
            ),
            C(
                msg="person ok",
                data=dict(target=dict(name="foo", age="10")),
                expected=UnmarshalResult(
                    data=dict(target=dict(name="foo", age=10)),
                    errors={},
                ),
            ),
            C(
                msg="both",
                data=dict(target=dict(age="10", name="A", members=[])),
                expected=UnmarshalResult(
                    data=dict(target=dict(age=10, name="A", members=[])),
                    errors={},
                ),
            ),
        ]
        for c in candidates:
            with self.subTest(msg=c.msg):
                s = S()
                got = s.load(c.data)
                self.assertEqual(got.errors, c.expected.errors)
                self.assertEqual(got.data, c.expected.data)

    def test_decorator(self):
        from marshmallow import UnmarshalResult
        from marshmallow import pre_load, post_load

        class S(self._getTargetClass()):
            @pre_load
            def lowercase(self, data):
                return {k.lower(): v for k, v in data.items()}

            @post_load
            def wrap(self, data):
                return {"wrap": data}

        C = namedtuple("C", "data, expected, msg, many")
        candidates = [
            C(
                msg="person missing",
                many=False,
                data=dict(age="10"),
                expected=UnmarshalResult(
                    data=dict(age=10),
                    errors=dict(_schema=["not matched, any of ['Person', 'Group']"])
                ),
            ),
            C(
                msg="person ok",
                many=False,
                data=dict(NAME="foo", AGE="10"),
                expected=UnmarshalResult(data=dict(wrap=dict(name="foo", age=10)), errors={})
            ),
            C(
                msg="people ok",
                many=True,
                data=[dict(NAME="foo", AGE="10"),
                      dict(NAME="bar", AGE="10")],
                expected=UnmarshalResult(
                    [dict(wrap=dict(name="foo", age=10)),
                     dict(wrap=dict(name="bar", age=10))],
                    errors={}
                )
            ),
        ]
        s = S()
        for c in candidates:
            with self.subTest(msg=c.msg):
                got = s.load(c.data, many=c.many)
                self.assertEqual(got.errors, c.expected.errors)
                self.assertEqual(got.data, c.expected.data)

    def test_load_with_unmatched(self):
        from marshmallow import UnmarshalResult, fields, Schema
        from .schema import Person
        C = namedtuple("C", "schema, msg, opts, expected")

        S1 = self._getTargetClass()

        class S2(Schema):
            target = fields.Nested(self._getTargetClass())

        candidates = [
            C(
                schema=Person,
                msg="default marshmallow",
                opts={"many": True},
                expected=UnmarshalResult(data=[], errors={})
            ),
            C(
                schema=S1,
                msg="default marshmallow",
                opts={"many": True},
                expected=UnmarshalResult(data=[], errors={})
            ),
            C(
                schema=S1,
                msg="default marshmallow",
                opts={"many": True},
                expected=UnmarshalResult(data=[], errors={})
            )
        ]
        for c in candidates:
            with self.subTest(msg=c.msg):
                got = c.schema(**c.opts).load({})
                self.assertEqual(got, c.expected)


@mark.anyof
class DumpTests(unittest.TestCase):
    def _getTargetClass(self):
        from swagger_marshmallow_codegen.schema import AnyOfSchema
        from .schema import Person, Group

        class S(AnyOfSchema):
            class Meta:
                schema_classes = (Person, Group)

        return S

    def test_many_false(self):
        from marshmallow import MarshalResult
        S = self._getTargetClass()
        C = namedtuple("C", "data, expected, msg")
        candidates = [
            C(
                msg="person missing",
                data=dict(age=10),
                expected=MarshalResult(
                    data=dict(age=10),
                    errors=dict(_schema=["not matched, any of ['Person', 'Group']"])
                ),
            ),
            C(
                msg="person ok",
                data=dict(name="foo", age=10),
                expected=MarshalResult(data=dict(name="foo", age=10), errors={})
            ),
            C(
                msg="group ok",
                data=dict(name="A", members=[]),
                expected=MarshalResult(data=dict(name="A", members=[]), errors={}),
            ),
            C(
                msg="group ok2",
                data=dict(name="A", members=[dict(name="foo", age=10)]),
                expected=MarshalResult(
                    data=dict(name="A", members=[dict(name="foo", age=10)]), errors={}
                ),
            ),
            C(
                msg="both",
                data=dict(age="10", name="A", members=[]),
                expected=MarshalResult(data=dict(age=10, name="A", members=[]), errors={}),
            ),
        ]
        for c in candidates:
            with self.subTest(msg=c.msg):
                s = S()
                got = s.dump(c.data)
                self.assertEqual(got.errors, c.expected.errors)
                self.assertEqual(got.data, c.expected.data)

    def test_decorator(self):
        from marshmallow import MarshalResult
        from marshmallow import pre_dump, post_dump

        class S(self._getTargetClass()):
            @pre_dump
            def lowercase(self, data):
                return {k.lower(): v for k, v in data.items()}

            @post_dump
            def wrap(self, data):
                return {"wrap": data}

        C = namedtuple("C", "data, expected, msg, many")
        candidates = [
            C(
                msg="person missing",
                many=False,
                data=dict(AGE="10"),
                expected=MarshalResult(
                    data=dict(age="10"),
                    errors=dict(_schema=["not matched, any of ['Person', 'Group']"])
                ),
            ),
            C(
                msg="person ok",
                many=False,
                data=dict(name="foo", AGE=10),
                expected=MarshalResult(data=dict(wrap=dict(name="foo", age=10)), errors={})
            ),
            C(
                msg="people ok",
                many=True,
                data=[dict(name="foo", AGE=10), dict(name="bar", AGE=10)],
                expected=MarshalResult(
                    [dict(wrap=dict(name="foo", age=10)),
                     dict(wrap=dict(name="bar", age=10))],
                    errors={}
                )
            ),
        ]
        s = S()
        for c in candidates:
            with self.subTest(msg=c.msg):
                got = s.dump(c.data, many=c.many)
                self.assertEqual(got.errors, c.expected.errors)
                self.assertEqual(got.data, c.expected.data)
