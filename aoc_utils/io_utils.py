from pathlib import Path
from typing import List


def read_input(year: int, day: int, lines=True) -> List[str]:
    base_dir = Path(__file__).parent.parent.resolve()
    input_path = base_dir / "local" / "input" / str(year) / str(day)

    with input_path.open("r") as fd:
        if lines:
            return fd.readlines()
        else:
            return fd.read()
