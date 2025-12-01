

MAX_HEIGHT = 6
MAX_TURNS = 43


def piece(p1_turn):
    return p1_turn and 'x' or 'o'
    # return 'x' if p1_turn else 'o'


def player_name(p1_turn):
    return p1_turn and "Player1" or "Player2"


def take_input(msg):
    column = input(msg)
    try:
        if 0 <= int(column) <= 6:
            return int(column)
    except ValueError:
        pass
    return -1


def take_turn(board, p1_turn):
    column = take_input(f"{player_name(p1_turn)} choose a column (0-6):")
    while column == -1 or column_is_full(board, column):
        column = take_input(f"Invalid move. {player_name(p1_turn)} choose a column (0-6):")
        
    board[column].append(piece(p1_turn))
    return column
   

def column_is_full(board, column):
    return len(board[column]) == MAX_HEIGHT


def print_board(board):
    output = ""
    for row in range(MAX_HEIGHT -1, -1, -1):
        output += " "
        for column in range(len(board)):
            try:
                output += board[column][row]
            except IndexError:
                output += '-'
            if column != len(board) - 1:
                output += ' | '
        output += '\n'
    print(output)


def check_win(board, column_idx):
    last_piece = board[column_idx][-1]
    row_idx = len(board[column_idx]) - 1
    return (
        check_win_horizontal(board, row_idx, last_piece) or
        check_win_vertical(board[column_idx], last_piece) or
        check_win_diagonal(board, last_piece)
    )


def check_win_horizontal(board, row, last_piece):
    board_row = []
    for i in range(0, len(board)):
        try:
            board_row.append(board[i][row])
        except IndexError:
            board_row.append('-')

    for start_idx in range(3):
        if all(cell == last_piece for cell in board_row[start_idx:start_idx+4]):
            return True
    return False


def check_win_vertical(board_column, last_piece):
    if len(board_column) < 4:
        return False
    if all(cell == last_piece for cell in board_column[-4:-1]):
        return True
    return False


def check_win_diagonal(board, last_piece):
    return (
        check_rising_diag_win(board, last_piece)
        or check_falling_diag_win(board, last_piece)
    )


def check_rising_diag_win(board, last_piece):
    counter = 0
    for col_idx_start in range(0, 4):
        for offset in range(0, 4):
            # print(board[col_idx_start+offset])
            try:
                if board[col_idx_start+offset][offset] == last_piece:
                    # print(f"Diag ({col_idx_start+offset},{offset}): Yes")
                    counter += 1
                    if counter == 4:
                        return True
                else:
                    counter = 0
            except IndexError:
                counter = 0
    return False
        

def check_falling_diag_win(board, last_piece):
    counter = 0
    for col_idx_start in range(6, 2, -1):
        for offset in range(0, 4):
            # print(board[col_idx_start+offset])
            try:
                if board[col_idx_start-offset][offset] == last_piece:
                    # print(f"Diag ({col_idx_start+offset},{offset}): Yes")
                    counter += 1
                    if counter == 4:
                        return True
                else:
                    counter = 0
            except IndexError:
                counter = 0
    return False


def run():
    board = [
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        # ['o', 'o', 'o',],
        # ['x', 'o', 'x'],
        # ['o', 'x'],
        # ['x'],
    ]
    p1_turn = True

    print("Welcome to connect 4! Player 1 goes first.")
    
    turn_counter = 0
    while turn_counter < MAX_TURNS:
        print_board(board)

        column = take_turn(board, p1_turn)

        if check_win(board, column):
            print_board(board)
            print(f"{player_name(p1_turn)} is the winner")
            print("Congratuations!")
            return
        
        p1_turn = not p1_turn # swap players
        turn_counter += 1

    print("Draw game.")


if __name__ == '__main__':
    run()