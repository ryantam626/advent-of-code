from pathlib import Path
from typing import List


def read_input(year: int, day: int) -> List[str]:
    base_dir = Path(__file__).parent.parent.resolve()
    input_path = base_dir / "local" / "input" / str(year)/ str(day)

    with input_path.open('r') as fd:
        return fd.readlines()

