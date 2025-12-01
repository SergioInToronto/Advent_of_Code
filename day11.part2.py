import math


input_filename = __file__.split('.')[0] + ".input"
with open(input_filename) as f:
    raw = f.read().strip().split('\n')

room_width = len(raw[0])
room_height = len(raw)

# x
# v y-> 0 1 2 3 4
# 0
# 1
# 2
# 3


def _adjacent_seat_is_occupied(model, x, y, delta_x, delta_y):
    x = x + delta_x
    y = y + delta_y
    if x < 0 or y < 0 or x >= room_height or y >= room_width:
        return False
    if model[x][y] == '#':
        return True
    if model[x][y] == 'L':
        return False
    if model[x][y] == '.':
        # continue searching
        return _adjacent_seat_is_occupied(model, x, y, delta_x, delta_y)

    raise ValueError()


def _visible_neighbours_occupied(model, x, y):
    adjacencies = []
    # top left
    adjacencies.append(_adjacent_seat_is_occupied(model, x, y, -1, -1))
    # top
    adjacencies.append(_adjacent_seat_is_occupied(model, x, y, -1, 0))
    # top right
    adjacencies.append(_adjacent_seat_is_occupied(model, x, y, -1, +1))
    # left
    adjacencies.append(_adjacent_seat_is_occupied(model, x, y, 0, -1))
    # right
    adjacencies.append(_adjacent_seat_is_occupied(model, x, y, 0, +1))
    # bottom left
    adjacencies.append(_adjacent_seat_is_occupied(model, x, y, +1, -1))
    # bottom
    adjacencies.append(_adjacent_seat_is_occupied(model, x, y, +1, 0))
    # bottom right
    adjacencies.append(_adjacent_seat_is_occupied(model, x, y, +1, +1))
    return sum(int(x) for x in adjacencies)


def _recalculate_seat(model, x, y):
    adjacencies =  _visible_neighbours_occupied(model, x, y)
    if adjacencies == 0:  # No neighbours -> sit down
        return '#'
    if adjacencies >= 5:  # too many neighbours -> get up
        return 'L'
    return model[x][y]  # Unchanged


current_state = []
for row in raw:
    current_state.append([c for c in row])\

for iteration in range(999999):
    if iteration % 100 == 0:
        print(f"Step {iteration}")

    next_state = []
    for x, row in enumerate(current_state):
        next_row = []
        next_state.append(next_row)
        for y, seat in enumerate(row):
            if seat == '.':
                next_row.append('.')
            else:
                next_row.append(_recalculate_seat(current_state, x, y))

    if current_state == next_state:
        print(f"Steady after {iteration} rounds")
        break

    # print('\n'.join(''.join(c for c in row) for row in current_state))

    current_state = next_state
    next_state = [[['']] * room_width] * room_height

print(sum(row.count('#') for row in current_state))

