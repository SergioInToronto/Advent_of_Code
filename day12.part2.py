input_filename = __file__.split('.')[0] + ".input"
with open(input_filename) as f:
    raw = f.read().strip().split('\n')

ship_pos_north = 0
ship_pos_east = 0
waypoint_pos_north = 1
waypoint_pos_east = 10

for instruction in raw:
    action, value = instruction[0], int(instruction[1:])
    if action == 'N':
        waypoint_pos_north += value
    elif action == 'S':
        waypoint_pos_north -= value
    elif action == 'E':
        waypoint_pos_east += value
    elif action == 'W':
        waypoint_pos_east -= value
    elif action == 'F':
        ship_pos_north += waypoint_pos_north * value
        ship_pos_east += waypoint_pos_east * value
    elif action == 'R':
        for _ in range(int(value/90)):
            temp = waypoint_pos_north
            waypoint_pos_north = -waypoint_pos_east
            waypoint_pos_east = temp
    elif action == 'L':
        for _ in range(int(value/90)):
            temp = waypoint_pos_north
            waypoint_pos_north = waypoint_pos_east
            waypoint_pos_east = -temp
    else:
        raise ValueError

    print(f" {instruction} \t ({ship_pos_north}, {ship_pos_east}) \t ({waypoint_pos_north}, {waypoint_pos_east})")

print(f"at ({ship_pos_north}, {ship_pos_east})")
print(f"Distance from start: {abs(ship_pos_east) + abs(ship_pos_north)}")
