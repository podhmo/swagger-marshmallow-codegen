from __future__ import annotations
import typing as t
from swagger_marshmallow_codegen.cmd import main

if t.TYPE_CHECKING:
    from swagger_marshmallow_codegen.driver import Driver


def setup(driver: Driver) -> None:
    driver.options["targets"]["emit_schema_even_primitive_type"] = True


main(setup)
