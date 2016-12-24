import unittest


class CodegenTests(unittest.TestCase):
    def _getTargetClass(self):
        from ..codegen import Codegen
        return Codegen

    def _makeOne(self):
        from ..dispatcher import FormatDispatcher
        dispatcher = FormatDispatcher()
        return self._getTargetClass()(dispatcher)

    def _makeContext(self):
        from ..codegen import Context
        return Context()

    def test_simple(self):
        d = {
            "definitions": {
                "person": {
                    "properties": {
                        "name": {"type": "string"},
                        "age": {"type": "integer"},
                    }
                }
            }
        }
        target = self._makeOne()
        ctx = self._makeContext()
        target.write_schema(ctx, d)
        expected = """\
class Person(Schema):
    age = fields.Integer()
    name = fields.String()"""
        self.assertEqual(str(ctx.m), expected)
