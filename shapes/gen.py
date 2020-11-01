from __future__ import annotations
import typing as t
import pathlib
import logging
from handofcats import as_command
from metashape.outputs.openapi import emit, scan
from metashape.runtime import get_walker
from magicalimport import import_module

logger = logging.getLogger(__name__)
logging.getLogger("metashape.analyze.walker").setLevel(logging.WARNING)
here = pathlib.Path(__file__).parent


@as_command
def run(filenames: t.List[str], *, aggressive: bool = True) -> None:
    for filename in filenames:
        m = import_module(filename, cwd=True)
        walker = get_walker(m, aggressive=aggressive)
        walker.config.option.strict = False
        ctx = scan(walker)

        name = pathlib.Path(filename).with_suffix(".json").name

        # v3
        with (here / "v3" / name).open("w") as wf:
            logger.info("write %s", wf.name)
            ctx.result["version"] = "3.x.x"
            emit(ctx, output=wf)

        # v2
        with (here / "v2" / name).open("w") as wf:
            logger.info("write %s", wf.name)
            ctx.result["version"] = "2.0.0"
            ctx.result["definitions"] = ctx.result["components"].pop("schemas")
            ctx.result.pop("components")
            from io import StringIO

            o = StringIO()
            emit(ctx, output=o)
            print(o.getvalue().replace("/components/schemas", "/definitions/"), file=wf)
