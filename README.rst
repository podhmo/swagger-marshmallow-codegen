swagger-marshmallow-codegen
========================================

concepts
----------------------------------------

- Code generation is better than meta programming
- Don't touch me(generated code) if you can

todo: write down detail.

examples
----------------------------------------

.. code-block:: bash

   $ swagger-marshmallow-codegen definition.yaml > definition.py

definition.yaml

.. code-block:: yaml

  # todo: gentle example
  definitions:
    default:
      properties:
        string:
          type: string
          default: "default"
        integer:
          type: integer
          default: 10
        boolean:
          type: boolean
          default: true
        date:
          type: string
          format: date
          default: 2000-01-01
        datetime:
          type: string
          format: date-time
          default: 2000-01-01T01:01:01Z
        object:
          type: object
          properties:
            name:
              type: string
              default: foo
            age:
              type: integer
              default: 20
          default:
            name: foo
            age: 20
        array:
          type: array
          items:
            type: integer
          default:
            - 1
            - 2
            - 3

    length-validation:
      type: object
      properties:
        s0:
          type: string
        s1:
          type: string
          maxLength: 10
        s2:
          type: string
          minLength: 5
        s3:
          type: string
          maxLength: 10
          minLength: 5

    maximum-validation:
      type: object
      properties:
        n0:
          type: number
          maximum: 100
        n1:
          type: number
          maximum: 100
          exclusiveMaximum: true
        n2:
          type: number
          maximum: 100
          exclusiveMaximum: false
        m0:
          type: number
          minimum: 100
        m1:
          type: number
          minimum: 100
          exclusiveMinimum: true
        m2:
          type: number
          minimum: 100
          exclusiveMinimum: false

    regex-validation:
      type: object
      properties:
        team:
          type: string
          pattern: team[1-9][0-9]+
        team2:
          type: string
          pattern: team[1-9][0-9]+
          maxLength: 10

    array-validation:
      type: object
      properties:
        nums:
          type: array
          items:
            type: integer
          maxItems: 10
          minItems: 1
          uniqueItems: true

    color:
      type: string
      enum:
        - R
        - G
        - B
    yen:
      type: integer
      enum:
        - 1
        - 5
        - 10
        - 50
        - 100
        - 500
        - 1000
        - 5000
        - 10000
    huge-yen:
      type: integer
      multipleOf: 10000
    enum-validation:
      type: object
      required:
        - name
        - color
      properties:
        name:
          type: string
        money:
          $ref: "#/definitions/yen"
        deposit:
          $ref: "#/definitions/huge-yen"
        color:
          $ref: "#/definitions/color"

definition.py

.. code-block:: python

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
      string = fields.String(default='default')
      integer = fields.Integer(default=10)
      boolean = fields.Boolean(default=True)
      date = fields.Date(default=datetime.date(2000, 1, 1))
      datetime = fields.DateTime(default=datetime.datetime(2000, 1, 1, 1, 1, 1))
      object = fields.Nested('DefaultObject', default=OrderedDict([('name', 'foo'), ('age', 20)]))
      array = fields.Integer(many=True, default=[1, 2, 3])


  class DefaultObject(Schema):
      name = fields.String(default='foo')
      age = fields.Integer(default=20)


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
