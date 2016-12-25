from marshmallow import validate as v


class CustomRange(v.Range):
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


class CustomRangeWithRepr(CustomRange):
    """for code generation"""
    def __init__(self, *args, c=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.c = c

    def __repr__(self):
        self.c.im.from_("swagger_marshmallow_codegen", "validate")
        return "validate.CustomRange({})".format(self._repr_args())


class LengthWithRepr(v.Length):
    def __init__(self, *args, c=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.c = c

    def __repr__(self):
        self.c.im.from_("marshmallow.validate", "Length")
        return "Length({})".format(self._repr_args())


class RegexpWithRepr(v.Regexp):
    def __init__(self, *args, c=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.c = c

    def __repr__(self):
        self.c.im.from_("marshmallow.validate", "Regexp")
        msg = "Regexp(regex={self.regex.pattern!r})"
        return msg.format(self=self)


class OneOfWithRepr(v.OneOf):
    def __init__(self, *args, c=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.c = c

    def __repr__(self):
        self.c.im.from_("marshmallow.validate", "OneOf")
        return "OneOf({})".format(self._repr_args())


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


class MultipleOfWithRepr(MultipleOf):
    """for code generation"""
    def __init__(self, *args, c=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.c = c

    def __repr__(self):
        self.c.im.from_("swagger_marshmallow_codegen", "validate")
        return "validate.MultipleOf({})".format(self._repr_args())
