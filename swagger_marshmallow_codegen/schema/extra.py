from marshmallow import Schema, SchemaOpts, fields, ValidationError
from marshmallow import pre_load, pre_dump


class PrimitiveValueSchema:
    schema_class = None
    key = "value"
    missing_value = None

    def __init__(self, *args, **kwargs):
        self.schema = self.__class__.schema_class(*args, **kwargs)

    def _fix_exception(self, exc):  # xxx: side effect
        if hasattr(exc, "data") and self.key in exc.data:
            exc.data = exc.data[self.key]
        if (
            hasattr(exc, "messages")
            and hasattr(exc.messages, "keys")
            and self.key in exc.messages
        ):
            exc.messages = exc.messages[self.key]
            exc.args = tuple([exc.messages, *exc.args[1:]])
        if hasattr(exc, "valid_data") and self.key in exc.valid_data:
            exc.valid_data = exc.valid_data[self.key]
        return exc

    def load(self, value):  # don't support many
        try:
            r = self._do_load(value)
        except ValidationError as e:
            self._fix_exception(e)
            raise e.with_traceback(e.__traceback__)
        return r.get(self.key) or self.missing_value

    def _do_load(self, value):
        data = {self.key: value}
        return self.schema.load(data)

    def dump(self, value):  # don't support many
        try:
            r = self._do_dump(value)
        except ValidationError as e:
            self._fix_exception(e)
            raise e.with_traceback(e.__traceback__)
        return r.get(self.key) or self.missing_value

    def _do_dump(self, value):
        data = {self.key: value}
        return self.schema.dump(data)


class AdditionalPropertiesOpts(SchemaOpts):
    def __init__(self, meta, **kwargs):
        super().__init__(meta, **kwargs)
        self.additional_field = getattr(meta, "additional_field", fields.Field)


def make_additional_properties_schema_class(Schema):
    class AdditionalPropertiesSchema(Schema):
        """
        support addtionalProperties

        class MySchema(AdditionalPropertiesSchema):
            class Meta:
                additional_field = fields.Integer()
        """

        OPTIONS_CLASS = AdditionalPropertiesOpts

        @pre_load
        def wrap_load_dynamic_additionals(self, data, *, many=False, partial=False):
            diff = set(data.keys()).difference(self.load_fields.keys())
            for name in diff:
                f = self.opts.additional_field
                self.load_fields[name] = f() if callable(f) else f
            return data

        @pre_dump
        def wrap_dump_dynamic_additionals(self, data, *, many=False, partial=False):
            diff = set(data.keys()).difference(self.dump_fields.keys())
            for name in diff:
                f = self.opts.additional_field
                self.dump_fields[name] = f() if callable(f) else f
            return data

    return AdditionalPropertiesSchema


AdditionalPropertiesSchema = make_additional_properties_schema_class(Schema)
