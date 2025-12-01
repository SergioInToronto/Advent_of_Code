input_filename = __file__.split('.')[0] + ".input"
with open(input_filename) as f:
    raw = f.read().strip()

boards = raw.split('\n\n')
numbers = boards.pop(0).split(',')
boards = dict(enumerate(boards))
# import pdb; pdb.set_trace()


def check_rows(board, drawn_numbers):
    rows = board.split('\n')
    for row in rows:
        if all(value in drawn_numbers for value in row.split()):
            return True
    return False


def check_columns(board, drawn_numbers):
    rows = [r.split() for r in board.split('\n')]
    columns = [
        [row[0] for row in rows],
        [row[1] for row in rows],
        [row[2] for row in rows],
        [row[3] for row in rows],
        [row[4] for row in rows],
    ]
    # __import__('pprint').pprint(columns)
    for column in columns:
        if all(value in drawn_numbers for value in column):
            return True
    return False


def check_win(board, drawn_numbers):
    return (
        check_rows(board, drawn_numbers) or
        check_columns(board, drawn_numbers)
    )


def find_winning_board_and_final_number():
    # print(numbers)
    # print()
    print(boards[0])

    for i in range(5, len(numbers)):
        print(f"Checking {i} bingo numbers...")
        drawn_numbers = numbers[0:i]
        for index, board in boards.items():
            if check_win(board, drawn_numbers):
                print(f"WINNER! Board {index} wins!")
                return board, drawn_numbers

    raise ValueError("NOBODY WON!")


def part1():
    winning_board, drawn_numbers = find_winning_board_and_final_number()
    # print(winning_board, drawn_numbers)
    board_numbers = winning_board.split()
    unselected_numbers = [int(n) for n in board_numbers if n not in drawn_numbers]
    final_number = int(drawn_numbers[-1])
    print(f"Unselected Numbers: {unselected_numbers}")
    print(f"Sum: {sum(unselected_numbers)}")
    print(f"Final drawn number: {final_number}")
    print()
    print(f"Answer: {sum(unselected_numbers) * final_number}")




def last_to_win_board():
    won_boards = []
    for i in range(5, len(numbers)):
        print(f"Checking {i} bingo numbers...")
        drawn_numbers = numbers[0:i]
        for index, board in boards.items():
            if board in won_boards:
                continue
            if check_win(board, drawn_numbers):
                print(f"Board {index} wins on {drawn_numbers[-1]}")
                won_boards.append(board)
        if len(won_boards) >= len(boards):
            return won_boards[-1], drawn_numbers


def part2():
    final_board, drawn_numbers = last_to_win_board()
    print(f"Final Board:\n{final_board}")
    board_numbers = final_board.split()
    unselected_numbers = [int(n) for n in board_numbers if n not in drawn_numbers]
    print(f"Unselected Numbers: {unselected_numbers}")
    print(f"Sum: {sum(unselected_numbers)}")
    final_number = int(drawn_numbers[-1])
    print(f"Final drawn number: {final_number}")
    print()
    print(f"Answer: {sum(unselected_numbers) * final_number}")
    # 12648 was too low
    # I had forgotten to let the final board win lol



part1()
part2()
