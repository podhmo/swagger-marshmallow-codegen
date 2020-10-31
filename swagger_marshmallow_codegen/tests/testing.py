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
