input_filename = __file__.split('.')[0] + ".input"
with open(input_filename) as f:
    raw = f.read().strip().split('\n')

instructions = raw

h_pos = 0
depth = 0

for instruction in instructions:
    direction, scalar = instruction.split()
    if direction == 'forward':
        h_pos += int(scalar)
    elif direction == 'down':
        depth += int(scalar)
    elif direction == 'up':
        depth -= int(scalar)
    else:
        raise ValueError(f"Cannot handle {direction}")
    if depth < 0:
        raise ValueError("Cannot fly")

print(f"h_pos: {h_pos}")
print(f"depth: {depth}")
print(f"Result: {h_pos * depth}")


# Part 2

h_pos = 0
depth = 0
aim = 0

for instruction in instructions:
    direction, scalar = instruction.split()
    value = int(scalar)
    if direction == 'forward':
        h_pos += value
        depth += (aim * value)
    elif direction == 'down':
        aim += value
    elif direction == 'up':
        aim -= value
    else:
        raise ValueError(f"Cannot handle {direction}")
    if depth < 0:
        raise ValueError("Cannot fly")

print(f"h_pos: {h_pos}")
print(f"depth: {depth}")
print(f"aim: {aim}")
print(f"Result: {h_pos * depth}")
