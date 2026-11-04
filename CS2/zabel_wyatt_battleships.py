""""
┌───────────────────────────────────────────────────────────────────────────┐
│                               Tic Tac Toe                                 |
├───────────────────────────────────────────────────────────────────────────┤
│ Name: Wyatt Zabel                                                         │
| Course: CS2                                                               |
│ Log: Finished project (1.0)                                               |
| Bugs: N/K                                                                 │
│ Description:  Play Tic Tac Toe against another player or robot.          |
|Board is created by nested lists in list and winner is checked by cycling  |
|through list.                                                              |
└───────────────────────────────────────────────────────────────────────────┘
"""
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
        {"".join(board[0])}
        {"".join(board[1])}
        {"".join(board[2])}
        {"".join(board[3])}
        {"".join(board[4])}""")


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
            
            if num not in [1, 2, 3, 4, 5]:
                print("Choose a number 1 to 5")
                continue
            return num - 1
        except ValueError:
            print("Enter a number from 1-5")


def get_player_move(board, symbol):
    """
    gets number for column and row
                            
    Args:
        board(list): list that makes up spots on tic tac toe board
        x_or_o(str): "X" or "O" when playing game   
    Returns:
        board adding "X" or "O"                   
    """
    print_board(board)
    print(f"Time to pick a spot!")

    while True:
        col = get_integer("column")
        row = get_integer("row")
    
        if board[row][col] != "🟦":                                              #only take space if its blank
            print("That space is taken. Choose another!")
            continue
        board[row][col] = {symbol}                                                #substitute in list in list
        return board
        

def robot_player():
    for i in range(4):
        player_one_spots = [["🟦","🟦","🟦", "🟦", "🟦"], ["🟦","🟦","🟦", "🟦", "🟦"], ["🟦","🟦","🟦", "🟦", "🟦"], ["🟦","🟦","🟦", "🟦", "🟦"], ["🟦","🟦","🟦", "🟦", "🟦"]]
        get_player_move(player_one_spots, "🌊")
    for i in range(4):
        robot_spots = [["🟦","🟦","🟦", "🟦", "🟦"], ["🟦","🟦","🟦", "🟦", "🟦"], ["🟦","🟦","🟦", "🟦", "🟦"], ["🟦","🟦","🟦", "🟦", "🟦"], ["🟦","🟦","🟦", "🟦", "🟦"]]
        while True:
            row = random.randint(0, 4)
            col = random.randint(0, 4)
        
            if robot_spots[row][col] != "🟦":
                continue
            robot_spots[row][col] = "🌊"
            break
    while True:
        player_one_play = [["🟦","🟦","🟦", "🟦", "🟦"], ["🟦","🟦","🟦", "🟦", "🟦"], ["🟦","🟦","🟦", "🟦", "🟦"], ["🟦","🟦","🟦", "🟦", "🟦"], ["🟦","🟦","🟦", "🟦", "🟦"]
        get_player_move(player_one_play, "🌊")
        if robot_spots[row][col] == player_one_play[row][col]:
            player_one_play[row][col] = "💥"
        while True:
            row = random.randint(0, 4)
            col = random.randint(0, 4)
        
            if robot_spots[row][col] != "🟦":
                continue
            robot_spots[row][col] = "🌊"
            break
        

        



def two_player():
    


def main():
    """
    menu for what user would like to do
    """
    while True:
        play = input("""would you like to play:
        1) 2 player tic tac toe
        2) tic tac toe against a robot
        3) quit
        response:  """).lower()
        
        if play == "1":
            board = [["🟦","🟦","🟦", "🟦", "🟦"], ["🟦","🟦","🟦", "🟦", "🟦"], ["🟦","🟦","🟦", "🟦", "🟦"], ["🟦","🟦","🟦", "🟦", "🟦"], ["🟦","🟦","🟦", "🟦", "🟦"]]               #set to blank before playing
            two_player(board)
        elif play == "2":
            board = [[" "," "," "], [" "," "," "], [" "," "," "]]               #set to blank before playing
            robot_player(board)
        elif play == "3":
            exit()
        else:
            print('Invalid')

print_board()