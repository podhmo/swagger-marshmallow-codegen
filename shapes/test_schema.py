from magicalimport import import_module


def test_00():
    m = import_module("./expected/00simple-object.py", cwd=False)
    s = m.Person()
    data = {"name": "foo", "age": 20}
    s.load(data)


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
