from __future__ import annotations
import logging
import typing as t
from prestring.output import output as create_separated_output
from . import loading
from .resolver import Resolver
from .codegen import Codegen, SchemaWriter
from .dispatcher import FormatDispatcher
from .lifting import lifting_definition
from .langhelpers import normalize

if t.TYPE_CHECKING:
    from .codegen.config import ConfigDict
    from .codegen.context import InputData, OutputData

logger = logging.getLogger(__name__)


class Driver:
    dispatcher_factory = FormatDispatcher
    resolver_factory = Resolver
    codegen_factory = Codegen

    def __init__(self, config: ConfigDict):
        self.config: ConfigDict = config

    def load(self, fp: t.Any) -> InputData:
        # hack:
        # import dictknife.loading._yaml as xxx
        # xxx.make_dict = dict
        return loading.load(fp)

    def dump(self, d: OutputData, *, output: t.Optional[str] = None) -> None:
        if output is None:
            for name, m in d.files:
                print(m)
            return

        with create_separated_output(normalize(output), suffix=".py") as fs:
            seen = set()
            for name, m in d.files:
                seen.add(name)
                with fs.open(name, "w") as wf:
                    print(m, file=wf)

    def transform(self, d: InputData) -> OutputData:
        d = lifting_definition(d)
        return self.create_codegen().codegen(d, config=self.config)

    def run(self, inp, *, output: t.Optional[str] = None):
        data = self.load(inp)
        result = self.transform(data)
        self.dump(result, output=output)

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
    def __init__(self, config: ConfigDict) -> None:
        self.config: ConfigDict = config

    def load(self, fp: t.Any) -> InputData:
        return loading.load(fp)

    def dump(self, result: OutputData, *, output: t.Optional[str] = None) -> None:
        for _, d in result.files:
            return loading.dump(d, output)

    def transform(self, d: InputData) -> OutputData:
        lifted = lifting_definition(d)

        class _Data:
            @property
            def files(self) -> t.Iterator[t.Tuple[str, t.Any]]:
                yield lifted

        return _Data()

    def run(self, inp, *, output: t.Optional[str] = None):
        data = self.load(inp)
        result = self.transform(data)
        self.dump(result, output=output)


class ProfileDriver(Driver):
    def run(self, inp, *, output: t.Optional[str] = None):
        import cProfile
        import pstats

        profile = cProfile.Profile()
        profile.enable()
        data = self.load(inp)
        result = self.transform(data)
        profile.disable()
        s = pstats.Stats(profile)
        s.dump_stats("swagger-marshmallow-codegen.prof")
        self.dump(result, output=output)
