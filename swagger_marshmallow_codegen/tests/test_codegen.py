from __future__ import annotations
import pytest
import pathlib
from .testing import load_srcfile, load_dstfile, get_codegen
from .codegen_candidates import CANDIDATES


here = pathlib.Path(__file__).parent


@pytest.mark.parametrize("msg, src_file, dst_file", CANDIDATES)
def test_v2(
    msg,
    src_file,
    dst_file,
    *,
    src_dir=pathlib.Path("v2src"),
    dst_dir=pathlib.Path("v2dst")
):

    from swagger_marshmallow_codegen.lifting import lifting_definition
    from swagger_marshmallow_codegen.codegen import Context

    d = load_srcfile(src_dir / src_file, here=here)
    ctx = Context()
    get_codegen().codegen(
        lifting_definition(d),
        {
            "schema": True,
            "input": True,
            "output": True,
            "emit_schema_even_primitive_type": True,
            "additional_properties_default": False,
        },
        ctx=ctx,
        test=True,
    )

    expected = load_dstfile(dst_dir / dst_file, here=here).rstrip("\n")
    actual = str(ctx.m).rstrip("\n")
    assert actual == expected


@pytest.mark.parametrize("msg, src_file, dst_file", CANDIDATES)
def test_v3(
    msg,
    src_file,
    dst_file,
    *,
    src_dir=pathlib.Path("v3src"),
    dst_dir=pathlib.Path("v3dst")
):

    from swagger_marshmallow_codegen.lifting import lifting_definition
    from swagger_marshmallow_codegen.codegen import Context

    d = load_srcfile(src_dir / src_file, here=here)
    ctx = Context()
    get_codegen().codegen(
        lifting_definition(d),
        {
            "schema": True,
            "input": True,
            "output": True,
            "emit_schema_even_primitive_type": True,
            "additional_properties_default": False,
        },
        ctx=ctx,
        test=True,
    )

    expected = load_dstfile(dst_dir / dst_file, here=here).rstrip("\n")
    actual = str(ctx.m).rstrip("\n")
    assert actual == expected
