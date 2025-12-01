

with open('input.txt') as f:
    lines = f.read().split('\n')


def elf_sections(entry):
    first_section, last_section = entry.split('-')
    sections = list(range(int(first_section), int(last_section) + 1))
    return sections


def part1():
    fully_contained_count = 0

    for line in lines:
        if not line:
            continue

        elf1, elf2 = line.split(',')
        elf1_sections = elf_sections(elf1)
        elf2_sections = elf_sections(elf2)

        if (
            any(section in elf2_sections for section in elf1_sections)
            or any(section in elf1_sections for section in elf2_sections)
        ):
            fully_contained_count += 1

    return fully_contained_count


print(part1()) # first try woop woop!

# part2 changed all() to any()