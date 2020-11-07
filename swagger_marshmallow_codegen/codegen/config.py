from __future__ import annotations
import typing_extensions as tx


class ConfigDict(tx.TypedDict, total=False):
    emit_schema: bool  # emit definitions schemas
    emit_input: bool  # emit input schema
    emit_output: bool  # emit output schema

    separated_output: bool  # activate separated output

    explicit: bool  # emit Meta.unknown=RAISE, explicitly
    additional_properties_default: bool  # if true meta.unknown=INCLUDE

    emit_schema_even_primitive_type: bool  # emit not used toplevel definitions
    header_comment: str  # header comment
