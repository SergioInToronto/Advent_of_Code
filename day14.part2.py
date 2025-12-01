import re


MEMORY_REGEX = re.compile("^mem\\[([0-9]+)\\] = ([0-9]+)$")


input_filename = __file__.split(".")[0] + ".input"
with open(input_filename) as f:
    raw = f.read().strip().split("\n")


def _get_addresses(address, mask):
    address = address.zfill(len(mask))
    addresses = ['']
    for i, c in enumerate(mask):
        if c == '0':  # unchanged
            for idx, _ in enumerate(addresses):
                addresses[idx] += address[i]
        elif c == '1':  # force 1
            for idx, _ in enumerate(addresses):
                addresses[idx] += '1'
        elif c == 'X':  # quantum bit
            addresses *= 2  # double number of addresses
            half = int(len(addresses)/2)
            for idx, _ in enumerate(addresses[:half]):
                addresses[idx] += '0'
            for idx, _ in enumerate(addresses[half:], half):
                addresses[idx] += '1'

    return addresses


import pdb;pdb.set_trace()


memory = {}
current_bitmask = None
for line in raw:
    if line.startswith("mask"):
        _, current_bitmask = line.split(" = ")
    else:
        address, value = re.match(MEMORY_REGEX, line).groups()
        value = int(value)
        address = bin(int(address)).split('b')[1]
        addresses = _get_addresses(address, current_bitmask)
        for adr in addresses:
            memory[adr] = value


answer = sum(memory.values())
print(answer)
if answer <= 3812194945915:
    print("It's probably wrong")
