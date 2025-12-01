import string
import re

OP = re.compile('move (\d+) from (\d) to (\d)')

def parse_stacks(stack_input):
    lines = stack_input.split('\n')
    stack_count = int(lines[-1].strip()[-1])

    stacks = [[] for _ in range(stack_count)]
    for line in lines[:-1]:
        for offset, char in enumerate(line):
            if char not in string.ascii_uppercase:
                continue
            # offsets: 1, 5, 9, 13, ...
            # sub 1: 0, 4, 8, 12, ...
            stack_idx = int((offset - 1) / 4)
            stacks[stack_idx].insert(0, char)

    return stacks


def debug_print(stacks):
    for idx, stack in enumerate(stacks, 1):
        print(f"Stack {idx}: {stack}")


def part1():
    with open('input.txt') as f:
        text = f.read()

    stack_input, instructions_input = text.split('\n\n')

    stacks = parse_stacks(stack_input)
    instructions = (re.match(OP, line) for line in instructions_input.split('\n'))
    for op_idx, instruction in enumerate(instructions):
        if instruction is None:
            continue # last line is blank
        
        count, source_idx, dest_idx = instruction.groups()
        count, source_idx, dest_idx = int(count), int(source_idx) - 1, int(dest_idx) - 1
        # part1
        # for step in range(count):
        #     try:
        #         crate = stacks[source_idx].pop()
        #         stacks[dest_idx].append(crate)
        #     except IndexError:
        #         print(f"Failure on step {step}")
        #         raise


        # part2
        crates = stacks[source_idx][-count:]
        stacks[dest_idx].extend(crates)
        for _ in range(count):
            stacks[source_idx].pop()
            
        print(f"\nLine {op_idx + 11} op: {instruction}")
        print(f"Groups: {instruction.groups()}")
        debug_print(stacks)

    # print creates at the top of each stack:
    print(''.join(stack and stack[-1] or '?' for stack in stacks))


part1()

