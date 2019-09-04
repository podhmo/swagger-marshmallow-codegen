import bson
from marshmallow import Schema, fields


class MySchema(Schema):
    class Meta:
        ordered = True
        strict = True


class ObjectId(fields.String):
    default_error_messages = {
        'invalid_object_id': 'Not a valid bson.ObjectId.',
    }

    def _validated(self, value):
        """Format the value or raise a :exc:`ValidationError` if an error occurs."""
        if value is None:
            return None
        if isinstance(value, bson.ObjectId):
            return value
        try:
            return bson.ObjectId(value)
        except (ValueError, AttributeError):
            self.fail('invalid_object_id')

    def _deserialize(self, value, attr, data, **kwargs):
        return self._validated(value)

    def _serialize(self, value, attr, data, **kwargs):
        if not value:
            return value
        return str(value)
