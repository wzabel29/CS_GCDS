import random

choices = ['rock', 'paper', 'scissors']

while True:
    user_choice = input('Enter rock, paper, or scissors...').lower()
    bot_choice = random.choice(choices)
    print(f'your choice was... {user_choice}')
    print(f'computer choice is... {bot_choice}')
    
    if user_choice == bot_choice:
        print('' \
        'You tied. Go again.')
        continue
    elif user_choice == 'rock' and bot_choice == 'paper':
        print('' \
        'You lose  :(')
    elif user_choice == 'rock' and bot_choice == 'scissors':
        print('You win!')
    elif user_choice == 'paper' and bot_choice == 'rock':
        print('You win!')
    elif user_choice == 'paper' and bot_choice == 'scissors':
        print('You lose  :(')
    elif user_choice == 'scissors' and bot_choice == 'paper':
        print('You win!')
    elif user_choice == 'scissors' and bot_choice == 'rock':
        print('You lose  :(')