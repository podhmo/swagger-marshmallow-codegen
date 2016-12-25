from marshmallow import validate as v


class Range(v.Range):
    def __init__(self, min=None, max=None, error=None, exclusive_max=False, exclusive_min=False):
        super().__init__(min=min, max=max, error=error)
        self.exclusive_max = exclusive_max
        self.exclusive_min = exclusive_min

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


class RangeWithRepr(Range):
    """for code generation"""
    def __init__(self, *args, c=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.c = c

    def __repr__(self):
        self.c.im.from_("swagger_marshmallow_codegen", "validate")
        msg = "validate.Range(min={self.min}, max={self.max}, exclusive_max={self.exclusive_max}, exclusive_min={self.exclusive_min})"
        return msg.format(self=self)

