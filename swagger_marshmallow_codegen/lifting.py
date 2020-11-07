from __future__ import annotations
import copy
from dictknife.jsonknife.lifting import Handler
from dictknife.accessing import Accessor
from swagger_marshmallow_codegen.constants import X_MARSHMALLOW_INLINE
from .langhelpers import titleize


class Flattener:
    def __init__(self, replace=True, *, prefix="#/definitions/"):
        self.replace = replace
        self.prefix = prefix

    def extract(self, data, ctx):
        self._extract(data, ctx)
        for k in list(ctx.r.keys()):
            ctx.r[k] = copy.deepcopy(ctx.r[k])
        return ctx.r

    def _extract(self, data, ctx, from_array=False):
        typ = data.get("type")
        if typ == "array" and "items" in data:
            return self.on_array_has_items(data, ctx)
        elif typ is None or typ == "object":
            if from_array or "properties" in data:
                return self.on_object_has_properties(data, ctx)
            elif (
                hasattr(data.get("additionalProperties"), "keys")
                and "properties" in data["additionalProperties"]
            ):
                ctx.add_name("__additionalProperties")
                r = self.on_object_has_properties(data["additionalProperties"], ctx)
                ctx.pop_name()
                data["additionalProperties"] = r
                return data
            else:
                return data
        else:
            return data

    def return_definition(self, definition, fullname, typ="object"):
        if self.replace:
            return {"$ref": self.prefix + fullname}
        else:
            return definition

    def on_object_has_properties(self, data, ctx):
        for name in data.get("properties") or {}:
            ctx.add_name(name)
            data["properties"][name] = self._extract(data["properties"][name], ctx)
            ctx.pop_name()

        if "$ref" in data:
            return data
        fullname = ctx.full_name()

        if ctx.path[0] != fullname:
            data[X_MARSHMALLOW_INLINE] = ctx.path[0]
        ctx.save_object(fullname, data)

        return self.return_definition(data, fullname, typ="object")

    def on_array_has_items(self, data, ctx):
        if "$ref" in data["items"]:
            return data
        fullname = ctx.full_name()
        ctx.add_array_item()
        data["items"] = self._extract(data["items"], ctx, from_array=True)

        if ctx.path[0] != fullname:
            data[X_MARSHMALLOW_INLINE] = ctx.path[0]
        ctx.save_array(fullname, data)

        ctx.pop_name()
        return self.return_definition(data, fullname, typ="array")


class MyHandler(Handler):
    def add_name(self, name):
        self.path.append(titleize(name))


# TODO: separate implementation
# TODO: handling, paths,response,params
def lifting_definition(data, replace=True, *, a=Accessor()):
    if "definitions" in data:
        definitions = data["definitions"]
        w = Flattener(replace=replace, prefix="#/definitions/")
    elif "components" in data:
        definitions = data["components"]
        if "schemas" not in definitions:
            return data
        definitions = definitions["schemas"]
        w = Flattener(replace=replace, prefix="#/components/schemas/")
    else:
        return data

    for name in list(definitions.keys()):
        prop = definitions.pop(name)
        extracted = w.extract(prop, MyHandler([name]))
        extracted[name] = prop
        definitions.update(reversed(list(extracted.items())))
    return data
