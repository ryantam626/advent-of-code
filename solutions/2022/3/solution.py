import string
from functools import reduce

import more_itertools

from aoc_utils.io_utils import read_input

YEAR = 2022
DAY = 3

lines = read_input(YEAR, DAY)
# lines = """vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw
# """.splitlines()

prio = {s: ind + 1 for ind, s in enumerate(string.ascii_letters)}


def gen():
    for line in lines:
        line = line.strip()
        left, right = more_itertools.chunked(line, len(line) // 2)
        (duplicate,) = list(set(left).intersection(set(right)))
        assert duplicate is not None
        yield prio[duplicate]


sum(gen())


def gen2():
    for line_group in more_itertools.chunked(lines, 3):
        items = [set(line.strip()) for line in line_group]

        badge_set = reduce(
            lambda l, r: l.intersection(r),
            items,
        )

        (badge,) = list(badge_set)
        yield prio[badge]


sum(gen2())
