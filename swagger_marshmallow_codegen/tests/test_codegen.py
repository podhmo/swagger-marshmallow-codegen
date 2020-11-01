import pathlib
from .testing import CodegenTests


CANDIDATES = [("simple", "00simple-object.json", "00simple-object.py")]


class V2Tests(CodegenTests):
    src_dir = pathlib.Path("v2src")
    dst_dir = pathlib.Path("v2dst")

    def test_it(self):
        from swagger_marshmallow_codegen.lifting import lifting_definition

        for msg, src_file, dst_file in CANDIDATES:
            with self.subTest(msg=msg, src_file=src_file, dst_file=dst_file):
                d = self.load_srcfile(self.src_dir / src_file)
                target = self._makeOne()
                ctx = self._makeContext()

                target.codegen(
                    lifting_definition(d),
                    {"schema": True, "input": True, "output": True},
                    ctx=ctx,
                    test=True,
                )

                expected = self.load_dstfile(self.dst_dir / dst_file).rstrip("\n")
                actual = str(ctx.m).rstrip("\n")
                self.assertEqual(actual, expected)


class V3Tests(CodegenTests):
    src_dir = pathlib.Path("v3src")
    dst_dir = pathlib.Path("v3dst")

    def test_it(self):
        from swagger_marshmallow_codegen.lifting import lifting_definition

        for msg, src_file, dst_file in CANDIDATES:
            with self.subTest(msg=msg, src_file=src_file, dst_file=dst_file):
                d = self.load_srcfile(self.src_dir / src_file)
                target = self._makeOne()
                ctx = self._makeContext()

                target.codegen(
                    lifting_definition(d),
                    {"schema": True, "input": True, "output": True},
                    ctx=ctx,
                    test=True,
                )

                expected = self.load_dstfile(self.dst_dir / dst_file).rstrip("\n")
                actual = str(ctx.m).rstrip("\n")
                self.assertEqual(actual, expected)
