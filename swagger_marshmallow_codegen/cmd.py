from __future__ import annotations
import typing as t
import sys
import logging
import argparse
from magicalimport import import_symbol


if t.TYPE_CHECKING:
    from swagger_marshmallow_codegen.driver import Driver, ConfigDict

logger = logging.getLogger(__name__)


def main(setup: t.Optional[t.Callable[[Driver], None]] = None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--driver", default="Driver")
    parser.add_argument(
        "--logging",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
    )
    parser.add_argument("--full", action="store_true")
    parser.add_argument("--legacy", action="store_true")
    parser.add_argument("--strict-additional-properties", action="store_true")
    parser.add_argument("--explicit", action="store_true")

    parser.add_argument("-d", "--separated-output", default=None)

    parser.add_argument("file", default=None)
    args = parser.parse_args()

    logging.basicConfig(
        format="%(levelname)5s:%(name)36s:%(message)s",
        level=logging._nameToLevel[args.logging],
    )

    driver_cls = args.driver
    if args.legacy and driver_cls == "Driver":  # xxx
        logger.info("legacy option is added. output Schema is legacy flavor")
        driver_cls = "LegacyDriver"
    if ":" not in driver_cls:
        driver_cls = "swagger_marshmallow_codegen.driver:{}".format(driver_cls)

    config: ConfigDict = {
        "emit_schema": True,
        "emit_input": False,
        "emit_output": False,
        "additional_properties_default": not args.strict_additional_properties,
        "separated_output": bool(args.separated_output),
    }
    if args.full:
        config["emit_input"] = True
        config["emit_output"] = True

    logger.debug("config is %r", config)

    driver = import_symbol(driver_cls, cwd=True)(config)
    if setup is not None:
        setup(driver)

    if args.file is None:
        driver.run(sys.stdin, output=args.separated_output)
    else:
        with open(args.file) as rf:
            driver.run(rf, output=args.separated_output)
