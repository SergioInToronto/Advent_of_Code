input_filename = __file__.split('.')[0] + ".input"
with open(input_filename) as f:
    raw = f.read().strip().split('\n')

jolts = sorted(int(x) for x in raw)
jolts.insert(0, 0)
jolts.append(max(jolts) + 3)
# print(jolts)

# diffs = {1:0, 3:0}

# for i, number in enumerate(jolts[1:], 1):
#     diff = number - jolts[i-1]
#     diffs[diff] += 1

# print(diffs)
# print(diffs[1] * diffs[3])


#### Part 2 ####
paths_to_start = {1: 1, 2: 2, 3: 4}

for index, number in enumerate(jolts[4:], 4):
    # print(index, number)

    possible_paths_down = []
    for x in range(1, 4):
        if (number - x) in jolts:
            possible_paths_down.append((number - x))
    if not possible_paths_down:
        raise ValueError("No way down!")

    if len(possible_paths_down) == 1:
        # no branches here
        paths_to_start[number] = paths_to_start[possible_paths_down[0]]

        # print(index, number, possible_paths_down, paths_to_start[number])
        continue

    costs_of_paths_down = [paths_to_start[x] for x in possible_paths_down]
    paths_to_start[number] = sum(costs_of_paths_down)

    # print(index, number, possible_paths_down, paths_to_start[number])

print(paths_to_start[jolts[-1]])