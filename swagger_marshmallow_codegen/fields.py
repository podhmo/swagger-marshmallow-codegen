from marshmallow import fields
import datetime


class Date(fields.Date):
    def _deserialize(self, value, attr, data):
        if isinstance(value, datetime.date):
            return value
        return super(value, attr, data)


class DateTime(fields.Date):
    def _deserialize(self, value, attr, data):
        if isinstance(value, datetime.datetime):
            return value
        return super(value, attr, data)


class Time(fields.Time):
    def _deserialize(self, value, attr, data):
        if isinstance(value, datetime.time):
            return value
        return super(value, attr, data)
