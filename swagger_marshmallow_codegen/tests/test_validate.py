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
            with self.subTest(
                maximum=c.maximum, exclusive_maximum=c.exclusive_maximum, value=c.value
            ):
                target = self._makeOne(
                    max=c.maximum, max_inclusive=not c.exclusive_maximum
                )
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
            with self.subTest(
                minimum=c.minimum, exclusive_minimum=c.exclusive_minimum, value=c.value
            ):
                target = self._makeOne(
                    min=c.minimum, min_inclusive=not c.exclusive_minimum
                )
                try:
                    target(c.value)
                    self.assertTrue(c.ok)
                except ValidationError:
                    self.assertFalse(c.ok)


class ItemsRangeTests(unittest.TestCase):
    def _makeOne(self, *args, **kwargs):
        from swagger_marshmallow_codegen.validate import ItemsRange

        return ItemsRange(*args, **kwargs)

    def test_it(self):
        from marshmallow.validate import ValidationError

        C = namedtuple("C", "kwargs, value, ok")

        # minItems: 1
        min1_kwargs = dict(min=1, max=None, min_inclusive=True, max_inclusive=True)

        candidates = [
            C(kwargs=min1_kwargs, value=[], ok=False),
            C(kwargs=min1_kwargs, value=[1], ok=True),
        ]
        for c in candidates:
            with self.subTest(kwargs=c.kwargs, value=c.value):
                target = self._makeOne(**c.kwargs)
                try:
                    target(c.value)
                    self.assertTrue(c.ok)
                except ValidationError:
                    self.assertFalse(c.ok)


class MultipleOfTests(unittest.TestCase):
    def _makeOne(self, *args, **kwargs):
        from swagger_marshmallow_codegen.validate import MultipleOf

        return MultipleOf(*args, **kwargs)

    def test_it(self):
        from marshmallow.validate import ValidationError

        C = namedtuple("C", "n, value, ok")
        candidates = [
            C(n=1, value=99, ok=True),
            C(n=2, value=99, ok=False),
            C(n=2, value=100, ok=True),
            C(n=2.0, value=99.0, ok=False),
            C(n=2.0, value=100.0, ok=True),
        ]
        for c in candidates:
            with self.subTest(n=c.n, value=c.value):
                target = self._makeOne(n=c.n)
                try:
                    target(c.value)
                    self.assertTrue(c.ok)
                except ValidationError:
                    self.assertFalse(c.ok)
