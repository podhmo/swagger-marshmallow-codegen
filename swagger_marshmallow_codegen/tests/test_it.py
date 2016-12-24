import unittest
import difflib
import os.path


class DiffTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.addTypeEqualityFunc(str, 'assertDiff')

    def assertDiff(self, first, second, msg=None):
        self.assertIsInstance(first, str, 'First argument is not a string')
        self.assertIsInstance(second, str, 'Second argument is not a string')

        msg = msg or "{} != {}".format(repr(first)[:40], repr(second)[:40])

        if first != second:
            # don't use difflib if the strings are too long
            if (len(first) > self._diffThreshold or len(second) > self._diffThreshold):
                self._baseAssertEqual(first, second, msg)

            firstlines = first.splitlines(keepends=True)
            secondlines = second.splitlines(keepends=True)
            if not firstlines[-1].endswith("\n"):
                firstlines[-1] = firstlines[-1] + "\n"
            if not secondlines[-1].endswith("\n"):
                secondlines[-1] = secondlines[-1] + "\n"
            diff = '\n' + ''.join(difflib.unified_diff(firstlines, secondlines, fromfile="first", tofile="second"))
            raise self.fail(self._formatMessage(diff, msg))


class CodegenTests(DiffTestCase):
    here = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))

    def _getTargetClass(self):
        from ..codegen import Codegen
        return Codegen

    def _makeOne(self):
        from ..dispatcher import FormatDispatcher
        from ..accessor import Accessor
        dispatcher = FormatDispatcher()
        accessor = Accessor()
        return self._getTargetClass()(dispatcher, accessor)

    def _makeContext(self):
        from ..codegen import Context
        return Context()

    def load_srcfile(self, src):
        from ..loading import load
        with open(os.path.join(self.here, src)) as rf:
            return load(rf)

    def load_dstfile(self, dst):
        with open(os.path.join(self.here, dst)) as rf:
            return rf.read()

    def test_it(self):
        candidates = [
            ("./src/00person.yaml", "./dst/00person.py"),
            ("./src/01person.yaml", "./dst/01person.py"),
            ("./src/02person.yaml", "./dst/02person.py"),
            ("./src/03person.yaml", "./dst/03person.py"),
        ]
        for src_file, dst_file in candidates:
            with self.subTest(src_file=src_file, dst_file=dst_file):
                d = self.load_srcfile(src_file)
                target = self._makeOne()
                ctx = self._makeContext()
                target.write_schema(ctx, d)

                expected = self.load_dstfile(dst_file).rstrip("\n")
                actual = str(ctx.m).rstrip("\n")
                self.assertEqual(actual, expected)
