import sys
from definition import Default


if __name__ == "__main__":
    try:
        d = {}
        data, err = Default(strict=True).load(d)
        print("ok", Default().dump(data).data)
    except Exception as e:
        print("ng", e)
        sys.exit(-1)
