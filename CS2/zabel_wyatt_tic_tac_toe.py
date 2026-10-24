import random

def print_board(board):
    """
    prints tic tac toe board
                    
    Args:
        board (list): list that makes up spots on tic tac toe board
    Returns:
        print: board in format of tic tac toe board                   
    """
    print(f"""
        {" |  ".join(board[0])}
        --+----+--
        {" |  ".join(board[1])}
        --+----+--
        {" |  ".join(board[2])}""")


def get_integer(row_or_column):
    """
    gets number for column and row
                        
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
    """
    gets number for column and row
                            
    Args:
        board(list): list that makes up spots on tic tac toe board
        x_or_o(str): "X" or "O" when playing game   
    Returns:
        board adding "X" or "O"                   
    """
    print_board(board)
    print(f"Player {x_or_o}, time to pick a spot!")

    while True:
        col = get_integer("column")
        row = get_integer("row")
    
        if board[row][col] != " ":                                              #only take space if its blank
            print("That space is taken. Choose another!")
            continue
        board[row][col] = x_or_o                                                #substitute in list in list
        return board
        

def winner(board):
    """
    gets number for column and row
                                
    Args:
        board(list): list that makes up spots on tic tac toe board   
    Returns:
        True: if there is a winner
        False: if there is no winner
        None: if no player wins
        player_winner(str): "X" or "O" which wins             
    """
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":        # if 3 diagnal and not space
        return True, board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":      #if other way across
        return True, board[0][2]

    for i in range(3):
        if board[i][0] == board [i][1] == board[i][2] and board[i][0] != " ":   #cycle through index in columns
            return True, board[i][0]
        elif board[0][i] == board [1][i] == board[2][i] and board[0][i] != " ": #cycle through inex in rows
            return True, board[0][i]
    return False, None        


def two_player(board):
    """
    Plays 2 person tic tac toe
                                
    Args:
        board(list): list that makes up spots on tic tac toe board  
    Returns:
        prints congrats to winning player
        return: ends function                  
    """
    turns = 0

    while turns < 10:
        board = get_player_move(board, "X")
        win, player = winner(board)

        if win:                                                                 #if true
            print(f"Congrats player {player}") 
            return
        turns += 1
        
        if turns == 9:
            break

        board = get_player_move(board, "O")
        win, player = winner(board)

        if win: 
            print(f"Congrats player {player}") 
            return
        turns += 1
    print("Game over! It's a tie.")                                             #if never returns true


def robot_player(board):
    """
    Plays tic tac toe against a robot
                                
    Args:
        board(list): list that makes up spots on tic tac toe board  
    Returns:
        prints congrats to winning player
        return: ends function                  
    """
    turns = 0
    
    while turns < 10:
        board = get_player_move(board, "X")
        win, player = winner(board)

        if win:                                                                 #if true
            print(f"Congrats player {player}") 
            return
        turns += 1
        
        if turns == 9:
            break

        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
        
            if board[row][col] != " ":
                continue
            board[row][col] = "O"
            break

        if win: 
            print(f"Congrats player {player}") 
            return
        turns += 1
    print("Game over! It's a tie.") 


def main():
    """
    menu for what user would like to do
    """
    while True:
        play = input("""would you like to play:"
        "1) 2 player tic tac toe"
        "2) tic tac toe against a robot"
        "3) quit
        response:  """).lower()
        
        if play == "1":
            board = [[" "," "," "], [" "," "," "], [" "," "," "]]               #set to blank before playing
            two_player(board)
        elif play == "2":
            board = [[" "," "," "], [" "," "," "], [" "," "," "]]               #set to blank before playing
            robot_player(board)
        elif play == "3":
            exit()
        else:
            print('Invalid')

main()