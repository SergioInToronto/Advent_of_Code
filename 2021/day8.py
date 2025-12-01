input_filename = __file__.split('.')[0] + ".input"
with open(input_filename) as f:
    raw = f.read().strip().split('\n')

rows = [x.split("|") for x in raw]


def part1():
    counter = 0
    for index, (_, display_output) in enumerate(rows):
        display_digits = display_output.split()
        found = len([d for d in display_digits if len(d) in (2, 3, 4, 7)]) # digits 1, 7, 4, 8
        counter += found
        # print(f"Index {index} - Inspecting {display_output}: found {found}")
    print(f"Found {zcounter} digits that must be 1, 4, 7, and 8")
    # 257 is too low


def digits_with_length(digits, length):
    return [d for d in digits if len(d) == length]


def digit_with_length(digits, length):
    result = digits_with_length(digits, length)
    assert len(result) == 1
    return result[0]


def determine_top_segment(one, seven):
    return next(s for s in seven if s not in one)


def decode_display(display_output, numbers):
    def decode(display_number):
        for number, code in enumerate(numbers):
            if set(display_number) == set(code):
                return str(number)
        breakpoint()
        raise ValueError

    digits = map(decode, display_output.split())
    return int(''.join(digits))


def determine_display_value(all_digits, display_output):
    print(f"\tWorking on {all_digits}")
    digits = all_digits.split()

    one = digit_with_length(digits, 2)
    seven = digit_with_length(digits, 3)
    top_segment = determine_top_segment(one, seven)

    four = digit_with_length(digits, 4)
    eight = digit_with_length(digits, 7)

    topleft_and_middle = ''.join(s for s in four if s not in one)

    two_three_and_five = digits_with_length(digits, 5)
    middle_segment = next(s for s in four if all(s in d for d in two_three_and_five))
    topleft_segment = next(s for s in topleft_and_middle if s != middle_segment)

    three = next(d for d in two_three_and_five if all(s in d for s in one))
    five = next(d for d in two_three_and_five if topleft_segment in d)
    two = next(d for d in two_three_and_five if d not in (three, five))

    topright_segment = next(s for s in one if s in two)
    bottomright_segment = next(s for s in one if s in five)
    bottomleft_segment = next(s for s in two if s not in three)

    six_nine_and_zero = [d for d in digits if len(d) == 6]
    six = next(d for d in six_nine_and_zero if topright_segment not in d)
    nine = next(d for d in six_nine_and_zero if bottomleft_segment not in d)
    zero = next(d for d in six_nine_and_zero if middle_segment not in d)

    numbers = [
        zero,
        one,
        two,
        three,
        four,
        five,
        six,
        seven,
        eight,
        nine,
    ]
    output = decode_display(display_output.strip(), numbers)
    print(f"Decoded {output} from {display_output}")
    return output

    # print(f"\t\t Zero Six Nine: {zero}, {six}, {nine}")
    # print(f"\t\tTop Segment (Segment A): {top_segment}")
    # print(f"\t\tTop Left and Middle (Segment B & D): {topleft_and_middle}")
    # print(f"\t\t Middle Segment (Segment D): {middle_segment}")
    # print(f"\t\t Top Left Segment (Segment D): {topleft_segment}")
    # print(f"\t\t Three: {three}")
    # return 0


def part2():
    total = sum(determine_display_value(*row) for row in rows)
    print(f"Totall of all {len(rows)} displays is: {total}")


# part1()
part2()
