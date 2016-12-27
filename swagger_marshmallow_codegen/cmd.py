# -*- coding:utf-8 -*-
import sys
import logging
import argparse
from swagger_marshmallow_codegen.langhelpers import load_function


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--driver", default="swagger_marshmallow_codegen.driver:Driver")
    parser.add_argument("--logging", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"])
    parser.add_argument("file", default=None)
    args = parser.parse_args()

    driver_cls = args.driver
    if ":" not in driver_cls:
        driver_cls = "swagger_marshmallow_codegen.driver:{}".format(driver_cls)
    driver = load_function(driver_cls)()

    # todo: option
    logging.basicConfig(
        format="%(levelname)5s:%(name)36s:%(message)s",
        level=logging._nameToLevel[args.logging]
    )

    if args.file is None:
        driver.run(sys.stdin, sys.stdout)
    else:
        with open(args.file) as rf:
            driver.run(rf, sys.stdout)
