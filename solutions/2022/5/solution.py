import string
from functools import reduce

import more_itertools

from aoc_utils.io_utils import read_input

YEAR = 2022
DAY = 5

blob = read_input(YEAR, DAY, lines=False)
# blob = """    [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3
#
# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2
# """


def solution():
    v_stacks_with_number, instructions = blob.split("\n\n")
    v_stacks = v_stacks_with_number.split("\n")[:-1]
    n_stacks = int(v_stacks_with_number.strip()[-1])
    stacks = [[] for _ in range(n_stacks)]

    for v_stack in v_stacks:
        items = [v_stack[pos] for pos in range(1, len(v_stack), 4)]
        for ind, item in enumerate(items):
            if item != " ":
                stacks[ind].insert(0, item)

    for instruction in filter(None, instructions.split("\n")):
        repeats = int(instruction.split("move ")[1].split(" from")[0])
        from_, to = map(
            lambda x: int(x) - 1, instruction.split("from ")[1].split(" to ")
        )
        for _ in range(repeats):
            stacks[to].append(stacks[from_].pop())

    print("".join([s[-1] for s in stacks]))


solution()


def solution2():
    v_stacks_with_number, instructions = blob.split("\n\n")
    v_stacks = v_stacks_with_number.split("\n")[:-1]
    n_stacks = int(v_stacks_with_number.strip()[-1])
    stacks = [[] for _ in range(n_stacks)]

    for v_stack in v_stacks:
        items = [v_stack[pos] for pos in range(1, len(v_stack), 4)]
        for ind, item in enumerate(items):
            if item != " ":
                stacks[ind].insert(0, item)

    for instruction in filter(None, instructions.split("\n")):
        repeats = int(instruction.split("move ")[1].split(" from")[0])
        from_, to = map(
            lambda x: int(x) - 1, instruction.split("from ")[1].split(" to ")
        )
        tmp = []
        for _ in range(repeats):
            tmp.insert(0, stacks[from_].pop())
        stacks[to].extend(tmp)

    print("".join([s[-1] for s in stacks]))


solution2()
