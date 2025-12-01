import cProfile
from itertools import chain
import numpy as np


input_filename = __file__.split('.')[0] + ".input"
with open(input_filename) as f:
    raw = f.read().strip().split('\n')


def new_fish_value(fish):
    return 6 if fish == 0 else fish - 1


def simulate(days):
    current_fish = [int(x) for x in raw[0].split(',')]
    for day in range(days):
        print(f"Start day {day + 1}. There are {len(current_fish)} fish")
        new_fish = (8 for fish in current_fish if fish == 0)
        # next_fish = map(new_fish_value, current_fish)
        next_fish = (6 if fish == 0 else fish-1 for fish in current_fish)
        current_fish = list(chain(next_fish, new_fish))
    return len(current_fish)


def simulate_no_copy(days):
    current_fish = [int(x) for x in raw[0].split(',')]
    for day in range(days):
        print(f"Start day {day + 1}. There are {len(current_fish)} fish")
        new_fish_count = 0
        for index, fish in enumerate(current_fish):
            if fish == 0:
                new_fish_count += 1
            current_fish[index] = 6 if fish == 0 else fish - 1
        current_fish.extend([8] * new_fish_count)


def simulate_with_numpy(days):
    current_fish = [int(x) for x in raw[0].split(',')]
    current_fish =  np.array(current_fish)
    for day in range(days):
        print(f"Start day {day + 1}. There are {len(current_fish)} fish")
        new_fish_count = 0
        for index, fish in enumerate(current_fish):
            if fish == 0:
                new_fish_count += 1
            current_fish[index] = 6 if fish == 0 else fish - 1
        current_fish = np.append(current_fish, [8] * new_fish_count)


def simulate_with_counts(days):
    # This is the obvious solution. I feel silly I tried numpy first
    fish = [int(x) for x in raw[0].split(',')]
    fish_counts = [
        fish.count(0), # 0
        fish.count(1),
        fish.count(2),
        fish.count(3),
        fish.count(4),
        fish.count(5),
        fish.count(6), # 0
        fish.count(7), # 0
        fish.count(8), # 0
    ]
    for day in range(days):
        print(f"Start day {day + 1}. There are {sum(fish_counts)} fish")
        new_counts = [0] * 9
        for life_counter, count in enumerate(fish_counts):
            if life_counter == 0:
                new_counts[8] = count
                new_counts[6] = count
            else:
                new_counts[life_counter - 1] += count
        fish_counts = new_counts

    return sum(fish_counts)


def part1():
    days = 80
    fish_count = simulate(days)
    print(f"After {days} days there are {fish_count} fish")



def part2():
    days = 256
    fish_count = simulate_with_counts(days)
    print(f"After {days} days there are {fish_count} fish")


# breakpoint()
# print(cProfile.run("simulate(100)"))
# print(cProfile.run("simulate_no_copy(110)"))
# print(cProfile.run("simulate_with_numpy(110)"))
# print(cProfile.run("simulate_with_counts(120)"))
part2()


# Start day 120. There are 11216969 fish
# Start day 120. There are 11216969 fish
# Start day 120. There are 11216969 fish
