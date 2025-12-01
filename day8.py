input_filename = __file__.split('.')[0] + ".input"
with open(input_filename) as f:
    raw = f.read().strip().split('\n')

instructions = [x for x in raw]

def _run_program(program):
    already_executed = [False] * len(program)
    program_counter = 0
    accumulator = 0

    end_of_program = len(program)
    while program_counter < end_of_program:
        if program_counter < 0:
            raise ValueError("Cannot jump below zero. Fix your code")

        if already_executed[program_counter]:
            # print(f"Line {program_counter} has run before. Accumulator is {accumulator}.")
            return False, accumulator
        already_executed[program_counter] = True

        opcode, offset = program[program_counter].split()
        if opcode == 'acc':
            accumulator += int(offset)
        if opcode == 'jmp':
            program_counter += int(offset)
        else:
            program_counter += 1

    # print("Program completed successfully")
    return True, accumulator

# _run_program(instructions)

for line_no, line in enumerate(instructions):
    if line.startswith('acc'):
        continue
    if line.startswith('nop'):
        replaced_instruction = line.replace('nop', 'jmp')
    else:
        replaced_instruction = line.replace('jmp', 'nop')

    temp_program = [x for x in instructions]
    temp_program[line_no] = replaced_instruction

    success, accumulator = _run_program(temp_program)
    if not success:
        continue

    print(f"Sir, we found it! Line {line_no} was the problem")
    print(f"Accumulator was {accumulator}")
