from __future__ import annotations
import typing as t
import logging
from functools import partial
from .config import ConfigDict
from .context import Context
from .context import OnceContextFactory
from .v2.codegen import SchemaWriter  # noqa:F401

if t.TYPE_CHECKING:
    from swagger_marshmallow_codegen.resolver import Resolver
    from .context import InputData
    from .context import OutputData

logger = logging.getLogger(__name__)


class Codegen:
    version_path: str = "openapi"

    @classmethod
    def override(
        cls,
        *,
        schema_class_path: t.Optional[str] = None,
        schema_writer_factory: t.Callable[[...], SchemaWriter] = None,
    ):
        return partial(
            cls,
            schema_class_path=schema_class_path,
            schema_writer_factory=schema_writer_factory,
        )

    def __init__(
        self,
        resolver: Resolver,
        *,
        schema_class_path: t.Optional[str] = None,
        schema_writer_factory: t.Optional[t.Any] = None,  # todo: type
    ):
        self.resolver = resolver
        self.schema_class_path = schema_class_path
        self.schema_writer_factory = schema_writer_factory

    def codegen(
        self,
        d: InputData,
        config: ConfigDict,
        *,
        ctx: t.Optional[Context] = None,
        test: bool = False,
    ) -> OutputData:
        if test:
            # todo: use dataclasses?
            config["skip_header_comment"] = True

        cls = self.guess_factory(d, config=config, path=self.version_path)
        codegen = cls(
            schema_class_path=self.schema_class_path,
            schema_writer_factory=self.schema_writer_factory,
        )
        context_factory = OnceContextFactory(Context(), setup=codegen.setup_context)
        return codegen.codegen(d, context_factory=context_factory)

    def guess_factory(
        self, d: t.Dict, *, config: ConfigDict, path: str
    ) -> t.Type[t.Any]:
        version = d.get(path)
        if version is None:
            logger.info("version is not found, guessing... v2")
            version = "2.0"

        if version.strip()[0] == "2":
            from .v2.codegen import Codegen
            from .v2.accessor import Accessor

            logger.info("openapi version is v2")
            return partial(Codegen, Accessor(self.resolver, config=config))
        elif version.strip()[0] >= "3":
            from .v3.codegen import Codegen
            from .v3.accessor import Accessor

            logger.info("openapi version is v3")
            return partial(Codegen, Accessor(self.resolver, config=config))
        else:
            raise RuntimeError(f"unexpected openapi version {version}")
