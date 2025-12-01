with open("/tmp/day3.input") as f:
    rows = f.read().strip().split('\n')
    width = len(rows[0])

# start pos already set in row0. Nothing to do
rows = rows[1:]

h_pos = 0
trees_hit = 0  # assume start is not a tree

h_movement = 1

# debugging
# rows = rows[:15]

for v_pos, row in enumerate(rows):
    if v_pos % 2 == 0: continue
    h_pos = (h_pos + h_movement) % width
    if row[h_pos] == '#':
        trees_hit += 1
    # print(row)
    # print((' ' * h_pos) + "^")

print(trees_hit)


# Slopes:
# 1/1: 90
# 3/1: 244
# 5/1: 97
# 7/1: 92
# 1/2: 48