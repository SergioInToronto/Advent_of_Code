

with open('input.txt') as f:
    elves_lines = f.read().split('\n\n')

elf_food_calories = [sum(int(x) for x in inventory.split()) for inventory in elves_lines]
elf_food_calories.sort()
print(elf_food_calories)


print("Top 3:", elf_food_calories[-3:], sum(elf_food_calories[-3:]))
