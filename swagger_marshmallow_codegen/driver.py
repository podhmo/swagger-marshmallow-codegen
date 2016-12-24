# -*- coding:utf-8 -*-
import logging
from . import loading
from .dispatcher import FormatDispatcher
from .accessor import Accessor
from .codegen import Codegen
logger = logging.getLogger(__name__)


class Driver(object):
    def load(self, fp):
        return loading.load(fp)

    def dump(self, m, fp):
        return print(m, file=fp)

    def transform(self, d):
        dispatcher = FormatDispatcher()
        accessor = Accessor()
        return Codegen(dispatcher, accessor).codegen(d)

    def run(self, inp, outp):
        data = self.load(inp)
        result = self.transform(data)
        self.dump(result, outp)
