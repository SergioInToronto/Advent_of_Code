input_filename = __file__.split('.')[0] + ".input"
with open(input_filename) as f:
    raw = f.read().strip().split('\n')

rows = [x for x in raw]


def generate_lines():
    for row in rows:
        start, end = row.split(' -> ')
        yield (
            tuple(int(x) for x in start.split(',')),
            tuple(int(x) for x in end.split(','))
        )

def empty_grid(rows, columns):
    return [
        [0] * columns for _ in range(rows)
    ]


def line_shares_x_or_y(start, end):
    return (start[0] == end[0]) or (start[1] == end[1])


def non_shared_axis_index(start, end):
    if start[0] == end[0]:
        return 1
    if start[1] == end[1]:
        return 0
    return None


def other_axis(axis):
    # Should have used collections.Counter in hindsight
    if axis == 0:
        return 1
    return 0


def mark_row(grid, x, start_y, end_y):
    step = 1 if end_y > start_y else -1
    for i in range(start_y, end_y + step, step):
        # print(f"Marking ({x}, {i})")
        # grid[x][i] += 1
        grid[(x, i)] += 1


def mark_column(grid, y, start_x, end_x):
    step = 1 if end_x > start_x else -1
    for i in range(start_x, end_x + step, step):
        # print(f"Marking ({i}, {y})")
        # grid[i][y] += 1
        grid[(i, y)] += 1


def mark_line(grid, start, end):
    # import pdb; pdb.set_trace()
    moving_axis = non_shared_axis_index(start, end)
    if moving_axis == 0:
        assert start[1] == end[1]
        print(f"Marking column of length {abs(start[0] - end[0])}")
        return mark_column(grid, start[1], start[0], end[0])
    if moving_axis == 1:
        assert start[0] == end[0]
        print(f"Marking row of length {abs(start[1] - end[1])}")
        return mark_row(grid, start[0], start[1], end[1])
    # raise ValueError
    print(f"Marking diagonal ({start} -> {end})")
    mark_diagonal(grid, start, end)


def count_dangerous_points(grid, safe_threshold=1):
    # tally = 0
    # for column in grid:
    #     for cell in column:
    #         if cell > safe_threshold:
    #             tally += 1
    # return tally
    return sum(1 if count > safe_threshold else 0 for count in grid.values())


def part1():
    lines = [x for x in generate_lines()]
    max_x = max(max([start[0], end[0]]) for start, end in lines)
    max_y = max(max([start[1], end[1]]) for start, end in lines)

    print(f"Grid Dimensions: {max_x} x {max_y}")

    # grid = empty_grid(max_x + 1, max_y + 1)
    from collections import Counter
    grid = Counter()

    # skipped = 0
    for line in lines:
        start, end = line
        # if not line_shares_x_or_y(start, end):
        #     # print(f"Skipping ({start} -> {end})")
        #     skipped += 1
        #     continue
        mark_line(grid, start, end)

    # print(grid)
    from collections import Counter
    counter = Counter()
    for row in grid:
        for cell in row:
            counter[cell] += 1
    print(counter)
    # print(f"Skipped: {skipped}")
    # danger_points = count_dangerous_points(grid)
    # print(f"Safe points: {danger_points}")
    # not 974977
    # not 975968
    dangerous_points = count_dangerous_points(grid)
    print(f"Unsafe points: {dangerous_points}")
    # I misread the question. It was *danger* points, not safe lol
    # 6113


#####################################


def mark_diagonal(grid, start, end):
    start_x, start_y = start
    end_x, end_y = end
    # print(f"\tDiag ({start_x}, {start_y}) -> ({end_x}, {end_y})")
    length_x = end_x - start_x
    length_y = end_y - start_y
    print(f"\tDiag x: {length_x}")
    print(f"\tDiag y: {length_y}")
    print(f"\tDiag length: {abs(length_x)}")
    assert abs(length_x) == abs(length_y)
    step_x = 1 if end_x > start_x else -1
    step_y = 1 if end_y > start_y else -1
    cur_x = start_x
    cur_y = start_y
    while cur_x != end_x:
        # grid[cur_x][cur_y] += 1
        grid[(cur_x, cur_y)] += 1
        cur_x += step_x
        cur_y += step_y

    assert cur_y == end_y
    grid[(end_x, end_y)] += 1


def part2():
    print("\n###########################\n")
    return part1()
    # 20352 is too low
    # 20353 is wrong. I'm not off-by-one
    # 341348 is wrong
    # After converting to Counter() I get the same result, 20352
    # Fixed - I forgot to mark the final point of diagonals



# part1()
part2()
