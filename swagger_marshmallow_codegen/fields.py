from marshmallow import fields, validate

# for backward compatibility
Date = fields.Date
DateTime = fields.DateTime
Time = fields.Time


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
        return {
            self.key_field.deserialize(k): self.nested_field.deserialize(v)
            for k, v in value.items()
        }

    def _serialize(self, value, attr, obj):
        return {
            self.key_field._serialize(k, attr, obj): self.nested_field.serialize(
                k, self.get_value(attr, obj)
            )
            for k, v in value.items()
        }
