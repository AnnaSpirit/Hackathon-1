def init_board():
    board = [['' for _ in range(8)] for _ in range(8)]
    board[0] = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']  # Black pieces
    board[1] = ['p'] * 8  # Black pawns
    board[6] = ['P'] * 8  # White pawns
    board[7] = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']  # White pieces
    return board


def show_board(board):
    for line in board:
        print(' '.join(['.' if case == '' else case for case in line]))
    print()


def transform_input(moove):
    try:
        depart, arrivee = moove.split()
        if len(depart) != 2 or len(arrivee) != 2:
            raise ValueError
        col_depart = ord(depart[0]) - ord('a')
        row_depart = 8 - int(depart[1])
        col_arrivee = ord(arrivee[0]) - ord('a')
        row_arrivee = 8 - int(arrivee[1])
        return (row_depart, col_depart), (row_arrivee, col_arrivee)
    except Exception:
        raise ValueError("Invalid move format.'")


def valid_moove(board, coords, piece):
    (from_row, from_col), (to_row, to_col) = coords
    direction = -1 if piece.isupper() else 1

    delta_row = to_row - from_row
    delta_col = to_col - from_col

    def is_opponent(target):
        return target != '' and piece.isupper() != target.isupper()

    # Pawn
    if piece.lower() == 'p':
        if delta_col == 0:
            if delta_row == direction and board[to_row][to_col] == '':
                return True
            if delta_row == 2 * direction and from_row in (6, 1) and board[to_row][to_col] == '' and board[from_row + direction][to_col] == '':
                return True
        if abs(delta_col) == 1 and delta_row == direction and is_opponent(board[to_row][to_col]):
            return True

    # Rook
    if piece.lower() == 'r':
        if from_row == to_row or from_col == to_col:
            step_row = (to_row - from_row) // max(1, abs(to_row - from_row)) if from_row != to_row else 0
            step_col = (to_col - from_col) // max(1, abs(to_col - from_col)) if from_col != to_col else 0
            row, col = from_row + step_row, from_col + step_col
            while (row, col) != (to_row, to_col):
                if board[row][col] != '':
                    return False
                row += step_row
                col += step_col
            return board[to_row][to_col] == '' or is_opponent(board[to_row][to_col])

    # Knight
    if piece.lower() == 'n':
        if (abs(delta_row), abs(delta_col)) in [(2, 1), (1, 2)]:
            return board[to_row][to_col] == '' or is_opponent(board[to_row][to_col])

    # Bishop
    if piece.lower() == 'b':
        if abs(delta_row) == abs(delta_col):
            step_row = (to_row - from_row) // abs(delta_row)
            step_col = (to_col - from_col) // abs(delta_col)
            row, col = from_row + step_row, from_col + step_col
            while (row, col) != (to_row, to_col):
                if board[row][col] != '':
                    return False
                row += step_row
                col += step_col
            return board[to_row][to_col] == '' or is_opponent(board[to_row][to_col])

    # Queen
    if piece.lower() == 'q':
        if abs(delta_row) == abs(delta_col) or from_row == to_row or from_col == to_col:
            step_row = (to_row - from_row) // max(1, abs(to_row - from_row)) if delta_row != 0 else 0
            step_col = (to_col - from_col) // max(1, abs(to_col - from_col)) if delta_col != 0 else 0
            row, col = from_row + step_row, from_col + step_col
            while (row, col) != (to_row, to_col):
                if board[row][col] != '':
                    return False
                row += step_row
                col += step_col
            return board[to_row][to_col] == '' or is_opponent(board[to_row][to_col])

    # King
    if piece.lower() == 'k':
        if abs(delta_row) <= 1 and abs(delta_col) <= 1:
            return board[to_row][to_col] == '' or is_opponent(board[to_row][to_col])

    return False


def play_moove(board, coords):
    (from_row, from_col), (to_row, to_col) = coords
    piece = board[from_row][from_col]

    if piece == '':
        print("Error: no piece to move here.")
        return

    if not valid_moove(board, coords, piece):
        print("Invalid move for this piece.")
        return

    board[to_row][to_col] = piece
    board[from_row][from_col] = ''


# Main game loop
board = init_board()

while True:
    show_board(board)
    moove = input("Enter a move  or 'quit' to exit: ")

    if moove.lower() == 'quit':
        print("Game over. See you next time!")
        break

    try:
        coords = transform_input(moove)
        play_moove(board, coords)
    except ValueError:
        print("Invalid format. Please enter a valid move .")
