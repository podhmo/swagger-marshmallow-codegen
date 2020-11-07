from __future__ import annotations
import pytest
import pathlib
from .testing import load_srcfile, load_dstfile, get_codegen


here = pathlib.Path(__file__).parent


@pytest.mark.parametrize(
    "src_file, dst_file, header_comment",
    [
        ("./legacy_src/00person.yaml", "./legacy_dst/00person.py", ""),
        ("./legacy_src/01person.yaml", "./legacy_dst/01person.py", ""),
        ("./legacy_src/02person.yaml", "./legacy_dst/02person.py", ""),
        ("./legacy_src/03person.yaml", "./legacy_dst/03person.py", ""),
        ("./legacy_src/04person.yaml", "./legacy_dst/04person.py", ""),
        ("./legacy_src/05person.yaml", "./legacy_dst/05person.py", ""),
        ("./legacy_src/00commit.yaml", "./legacy_dst/00commit.py", ""),
        ("./legacy_src/01commit.yaml", "./legacy_dst/01commit.py", ""),
        ("./legacy_src/00emojis.yaml", "./legacy_dst/00emojis.py", ""),
        ("./legacy_src/00stat.yaml", "./legacy_dst/00stat.py", ""),
        ("./legacy_src/00default.yaml", "./legacy_dst/00default.py", ""),
        ("./legacy_src/00maximum.yaml", "./legacy_dst/00maximum.py", ""),
        ("./legacy_src/00length.yaml", "./legacy_dst/00length.py", ""),
        ("./legacy_src/00regex.yaml", "./legacy_dst/00regex.py", ""),
        ("./legacy_src/00enum.yaml", "./legacy_dst/00enum.py", ""),
        ("./legacy_src/00items.yaml", "./legacy_dst/00items.py", ""),
        ("./legacy_src/00readonly.yaml", "./legacy_dst/00readonly.py", ""),
        ("./legacy_src/00allOf.yaml", "./legacy_dst/00allOf.py", ""),
        ("./legacy_src/00allOf2.yaml", "./legacy_dst/00allOf2.py", ""),
        ("./legacy_src/01allOf2.yaml", "./legacy_dst/01allOf2.py", ""),
        ("./legacy_src/02allOf2.yaml", "./legacy_dst/02allOf2.py", ""),
        ("./legacy_src/00paths.yaml", "./legacy_dst/00paths.py", ""),
        ("./legacy_src/01paths.yaml", "./legacy_dst/01paths.py", ""),
        ("./legacy_src/02paths.yaml", "./legacy_dst/02paths.py", ""),
        ("./legacy_src/03paths.yaml", "./legacy_dst/03paths.py", ""),
        ("./legacy_src/00empty.yaml", "./legacy_dst/00empty.py", "# flake8: noqa"),
        ("./legacy_src/01empty.yaml", "./legacy_dst/01empty.py", ""),
        (
            "./legacy_src/00list_with_options.yaml",
            "./legacy_dst/00list_with_options.py",
            "",
        ),
        ("./legacy_src/00reserved.yaml", "./legacy_dst/00reserved.py", ""),
        ("./legacy_src/00typearray.yaml", "./legacy_dst/00typearray.py", ""),
        ("./legacy_src/00additional.yaml", "./legacy_dst/00additional.py", ""),
        ("./legacy_src/01additional.yaml", "./legacy_dst/01additional.py", ""),
        ("./legacy_src/02additional.yaml", "./legacy_dst/02additional.py", ""),
        ("./legacy_src/03additional.yaml", "./legacy_dst/03additional.py", ""),
        ("./legacy_src/00nullable.yaml", "./legacy_dst/00nullable.py", ""),
        ("./legacy_src/00primitiveapi.yaml", "./legacy_dst/00primitiveapi.py", ""),
        # ("./legacy_src/00patternProperties.yaml", "./legacy_dst/00patternProperties.py"),  not supported yet
        # x-marshmallow-name
        (
            "./legacy_src/00x_marshmallow_name.yaml",
            "./legacy_dst/00x_marshmallow_name.py",
            "",
        ),
        (
            "./legacy_src/00x_marshmallow_name.yaml",
            "./legacy_dst/00x_marshmallow_name.py",
            "",
        ),
    ],
)
def test(
    src_file: str, dst_file: str, header_comment: str,
):
    from swagger_marshmallow_codegen.lifting import lifting_definition
    from swagger_marshmallow_codegen.codegen import Context

    d = load_srcfile(src_file, here=here)
    ctx = Context()

    get_codegen().codegen(
        lifting_definition(d),
        {
            "emit_schema": True,
            "emit_input": True,
            "emit_output": True,
            "header_comment": header_comment,
            "additional_properties_default": False,
        },
        ctx=ctx,
    )

    expected = load_dstfile(dst_file, here=here).rstrip("\n")
    actual = str(ctx.m).rstrip("\n")
    assert actual == expected
