import sys
from schema import IdsIdOutput, IdsOutput


if __name__ == "__main__":
    try:
        d = "1"
        data = IdsIdOutput.Get200().load(d)
        print("ok", data)
    except Exception as e:
        print("ng", e)
        sys.exit(-1)

    try:
        d = ["1", "2", "3"]
        data = IdsOutput.Get200().load(d)
        print("ok", data)
    except Exception as e:
        print("ng", e)
        sys.exit(-1)
