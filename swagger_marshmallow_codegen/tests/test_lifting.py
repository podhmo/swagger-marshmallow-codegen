from __future__ import annotations
import pathlib
import json
import pytest
from .testing import load_srcfile

here = pathlib.Path(__file__).parent


@pytest.mark.parametrize(
    "unflatten_file, flatten_file",
    [
        ("./legacy_src/01commit.yaml", "./legacy_src/00commit.yaml"),
        ("./legacy_src/01empty.yaml", "./legacy_src/02empty.yaml"),
    ],
)
def test(
    unflatten_file, flatten_file,
):
    from swagger_marshmallow_codegen.lifting import lifting_definition as _callFUT

    d = load_srcfile(unflatten_file, here=here)
    got = _callFUT(d)
    want = load_srcfile(flatten_file, here=here)
    assert json.dumps(got, indent=2, sort_keys=True) == json.dumps(
        want, indent=2, sort_keys=True
    )
