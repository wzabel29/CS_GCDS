"""
┌───────────────────────────────────────────────────────────────────────────┐
│                               Battleships                                 |
├───────────────────────────────────────────────────────────────────────────┤
│ Name: Wyatt Zabel                                                         │
| Course: CS2                                                               |
│ Log: Finished project (1.0)                                               |
| Bugs: N/K                                                                 │
│ Description:  Play battleships against another player or robot.           |
| Board is created by nested lists in list.                                 |
└───────────────────────────────────────────────────────────────────────────┘
"""
import random
import time

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


def init_board():
    return [["🟦","🟦","🟦", "🟦", "🟦"], ["🟦","🟦","🟦", "🟦", "🟦"], ["🟦","🟦","🟦", "🟦", "🟦"], ["🟦","🟦","🟦", "🟦", "🟦"], ["🟦","🟦","🟦", "🟦", "🟦"]]


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


def get_player_move(board, symbol, hit_or_pick):
    """
    gets number for column and row
                            
    Args:
        board(list): list that makes up spots on tic tac toe board
        x_or_o(str): "X" or "O" when playing game   
    Returns:
        board adding "X" or "O"                   
    """
    print_board(board)
    print(f"Time to pick a spot to {hit_or_pick}!")

    while True:
        col = get_integer("column")
        row = get_integer("row")
    
        if board[row][col] != "🟦":                                              #only take space if its blank
            print("That space is taken. Choose another!")
            continue
        board[row][col] = symbol                                                  #substitute in list in list

        return row, col
        

def two_player():
    player_one_spots = init_board()
    player_two_spots = init_board()

    print("Player 1, Place your 4 ships please. Hide the screen from player 2.")
    for i in range(4):
        get_player_move(player_one_spots, "🚢", "pick")
    print_board(player_one_spots)

    print("\n" * 30)
    print("Please give the screen to player 2.")
    time.sleep(2)
    print("Player 2, Place your 4 ships please. Hide the screen from player 1.")
    for i in range(4):
        get_player_move(player_two_spots, "🚢", "pick")
    print_board(player_two_spots)

    print("\n" * 30)
    player_one_play = init_board()
    player_two_play = init_board()
    player_one_hits = 0
    player_two_hits = 0
    print("Begin!")

    while True:
        print("Player 1, choose where to hit")
        row, col = get_player_move(player_one_play, "🌊", "hit")
        if player_two_spots[row][col] != "🟦":
            player_one_play[row][col] = "💥"
            player_one_hits += 1
            print("Hit!")
        else:
            print("Miss.")

        print("Player 1 shots:")
        print_board(player_one_play)

        if winner(player_one_hits):
            print("Congrats player 1 on winning!")
            break

        print("Player 2, choose where to hit")
        row, col = get_player_move(player_two_play, "🌊", "hit")
        if player_one_spots[row][col] != "🟦":
            player_two_play[row][col] = "💥"
            player_two_hits += 1
            print("Hit!")
        else:
            print("Miss.")

        print("Player 2 shots:")
        print_board(player_two_play)

        if winner(player_two_hits):
            print("Congrats player 2 on winning!")
            break



def robot_player():
    player_one_spots = init_board()
    robot_spots = init_board()

    print("Place your 4 ships please.")
    for i in range(4):
        get_player_move(player_one_spots, "🚢", "pick")
    print_board(player_one_spots)

    print("robot choosing spots...")
    time.sleep(2)
    for i in range(4):
        while True:
            row = random.randint(0, 4)
            col = random.randint(0, 4)
            if robot_spots[row][col] != "🟦":
                continue
            robot_spots[row][col] = "🚢"
            break

    player_one_play = init_board()
    robot_play = init_board()
    player_one_hits = 0
    robot_hits = 0
    print("Begin!")

    while True:
        row, col = get_player_move(player_one_play, "🌊", "hit")
        if robot_spots[row][col] != "🟦":
            player_one_play[row][col] = "💥"
            player_one_hits += 1
            print("Hit!")
        else:
            print("Miss.")

        print("Your shots:")
        print_board(player_one_play)

        if winner(player_one_hits):
            print("Congrats player 1 on winning!")
            break

        while True:
            row = random.randint(0, 4)
            col = random.randint(0, 4)
        
            if robot_play[row][col] != "🟦":
                continue
            robot_play[row][col] = "🌊"
            break
        
        print("Robot shooting shot...")
        time.sleep(2)
        if player_one_spots[row][col] != "🟦":
            robot_play[row][col] = "💥"
            robot_hits += 1
            print("You have been hit!")
        else:
            print("your ships have not been hit")

        print("The damage on your board:")
        print_board(robot_play)
           
        if winner(robot_hits):
            print("Player 1, you have lost")
            break


def winner(hits):
    return hits == 4


def main():
    """
    menu for what user would like to do
    """
    while True:
        play = input("""would you like to play:
        1) 2 player battleships
        2) battleship against a robot
        3) quit
        response:  """)
        
        if play == "1":
            two_player()
        elif play == "2":
            robot_player()
        elif play == "3":
            exit()
        else:
            print('Invalid')

main()