import re


MEMORY_REGEX = re.compile("^mem\\[([0-9]+)\\] = ([0-9]+)$")


input_filename = __file__.split(".")[0] + ".input"
with open(input_filename) as f:
    raw = f.read().strip().split("\n")


def _apply_mask(mask, value):
    value = bin(int(value)).replace("b", "")
    longest = len(mask)  # Assume mask is always longest
    value = value.zfill(longest)  # fill with leading zeros
    result = ""
    for cm, cv in zip(mask, value):
        if cm in ('1', '0'):
            result += cm
        else:
            result += cv
    return int(result, 2)


memory = {}
current_bitmask = None
for line in raw:
    if line.startswith("mask"):
        _, current_bitmask = line.split(" = ")
    else:
        address, value = re.match(MEMORY_REGEX, line).groups()
        adjusted_value = _apply_mask(current_bitmask, value)
        memory[address] = adjusted_value


print(sum(memory.values()))
