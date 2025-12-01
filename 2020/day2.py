import re

DAY_2_PUZZLE_REX = re.compile("([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)")


with open("/tmp/day2.input") as f:
    li = f.read().split('\n')

validity = []

for x in filter(None, li):
    p1, p2, l, p = re.search(DAY_2_PUZZLE_REX, x).groups()
    c1 = p[int(p1) - 1]
    c2 = p[int(p2) - 1]
    valid = (c1 == l or c2 == l) and c1 != c2
    validity.append(valid)


sum(1 for x in validity if x)
