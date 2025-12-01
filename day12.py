input_filename = __file__.split('.')[0] + ".input"
with open(input_filename) as f:
    raw = f.read().strip().split('\n')

EAST = 0
SOUTH = 1
WEST = 2
NORTH = 3


facing = EAST
pos_east = 0
pos_north = 0

for instruction in raw:
    action, value = instruction[0], int(instruction[1:])
    if action == 'N':
        pos_north += value
    elif action == 'S':
        pos_north -= value
    elif action == 'E':
        pos_east += value
    elif action == 'W':
        pos_east -= value
    elif action == 'F':
        if facing == EAST:
            pos_east += value
        elif facing == WEST:
            pos_east -= value
        elif facing == NORTH:
            pos_north += value
        elif facing == SOUTH:
            pos_north -= value
        else:
            raise ValueError
    else:
        value = value / 90
        if action == 'L':
            value = -value
        facing = (facing + value) % 4

    # print(f"{instruction} - ({pos_north}, {pos_east}) facing {facing}")

print(f"Facing {facing} at ({pos_north}, {pos_east})")
print(f"Distance from start: {abs(pos_east) + abs(pos_north)}")
