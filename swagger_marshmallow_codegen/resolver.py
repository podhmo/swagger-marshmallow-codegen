from __future__ import annotations
import typing as t
import logging
from collections import OrderedDict
import dictknife
from .constants import X_MARSHMALLOW_INLINE
from .langhelpers import titleize, normalize
from .dispatcher import Pair
from . import validate

if t.TYPE_CHECKING:
    from .dispatcher import FormatDispatcher
    from .codegen.context import Context

logger = logging.getLogger(__name__)


class Resolver:
    def __init__(self, dispatcher: FormatDispatcher) -> None:
        self.dispatcher = dispatcher
        self.accessor = dictknife.Accessor()  # todo: rename

    def has_ref(self, d) -> bool:
        return "$ref" in d

    def has_allof(self, d) -> bool:
        return "allOf" in d

    def has_schema(self, fulldata, d, cand=("object",), fullscan=True) -> bool:
        typ = d.get("type", None)
        if typ in cand:
            return True
        if "properties" in d:
            return True
        if self.has_allof(d):
            return True
        if not self.has_ref(d):
            return False
        if not fullscan:
            return False
        _, definition = self.resolve_ref_definition(None, fulldata, d)
        return self.has_schema(fulldata, definition, fullscan=False)

    def has_nested(self, fulldata, d) -> bool:
        if self.has_schema(fulldata, d, fullscan=False):
            return True
        return self.has_many(d) and self.has_schema(fulldata, d["items"])

    def has_many(self, d) -> bool:
        return d.get("type") == "array" or "items" in d

    def resolve_normalized_name(self, name: str) -> str:
        return normalize(name)

    def resolve_schema_name(self, name: str) -> str:
        return titleize(name)

    def resolve_type_and_format(self, name: str, field: t.Dict[str, t.Any]) -> Pair:
        try:
            typ = field["type"]
            if isinstance(typ, (list, tuple)):
                for typ in typ:
                    if typ is None:
                        continue
                    break
            format = field.get("format")
            return Pair(type=typ, format=format)
        except KeyError as e:
            logger.debug("%s is not found. name=%s", e.args[0], name)
            if "enum" in field:
                return Pair(type="string", format=None)
            if not field:
                return Pair(type="any", format=None)
            return Pair(type="object", format=None)

    def resolve_caller_name(
        self, c: Context, field_name: str, field: t.Dict[str, t.Any]
    ) -> t.Optional[str]:
        if "additionalProperties" in field and "properties" not in field:
            path = "marshmallow.fields:Dict"
        else:
            pair = self.resolve_type_and_format(field_name, field)
            logger.debug("    resolve: type=%s, format=%s", pair.type, pair.format)
            path = self.dispatcher.dispatch(pair, field)
            if path is None:
                return None

        module, cls_name = path.rsplit(":", 1)
        if module == "marshmallow.fields":
            caller_name = "{}.{}".format("fields", cls_name)  # xxx:
        else:
            c.from_(module, cls_name)  # xxx
            caller_name = cls_name
        logger.debug("    resolve: field=%s", caller_name)
        return caller_name

    def resolve_allof_definition(
        self, c: Context, fulldata: t.Dict[str, t.Any], d: t.Dict[str, t.Any]
    ) -> t.Tuple[t.List[t.Dict[str, t.Any]], t.Dict[str, t.Any]]:
        ref_list = []
        r = OrderedDict()
        for subdef in d["allOf"]:
            if self.has_ref(subdef):
                ref_list.append(self.resolve_ref_definition(c, fulldata, subdef))
            else:
                r = dictknife.deepmerge(r, subdef)
        return ref_list, r

    def resolve_ref_definition(
        self,
        c: t.Optional[Context],  # xxx
        fulldata: t.Dict[str, t.Any],
        d: t.Dict[str, t.Any],
        name: t.Optional[str] = None,
        i: int = 0,
        level: int = -1,
    ) -> t.Tuple[str, t.Dict[str, t.Any]]:
        # return schema_name, definition_dict
        # todo: support quoted "/"
        # on array
        if "items" in d:
            definition = d
            name, _ = self.resolve_ref_definition(
                c, fulldata, d["items"], name=name, i=i, level=level + 1
            )  # xxx
            return name, definition

        if "$ref" not in d:
            return self.resolve_schema_name(name), d
        if level == 0:
            return self.resolve_schema_name(name), d

        logger.debug("    resolve: %sref=%r", "  " * i, d["$ref"])

        path = d["$ref"][len("#/") :].split("/")
        name = path[-1]

        parent = self.accessor.maybe_access_container(fulldata, path)
        if parent is None:
            logger.warning("%r is not found", d["$ref"])
            return self.resolve_schema_name(name), d
        ref_name, definition = self.resolve_ref_definition(
            c, fulldata, parent[name], name=name, i=i + 1, level=level - 1
        )

        # import for separated output
        if X_MARSHMALLOW_INLINE not in definition:
            if c is not None and (
                "properties" in definition
                or (
                    (
                        "additionalProperties" in definition
                        or "items" in definition
                        or "allOf" in definition
                    )
                    and self.has_schema(fulldata, definition)
                )
            ):
                c.relative_import_from_lazy(ref_name)
        return ref_name, definition

    def resolve_validators_on_property(
        self, c: Context, field: t.Dict[str, t.Any]
    ) -> t.List[t.Any]:
        validators = []

        def add(validator):
            logger.debug("    resolve: validator=%s", validator.__class__.__name__)
            return validators.append(self.dispatcher.handle_validator(c, validator))

        # range
        if "minimum" in field or "maximum" in field:
            range_opts = {
                "min": field.get("minimum"),
                "min_inclusive": not field.get("exclusiveMinimum", False),
                "max": field.get("maximum"),
                "max_inclusive": not field.get("exclusiveMaximum", False),
            }
            add(validate.Range(**range_opts))
        if "minLength" in field or "maxLength" in field:
            length_opts = {"min": field.get("minLength"), "max": field.get("maxLength")}
            add(validate.Length(**length_opts))
        if "pattern" in field:
            regex_opts = {"regex": field["pattern"]}
            add(validate.Regexp(**regex_opts))
        if "enum" in field:
            enum_opts = {"choices": field["enum"]}
            add(validate.OneOf(**enum_opts))
        if "multipleOf" in field:
            multipleof_opts = {"n": field["multipleOf"]}
            add(validate.MultipleOf(**multipleof_opts))
        if "maxItems" in field or "minItems" in field:
            itemrange_opts = {
                "max": field.get("maxItems"),
                "min": field.get("minItems"),
            }
            add(validate.ItemsRange(**itemrange_opts))
        if field.get("uniqueItems", False):
            add(validate.Unique())
        return validators
