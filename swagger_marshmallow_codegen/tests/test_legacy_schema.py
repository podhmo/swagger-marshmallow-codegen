import unittest
from marshmallow import fields, ValidationError


class Tests(unittest.TestCase):
    def _getTargetClass(self):
        from swagger_marshmallow_codegen.schema.legacy import LegacySchema

        return LegacySchema

    def test_load_ok(self):
        class S(self._getTargetClass()):
            name = fields.String(required=True)

        r = S().load({"name": "foo"})
        self.assertEqual(r.data, {"name": "foo"})
        self.assertEqual(r.errors, None)

    def test_load_ok__many(self):
        class S(self._getTargetClass()):
            name = fields.String(required=True)

        r = S().load([{"name": "foo"}], many=True)
        self.assertEqual(r.data, [{"name": "foo"}])
        self.assertEqual(r.errors, None)

    def test_load_ok__many2(self):
        class S(self._getTargetClass()):
            name = fields.String(required=True)

        r = S(many=True).load([{"name": "foo"}])
        self.assertEqual(r.data, [{"name": "foo"}])
        self.assertEqual(r.errors, None)

    def test_load_ng(self):
        class S(self._getTargetClass()):
            name = fields.String(required=True)

        r = S().load({})
        self.assertEqual(r.data, {})
        self.assertIsInstance(r.errors, ValidationError)

    def test_load_ng__many(self):
        class S(self._getTargetClass()):
            name = fields.String(required=True)

        r = S().load([{}], many=True)
        self.assertEqual(r.data, [])
        self.assertIsInstance(r.errors, ValidationError)

    def test_load_ng__many2(self):
        class S(self._getTargetClass()):
            name = fields.String(required=True)

        r = S(many=True).load([{}])
        self.assertEqual(r.data, [])
        self.assertIsInstance(r.errors, ValidationError)

    def test_load_ng__strict(self):
        class S(self._getTargetClass()):
            name = fields.String(required=True)

        with self.assertRaises(ValidationError):
            S(strict=True).load({})
