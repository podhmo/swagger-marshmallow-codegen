from .v2 import Context  # noqa:F401
from .v2 import SchemaWriter  # noqa:F401
from .options import CodegenTargetDict


class Codegen:
    def __init__(self, accessor, *, schema_class_path=None, schema_writer_factory=None):
        self.accessor = accessor
        self.schema_class_path = schema_class_path
        self.schema_writer_factory = schema_writer_factory

    def codegen(self, d, targets: CodegenTargetDict):
        from .v2 import Codegen

        codegen = Codegen(
            self.accessor,
            schema_class_path=self.schema_class_path,
            schema_writer_factory=self.schema_writer_factory,
        )
        return codegen.codegen(d, targets=targets)
