from __future__ import annotations
import typing as t
import logging
from .v2 import Context  # noqa:F401
from .v2 import SchemaWriter  # noqa:F401
from .options import CodegenTargetDict

if t.TYPE_CHECKING:
    from swagger_marshmallow_codegen.accessor import Accessor

logger = logging.getLogger(__name__)


class Codegen:
    version_path: str = "version"

    def __init__(
        self,
        accessor: Accessor,
        *,
        schema_class_path: t.Optional[str] = None,
        schema_writer_factory: t.Optional[t.Any] = None,  # todo: type
    ):
        self.accessor = accessor
        self.schema_class_path = schema_class_path
        self.schema_writer_factory = schema_writer_factory

    def codegen(self, d, targets: CodegenTargetDict):
        cls = self.guess_class(d, path="version")
        codegen = cls(
            self.accessor,
            schema_class_path=self.schema_class_path,
            schema_writer_factory=self.schema_writer_factory,
        )
        return codegen.codegen(d, targets=targets)

    def guess_class(self, d: t.Dict, *, path: str = "version") -> t.Type[t.Any]:
        version = d.get(path)
        if version is None:
            from .v2 import Codegen

            logger.info("version is not found, guessing... v2")

            return Codegen

        if version.strip()[0] == "2":
            from .v2 import Codegen

            logger.info("openapi version is v2")
            return Codegen
        elif version.strip()[0] == "3":
            from .v2 import Codegen

            logger.info("openapi version is v3")
            raise Exception("oops")
            return Codegen
        else:
            raise RuntimeError(f"unexpected openapi version {version}")
