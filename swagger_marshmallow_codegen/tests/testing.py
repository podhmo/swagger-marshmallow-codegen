from __future__ import annotations
import typing as t
import pathlib


def get_codegen():
    from swagger_marshmallow_codegen.codegen import Codegen as _TargetClass
    from swagger_marshmallow_codegen.resolver import Resolver
    from swagger_marshmallow_codegen.dispatcher import FormatDispatcher

    resolver = Resolver(FormatDispatcher())
    return _TargetClass(resolver=resolver)


def load_srcfile(
    src: t.Union[str, pathlib.Path], *, here: pathlib.Path
) -> t.Dict[str, t.Any]:
    from swagger_marshmallow_codegen.loading import load

    filepath = here / src
    with filepath.open() as rf:
        return load(rf)


def load_dstfile(dst: t.Union[str, pathlib.Path], *, here: pathlib.Path) -> str:
    try:
        filepath = here / dst
        with filepath.open() as rf:
            return rf.read()
    except FileNotFoundError:
        return "# dummy\n"
