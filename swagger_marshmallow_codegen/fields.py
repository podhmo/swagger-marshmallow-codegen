import datetime
from marshmallow import fields, validate


class Date(fields.Date):
    def _deserialize(self, value, attr, data):
        if isinstance(value, datetime.date):
            return value
        return super()._deserialize(value, attr, data)


class DateTime(fields.Date):
    def _deserialize(self, value, attr, data):
        if isinstance(value, datetime.datetime):
            return value
        return super()._deserialize(value, attr, data)


class Time(fields.Time):
    def _deserialize(self, value, attr, data):
        if isinstance(value, datetime.time):
            return value
        return super()._deserialize(value, attr, data)


class PatternProperties(fields.Field):  # not supported yet
    """
    for jsonschma's patternProperties option.

    .. code-block:: yaml

      scoreData:
        type: object
        patternProperties:
          ".+Score$":
            type: integer
        additionalProperties: false
    """

    def __init__(self, pattern, nested_field, *args, **kwargs):
        fields.Field.__init__(self, *args, **kwargs)
        self.key_field = fields.Str(validate=validate.Regexp(pattern))
        self.nested_field = nested_field

    def _deserialize(self, value):
        return {self.key_field.deserialize(k): self.nested_field.deserialize(v) for k, v in value.items()}

    def _serialize(self, value, attr, obj):
        return {self.key_field._serialize(k, attr, obj): self.nested_field.serialize(k, self.get_value(attr, obj)) for k, v in value.items()}
