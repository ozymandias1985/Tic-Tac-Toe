import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def user_move(board):
    while True:
        try:
            row = int(input("Enter row number (0, 1, or 2): "))
            col = int(input("Enter column number (0, 1, or 2): "))

            if board[row][col] != " ":
                print("That cell is already occupied. Try again.")
                continue

            return row, col
        except ValueError:
            print("Please enter valid row and column numbers.")

def computer_move(board):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)

        if board[row][col] == " ":
            return row, col

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)

        if current_player == "X":
            row, col = user_move(board)
        else:
            print("Computer's turn...")
            row, col = computer_move(board)

        board[row][col] = current_player

        if check_win(board, current_player):
            print_board(board)
            if current_player == "X":
                print("Congratulations! You win!")
            else:
                print("Sorry, the computer wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

play_tic_tac_toe()
