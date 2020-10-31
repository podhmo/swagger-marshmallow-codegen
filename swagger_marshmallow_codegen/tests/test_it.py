import unittest
import difflib
import os.path


class DiffTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.addTypeEqualityFunc(str, "assertDiff")

    def assertDiff(self, first, second, msg=None):
        self.assertIsInstance(first, str, "First argument is not a string")
        self.assertIsInstance(second, str, "Second argument is not a string")

        msg = msg or "{} != {}".format(repr(first)[:40], repr(second)[:40])

        if first != second:
            # don't use difflib if the strings are too long
            if len(first) > self._diffThreshold or len(second) > self._diffThreshold:
                self._baseAssertEqual(first, second, msg)

            firstlines = first.splitlines(keepends=True)
            secondlines = second.splitlines(keepends=True)
            if not firstlines[-1].endswith("\n"):
                firstlines[-1] = firstlines[-1] + "\n"
            if not secondlines[-1].endswith("\n"):
                secondlines[-1] = secondlines[-1] + "\n"
            diff = "\n" + "".join(
                difflib.unified_diff(
                    firstlines, secondlines, fromfile="first", tofile="second"
                )
            )
            raise self.fail(self._formatMessage(diff, msg))


class CodegenTests(DiffTestCase):
    here = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))

    def _getTargetClass(self):
        from swagger_marshmallow_codegen.codegen import Codegen

        return Codegen

    def _makeOne(self):
        from swagger_marshmallow_codegen.resolver import Resolver
        from swagger_marshmallow_codegen.dispatcher import FormatDispatcher

        resolver = Resolver(FormatDispatcher())
        return self._getTargetClass()(resolver)

    def _makeContext(self):
        from swagger_marshmallow_codegen.codegen import Context

        return Context()

    def load_srcfile(self, src):
        from swagger_marshmallow_codegen.loading import load

        with open(os.path.join(self.here, src)) as rf:
            return load(rf)

    def load_dstfile(self, dst):
        with open(os.path.join(self.here, dst)) as rf:
            return rf.read()

    def test_it(self):
        from swagger_marshmallow_codegen.lifting import lifting_definition

        candidates = [
            ("./v2src/00person.yaml", "./v2dst/00person.py"),
            ("./v2src/01person.yaml", "./v2dst/01person.py"),
            ("./v2src/02person.yaml", "./v2dst/02person.py"),
            ("./v2src/03person.yaml", "./v2dst/03person.py"),
            ("./v2src/04person.yaml", "./v2dst/04person.py"),
            ("./v2src/05person.yaml", "./v2dst/05person.py"),
            ("./v2src/00commit.yaml", "./v2dst/00commit.py"),
            ("./v2src/01commit.yaml", "./v2dst/01commit.py"),
            ("./v2src/00emojis.yaml", "./v2dst/00emojis.py"),
            ("./v2src/00stat.yaml", "./v2dst/00stat.py"),
            ("./v2src/00default.yaml", "./v2dst/00default.py"),
            ("./v2src/00maximum.yaml", "./v2dst/00maximum.py"),
            ("./v2src/00length.yaml", "./v2dst/00length.py"),
            ("./v2src/00regex.yaml", "./v2dst/00regex.py"),
            ("./v2src/00enum.yaml", "./v2dst/00enum.py"),
            ("./v2src/00items.yaml", "./v2dst/00items.py"),
            ("./v2src/00readonly.yaml", "./v2dst/00readonly.py"),
            ("./v2src/00allOf.yaml", "./v2dst/00allOf.py"),
            ("./v2src/00allOf2.yaml", "./v2dst/00allOf2.py"),
            ("./v2src/01allOf2.yaml", "./v2dst/01allOf2.py"),
            ("./v2src/02allOf2.yaml", "./v2dst/02allOf2.py"),
            ("./v2src/00paths.yaml", "./v2dst/00paths.py"),
            ("./v2src/01paths.yaml", "./v2dst/01paths.py"),
            ("./v2src/02paths.yaml", "./v2dst/02paths.py"),
            ("./v2src/03paths.yaml", "./v2dst/03paths.py"),
            ("./v2src/00empty.yaml", "./v2dst/00empty.py"),
            ("./v2src/01empty.yaml", "./v2dst/01empty.py"),
            ("./v2src/00list_with_options.yaml", "./v2dst/00list_with_options.py"),
            ("./v2src/00reserved.yaml", "./v2dst/00reserved.py"),
            ("./v2src/00typearray.yaml", "./v2dst/00typearray.py"),
            ("./v2src/00additional.yaml", "./v2dst/00additional.py"),
            ("./v2src/01additional.yaml", "./v2dst/01additional.py"),
            ("./v2src/00nullable.yaml", "./v2dst/00nullable.py"),
            ("./v2src/00primitiveapi.yaml", "./v2dst/00primitiveapi.py"),
            # ("./v2src/00patternProperties.yaml", "./v2dst/00patternProperties.py"),  not supported yet
        ]
        for src_file, dst_file in candidates:
            with self.subTest(src_file=src_file, dst_file=dst_file):
                d = self.load_srcfile(src_file)
                target = self._makeOne()
                ctx = self._makeContext()

                target.codegen(
                    lifting_definition(d),
                    {"schema": True, "input": True, "output": True},
                    ctx=ctx,
                    test=True,
                )

                expected = self.load_dstfile(dst_file).rstrip("\n")
                actual = str(ctx.m).rstrip("\n")
                self.assertEqual(actual, expected)


class FlattenTests(unittest.TestCase):
    here = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))

    def _callFUT(self, d):
        from swagger_marshmallow_codegen.lifting import lifting_definition

        return lifting_definition(d)

    def load_srcfile(self, src):
        from swagger_marshmallow_codegen.loading import load

        with open(os.path.join(self.here, src)) as rf:
            return load(rf)

    def load_dstfile(self, dst):
        from swagger_marshmallow_codegen.loading import load

        with open(os.path.join(self.here, dst)) as rf:
            return load(rf)

    def test_it(self):
        candidates = [
            ("./v2src/01commit.yaml", "./v2src/00commit.yaml"),
            ("./v2src/01empty.yaml", "./v2src/02empty.yaml"),
        ]
        for src_file, dst_file in candidates:
            with self.subTest(src_file=src_file, dst_file=dst_file):
                noflatten = self.load_srcfile(src_file)
                actual = self._callFUT(noflatten)
                flatten = self.load_dstfile(dst_file)
                from dictknife import deepequal

                self.assertTrue(deepequal(flatten, actual))
