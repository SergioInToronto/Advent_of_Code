

lines = open('input.txt').read().strip().split('\n')

def move_head(direction, head_coord):
    head_x, head_y = head_coord
    match direction:
        case 'U':
            return (head_x - 1, head_y)
        case 'D':
            return (head_x + 1, head_y)
        case 'L':
            return (head_x, head_y - 1)
        case 'R':
            return (head_x, head_y + 1)
        case _:
            raise ValueError(f"Cannot handle direction {direction}")


def move_tail(head_coord, tail_coord):
    head_x, head_y = head_coord
    tail_x, tail_y = tail_coord
    delta_x = head_x - tail_x
    delta_y = head_y - tail_y

    # tail is within 1 cell of head. No need to move
    if -1 <= delta_x <= 1 and -1 <= delta_y <= 1:
        return tail_coord

    # pull in a straight line
    elif delta_y == 0:
        change = delta_x == 2 and 1 or -1
        return (tail_x + change, tail_y)
    elif delta_x == 0:
        change = delta_y == 2 and 1 or -1
        return (tail_x, tail_y + change)
    
    # pull diagonally
    elif delta_x in (2, -2) and delta_y in (1, -1):
        x_change = 1 if delta_x == 2 else -1
        return (tail_x + x_change, head_y)
    elif delta_x in (1, -1) and delta_y in (2, -2):
        y_change = 1 if delta_y == 2 else -1
        return (head_x, tail_y + y_change)
    
    # In part2 double diagonal pulls are now possible
    elif delta_x in (2, -2) and delta_y in (2, -2):
        x_change = 1 if delta_x == 2 else -1
        y_change = 1 if delta_y == 2 else -1
        return (tail_x + x_change, tail_y + y_change)
    else:
        raise ValueError(f"What's going on here?")


def part1():
    head_coord = (0, 0)
    tail_coord = (0, 0)
    tail_visits = set()
    for line in lines:
        direction, count = line.split()
        for step in range(int(count)):
            print(f"Head {head_coord} - Tail {tail_coord}")
            head_coord = move_head(direction, head_coord)
            tail_coord = move_tail(head_coord, tail_coord)
            tail_visits.add(tail_coord)
    return tail_visits


# print(f"Unique tail positions: {len(part1())}")


def part2():
    head = (0, 0)
    tails = [(0, 0)] * 9
    last_tail_visits = set()
    for line in lines:
        direction, count = line.split()
        for step in range(int(count)):
            head = move_head(direction, head)
            for idx, tail in enumerate(tails):
                leader = head if idx == 0 else tails[idx - 1]
                print(f"Moving tail {idx} from {tail} following {leader}")
                tails[idx] = move_tail(leader, tail)
            last_tail_visits.add(tails[-1])
    return last_tail_visits


print(f"Part 2, Unique last tail positions: {len(part2())}")
# 2274 is too low. Accidentally had 10 tails instread of 9

