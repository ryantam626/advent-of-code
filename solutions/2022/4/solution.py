import string
from functools import reduce

import more_itertools

from aoc_utils.io_utils import read_input

YEAR = 2022
DAY = 4

lines = read_input(YEAR, DAY)
# lines = """2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8""".splitlines()


def cmp(l, r):
    return (l[0] <= r[0]) and (r[1] <= l[1])


def gen():
    for line in lines:
        left, right = line.split(',')
        left = tuple(map(int, left.split('-')))
        right = tuple(map(int, right.split('-')))
        res = cmp(left, right) or cmp(right, left)
        yield res

print(sum(gen()))


def cmp2(l, r):
    return (r[0] <= l[1])


def gen2():
    for line in lines:
        left, right = line.split(',')
        left = tuple(map(int, left.split('-')))
        right = tuple(map(int, right.split('-')))
        left, right = sorted([left, right])
        res = cmp2(left, right)
        print(left, right ,res)
        yield res

print(sum(gen2()))

