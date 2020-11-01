# -*- coding:utf-8 -*-
import logging
from . import loading
from .resolver import Resolver
from .codegen import Codegen, SchemaWriter
from .dispatcher import FormatDispatcher
from .lifting import lifting_definition

logger = logging.getLogger(__name__)


class Driver:
    dispatcher_factory = FormatDispatcher
    resolver_factory = Resolver
    codegen_factory = Codegen

    def __init__(self, options):
        self.options = options

    def load(self, fp):
        # hack:
        # import dictknife.loading._yaml as xxx
        # xxx.make_dict = dict
        return loading.load(fp)

    def dump(self, m, fp):
        return print(m, file=fp)

    def transform(self, d):
        d = lifting_definition(d)
        return self.create_codegen().codegen(d, config=self.options["targets"])

    def run(self, inp, outp):
        data = self.load(inp)
        result = self.transform(data)
        self.dump(result, outp)

    def create_codegen(self):
        dispatcher = self.dispatcher_factory()
        resolver = self.resolver_factory(dispatcher)
        return self.codegen_factory(resolver)


class LegacyDriver(Driver):
    def codegen_factory(self, accessor):
        factory = Codegen.override(
            schema_class_path="swagger_marshmallow_codegen.schema.legacy:LegacySchema",
            schema_writer_factory=SchemaWriter.override(
                extra_schema_module="swagger_marshmallow_codegen.schema.legacy"
            ),
        )
        return factory(accessor)


class Flatten:
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
