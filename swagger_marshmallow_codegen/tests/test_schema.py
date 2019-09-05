import unittest
from collections import namedtuple
from marshmallow import fields, Schema


class PrimitiveValueSchemaTests(unittest.TestCase):
    def _getTargetClass(self):
        from swagger_marshmallow_codegen.schema import PrimitiveValueSchema

        return PrimitiveValueSchema

    def assert_load_value(self, fut, c):
        if c.ok:
            actual = fut()
            self.assertEqual(actual, c.expected)
        else:
            from marshmallow import ValidationError

            with self.assertRaises(ValidationError):
                fut()

    def assert_dump_value(self, fut, c):
        if c.ok:
            actual = fut()
            self.assertEqual(actual, c.expected)
        else:
            with self.assertRaises(ValueError):
                fut()

    def test_load_atom(self):
        class S(self._getTargetClass()):
            class schema_class(Schema):
                value = fields.Integer(required=True)

        C = namedtuple("C", "value, expected, ok")
        candidates = [
            C(value="10", expected=10, ok=True),
            C(value="foo", expected=None, ok=False),
        ]
        for c in candidates:
            with self.subTest(value=c.value, ok=c.ok):
                self.assert_load_value(lambda: S().load(c.value), c)

    def test_load_list(self):
        class S(self._getTargetClass()):
            class schema_class(Schema):
                value = fields.List(fields.Integer(), required=True)

        C = namedtuple("C", "value, expected, ok")
        candidates = [
            C(value=["10"], expected=[10], ok=True),
            C(value=["10", "20"], expected=[10, 20], ok=True),
            C(value=["foo", "bar"], expected=None, ok=False),
        ]
        for c in candidates:
            with self.subTest(value=c.value, ok=c.ok):
                self.assert_load_value(lambda: S().load(c.value), c)

    def test_dump_atom(self):
        class S(self._getTargetClass()):
            class schema_class(Schema):
                value = fields.Integer(required=True)

        C = namedtuple("C", "value, expected, ok")
        candidates = [
            C(value="10", expected=10, ok=True),
            C(value=10, expected=10, ok=True),
            C(value="foo", expected=None, ok=False),
        ]
        for c in candidates:
            with self.subTest(value=c.value, ok=c.ok):
                self.assert_dump_value(lambda: S().dump(c.value), c)

    def test_dump_list(self):
        class S(self._getTargetClass()):
            class schema_class(Schema):
                value = fields.List(fields.Integer(), required=True)

        C = namedtuple("C", "value, expected, ok")
        candidates = [
            C(value=["10"], expected=[10], ok=True),
            C(value=["10", "20"], expected=[10, 20], ok=True),
            C(value=["foo", "bar"], expected=None, ok=False),
        ]
        for c in candidates:
            with self.subTest(value=c.value, ok=c.ok):
                self.assert_dump_value(lambda: S().dump(c.value), c)


class AdditioinalSchemaTests(unittest.TestCase):
    def _getTargetClass(self):
        from swagger_marshmallow_codegen.schema import AdditionalPropertiesSchema

        return AdditionalPropertiesSchema

    def assert_value(self, fut, c):
        if c.ok:
            actual = fut()
            self.assertEqual(actual, c.expected)
        else:
            from marshmallow import ValidationError

            with self.assertRaises(ValidationError):
                fut()

    def test_load_default(self):
        class S(self._getTargetClass()):
            name = fields.String()

        C = namedtuple("C", "value, expected, ok")
        candidates = [
            C(
                value={"name": "foo", "value": "100"},
                expected={"name": "foo", "value": "100"},
                ok=True,
            )
        ]
        for c in candidates:
            with self.subTest(value=c.value, ok=c.ok):
                self.assert_value(lambda: S().load(c.value), c)

    def test_load_specific(self):
        class S(self._getTargetClass()):
            name = fields.String()

            class Meta:
                additional_field = fields.Integer()

        C = namedtuple("C", "value, expected, ok")
        candidates = [
            C(
                value={"name": "foo", "value": "100"},
                expected={"name": "foo", "value": 100},
                ok=True,
            ),
            C(
                value={"name": "foo", "value": "100"},
                expected={"name": "foo", "value": 100},
                ok=True,
            ),
        ]
        for c in candidates:
            with self.subTest(value=c.value, ok=c.ok):
                self.assert_value(lambda: S().load(c.value), c)

    def test_load_specific_list(self):
        from marshmallow import Schema

        class X(Schema):
            v = fields.Integer(required=True)

        class S(self._getTargetClass()):
            name = fields.String()

            class Meta:
                additional_field = fields.List(fields.Nested(X))

        C = namedtuple("C", "value, expected, ok")
        candidates = [
            C(
                value={"name": "foo", "xs": []},
                expected={"name": "foo", "xs": []},
                ok=True,
            ),
            C(
                value={"name": "foo", "xs": [{"v": "100"}]},
                expected={"name": "foo", "xs": [{"v": 100}]},
                ok=True,
            ),
            C(value={"name": "foo", "xs": [{}]}, expected=None, ok=False),
        ]
        for c in candidates:
            with self.subTest(value=c.value, ok=c.ok):
                self.assert_value(lambda: S().load(c.value), c)

    def test_dump_default(self):
        class S(self._getTargetClass()):
            name = fields.String()

        C = namedtuple("C", "value, expected, ok")
        candidates = [
            C(
                value={"name": "foo", "value": "100"},
                expected={"name": "foo", "value": "100"},
                ok=True,
            )
        ]
        for c in candidates:
            with self.subTest(value=c.value, ok=c.ok):
                self.assert_value(lambda: S().dump(c.value), c)

    def test_dump_specific(self):
        class S(self._getTargetClass()):
            name = fields.String()

            class Meta:
                additional_field = fields.Integer()

        C = namedtuple("C", "value, expected, ok")
        candidates = [
            C(
                value={"name": "foo", "value": "100"},
                expected={"name": "foo", "value": 100},
                ok=True,
            ),
            C(
                value={"name": "foo", "value": "100"},
                expected={"name": "foo", "value": 100},
                ok=True,
            ),
        ]
        for c in candidates:
            with self.subTest(value=c.value, ok=c.ok):
                self.assert_value(lambda: S().dump(c.value), c)

    def test_dump_specific_list(self):
        from marshmallow import Schema

        class X(Schema):
            v = fields.Integer(required=True)

        class S(self._getTargetClass()):
            name = fields.String()

            class Meta:
                additional_field = fields.List(fields.Nested(X))

        C = namedtuple("C", "value, expected, ok")
        candidates = [
            C(
                value={"name": "foo", "xs": [], "ys": [{"v": "100"}]},
                expected={"name": "foo", "xs": [], "ys": [{"v": 100}]},
                ok=True,
            ),
            C(
                value={"name": "foo", "xs": [{"v": "100", "*another*": "*another*"}]},
                expected={"name": "foo", "xs": [{"v": 100}]},
                ok=True,
            ),
        ]
        for c in candidates:
            with self.subTest(value=c.value, ok=c.ok):
                self.assert_value(lambda: S().dump(c.value), c)
