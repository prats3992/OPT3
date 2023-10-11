import random

def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    # Check if the game is a draw
    return all(board[i][j] != '-' for i in range(3) for j in range(3))

def get_empty_cells(board):
    # Get a list of empty cells on the board
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == '-']
    return empty_cells

def make_best_move(board, player):
    empty_cells = get_empty_cells(board)

    for row, col in empty_cells:
        # Simulate a move and check if it results in a win
        board[row][col] = player
        if check_win(board, player):
            return row, col
        board[row][col] = '-'  # Undo the move

    for row, col in empty_cells:
        # Simulate the opponent's move and check if it results in a win for the opponent
        opponent = 'O' if player == 'X' else 'X'
        board[row][col] = opponent
        if check_win(board, opponent):
            return row, col
        board[row][col] = '-'  # Undo the move

    # If no winning or blocking moves, choose a random empty cell
    return random.choice(empty_cells)

if __name__ == "__main__":
    # Example usage
    current_board = [
        ['X', 'O', 'X'],
        ['-', 'X', 'O'],
        ['O', '-', '-']
    ]

    next_move_row, next_move_col = make_best_move(current_board, 'X')
    print(f"Next move: ({next_move_row}, {next_move_col})")
