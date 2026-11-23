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
to do list:
-put choosing ships in its own function
-check returns
-challenges
"""
import random
import time
import os


def print_board(board):
    """
    prints battleship board
                    
    Args:
        board (list): list that makes up spots on battleship board
    Returns:
        print: board in format of battleship board                   
    """
    print(f"""
    {"".join(board[0])}
    {"".join(board[1])}
    {"".join(board[2])}
    {"".join(board[3])}
    {"".join(board[4])}""")


def init_board():
    """
    turns board blank
                    
    Args:
        none
    Returns:
        blank board                   
    """
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
        board(list): board being changed
        symbol(str): emoji to be added to the board
        hit_or_pick(str): whether the user is picking a spot for ship or trying to hit a ship      
    Returns:
        row(int): row of symbol being added
        col(int): column of symbol being added                  
    """
    print_board(board)
    print(f"Time to pick a spot to {hit_or_pick}!")

    while True:
        col = get_integer("column")
        row = get_integer("row")
    
        if board[row][col] != "🟦":                                              #only take space if its blank
            print("That space is taken. Choose another!")
            continue

        board[row][col] = symbol
        return row, col


def take_shot(play, spots, player, hits, bot_or_player):
    """
    takes shot and says if player hits
                            
    Args:
        play(lst): the display board of the player
        spots(lst): where the players ships are
        player(str): name of player
        hits(int): number of time player has hit an enemy ship
        bot_or_player(str): if it is a bot or player     
    Returns:
        hits(int): number of time player has hit an enemy ship                  
    """
    print(f"{player}, choose where to hit")

    if bot_or_player == "player":
        row, col = get_player_move(play, "🌊", "hit")
    else:
        while True:
            row = random.randint(0, 4)
            col = random.randint(0, 4)
        
            if play[row][col] == "🟦":
                break

        print("Robot shooting shot...")
        time.sleep(2)

    if spots[row][col] != "🟦":
        play[row][col] = "💥"
        hits += 1
        print(f"{player} got a hit!")
    else:
        print(f"{player} missed!")
        play[row][col] = "🌊"

    print(f"{player} shots:")
    print_board(play)
    return hits


def winner(player, hits):
    """
    if the player has hist four ships and won
                        
    Args:
        player(str): name of player
        hits(int): number of time player has hit an enemy ship   
    Returns:
        True: if player one won
        False: if no one won                 
    """
    if hits == 4:
        print(f"Congrats {player} on winning!")
        return True
    return False


def gameplay(p_one_play, p_two_play, p_one_spots, p_two_spots, p_one, p_two, p_one_hits, p_two_hits, against_player):
    """
    series of taking shots, displaying, board, and checking winner in game
                            
    Args:
        p_one_play(lst): display board of first player
        p_two_play(lst): display board of second player
        p_one_spots(lst): ships of first player
        p_two_spots(lst): ships of second player
        p_one(str): name of player
        p_two(str): name of player
        p_one_hits(int): hits of the first player
        p_two_hits(int): hits of the second player
        against_player(Boolean): true for if agaisnt a player, false if against a robot    
    Returns:
        none                  
    """
    while True:
        p_one_hits = take_shot(p_one_play, p_two_spots, p_one, p_one_hits, "player")

        if winner(p_one, p_one_hits):
            break

        if against_player:
            p_two_hits = take_shot(p_two_play, p_one_spots, p_two, p_two_hits, "player")

            if winner(p_two, p_two_hits):
                break
        else:
            p_two_hits = take_shot(p_two_play, p_one_spots, p_two, p_two_hits, "bot")
            print("The damage on your board:")
            print_board(p_two_play)
                
            if winner(p_two, p_two_hits):
                break
    return


def two_player(player_one_spots, player_two_spots, player_one_play, player_two_play):
    """
    playing of two player battleships
                        
    Args:
        player_one_spots(lst): ships of first player
        player_two_spots(lst): ships of the second player
        player_one_play(lst): display board of first player
        player_two_play(lst): display board of second player
    Returns:
        none              
    """
    print("Player 1, Place your 4 ships please. Hide the screen from player 2.")
    
    for i in range(4):
        get_player_move(player_one_spots, "🚢", "pick")
    print_board(player_one_spots)

    time.sleep(2)
    os.system("cls")
    print("Please give the screen to player 2.")
    time.sleep(2)
    print("Player 2, Place your 4 ships please. Hide the screen from player 1.")
    for i in range(4):
        get_player_move(player_two_spots, "🚢", "pick")
    print_board(player_two_spots)

    time.sleep(2)
    os.system("cls")

    player_one_hits = 0
    player_two_hits = 0
    print("Begin!")

    gameplay(player_one_play, player_two_play, player_one_spots, player_two_spots, "Player 1", "Player 2", player_one_hits, player_two_hits, True)


def robot_player(player_one_spots, robot_spots, player_one_play, robot_play):
    """
    playing of battleships against a robot
                        
    Args:
        player_one_spots(lst): ships of first player
        robot_spots(lst): ships of the robot
        player_one_play(lst): display board of first player
        robot_play(lst): display board of robot
    Returns:
        none              
    """
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

    player_one_hits = 0
    robot_hits = 0
    print("Begin!")

    gameplay(player_one_play, robot_play, player_one_spots, robot_spots, "Player 1", "Robot", player_one_hits, robot_hits, False)




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
            player_one_spots = init_board()
            player_two_spots = init_board()
            player_one_play = init_board()
            player_two_play = init_board()
            two_player(player_one_spots, player_two_spots, player_one_play, player_two_play)
        elif play == "2":
            player_one_spots = init_board()
            robot_spots = init_board()
            player_one_play = init_board()
            robot_play = init_board()
            robot_player(player_one_spots, robot_spots, player_one_play, robot_play)
        elif play == "3":
            exit()
        else:
            print('Invalid')

main()