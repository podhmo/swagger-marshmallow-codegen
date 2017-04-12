from marshmallow import Schema, SchemaOpts, fields
from marshmallow import pre_load, post_load, pre_dump, post_dump
from marshmallow import UnmarshalResult, MarshalResult


class PrimitiveValueSchema(Schema):
    """tempoary primitive value schema"""

    v = None
    default = {}

    @pre_load
    def to_dict(self, v):
        return {"v": v}

    @post_load
    def to_v(self, v):
        return v.get("v")

    @pre_dump
    def to_dict2(self, v):
        return {"v": v}

    @post_dump
    def to_v2(self, v):
        return v.get("v")

    def load(self, data, many=None, partial=None):
        r = super().load(data, many=many, partial=partial)
        if r.errors:
            if self.many if many is None else bool(many):
                # xxx:
                data = [d.get("v") or self.default for d in r.data]
                errors = {k: v["v"] for k, v in r.errors.items()}
            else:
                data = data["v"]
                errors = r.errors["v"]
            return UnmarshalResult(data=data, errors=errors)
        return r

    def dump(self, obj, many=None, update_fields=True, **kwargs):
        r = super().dump(obj, many=many, update_fields=update_fields, **kwargs)
        if r.errors:
            if self.many if many is None else bool(many):
                # xxx:
                data = [d.get("v") or self.default for d in r.data]
                errors = {k: v["v"] for k, v in r.errors.items()}
            else:
                data = data["v"]
                errors = r.errors["v"]
            return MarshalResult(data=data, errors=errors)
        return r


class AdditionalPropertiesOpts(SchemaOpts):
    def __init__(self, meta, **kwargs):
        super().__init__(meta, **kwargs)
        self.additional_field = getattr(meta, "additional_field", fields.Field)


class AdditionalPropertiesSchema(Schema):
    """
    support addtionalProperties

    class MySchema(AdditionalPropertiesSchema):
        class Meta:
            additional
    """

    OPTIONS_CLASS = AdditionalPropertiesOpts

    @pre_load
    @pre_dump
    def wrap_dynamic_additionals(self, data):
        diff = set(data.keys()).difference(self.fields.keys())
        for name in diff:
            f = self.opts.additional_field
            self.fields[name] = f() if callable(f) else f
        return data

    def dumps(self, obj, many=None, update_fields=False, *args, **kwargs):
        return super().dumps(obj, many=many, update_fields=update_fields, *args, **kwargs)

    def dump(self, obj, many=None, update_fields=False, *args, **kwargs):
        return super().dump(obj, many=many, update_fields=update_fields, *args, **kwargs)
