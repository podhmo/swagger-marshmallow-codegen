from __future__ import annotations
import pytest
import pathlib
from .testing import load_srcfile, load_dstfile
from .codegen_candidates import CANDIDATES


here = pathlib.Path(__file__).parent


def _getTargetClass():
    from swagger_marshmallow_codegen.codegen import Codegen

    return Codegen


def _makeOne():
    from swagger_marshmallow_codegen.resolver import Resolver
    from swagger_marshmallow_codegen.dispatcher import FormatDispatcher

    resolver = Resolver(FormatDispatcher())
    return _getTargetClass()(resolver)


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
    target = _makeOne()
    target.codegen(
        lifting_definition(d),
        {
            "schema": True,
            "input": True,
            "output": True,
            "emit_schema_even_primitive_type": True,
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
    target = _makeOne()
    target.codegen(
        lifting_definition(d),
        {
            "schema": True,
            "input": True,
            "output": True,
            "emit_schema_even_primitive_type": True,
        },
        ctx=ctx,
        test=True,
    )

    expected = load_dstfile(dst_dir / dst_file, here=here).rstrip("\n")
    actual = str(ctx.m).rstrip("\n")
    assert actual == expected

