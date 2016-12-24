# -*- coding:utf-8 -*-
import logging
from . import loading
from .dispatcher import FormatDispatcher
from .accessor import Accessor
from .codegen import Codegen
from .lifting import lifting_definition
logger = logging.getLogger(__name__)


class Driver(object):
    def load(self, fp):
        return loading.load(fp)

    def dump(self, m, fp):
        return print(m, file=fp)

    def transform(self, d):
        d = lifting_definition(d)
        with open("/tmp/x.json", "w") as wf:
            import json
            json.dump(d["definitions"], wf, indent=2)
        dispatcher = FormatDispatcher()
        accessor = Accessor()
        return Codegen(dispatcher, accessor).codegen(d)

    def run(self, inp, outp):
        data = self.load(inp)
        result = self.transform(data)
        self.dump(result, outp)


class Flatten(object):
    def load(self, fp):
        return loading.load(fp)

    def dump(self, d, fp):
        return loading.dump(d, fp)

    def transform(self, d):
        return lifting_definition(d)

    def run(self, inp, outp):
        data = self.load(inp)
        result = self.transform(data)
        self.dump(result, outp)
