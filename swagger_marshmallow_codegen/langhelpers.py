# -*- coding:utf-8 -*-
import sys
import os.path
import importlib
import magicalimport


def titlize(name):
    if not name:
        return name
    return "{}{}".format(name[0].upper(), name[1:]).replace("-", "_")


def untitlize(name):
    if not name:
        return name
    return "{}{}".format(name[0].lower(), name[1:])


def load_function(sym, here=None):
    module_path, fn_name = sym.rsplit(":", 2)
    try:
        _, ext = os.path.splitext(module_path)
        if ext == ".py":
            module = magicalimport.import_from_physical_path(module_path, here=here)
        else:
            module = importlib.import_module(module_path)
        return getattr(module, fn_name)
    except (ImportError, AttributeError) as e:
        sys.stderr.write("could not import {!r}\n{}\n".format(sym, e))
        raise
