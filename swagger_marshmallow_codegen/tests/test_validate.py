import unittest
from collections import namedtuple


class RangeTests(unittest.TestCase):
    def _makeOne(self, *args, **kwargs):
        from swagger_marshmallow_codegen.validate import Range
        return Range(*args, **kwargs)

    def test_maximum(self):
        from marshmallow.validate import ValidationError

        C = namedtuple("C", "maximum, exclusive_maximum, value, ok")
        candidates = [
            C(maximum=100, exclusive_maximum=False, value=99, ok=True),
            C(maximum=100, exclusive_maximum=False, value=100, ok=True),
            C(maximum=100, exclusive_maximum=False, value=101, ok=False),
            C(maximum=100, exclusive_maximum=True, value=99, ok=True),
            C(maximum=100, exclusive_maximum=True, value=100, ok=False),
            C(maximum=100, exclusive_maximum=True, value=101, ok=False),
        ]
        for c in candidates:
            with self.subTest(maximum=c.maximum, exclusive_maximum=c.exclusive_maximum, value=c.value):
                target = self._makeOne(max=c.maximum, exclusive_max=c.exclusive_maximum)
                try:
                    target(c.value)
                    self.assertTrue(c.ok)
                except ValidationError:
                    self.assertFalse(c.ok)

    def test_minimum(self):
        from marshmallow.validate import ValidationError

        C = namedtuple("C", "minimum, exclusive_minimum, value, ok")
        candidates = [
            C(minimum=100, exclusive_minimum=False, value=99, ok=False),
            C(minimum=100, exclusive_minimum=False, value=100, ok=True),
            C(minimum=100, exclusive_minimum=False, value=101, ok=True),
            C(minimum=100, exclusive_minimum=True, value=99, ok=False),
            C(minimum=100, exclusive_minimum=True, value=100, ok=False),
            C(minimum=100, exclusive_minimum=True, value=101, ok=True),
        ]
        for c in candidates:
            with self.subTest(minimum=c.minimum, exclusive_minimum=c.exclusive_minimum, value=c.value):
                target = self._makeOne(min=c.minimum, exclusive_min=c.exclusive_minimum)
                try:
                    target(c.value)
                    self.assertTrue(c.ok)
                except ValidationError:
                    self.assertFalse(c.ok)
