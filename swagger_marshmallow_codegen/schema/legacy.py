from collections import namedtuple
import marshmallow

from .extra import make_additional_properties_schema_class


#: Return type of :meth:`Schema.dump` including serialized data and errors
MarshalResult = namedtuple("MarshalResult", ["data", "errors"])
#: Return type of :meth:`Schema.load`, including deserialized data and errors
UnmarshalResult = namedtuple("UnmarshalResult", ["data", "errors"])


class LegacySchema(marshmallow.Schema):
    """legacy version"""

    strict = None

    def __init__(self, strict=None, **kwargs):
        if strict is None:
            strict = self.__class__.strict
        self.strict = strict
        super().__init__(**kwargs)

    def dump(self, obj, many=None):
        if many is None:
            many = self.many
        try:
            d = super().dump(obj, many=many)
            return MarshalResult(data=d, errors=None)
        except marshmallow.ValidationError as e:
            if self.strict:
                raise
            d = [] if many else {}
            return MarshalResult(data=d, errors=e)

    def dumps(self, obj, many=None, *args, **kwargs):
        if many is None:
            many = self.many
        try:
            d = super().dumps(obj, *args, many=many, **kwargs)
            return MarshalResult(data=d, errors=None)
        except marshmallow.ValidationError as e:
            if self.strict:
                raise
            d = [] if many else {}
            d = self.opts.render_module.dumps(d, *args, **kwargs)
            return MarshalResult(data=d, errors=e)

    def load(self, data, many=None, partial=None, unknown=None):
        if many is None:
            many = self.many
        try:
            d = super().load(data, many=many, partial=partial, unknown=unknown)
            return UnmarshalResult(data=d, errors=None)
        except marshmallow.ValidationError as e:
            if self.strict:
                raise
            d = [] if many else {}
            return UnmarshalResult(data=d, errors=e)

    def loads(self, json_data, many=None, partial=None, unknown=None, **kwargs):
        if many is None:
            many = self.many
        data = self.opts.render_module.loads(json_data, **kwargs)
        try:
            d = super().load(data, many=many, partial=partial, unknown=unknown)
            return UnmarshalResult(data=d, errors=None)
        except marshmallow.ValidationError as e:
            if self.strict:
                raise
            d = [] if many else {}
            return UnmarshalResult(data=d, errors=e)


LegacyAdditionalPropertiesSchema = make_additional_properties_schema_class(
    marshmallow.Schema, marshmallow.SchemaOpts
)

Schema = LegacySchema
AdditionalPropertiesSchema = LegacyAdditionalPropertiesSchema
