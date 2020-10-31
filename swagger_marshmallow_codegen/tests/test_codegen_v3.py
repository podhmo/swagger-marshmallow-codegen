from .testing import CodegenTests


class V2CodegenTests(CodegenTests):
    def test_it(self):
        from swagger_marshmallow_codegen.lifting import lifting_definition

        candidates = [
            ("./v3src/00person.yaml", "./v3dst/00person.py"),
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
