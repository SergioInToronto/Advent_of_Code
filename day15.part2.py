from datetime import datetime


# raw = '0,3,6'
raw = '12,1,16,3,11,0'
numbers = [int(x) for x in raw.split(',')]


# build from raw
index_last_used = {}
for i, n in enumerate(numbers[:-1]):
    index_last_used[n] = i


# most number at index 0
start = len(numbers)
prev_number = numbers[-1]

s = datetime.now()

# import pdb;pdb.set_trace()

for i in range(start, 30_000_000):
# for i in range(start, 2020):
    if i % 1_000_000 == 0: print(f"Step {i} in {datetime.now()-s}")

    if prev_number not in index_last_used:
        index_last_used[prev_number] = i - 1
        prev_number = 0
    else:
        turns_since_last_appearance = i - 1 - index_last_used[prev_number]
        index_last_used[prev_number] = i - 1
        prev_number = turns_since_last_appearance

    numbers.append(prev_number)


answer = numbers[-1]
print(answer)
# too low: 27460
# too high: 175594
if not 27460 < answer < 175594:
    print("It's probably wrong")
