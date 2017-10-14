import unittest
from collections import namedtuple
from marshmallow import fields, Schema


class PrimitiveValueSchemaTests(unittest.TestCase):
    def _getTargetClass(self):
        from swagger_marshmallow_codegen.schema import PrimitiveValueSchema
        return PrimitiveValueSchema

    def assert_value(self, actual, err, c):
        if c.ok:
            self.assertFalse(err)
            self.assertEqual(actual, c.expected)
        else:
            self.assertTrue(err)

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
                actual, err = S().load(c.value)
                self.assert_value(actual, err, c)

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
                actual, err = S().load(c.value)
                self.assert_value(actual, err, c)

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
                actual, err = S().dump(c.value)
                self.assert_value(actual, err, c)

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
                actual, err = S().dump(c.value)
                self.assert_value(actual, err, c)
