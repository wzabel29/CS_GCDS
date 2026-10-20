def print_board(board):
    """prints tic tac toe board
                    
            Args:
                board(list): list that makes up spots on tic tac toe board
                    
            Returns:
                prints board in format of tic tac toe board                   
    """
    print(f"""
        {" |  ".join(board[0])}
        --+----+--
        {" |  ".join(board[1])}
        --+----+--
        {" |  ".join(board[2])}""")


def get_integer(row_or_column):
    """gets number for column and row
                        
            Args:
                row_or_column(str): inputed string of row or column 
                        
            Returns:
                num(int): row or column in terms of index                   
        """
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
    """gets number for column and row
                            
            Args:
                board(list): list that makes up spots on tic tac toe board
                x_or_o(str): "X" or "O" when playing game 
                    
            Returns:
                board adding "X" or "O"                   
            """
    print_board(board)
    print(f"Player {x_or_o}: Choose a column and row:")

    while True:
        col = get_integer("column: ")
        row = get_integer("row: ")
    
        if board[row][col] != " ":
            print("That space is taken. Choose another!")
            continue
        else:
            board[row][col] = x_or_o
            break

        


def play_game(board):
    """gets number for column and row
                                
            Args:
                board(list): list that makes up spots on tic tac toe board
                    
            Returns:
                prints congrats to winning player
                return: ends function                  
                """
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

    get_player_move(board, "X")
    win, player = winner(board)
    print_board(board)
    if win:
        print(f"Congrats {player}")
    else:
        print("Game over! It's a tie.")


def winner(board):
    """gets number for column and row
                                
            Args:
                board(list): list that makes up spots on tic tac toe board
                    
            Returns:
                True: if there is a winner
                False: if there is no winner
                None: if no player wins
                player_winner(str): "X" or "O" which wins             
                """
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


def main():
    """
    menu for what user would like to do
    """
    while True:
        play = input("would you like to play 2 player tic tac toe? y or n: ").lower()
        if play == "y":
            board = [[" "," "," "], [" "," "," "], [" "," "," "]]
            play_game(board)
        elif play == "n":
            break

main()