import os.path
from pathlib import Path

import click
import requests


@click.command
@click.option("--year", default=2022)
@click.option("--day", required=True)
def main(year: int, day: int):
    base_dir = Path(__file__).parent.resolve()
    input_path = base_dir / "local" / "input" / str(year)/ str(day)
    input_path.parent.mkdir(parents=True, exist_ok=True)
    with open(input_path, 'w') as fd:
        response = requests.get(
            f"https://adventofcode.com/{year}/day/{day}/input",
            cookies={
                "session": os.getenv("AOC_COOKIE")
            }
        )
        fd.write(response.text)


if __name__ == "__main__":
    main()
