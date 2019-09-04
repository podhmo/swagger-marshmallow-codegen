from marshmallow import validate as v
from marshmallow.validate import Length, Regexp, OneOf  # NOQA


Range = v.Range


class MultipleOf(v.Validator):
    message = "{input} is Not divisible by {n}"

    def __init__(self, n=1, error=None):
        self.n = n
        self.error = error

    def _repr_args(self):
        return "n={0!r}".format(self.n)

    def _format_error(self, value):
        return self.message.format(input=value, n=self.n)

    def __call__(self, value):
        if value % self.n != 0:
            raise v.ValidationError(self._format_error(value))
        return value


class ItemsRange(v.Range):
    """for maxItems and minItems"""

    message_min = "Must be {min_op} {{min}} items."
    message_max = "Must be {max_op} {{max}} items."
    message_all = "Must be {min_op} {{min}} and {max_op} {{max}} items."

    message_gte = "greater than or equal to"
    message_gt = "greater than"
    message_lte = "less than or equal to"
    message_lt = "less than"


class Unique(v.Validator):
    message = "{input} is Not unique"

    def __init__(self, error=None):
        self.error = error

    def _repr_args(self):
        return ""

    def _format_error(self, value):
        return self.message.format(input=value)

    def __call__(self, value):
        if len(value) != len(set(value)):
            raise v.ValidationError(self._format_error(value))
        return value
