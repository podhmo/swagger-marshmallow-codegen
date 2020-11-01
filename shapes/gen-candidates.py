from handofcats import as_command
import pathlib


@as_command
def run(dirpath: str) -> None:
    import re

    rx = re.compile("^[0-9]+")
    print("CANDIDATES = [")
    for p in pathlib.Path(dirpath).glob("*.py"):
        m = rx.search(p.name)
        if m is None:
            continue
        print(
            f'    ({rx.sub("", p.with_suffix("").name)!r}, {p.with_suffix(".json").name!r}, {p.name!r}),'
        )
    print("]")
