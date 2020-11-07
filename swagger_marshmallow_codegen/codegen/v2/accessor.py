from __future__ import annotations
import typing as t
import logging

if t.TYPE_CHECKING:
    from swagger_marshmallow_codegen.resolver import Resolver
    from swagger_marshmallow_codegen.dispatcher import FormatDispatcher
    from ..config import ConfigDict
    from ..context import Context
logger = logging.getLogger(__name__)


class Accessor:
    def __init__(self, resolver: Resolver, *, config: ConfigDict) -> None:
        self.resolver = resolver
        self.config = config

    @property
    def dispatcher(self) -> FormatDispatcher:
        return self.resolver.dispatcher

    def paths(self, d: t.Dict[str, t.Any]) -> t.List[t.Dict[str, t.Any]]:
        return (d.get("paths") or {}).items()

    def methods(
        self,
        d: t.Dict[str, t.Any],
        candidates: t.Set[str] = set(
            ("get", "post", "put", "head", "delete", "options", "patch")
        ),
    ) -> t.Iterator[t.Tuple[str, t.Dict[str, t.Any]]]:
        for method, definition in d.items():
            if method in candidates:
                yield method, definition

    def parameters(self, d: t.Dict[str, t.Any]) -> t.List[t.Dict[str, t.Any]]:
        return d.get("parameters") or []

    def responses(
        self, d: t.Dict[str, t.Any]
    ) -> t.Iterator[t.Tuple[str, t.Dict[str, t.Any]]]:
        for name, definition in (d.get("responses") or {}).items():
            name = str(name)
            if not name.startswith("x-"):
                yield name, definition

    def definitions(self, d: t.Dict[str, t.Any]) -> t.Dict[str, t.Any]:
        return (d.get("definitions") or {}).items()

    def properties(self, d: t.Dict[str, t.Any]) -> t.Dict[str, t.Any]:
        return d.get("properties") or {}

    def pattern_properties(self, d: t.Dict[str, t.Any]) -> t.Dict[str, t.Any]:
        return d.get("patternProperties") or {}

    def update_options_pre_properties(
        self, d: t.Dict[str, t.Any], opts: t.Dict[str, t.Any]
    ) -> t.Dict[str, t.Any]:
        for name in d.get("required") or []:
            opts[name]["required"] = True
        return opts

    def update_option_on_property(
        self, c: Context, field: t.Dict[str, t.Any], opts: t.Dict[str, t.Any]
    ) -> t.Dict[str, t.Any]:
        if "description" in field:
            opts["description"] = field["description"]
        if self.resolver.has_many(field):
            logger.debug("    resolve: many=True")
            opts["many"] = True
        if "default" in field and not opts.get("required", False):
            logger.debug("    resolve: default=%r", field["default"])
            opts["missing"] = self.dispatcher.handle_default(
                c, field["default"], field
            )  # xxx
        if field.get("readOnly", False):
            logger.debug("    resolve: dump_only=True")
            opts["dump_only"] = True
        typ = field.get("type")

        if isinstance(typ, (list, tuple)):
            for typ in typ:
                if typ is None:
                    opts["allow_none"] = True
        if field.get("x-nullable") or field.get("nullable"):
            opts["allow_none"] = True

        validators = self.resolver.resolve_validators_on_property(c, field)
        if validators:
            opts["validate"] = validators
        return opts
