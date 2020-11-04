from __future__ import annotations
import typing_extensions as tx


class ConfigDict(tx.TypedDict, total=False):
    schema: bool  # emit definitions schemas
    input: bool  # emit input schema
    output: bool  # emit output schema

    explicit: bool  # emit Meta.unknown=RAISE, explicitly
    additional_properties_default: bool  # if true meta.unknown=INCLUDE

    emit_schema_even_primitive_type: bool  # emit not used toplevel definitions
    skip_header_comment: bool
    header_comment: str
