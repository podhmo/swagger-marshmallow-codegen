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
        from ..accessor import Accessor
        from ..resolver import Resolver
        from ..dispatcher import FormatDispatcher
        accessor = Accessor(Resolver(FormatDispatcher()))
        return self._getTargetClass()(accessor)

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
        from ..lifting import lifting_definition
        candidates = [
            ("./src/00person.yaml", "./dst/00person.py"),
            ("./src/01person.yaml", "./dst/01person.py"),
            ("./src/02person.yaml", "./dst/02person.py"),
            ("./src/03person.yaml", "./dst/03person.py"),
            ("./src/04person.yaml", "./dst/04person.py"),
            ("./src/05person.yaml", "./dst/05person.py"),
            ("./src/00commit.yaml", "./dst/00commit.py"),
            ("./src/01commit.yaml", "./dst/01commit.py"),
            ("./src/00emojis.yaml", "./dst/00emojis.py"),
            ("./src/00stat.yaml", "./dst/00stat.py"),
            ("./src/00default.yaml", "./dst/00default.py"),
            ("./src/00maximum.yaml", "./dst/00maximum.py"),
            ("./src/00length.yaml", "./dst/00length.py"),
            ("./src/00regex.yaml", "./dst/00regex.py"),
            ("./src/00enum.yaml", "./dst/00enum.py"),
            ("./src/00items.yaml", "./dst/00items.py"),
            ("./src/00readonly.yaml", "./dst/00readonly.py"),
            ("./src/00allOf.yaml", "./dst/00allOf.py"),
            ("./src/00allOf2.yaml", "./dst/00allOf2.py"),
            ("./src/01allOf2.yaml", "./dst/01allOf2.py"),
            ("./src/02allOf2.yaml", "./dst/02allOf2.py"),
            ("./src/00paths.yaml", "./dst/00paths.py"),
            ("./src/01paths.yaml", "./dst/01paths.py"),
            ("./src/02paths.yaml", "./dst/02paths.py"),
            ("./src/03paths.yaml", "./dst/03paths.py"),
            ("./src/00empty.yaml", "./dst/00empty.py"),
            ("./src/01empty.yaml", "./dst/01empty.py"),
            ("./src/00list_with_options.yaml", "./dst/00list_with_options.py"),
            ("./src/00reserved.yaml", "./dst/00reserved.py"),
            ("./src/00typearray.yaml", "./dst/00typearray.py"),
        ]
        for src_file, dst_file in candidates:
            with self.subTest(src_file=src_file, dst_file=dst_file):
                d = self.load_srcfile(src_file)
                target = self._makeOne()
                ctx = self._makeContext()

                target.codegen(lifting_definition(d), {"schema": True, "input": True, "output": True}, ctx=ctx)

                expected = self.load_dstfile(dst_file).rstrip("\n")
                actual = str(ctx.m).rstrip("\n")
                self.assertEqual(actual, expected)


class FlattenTests(unittest.TestCase):
    here = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))

    def _callFUT(self, d):
        from ..lifting import lifting_definition
        return lifting_definition(d)

    def load_srcfile(self, src):
        from ..loading import load
        with open(os.path.join(self.here, src)) as rf:
            return load(rf)

    def load_dstfile(self, dst):
        from ..loading import load
        with open(os.path.join(self.here, dst)) as rf:
            return load(rf)

    def test_it(self):
        candidates = [
            ("./src/01commit.yaml", "./src/00commit.yaml"),
            ("./src/01empty.yaml", "./src/02empty.yaml"),
        ]
        for src_file, dst_file in candidates:
            with self.subTest(src_file=src_file, dst_file=dst_file):
                noflatten = self.load_srcfile(src_file)
                actual = self._callFUT(noflatten)
                flatten = self.load_dstfile(dst_file)
                from dictknife import deepequal
                self.assertTrue(deepequal(flatten, actual))
