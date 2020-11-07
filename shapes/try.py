from __future__ import annotations
import typing as t

if t.TYPE_CHECKING:
    from swagger_marshmallow_codegen.driver import Driver


def setup(driver: Driver) -> None:
    driver.config["additional_properties_default"] = False
    driver.config["emit_schema_even_primitive_type"] = True
    driver.config["header_comment"] = ""


if __name__ == "__main__":
    from swagger_marshmallow_codegen.cmd import main

    main(setup)
