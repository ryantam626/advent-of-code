from math import prod

import numpy as np

from aoc_utils.io_utils import read_input

YEAR = 2022
DAY = 8

lines = read_input(YEAR, DAY, lines=True)
# lines = """30373
# 25512
# 65332
# 33549
# 35390""".splitlines(keepends=True)

# P1

arr = np.array(list(map(lambda x: list(map(int, x.strip())), lines)))
viewable = np.zeros_like(arr)

for _ in range(4):
    arr = np.rot90(arr)
    viewable = np.rot90(viewable)

    for y, line in enumerate(arr):
        cur = -1
        for x, val in enumerate(line):
            if val > cur:
                cur = val
                viewable[y, x] = 1

print(viewable.sum().sum())


# P2


def scenic_score(arr, i, j, item):
    if i in (0, arr.shape[0] - 1) or j in (0, arr.shape[1] - 1):
        return 0
    return prod(
        (
            score(arr[i, :j][::-1], item),
            score(arr[i, j + 1 :], item),
            score(arr[:i, j].T[::-1], item),
            score(arr[i + 1 :, j].T, item),
        )
    )


def score(arr, val):
    score = 0
    for item in arr:
        score += 1
        if not item < val:
            break
    return score


print(max(scenic_score(arr, i, j, val) for (i, j), val in np.ndenumerate(arr)))
