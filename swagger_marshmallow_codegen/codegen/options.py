from __future__ import annotations
import typing_extensions as tx


class CodegenTargetDict(tx.TypedDict):
    schema: bool
    input: bool
    output: bool
