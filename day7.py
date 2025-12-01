input_filename = __file__.split('.')[0] + ".input"
with open(input_filename) as f:
    raw = f.read().strip().split(',')

crab_positions = [int(x) for x in raw]


def part1():
    pos_min = min(crab_positions)
    pos_max = max(crab_positions)
    pos_to_fuel_cost = {}

    for group_pos in range(pos_min, pos_max + 1):
        deltas = [abs(crab_pos - group_pos) for crab_pos in crab_positions]
        pos_to_fuel_cost[group_pos] = sum(deltas)


    # debugging
    # print(pos_to_fuel_cost)
    # __import__("pprint").pprint(pos_to_fuel_cost)
    # print(f"\tAVERAGE: {sum(pos_to_fuel_cost.values()) / len(pos_to_fuel_cost)}")

    cheapest_fuel_cost = min(pos_to_fuel_cost.values())
    best_position = next(k for k, v in pos_to_fuel_cost.items() if v == cheapest_fuel_cost)
    fuel_cost = pos_to_fuel_cost[best_position]

    print(f"Quickly crabs, align to position {best_position}!")
    print(f"This manuver will require {fuel_cost} fuel")


def crab_fuel_cost(delta):
    if delta < 10:
        # print(f"Cost for delta {delta}: {sum(step - 1 for step in range(1, delta + 1))}")
        pass
    return sum(step for step in range(1, delta + 1))


def part2():
    pos_min = min(crab_positions)
    pos_max = max(crab_positions)
    pos_to_fuel_cost = {}
    print(f"Range of Positions: {pos_min} - {pos_max}")

    for group_pos in range(pos_min, pos_max + 1):
        print(f"Calculating position {group_pos}")
        deltas = [abs(crab_pos - group_pos) for crab_pos in crab_positions]
        pos_to_fuel_cost[group_pos] = sum(crab_fuel_cost(d) for d in deltas)

    cheapest_fuel_cost = min(pos_to_fuel_cost.values())
    best_position = next(k for k, v in pos_to_fuel_cost.items() if v == cheapest_fuel_cost)
    fuel_cost = pos_to_fuel_cost[best_position]

    print(f"Quickly crabs, align to position {best_position}!")
    print(f"This manuver will require {fuel_cost} fuel")
    # Too high: 357461350417091132998628818130170626710244303668212016473977567461747280851920454924692000993900741063265478491543370624613042413715357696532230413319279431699026030284817239206569555937047591949485769471037565895059820813230887719144588509796067787482270144880267834383677207432550238
    # Too low: 96003565
    # Too low: 96004565



# part1()
part2()
