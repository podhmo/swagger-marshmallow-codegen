import unittest
from collections import namedtuple
from marshmallow import fields


class AddtioinalSchemaTests(unittest.TestCase):
    def _getTargetClass(self):
        from swagger_marshmallow_codegen.schema import AdditionalPropertiesSchema
        return AdditionalPropertiesSchema

    def assert_value(self, actual, err, c):
        if c.ok:
            self.assertFalse(err)
            self.assertEqual(actual, c.expected)
        else:
            self.assertTrue(err)

    def test_load_default(self):
        class S(self._getTargetClass()):
            name = fields.String()

        C = namedtuple("C", "value, expected, ok")
        candidates = [
            C(value={"name": "foo", "value": "100"}, expected={"name": "foo", "value": "100"}, ok=True),
        ]
        for c in candidates:
            with self.subTest(value=c.value, ok=c.ok):
                actual, err = S().load(c.value)
                self.assert_value(actual, err, c)

    def test_load_specific(self):
        class S(self._getTargetClass()):
            name = fields.String()

            class Meta(object):
                additional_field = fields.Integer()

        C = namedtuple("C", "value, expected, ok")
        candidates = [
            C(value={"name": "foo", "value": "100"}, expected={"name": "foo", "value": 100}, ok=True),
            C(value={"name": "foo", "value": "100"}, expected={"name": "foo", "value": 100}, ok=True),
        ]
        for c in candidates:
            with self.subTest(value=c.value, ok=c.ok):
                actual, err = S().load(c.value)
                self.assert_value(actual, err, c)

    def test_dump_default(self):
        class S(self._getTargetClass()):
            name = fields.String()

        C = namedtuple("C", "value, expected, ok")
        candidates = [
            C(value={"name": "foo", "value": "100"}, expected={"name": "foo", "value": "100"}, ok=True),
        ]
        for c in candidates:
            with self.subTest(value=c.value, ok=c.ok):
                actual, err = S().dump(c.value)
                self.assert_value(actual, err, c)

    def test_dump_specific(self):
        class S(self._getTargetClass()):
            name = fields.String()

            class Meta(object):
                additional_field = fields.Integer()

        C = namedtuple("C", "value, expected, ok")
        candidates = [
            C(value={"name": "foo", "value": "100"}, expected={"name": "foo", "value": 100}, ok=True),
            C(value={"name": "foo", "value": "100"}, expected={"name": "foo", "value": 100}, ok=True),
        ]
        for c in candidates:
            with self.subTest(value=c.value, ok=c.ok):
                actual, err = S().dump(c.value)
                self.assert_value(actual, err, c)
