import math


input_filename = __file__.split('.')[0] + ".input"
with open(input_filename) as f:
    raw = f.read().strip().split('\n')

lines = raw


ILLEGAL_CLOSINGS_POINTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

FIXED_CLOSINGS_POINTS = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

BRACKET_PAIRS = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}


def matches(opening, closing):
    if opening not in BRACKET_PAIRS:
        raise ValueError(opening)
    return BRACKET_PAIRS[opening] == closing


def diagnose_line(line):
    stack = []
    illegal_closings = []
    for index, char in enumerate(line):
        if char in '[{(<':
            stack.append(char)
        elif char in '>)}]':
            opening = stack.pop()
            if matches(opening, char):
                continue
            # print(f'Char {index + 1}: "{opening}" does not match {char}')
            illegal_closings.append(char)
            break # part 1
    if illegal_closings:
        # print('Line is corrupted')
        return 'corrupted', illegal_closings
    if stack:
        # print(f'Char {index + 1} is incomplete')
        return 'incomplete', stack
    print(f'Char {index + 1} looks good')


def part1():
    tally = 0
    for line in lines:
        result, illegal_closings = diagnose_line(line)
        if not illegal_closings:
            continue
        if result != 'corrupted':
            continue
        assert len(illegal_closings) == 1
        score = ILLEGAL_CLOSINGS_POINTS[illegal_closings[0]]
        tally += score

    print(f"Total score: {tally}")


def brackets_needed(line):
    # I don't feel great calling it twice but for a puzzle this is fine
    _, unclosed_brackets = diagnose_line(line)
    return (BRACKET_PAIRS[bracket] for bracket in unclosed_brackets)


def score_for_fixing_line(added_brackets):
    score = 0
    for char in added_brackets:
        score *= 5
        score += FIXED_CLOSINGS_POINTS[char]
    return score


def part2():
    incomplete_lines = (line for line in lines if diagnose_line(line)[0] == 'incomplete')
    line_fixes = map(brackets_needed, incomplete_lines)
    scores = sorted(list(map(score_for_fixing_line, line_fixes)))
    __import__('pprint').pprint(list(enumerate(scores)))
    print(f"{len(scores)} scores")
    middle_index = math.floor(len(scores) / 2)
    middle_score = scores[middle_index]
    print(f"Middle score: {middle_score} (index {middle_index})")
    # 904972989 is too low
    # 907809167 is too low
    # 3001858996 is too high
    # 2848420806 is wrong too :(
    # 2760390341 is wrong too :(


part1()
part2()
# print(score_for_fixing_line('])}>'))
# print(score_for_fixing_line('}}]])})]'))
# print(score_for_fixing_line(')}>]})'))
# print(score_for_fixing_line('}}>}>))))'))
# print(score_for_fixing_line(']]}}]}]}>'))
