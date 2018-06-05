import sys
from definition import Default


if __name__ == "__main__":
    try:
        d = {}
        data = Default().load(d)
        print("ok", data)
    except Exception as e:
        print("ng", e)
        sys.exit(-1)
