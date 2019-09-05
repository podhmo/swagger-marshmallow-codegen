# -*- coding:utf-8 -*-
import re


def normalize(name, ignore_rx=re.compile("[^0-9a-zA-Z_]+")):
    c = name[0]
    if c.isdigit():
        name = "n" + name
    elif not (c.isalpha() or c == "_"):
        name = "x" + name
    return ignore_rx.sub("", name.replace("-", "_"))


def titleize(name):
    if not name:
        return name
    name = str(name)
    return normalize("{}{}".format(name[0].upper(), name[1:]))


def untitleize(name):
    if not name:
        return name
    return "{}{}".format(name[0].lower(), name[1:])


def clsname_from_path(
    path, ignore_rx=re.compile("[^0-9a-zA-Z_]+"), separate_rx=re.compile("[/_]")
):
    path_separated = separate_rx.split(path.lstrip("/"))  # xxx:
    return "".join(titleize(ignore_rx.sub("", name)) for name in path_separated)


class LazyCallString:
    def __init__(self, call, *args, **kwargs):
        self.call = call
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        return self.call(*self.args, **self.kwargs)
