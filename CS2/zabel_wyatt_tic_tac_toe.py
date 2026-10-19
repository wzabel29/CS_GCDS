board = [[" "," "," "], [" "," "," "], [" "," "," "]]

def print_board(board):
    print(f"""
        {" |  ".join(board[0])}
        --+----+--
        {" |  ".join(board[1])}
        --+----+--
        {" |  ".join(board[2])}""")


def get_integer(row_or_column):
    while True:
        try:
            num = int(input(f"Enter {row_or_column}: "))
            if num not in [1, 2, 3]:
                print("Choose a number 1 to 3")
                continue
            
            return num - 1

        except ValueError:
            print("Enter a number from 1-3")


def get_player_move(board, x_or_o):
    print_board(board)
    print(f"Player {x_or_o}: Choose a column and row:")

    while True:
        col = get_integer("column")
        row = get_integer("row")
    
        if board[row][col] != " ":
            print("That space is taken. Choose another!")
            continue
        else:
            board[row][col] = x_or_o
            break

        


def play_game(board):
    for i in range(4):
        get_player_move(board, "X")
        win, player = winner(board)
        if win: 
            print_board(board)
            print(f"Congrats player {player}") 
            return
        get_player_move(board, "O")
        win, player = winner(board)
        if win: 
            print_board(board)
            print(f"Congrats player {player}") 
            return
        if winner(board) == True:
            print(f"Congrats player {player}")
            return

    get_player_move(board, "X")
    win, player = winner(board)
    print_board(board)
    if win:
        print(f"Congrats {player}")
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