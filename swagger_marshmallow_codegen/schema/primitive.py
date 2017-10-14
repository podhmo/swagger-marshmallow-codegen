from marshmallow import UnmarshalResult, MarshalResult


class PrimitiveValueSchema:
    schema_class = None
    key = "value"
    missing = None

    def __init__(self, *args, **kwargs):
        self.schema = self.__class__.schema_class(*args, **kwargs)

    def load(self, value):  # don't support many
        data = {self.key: value}
        r, errors = self.schema.load(data)
        return UnmarshalResult(
            data=r.get(self.key) or self.missing,
            errors=errors.get(self.key) or errors,
        )

    def dump(self, value):  # don't support many
        data = {self.key: value}
        r, errors = self.schema.dump(data, update_fields=False)
        return MarshalResult(
            data=r.get(self.key) or self.missing,
            errors=errors.get(self.key) or errors,
        )
