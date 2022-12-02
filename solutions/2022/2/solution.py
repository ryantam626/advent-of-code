from aoc_utils.io_utils import read_input

YEAR = 2022
DAY = 2

lines = read_input(YEAR, DAY)


def gen():
    mat = [[3,0,6],[6,3,0],[0,6,3]]
    a = 'ABC'
    b = 'XYZ'
    for line in lines:
        left, right = map(str.strip, line.split())
        yield mat[b.index(right)][a.index(left)] + b.index(right) + 1


print(sum(gen()))


def gen2():
    mat = [[3,1,2],[1,2,3],[2,3,1]]
    a = 'ABC'
    b = 'XYZ'
    for line in lines:
        left, right = map(str.strip, line.split())
        yield mat[b.index(right)][a.index(left)] + (b.index(right) * 3)

print(sum(gen2()))
