from __future__ import annotations
import typing as t
import typing_extensions as tx


class ConfigDict(tx.TypedDict, total=False):
    schema: bool
    input: bool
    output: bool

    verbose: bool  # emit Meta.unknown=RAISE, explicitly
    additional_properties_default: bool

    emit_schema_even_primitive_type: bool
    skip_header_comment: bool
    header_comment: str
