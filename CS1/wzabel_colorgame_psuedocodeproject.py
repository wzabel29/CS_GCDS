import random

def print_colortext(text, color_name):
    colors_dictionary = {       # Dictionary mapping color names to their ANSI escape codes for terminal text coloring
        'black': '\033[30m',    # Black text color
        'red': '\033[31m',      # Red text color
        'green': '\033[32m',    # Green text color
        'yellow': '\033[33m',   # Yellow text color
        'blue': '\033[34m',     # Blue text color
        'magenta': '\033[35m',  # Magenta (purple) text color
        'cyan': '\033[36m',     # Cyan text color
        'white': '\033[37m',    # White text color
        'reset': '\033[0m',     # Reset text color to default
    }

    color_code = colors_dictionary.get(color_name.lower(), '\033[37m')
    print(f'{color_code}{text}\033[0m')

name = input('What is your name?')
print(f'Hello {name}. The goal of the game is to enter the color the text is written in.')

color_list = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan']
rounds = 0
correct = 0

while True:
    text_color = random.choice(color_list)
    text_print = random.choice(color_list)

    print_colortext(text_color, text_print)

    guess = input('What color is the text?').lower()

    if guess == text_print:
        print('CORRECT!')
        correct += 1
    else:
        print('incorrect')
    rounds += 1
    print(f'You have completed {rounds} rounds and have got {correct} correct.')

    again = input('please enter yes if you would like to play again.').lower()

    if again == 'yes':
        continue
    else:
        exit()