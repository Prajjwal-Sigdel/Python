def print_board(board):
    print("The board looks like this:\n")
    for i in range(3):
        for j in range(3):
            if board[i*3 + j] == 1:
                print('X', end="")
            elif board[i*3 + j] == 0:
                print('O', end="")
            else:
                print(' ', end="")

            if j != 2:
                print(" | ", end="")
        print()

        if i != 2:
            print("-----------------")
    print()


def print_instruction():
    print("Please use the following cell numbers to make your move:")
    print_board([1, 2, 3, 4, 5, 6, 7, 8, 9])


def get_input(turn):
    valid = False
    while not valid:
        try:
            user = input(f"Where would you like to place {turn} (1-9)? ")
            user = int(user)
            if user >= 1 and user <= 9:
                return user - 1  # Convert to 0-based index
            else:
                print("That is not a valid move! Please try again.\n")
                print_instruction()
        except ValueError:
            print(f"{user} is not a valid move! Please try again.\n")
            print_instruction()


def check_win(board):
    win_cond = ((0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                (0, 4, 8), (2, 4, 6))  # Diagonals

    for each in win_cond:
        if board[each[0]] == board[each[1]] == board[each[2]] and board[each[0]] != -1:
            return board[each[0]]  # Return the player (1 or 0)

    return -1  # No winner yet


def quit_game(board, msg):
    print_board(board)
    print(msg)
    quit()


def main():
    print_instruction()

    board = [-1] * 9  # Initialize the board with -1 representing empty cells
    move = 0
    while True:
        print_board(board)
        print(f"Turn number {move + 1}")
        turn = 'X' if move % 2 == 0 else 'O'

        # Get user input
        user = get_input(turn)
        while board[user] != -1:
            print("Invalid move! Cell already taken. Please try again.\n")
            user = get_input(turn)
        board[user] = 1 if turn == 'X' else 0  # Update the board

        # Check if there's a winner
        move += 1
        if move > 4:  # A winner is possible after 5 moves
            winner = check_win(board)
            if winner != -1:
                winner_str = "X" if winner == 1 else "O"
                quit_game(board, f"The winner is {winner_str} :)")
            elif move == 9:
                quit_game(board, "No winner :( It's a tie!")


if __name__ == "__main__":
    main()
