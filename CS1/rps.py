import random
import time

choices = ['rock', 'paper', 'scissors']
bot_score = 0
person_score = 0

while True:
    if person_score == 2:
        print('you win! Congrats.')
        break
    elif bot_score == 2:
        print('you lose. Good luck next time.')
        break
    else:
        user_choice = input('Enter rock, paper, or scissors...').lower()
        bot_choice = random.choice(choices)
        print(f'your choice was... {user_choice}')
        print(f'computer choice is... {bot_choice}')
        
        if user_choice == bot_choice:
            print('You tied. Go again.')
            time.sleep(1)
            print(f'Your score is... {person_score}.')
            time.sleep(1)
            print(f'Computer score is... {bot_score}.')
            time.sleep(1)
            continue
        elif user_choice == 'rock' and bot_choice == 'paper':
            print('You lose  :(')
            bot_score += 1
            time.sleep(1)
            print(f'Your score is... {person_score}.')
            time.sleep(1)
            print(f'Computer score is... {bot_score}.')
            time.sleep(1)
        elif user_choice == 'rock' and bot_choice == 'scissors':
            print('You win!')
            person_score += 1
            time.sleep(1)
            print(f'Your score is... {person_score}.')
            time.sleep(1)
            print(f'Computer score is... {bot_score}.')
            time.sleep(1)
        elif user_choice == 'paper' and bot_choice == 'rock':
            print('You win!')
            person_score += 1
            time.sleep(1)
            print(f'Your score is... {person_score}.')
            time.sleep(1)
            print(f'Computer score is... {bot_score}.')
            time.sleep(1)
        elif user_choice == 'paper' and bot_choice == 'scissors':
            print('You lose  :(')
            bot_score += 1
            time.sleep(1)
            print(f'Your score is... {person_score}.')
            time.sleep(1)
            print(f'Computer score is... {bot_score}.')
            time.sleep(1)
        elif user_choice == 'scissors' and bot_choice == 'paper':
            print('You win!')
            person_score += 1
            time.sleep(1)
            print(f'Your score is... {person_score}.')
            time.sleep(1)
            print(f'Computer score is... {bot_score}.')
            time.sleep(1)
        elif user_choice == 'scissors' and bot_choice == 'rock':
            print('You lose  :(')
            bot_score += 1
            time.sleep(1)
            print(f'Your score is... {person_score}.')
            time.sleep(1)
            print(f'Computer score is... {bot_score}.')
            time.sleep(1)