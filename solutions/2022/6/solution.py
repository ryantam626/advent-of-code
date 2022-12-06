import string
from functools import reduce

import more_itertools

from aoc_utils.io_utils import read_input

YEAR = 2022
DAY = 6

blob = read_input(YEAR, DAY, lines=False)
# blob = "nppdvjthqldpwncqszvftbrmjlhg"
blob = blob.strip()


def solution():
    windows = more_itertools.windowed(blob, 4)
    processed = 4
    for window in windows:
        window = list(filter(None, window))
        if len(set(window)) == 4:
            break
        processed += 1
    print(processed)


solution()


def solution2():
    windows = more_itertools.windowed(blob, 14)
    processed = 14
    for window in windows:
        window = list(filter(None, window))
        if len(set(window)) == 14:
            break
        processed += 1
    print(processed)


solution2()
