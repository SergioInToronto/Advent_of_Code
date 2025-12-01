input_filename = __file__.split('.')[0] + ".input"
with open(input_filename) as f:
    raw = f.read().strip().split('\n')

numbers = [int(x) for x in raw]

def _part1():
    working_set = numbers[:25]
    for number in numbers[25:]:
        if any(a + b == number for a in working_set for b in working_set):
            working_set.pop(0)
            working_set.append(number)
            continue
        print(f"Number {number} breaks the pattern")
        return number


invalid_number = _part1()
for start_line_no in range(len(numbers)):
    working_total = 0
    end_line_no = start_line_no + 2

    working_total = sum(numbers[start_line_no:end_line_no])
    while working_total < invalid_number:
        end_line_no += 1
        working_total = sum(numbers[start_line_no:end_line_no])

    if working_total != invalid_number:
        continue

    print("We found it!")
    parts = numbers[start_line_no:end_line_no]
    print(min(parts) + max(parts))