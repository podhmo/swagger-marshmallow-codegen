import pytest
from magicalimport import import_module
from marshmallow import ValidationError


def test_00():
    m = import_module("./expected/00simple-object.py", cwd=False)
    data = {"name": "foo", "age": 20}
    m.Person().load(data)

    with pytest.raises(ValidationError):
        data = {"name": "foo", "age": "foo"}
        m.Person().load(data)

    with pytest.raises(ValidationError):
        data = {"age": 20}
        m.Person().load(data)


def test_01():
    m = import_module("./expected/01simple-primitive.py", cwd=False)
    s = m.MyInt()
    data = 10
    s.load(data)


def test_02():
    m = import_module("./expected/02nesting.py", cwd=False)
    s = m.Person()
    data = {
        "name": "foo",
        "age": 20,
        "memo": {"title": "hello", "content": "this is first greeting"},
    }
    s.load(data)


def test_03():
    m = import_module("./expected/03self-nesting.py", cwd=False)
    s = m.Person()
    data = {
        "name": "foo",
        "age": 20,
        "father": {"name": "bar", "age": 40},
        "mother": {"name": "boo"},
    }
    s.load(data)


def test_04():
    m = import_module("./expected/04inline-nesting.py", cwd=False)
    s = m.Person()
    data = {
        "name": "foo",
        "age": 20,
        "memo": {"title": "hello", "content": "hello world"},
    }
    s.load(data)


def test_05():
    m = import_module(
        "./expected/05additionalProperties-without-properties.py", cwd=False
    )
    s = m.Person()
    data = {
        "name": "foo",
        "age": 20,
        "data": {"title": "hello", "content": "hello world"},
    }
    s.load(data)


def test_06():
    m = import_module("./expected/06additionalProperties.py", cwd=False)
    s = m.Box()
    data = {
        "name": "foo",
        "x": 1,
        "y": 20,
        "z": 300,
    }
    s.load(data)

    with pytest.raises(ValidationError):
        data = {
            "name": "foo",
            "x": "xxx",
        }
        s.load(data)


def test_07():
    m = import_module("./expected/07additionalProperties-with-bool.py", cwd=False)
    data = {
        "name": "foo",
        "xxxx": "xxxx",
    }

    # default
    with pytest.raises(ValidationError):
        m.Person().load(data)

    # true
    m.Person_AdditionalProperties_True().load(data)

    # false
    with pytest.raises(ValidationError):
        m.Person_AdditionalProperties_False().load(data)
