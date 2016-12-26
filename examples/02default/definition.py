# -*- coding:utf-8 -*-
from marshmallow import(
    Schema,
    fields
)
import datetime
from collections import OrderedDict
from marshmallow.validate import(
    Length,
    OneOf,
    Regexp
)
from swagger_marshmallow_codegen import(
    validate
)


class Default(Schema):
    string = fields.String(missing='default')
    integer = fields.Integer(missing=10)
    boolean = fields.Boolean(missing=True)
    date = fields.Date(missing=datetime.date(2000, 1, 1))
    datetime = fields.DateTime(missing=datetime.datetime(2000, 1, 1, 1, 1, 1))
    object = fields.Nested('DefaultObject', missing=OrderedDict([('name', 'foo'), ('age', 20)]))
    array = fields.Integer(many=True, missing=[1, 2, 3])


class DefaultObject(Schema):
    name = fields.String(missing='foo')
    age = fields.Integer(missing=20)


class Length_validation(Schema):
    s0 = fields.String()
    s1 = fields.String(validate=[Length(min=None, max=10, equal=None)])
    s2 = fields.String(validate=[Length(min=5, max=None, equal=None)])
    s3 = fields.String(validate=[Length(min=5, max=10, equal=None)])


class Maximum_validation(Schema):
    n0 = fields.Number(validate=[validate.CustomRange(min=None, max=100, exclusive_min=False, exclusive_max=False)])
    n1 = fields.Number(validate=[validate.CustomRange(min=None, max=100, exclusive_min=False, exclusive_max=True)])
    n2 = fields.Number(validate=[validate.CustomRange(min=None, max=100, exclusive_min=False, exclusive_max=False)])
    m0 = fields.Number(validate=[validate.CustomRange(min=100, max=None, exclusive_min=False, exclusive_max=False)])
    m1 = fields.Number(validate=[validate.CustomRange(min=100, max=None, exclusive_min=True, exclusive_max=False)])
    m2 = fields.Number(validate=[validate.CustomRange(min=100, max=None, exclusive_min=False, exclusive_max=False)])


class Regex_validation(Schema):
    team = fields.String(validate=[Regexp(regex='team[1-9][0-9]+')])
    team2 = fields.String(validate=[Length(min=None, max=10, equal=None), Regexp(regex='team[1-9][0-9]+')])


class Array_validation(Schema):
    nums = fields.Integer(many=True, validate=[validate.ItemsRange(min=1, max=10), validate.Unique()])


class Enum_validation(Schema):
    name = fields.String(required=True)
    money = fields.Integer(validate=[OneOf(choices=[1, 5, 10, 50, 100, 500, 1000, 5000, 10000], labels=[])])
    deposit = fields.Integer(validate=[validate.MultipleOf(n=10000)])
    color = fields.String(required=True, validate=[OneOf(choices=['R', 'G', 'B'], labels=[])])
