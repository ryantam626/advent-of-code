from aoc_utils.io_utils import read_input

YEAR = 2022
DAY = 1

lines = read_input(YEAR, DAY)


def gen():
    carried = 0
    for line in lines:
        stripped = line.strip()
        if stripped == '':
            yield carried
            carried = 0
        else:
            carried += int(stripped)

print(max(gen()))
print(sum(sorted(gen())[-3:]))
