def x_player_turn(game_board):
    print("'X' player's turn!")
    user_board = f"""#       B O A R D       #


B       {game_board[0][0]} | {game_board[0][1]} | {game_board[0][2]}       1
O       _________
A       {game_board[1][0]} | {game_board[1][1]} | {game_board[1][2]}       2
R       _________
D       {game_board[2][0]} | {game_board[2][1]} | {game_board[2][2]}       3


#       1   2   3       #
"""
    print(user_board)
    mark_placed = False
    while not mark_placed:
        mark_position = input(
            "Select where do you want to put your mark? (For example, type 11 for top left corner, 31 for top right corner and 21 for top middle cell): ")
        if game_board[int(mark_position[1]) - 1][int(mark_position[0]) - 1] == " ":
            game_board[int(mark_position[1]) - 1][int(mark_position[0]) - 1] = "X"
            mark_placed = True
        else:
            print("That field is already occupied!")
    print("Mark has been placed!")


def o_player_turn(game_board):
    print("'O' player's turn!")
    user_board = f"""#       B O A R D       #


B       {game_board[0][0]} | {game_board[0][1]} | {game_board[0][2]}       1
O       _________
A       {game_board[1][0]} | {game_board[1][1]} | {game_board[1][2]}       2
R       _________
D       {game_board[2][0]} | {game_board[2][1]} | {game_board[2][2]}       3


#       1   2   3       #
"""
    print(user_board)
    mark_placed = False
    while not mark_placed:
        mark_position = input(
            "Select where do you want to put your mark? (For example, type 11 for top left corner, 31 for top right corner and 21 for top middle cell): ")
        if game_board[int(mark_position[1]) - 1][int(mark_position[0]) - 1] == " ":
            game_board[int(mark_position[1]) - 1][int(mark_position[0]) - 1] = "O"
            mark_placed = True
        else:
            print("That field is already occupied!")
    print("Mark has been placed!")


def check_for_winners(game_board):
    user_board = f"""#       B O A R D       #


B       {game_board[0][0]} | {game_board[0][1]} | {game_board[0][2]}       1
O       _________
A       {game_board[1][0]} | {game_board[1][1]} | {game_board[1][2]}       2
R       _________
D       {game_board[2][0]} | {game_board[2][1]} | {game_board[2][2]}       3


#       1   2   3       #
"""
    # Player 'X' won
    if game_board[0][0] == "X":
        # Vertical win
        if game_board[1][0] == "X" and game_board[2][0] == "X":
            print("'X' player has won vertically!")
            print(user_board)
            return "X"
        # Horizontal win
        if game_board[0][1] == "X" and game_board[0][2] == "X":
            print("'X' player has won horizontally!")
            print(user_board)
            return "X"
    if game_board[1][1] == "X":
        # Vertical win
        if game_board[0][1] == "X" and game_board[2][1] == "X":
            print("'X' player has won vertically!")
            print(user_board)
            return "X"
        # Horizontal win
        if game_board[1][0] == "X" and game_board[1][2] == "X":
            print("'X' player has won horizontally!")
            print(user_board)
            return "X"
        # Diagonal wins
        if game_board[0][0] == "X" and  game_board[2][2] == "X":
            print("'X' player has won diagonally!")
            print(user_board)
            return "X"
        if game_board[0][2] == "X" and game_board[2][0] == "X":
            print("'X' player has won diagonally!")
            print(user_board)
            return "X"
    if game_board[2][2] == "X":
        # Vertical win
        if game_board[0][2] == "X" and game_board[1][2] == "X":
            print("'X' player has won vertically!")
            print(user_board)
            return "X"
        # Horizontal win
        if game_board[2][0] == "X" and game_board[2][1] == "X":
            print("'X' player has won horizontally!")
            print(user_board)
            return "X"

    # Player 'O' won
    if game_board[0][0] == "O":
        # Vertical win
        if game_board[1][0] == "O" and game_board[2][0] == "O":
            print("'O' player has won vertically!")
            print(user_board)
            return "O"
        # Horizontal win
        if game_board[0][1] == "O" and game_board[0][2] == "O":
            print("'O' player has won horizontally!")
            print(user_board)
            return "O"
    if game_board[1][1] == "O":
        # Vertical win
        if game_board[0][1] == "O" and game_board[2][1] == "O":
            print("'O' player has won vertically!")
            print(user_board)
            return "O"
        # Horizontal win
        if game_board[1][0] == "O" and game_board[1][2] == "O":
            print("'O' player has won horizontally!")
            print(user_board)
            return "O"
        # Diagonal wins
        if game_board[0][0] == "O" and game_board[2][2] == "O":
            print("'O' player has won diagonally!")
            print(user_board)
            return "O"
        if game_board[0][2] == "O" and game_board[2][0] == "O":
            print("'O' player has won diagonally!")
            print(user_board)
            return "O"
    if game_board[2][2] == "O":
        # Vertical win
        if game_board[0][2] == "O" and game_board[1][2] == "O":
            print("'O' player has won vertically!")
            print(user_board)
            return "O"
        # Horizontal win
        if game_board[2][0] == "O" and game_board[2][1] == "O":
            print("'O' player has won horizontally!")
            print(user_board)
            return "O"


def play_tic_tac_toe():
    someone_won = False
    game_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    whos_turn = "X"

    while not someone_won:
        if whos_turn == "X":
            x_player_turn(game_board)
            whos_turn = "O"
        elif whos_turn == "O":
            o_player_turn(game_board)
            whos_turn = "X"
        if check_for_winners(game_board) == "X":
            print("Congrats, 'X' player!")
            someone_won = True
        elif check_for_winners(game_board) == "O":
            print("Congrats, 'O' player!")
            someone_won = True
        else:
            pass


while input("Do you want to play a game of tic tac toe? Type 'y' or 'n': ") == "y":
    play_tic_tac_toe()
