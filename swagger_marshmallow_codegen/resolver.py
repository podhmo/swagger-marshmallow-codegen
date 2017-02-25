# -*- coding:utf-8 -*-
import logging
import sys
from collections import OrderedDict
import dictknife
from .langhelpers import titleize, normalize
from .dispatcher import Pair
from . import validate
logger = logging.getLogger(__name__)


class Resolver(object):
    def __init__(self, dispatcher):
        self.dispatcher = dispatcher
        self.accessor = dictknife.Accessor()  # todo: rename

    def has_ref(self, d):
        return "$ref" in d

    def has_allof(self, d):
        return "allOf" in d

    def has_schema(self, fulldata, d, cand=("object",), fullscan=True):
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
        _, definition = self.resolve_ref_definition(fulldata, d)
        return self.has_schema(fulldata, definition, fullscan=False)

    def has_nested(self, fulldata, d):
        if self.has_schema(fulldata, d, fullscan=False):
            return True
        return self.has_many(d) and self.has_schema(fulldata, d["items"])

    def has_many(self, d):
        return d.get("type") == "array" or "items" in d

    def resolve_normalized_name(self, name):
        return normalize(name)

    def resolve_schema_name(self, name):
        return titleize(name)

    def resolve_type_and_format(self, name, field):
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

    def resolve_caller_name(self, c, field_name, field):
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

    def resolve_allof_definition(self, fulldata, d):
        ref_list = []
        r = OrderedDict()
        for subdef in d["allOf"]:
            if self.has_ref(subdef):
                ref_list.append(self.resolve_ref_definition(fulldata, subdef))
            else:
                r = dictknife.deepmerge(r, subdef)
        return ref_list, r

    def resolve_ref_definition(self, fulldata, d, name=None, i=0, level=-1):
        # return schema_name, definition_dict
        # todo: support quoted "/"
        # on array
        if "items" in d:
            definition = d
            name, _ = self.resolve_ref_definition(fulldata, d["items"], name=name, i=i, level=level + 1)  # xxx
            return name, definition

        if "$ref" not in d:
            return self.resolve_schema_name(name), d
        if level == 0:
            return self.resolve_schema_name(name), d

        logger.debug("    resolve: %sref=%r", "  " * i, d["$ref"])

        path = d["$ref"][len("#/"):].split("/")
        name = path[-1]

        parent = self.accessor.maybe_access_container(fulldata, path)
        if parent is None:
            sys.stderr.write("\t{!r} is not found\n".format(d["$ref"]))
            return self.resolve_schema_name(name), d
        return self.resolve_ref_definition(fulldata, parent[name], name=name, i=i + 1, level=level - 1)

    def resolve_validators_on_property(self, c, field):
        validators = []

        def add(validator):
            logger.debug("    resolve: validator=%s", validator.__class__.__name__)
            return validators.append(self.dispatcher.handle_validator(c, validator))

        # range
        if "minimum" in field or "maximum" in field:
            range_opts = {
                "min": field.get("minimum"),
                "exclusive_min": field.get("exclusiveMinimum", False),
                "max": field.get("maximum"),
                "exclusive_max": field.get("exclusiveMaximum", False),
            }
            add(validate.Range(**range_opts))
        if "minLength" in field or "maxLength" in field:
            length_opts = {
                "min": field.get("minLength"),
                "max": field.get("maxLength")
            }
            add(validate.Length(**length_opts))
        if "pattern" in field:
            regex_opts = {
                "regex": field["pattern"]
            }
            add(validate.Regexp(**regex_opts))
        if "enum" in field:
            enum_opts = {
                "choices": field["enum"]
            }
            add(validate.OneOf(**enum_opts))
        if "multipleOf" in field:
            multipleof_opts = {
                "n": field["multipleOf"]
            }
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
