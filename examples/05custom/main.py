import sys
from person import Person


if __name__ == "__main__":
    try:
        d = {"name": "foo", "age": "20"}
        data, err = Person(strict=True).load(d)
        print("ok", data)
    except Exception as e:
        print("ng", e)
        sys.exit(-1)
    try:
        d = {"id": '5872c2e1c54d2d58294cbac6', "name": "bar", "age": "10"}
        data, err = Person(strict=True).load(d)
        print("ok", data)
    except Exception as e:
        print("ng", e)
        sys.exit(-1)
