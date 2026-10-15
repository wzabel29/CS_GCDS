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
        win, player = winner(board)
        if win: 
            print_board(board)
            print(f"Congrats Player {player}") 
            return
        get_player_move_2(board)
        win, player = winner(board)
        if win: 
            print_board(board)
            print(f"Congrats Player {player}") 
            return
        if winner(board) == True:
            print(f"Congrats Player {winner(board)}")
            return

    get_player_move_1(board)
    win, player = winner(board)
    print_board(board)
    if win:
        print(f"Congrats Player {player}")
    else:
        print("Game over! It's a tie.")


def winner(board):
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        player_winner = board[0][0]
        return True, player_winner
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        player_winner = board[0][2]
        return True, player_winner

    for i in range(3):
        if board[i][0] == board [i][1] == board[i][2] and board[i][0] != " ":
            player_winner = board[i][0]
            return True, player_winner
    
        elif board[0][i] == board [1][i] == board[2][i] and board[0][i] != " ":
            player_winner = board[0][i]
            return True, player_winner

    return False, None

play_game(board)