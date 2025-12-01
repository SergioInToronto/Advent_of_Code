input_filename = __file__.split('.')[0] + ".input"
with open(input_filename) as f:
    raw = f.read().strip().split('\n')

rows = [x for x in raw]

most_common_digits = ""
least_common_digits = ""

digits_per_row = len(rows[0])
print(f"digits_per_row: {digits_per_row}")
for digit_index in range(digits_per_row):
    values = {"0": 0, "1": 0}
    for row in rows:
        char = row[digit_index]
        values[char] += 1

    if values["0"] > values["1"]:
        most_common_digits += "0"
        least_common_digits += "1"
    else:
        most_common_digits += "1"
        least_common_digits += "0"

print(f"Most common digits per position: {most_common_digits}")
print(f"As decimal: {int(most_common_digits, 2)}")
print(f"Least common digits per position: {least_common_digits}")
print(f"As decimal: {int(least_common_digits, 2)}")
gamma_rate = int(most_common_digits, 2)
epsilon_rate = int(least_common_digits, 2)

print(f"Result: {gamma_rate * epsilon_rate}")


# Part 2


def most_common_in_position(position, items, value_if_tie):
    values = {"0": 0, "1": 0}
    for entry in items:
        values[entry[position]] += 1
    if values["0"] > values["1"]:
        return "0"
    if values["1"] > values["0"]:
        return "1"
    return value_if_tie


def least_common_in_position(position, items, value_if_tie):
    values = {"0": 0, "1": 0}
    for entry in items:
        values[entry[position]] += 1
    if values["0"] < values["1"]:
        return "0"
    if values["1"] < values["0"]:
        return "1"
    return value_if_tie


print('\n\n')
possible_values = [x for x in rows]
position = 0
while len(possible_values) > 1 and position < digits_per_row:
    print(f"Still considering {len(possible_values)} entries")
    most_common = most_common_in_position(position, possible_values, "1")
    possible_values = [x for x in possible_values if x[position] == most_common]
    position += 1

if len(possible_values) > 1:
    raise ValueError("NOPE you did it wrong")
oxygen_rating = int(possible_values[0], 2)
print(f"Oxygen Generator rating: {oxygen_rating}")

possible_values = [x for x in rows]
position = 0
while len(possible_values) > 1 and position < digits_per_row:
    print(f"Still considering {len(possible_values)} entries")
    least_common = least_common_in_position(position, possible_values, "0")
    possible_values = [x for x in possible_values if x[position] == least_common]
    position += 1

if len(possible_values) > 1:
    raise ValueError("NOPE you did it wrong v2")
co2_rating = int(possible_values[0], 2)
print(f"CO2 Scrubber rating: {co2_rating}")

print(f"Life support rating: {oxygen_rating * co2_rating}")

