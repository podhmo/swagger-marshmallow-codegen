from marshmallow import Schema, SchemaOpts, fields
from marshmallow import pre_load, pre_dump


class AdditionalPropertiesOpts(SchemaOpts):
    def __init__(self, meta, **kwargs):
        super().__init__(meta, **kwargs)
        self.additional_field = getattr(meta, "additional_field", fields.Field)


class AdditionalPropertiesSchema(Schema):
    """
    support addtionalProperties

    class MySchema(AdditionalPropertiesSchema):
        class Meta:
            additional_field = fields.Integer()
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
