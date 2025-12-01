# A for rock
# B for paper
# C for scissors
# X for rock
# Y for paper
# Z for scissors

# --- part2 ---
# X means loss
# Y means tie
# Z means win

# 1 point for rock, 2 for paper, 3 for scissors
# plus score of outcome: 0 for loss, 3 for draw, 6 for win


with open('input.txt') as f:
    lines = f.read().split('\n')


def my_move_score(move):
    if move == 'X':
        return 1
    if move == 'Y':
        return 2
    if move == 'Z':
        return 3
    raise ValueError

def outcome_score(opponent_move, my_move):
    if (opponent_move, my_move) in (('A', 'X'), ('B', 'Y'), ('C', 'Z')):
        return 3

    match opponent_move, my_move:
        case 'A', 'Y':
            return 6
        case 'B', 'Z':
            return 6
        case 'C', 'X':
            return 6
        case _:
            return 0

def part1():
    total_score = 0
    for game in lines:
        if not game: # last line is blank
            continue
        opponent_move, my_move = game.split()
        game_score = my_move_score(my_move) + outcome_score(opponent_move, my_move)
        total_score += game_score

        # print(f"{my_move_score(my_move)} + {outcome_score(opponent_move, my_move)} = {game_score}. Total: {total_score}")

    return total_score


# --- Part 2 ---


def figure_out_move(opponent_move, outcome):
    print()
    match (opponent_move, outcome):
        case ("A", "Y") | ('B', 'X') | ('C', 'Z'): # throw rock
        # case "A", "Y": # throw rock
            return 'X'
        case ('B', 'Y') | ('C', 'X') | ('A', 'Z'): # throw paper
            return 'Y'
        case ('C', 'Y') | ('A', 'X') | ('B', 'Z'): # throw scissors
            return 'Z'
    raise ValueError


def outcome_score_part2(outcome):
    if outcome == 'X':
        return 0
    if outcome == 'Y':
        return 3
    if outcome == 'Z':
        return 6


def part2():
    total_score = 0
    for game in lines:
        if not game: # last line is blank
            continue

        opponent_move, outcome = game.split()
        my_move = figure_out_move(opponent_move, outcome)
        game_score = my_move_score(my_move) + outcome_score_part2(outcome)
        total_score += game_score

    return total_score





# print(part1())
# 13322 is too low
# 14531 was right! I was counting ties as 0 instead of 3.


print(part2())
