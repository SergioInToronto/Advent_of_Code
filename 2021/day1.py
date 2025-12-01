input_filename = __file__.split('.')[0] + ".input"
with open(input_filename) as f:
    raw = f.read().strip().split('\n')

numbers = [int(x) for x in raw]
# print(len(numbers))

increases = 0

for index, number in enumerate(numbers[1:], 1):
    # print(numbers[index-1], number, number > numbers[index-1])
    if number > numbers[index-1]:
        increases += 1

print(increases)


# Part 2, sliding windows

increases = 0
num_windows = 0
# first window indexes: 0, 1, 2
for base_index in range(4, len(numbers)):
    num_windows += 1
    prev_window = sum(numbers[base_index-4:base_index-1])
    current_window = sum(numbers[base_index-3:base_index])
    # if base_index < 10:
    if base_index > 1990:
        print(prev_window, current_window, current_window > prev_window)
    if current_window == prev_window:
        print(prev_window, current_window, current_window > prev_window, "NO CAHNGE")
    if current_window > prev_window:
        increases += 1

print("windows:", num_windows)
print("INCREASES:", increases)
# I was off by one. I figured it out by looking at the final sum vs computing it myself.
# When I realized I added 1 to my answer and submitted. Sleep time now.
