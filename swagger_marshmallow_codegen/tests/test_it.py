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
            if len(firstlines) == 1 and first.strip('\r\n') == first:
                firstlines = [first + '\n']
                secondlines = [second + '\n']
            diff = '\n' + ''.join(difflib.unified_diff(firstlines, secondlines, fromfile="first", tofile="second"))
            raise self.fail(self._formatMessage(diff, msg))


class CodegenTests(DiffTestCase):
    here = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))

    def _getTargetClass(self):
        from ..codegen import Codegen
        return Codegen

    def _makeOne(self):
        from ..dispatcher import FormatDispatcher
        from ..resolver import Resolver
        dispatcher = FormatDispatcher()
        resolver = Resolver()
        return self._getTargetClass()(dispatcher, resolver)

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
