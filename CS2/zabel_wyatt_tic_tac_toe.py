board = [[" "," "," "], [" "," "," "], [" "," "," "]]

def print_board(board):
    print(f"""
        {" |  ".join(board[0])}
        --+----+--
        {" |  ".join(board[1])}
        --+----+--
        {" |  ".join(board[2])}""")


def get_player_move_1(board):
    print_board(board)
    print("Player 1: Choose a column and row:")
    while True:
        col = int(input("enter column:"))
        row = int(input("enter row:"))
        if col not in (1, 2, 3) or row not in (1, 2, 3):
            print("Choose a number 1 to 3")
        else:
            if board[row-1][col-1] == "X" or board[row-1][col-1] == "O":
                print("That space is taken. Choose another!")
            else:
                board[row-1][col-1] = "X"
                break


def get_player_move_2(board):
    print_board(board)
    print("Player 2: Choose a column and row:")
    while True:
        col = int(input("enter column:"))
        row = int(input("enter row:"))
        if col not in (1, 2, 3) or row not in (1, 2, 3):
            print("Choose a number 1 to 3")
        else:
            if board[row-1][col-1] == "X" or board[row-1][col-1] == "O":
                print("That space is taken. Choose another!")
            else:
                board[row-1][col-1] = "O"
                break


def play_game(board):
    for i in range(4):
        get_player_move_1(board)
        get_player_move_2(board)

    get_player_move_1(board)

    winner(board)


def winner(board):
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == "X":
            print("Congrats on winning player 1!")
        else:
            print("Congrats on winning player 2!")
    elif board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == "X":
            print("Congrats on winning player 1!")
        else:
            print("Congrats on winning player 2!")

    for i in range(3):
        if board[i][0] == board [i][1] == board[i][2]:
            if board[i][0] == "X":
                print("Congrats on winning player 1!")
            else:
                print("Congrats on winning player 2!")
        elif board[0][i] == board [1][i] == board[2][i]:
            if board[0][i] == "X":
                print("Congrats on winning player 1!")
            else:
                print("Congrats on winning player 2!")

    print("Tie.")

play_game(board)