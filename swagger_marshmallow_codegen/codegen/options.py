from __future__ import annotations
import typing as t


class CodegenTargetDict(t.TypedDict):
    schema: bool
    input: bool
    output: bool
