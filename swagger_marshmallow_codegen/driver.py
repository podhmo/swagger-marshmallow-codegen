# -*- coding:utf-8 -*-
import logging
from . import loading
from .accessor import Accessor
from .resolver import Resolver
from .codegen import Codegen
from .dispatcher import FormatDispatcher
from .lifting import lifting_definition
logger = logging.getLogger(__name__)


class Driver(object):
    dispatcher_factory = FormatDispatcher
    resolver_factory = Resolver
    accessor_factory = Accessor
    codegen_factory = Codegen

    def __init__(self, options):
        self.options = options

    def load(self, fp):
        return loading.load(fp)

    def dump(self, m, fp):
        return print(m, file=fp)

    def transform(self, d):
        d = lifting_definition(d)
        return self.create_codegen().codegen(d, targets=self.options["targets"])

    def run(self, inp, outp):
        data = self.load(inp)
        result = self.transform(data)
        self.dump(result, outp)

    def create_codegen(self):
        dispatcher = self.dispatcher_factory()
        resolver = self.resolver_factory(dispatcher)
        accessor = self.accessor_factory(resolver)
        return self.codegen_factory(accessor)


class Flatten(object):
    def __init__(self, options):
        self.options = options

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


class ProfileDriver(Driver):
    def run(self, inp, outp):
        import cProfile
        import pstats
        profile = cProfile.Profile()
        profile.enable()
        data = self.load(inp)
        result = self.transform(data)
        profile.disable()
        s = pstats.Stats(profile)
        s.dump_stats("swagger-marshmallow-codegen.prof")
        self.dump(result, outp)
