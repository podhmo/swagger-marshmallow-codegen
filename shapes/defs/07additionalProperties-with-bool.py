from __future__ import annotations
import typing as t


class Person:
    name: str
    age: t.Optional[int]


class Person_AdditionalProperties_True:
    name: str
    age: t.Optional[int]

    additionalProperties = True


class Person_AdditionalProperties_False:
    name: str
    age: t.Optional[int]

    additionalProperties = False
