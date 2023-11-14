# Initialize the Tic-Tac-Toe board as a 3x3 list
board = [[" " for _ in range(3)] for _ in range(3)]

# Function to display the current board
def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check for a win
def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check for a draw
def check_draw(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

# Main game loop
current_player = "X"
while True:
    display_board(board)
    print(f"Player {current_player}'s turn:")
    row = int(input("Enter row (0, 1, or 2): "))
    col = int(input("Enter column (0, 1, or 2): "))

    # Check if the chosen cell is empty
    if board[row][col] == " ":
        board[row][col] = current_player
        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        elif check_draw(board):
            display_board(board)
            print("It's a draw!")
            break
        current_player = "O" if current_player == "X" else "X"
    else:
        print("That cell is already taken. Try again.")
