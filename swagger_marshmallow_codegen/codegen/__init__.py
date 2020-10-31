from __future__ import annotations
import typing as t
import logging
from functools import partial
from .context import Context  # noqa:F401
from .v2.codegen import SchemaWriter  # noqa:F401
from .options import CodegenTargetDict

if t.TYPE_CHECKING:
    from swagger_marshmallow_codegen.resolver import Resolver

logger = logging.getLogger(__name__)


class Codegen:
    version_path: str = "version"

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
        d,
        targets: CodegenTargetDict,
        *,
        ctx: t.Optional[Context] = None,
        test: bool = False,
    ):
        cls = self.guess_factory(d, path="version")
        codegen = cls(
            schema_class_path=self.schema_class_path,
            schema_writer_factory=self.schema_writer_factory,
        )
        return codegen.codegen(d, targets=targets, ctx=ctx, test=test)

    def guess_factory(self, d: t.Dict, *, path: str = "version") -> t.Type[t.Any]:
        version = d.get(path)
        if version is None:
            logger.info("version is not found, guessing... v2")
            version = "2.0"

        if version.strip()[0] == "2":
            from .v2.codegen import Codegen
            from .v2.accessor import Accessor

            logger.info("openapi version is v2")
            return partial(Codegen, Accessor(self.resolver))
        elif version.strip()[0] == "3":
            from .v3.codegen import Codegen
            from .v3.accessor import Accessor

            logger.info("openapi version is v3")
            return partial(Codegen, Accessor(self.resolver))
        else:
            raise RuntimeError(f"unexpected openapi version {version}")
