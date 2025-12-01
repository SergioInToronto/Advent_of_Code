import string


ITEM_PRIORITIES = dict(zip(string.ascii_letters, range(1, 53)))


with open('input.txt') as f:
    lines = f.read().strip().split('\n')

total_priorities = 0

for rucksack in lines:
    middle_point = int(len(rucksack) / 2)
    items1, items2 = rucksack[:middle_point], rucksack[middle_point:]
    misplaced_item = next(x for x in items1 if x in items2)
    total_priorities += ITEM_PRIORITIES[misplaced_item]

print(f"Part1: {total_priorities}")

# ---

total_priorities = 0
for start_line in range(0, 300, 3):
    bag1, bag2, bag3 = lines[start_line:start_line+3]

    badge_item_type = next(x for x in bag1 if x in bag2 and x in bag3)
    total_priorities += ITEM_PRIORITIES[badge_item_type]

print(f"Part2: {total_priorities}")
