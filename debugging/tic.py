#!/usr/bin/python3

def print_board(board):
    """Display the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * (len(board) * 4 - 1))

def check_winner(board):
    """
    Check if there's a winner on the board.
    
    Returns:
        str: "X" or "O" if there's a winner, None otherwise.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_board_full(board):
    """Check if the board is full (no more moves available)."""
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """Main function to play Tic Tac Toe."""
    board = [[" "]*3 for _ in range(3)]  # 3x3 empty board
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        # Input validation
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if row not in range(3) or col not in range(3):
                print("Invalid input! Please enter numbers between 0 and 2.")
                continue
            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue
        except ValueError:
            print("Invalid input! Please enter numeric values only.")
            continue

        # Make the move
        board[row][col] = current_player

        # Check for a winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        # Check for a draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
    