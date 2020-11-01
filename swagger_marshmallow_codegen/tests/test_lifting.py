import unittest
import os.path


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
            ("./legacy_src/01commit.yaml", "./legacy_src/00commit.yaml"),
            ("./legacy_src/01empty.yaml", "./legacy_src/02empty.yaml"),
        ]
        for src_file, dst_file in candidates:
            with self.subTest(src_file=src_file, dst_file=dst_file):
                noflatten = self.load_srcfile(src_file)
                actual = self._callFUT(noflatten)
                flatten = self.load_dstfile(dst_file)
                from dictknife import deepequal

                self.assertTrue(deepequal(flatten, actual))
