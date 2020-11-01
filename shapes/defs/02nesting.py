from __future__ import annotations
import typing as t


class Person:
    name: str
    age: t.Optional[int]
    memo: Memo


class Memo:
    title: str
    content: str
