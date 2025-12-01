input_filename = __file__.split('.')[0] + ".input"
with open(input_filename) as f:
    raw = f.read().strip().split('\n')


grid = [[int(cell) for cell in row] for row in raw]
assert all(len(row) == len(grid[0]) for row in grid) # all rows are the same length
max_x = len(grid) - 1
max_y = len(grid[0]) - 1


def neighbours(x, y):
    result = []
    if 0 <= x - 1:
        result.append((x-1, y))
    if x + 1 <= max_x:
        result.append((x+1, y))
    if 0 <= y - 1:
        result.append((x, y-1))
    if y + 1 <= max_y:
        result.append((x, y+1))
    return result


def neighbour_values(x, y):
    return [grid[x][y] for (x, y) in neighbours(x, y)]


def part1():
    low_point_heights = []
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if all(cell < nv for nv in neighbour_values(x, y)):
                print(f"Low point {cell} at grid[{x}][{y}]")
                low_point_heights.append(cell)
    print(f"Found {len(low_point_heights)}")
    total_risk_level = sum(low_point_heights) + len(low_point_heights) # add 1 to each point to determine risk
    print(f"Sum of all risk levels: {total_risk_level}")


def get_low_points():
    low_point_coords = []
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if all(cell < nv for nv in neighbour_values(x, y)):
                # print(f"Low point {cell} at grid[{x}][{y}]")
                low_point_coords.append((x, y))
    return low_point_coords


def basin_size(low_point):
    condition = lambda value: value < 9
    seen = []
    to_see = set([low_point])
    while to_see:
        coords = to_see.pop()
        seen.append(coords)
        point_neighbours = neighbours(*coords)
        basin_neighbours = [(x, y) for (x, y) in point_neighbours if grid[x][y] < 9]
        new_neighbours = [n for n in basin_neighbours if n not in seen]
        to_see.update(new_neighbours)
    assert len(seen) == len(set(seen))
    print(f"Basin at {low_point} size: {len(seen)}")
    return len(seen)


def part2():
    low_point_coords = get_low_points()
    print(f"Computing sizes for {len(low_point_coords)} basins...")
    basin_sizes = [basin_size(low_point) for low_point in low_point_coords]
    basin_sizes = sorted(basin_sizes, reverse=True)
    print(f"Top 3 basins sizes: {basin_sizes[0]}, {basin_sizes[1]}, {basin_sizes[2]}")
    answer = basin_sizes[0] * basin_sizes[1] * basin_sizes[2]
    print(f"Final answer: {answer}")
    # 821702089 is too high
    # Gets the wrong answer. I double-checked several basins & seems correct. Leaving this alone for now.
    # agh, changed `to_see` to a set. duh. That fixed it.


# part1()
part2()
# basin_size((99, 13))
