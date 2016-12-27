from marshmallow import validate as v
from marshmallow.validate import (  # NOQA
    Length,
    Regexp,
    OneOf,
)


class Range(v.Range):
    def __init__(self, min=None, max=None, error=None, exclusive_max=False, exclusive_min=False):
        super().__init__(min=min, max=max, error=error)
        self.exclusive_max = exclusive_max
        self.exclusive_min = exclusive_min

    def _repr_args(self):
        return 'min={0!r}, max={1!r}, exclusive_min={2!r}, exclusive_max={3!r}'.format(self.min, self.max, self.exclusive_min, self.exclusive_max)

    def __call__(self, value):
        if self.min is not None:
            if self.exclusive_min:
                over = value <= self.min
            else:
                over = value < self.min
            if over:
                message = self.message_min if self.max is None else self.message_all
                raise v.ValidationError(self._format_error(value, message))

        if self.max is not None:
            if self.exclusive_max:
                over = value >= self.max
            else:
                over = value > self.max
            if over:
                message = self.message_max if self.min is None else self.message_all
                raise v.ValidationError(self._format_error(value, message))

        return value


class MultipleOf(v.Validator):
    message = '{input} is Not divisible by {n}'

    def __init__(self, n=1, error=None):
        self.n = n
        self.error = error

    def _repr_args(self):
        return 'n={0!r}'.format(self.n)

    def _format_error(self, value):
        return self.message.format(input=value, n=self.n)

    def __call__(self, value):
        if value % self.n != 0:
            raise v.ValidationError(self._format_error(value))
        return value


class ItemsRange(v.Range):
    """for maxItems and minItems"""

    message_min = 'Must be at least {min} items.'
    message_max = 'Must be at most {max} items.'
    message_all = 'Must be between {min} and {max} items.'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __call__(self, value):
        if self.min is not None and len(value) < self.min:
            message = self.message_min if self.max is None else self.message_all
            raise v.ValidationError(self._format_error(value, message))

        if self.max is not None and len(value) > self.max:
            message = self.message_max if self.min is None else self.message_all
            raise v.ValidationError(self._format_error(value, message))
        return value


class Unique(v.Validator):
    message = '{input} is Not unique'

    def __init__(self, error=None):
        self.error = error

    def _repr_args(self):
        return ''

    def _format_error(self, value):
        return self.message.format(input=value)

    def __call__(self, value):
        if len(value) != len(set(value)):
            raise v.ValidationError(self._format_error(value))
        return value
