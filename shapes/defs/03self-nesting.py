from __future__ import annotations
import typing as t


class Person:
    name: str
    age: t.Optional[int]
    father: t.Optional[Person]
    mother: t.Optional[Person]
