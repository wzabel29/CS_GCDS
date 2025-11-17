import random                                                                   #import
import time                                                                     #import

choices = ['rock', 'paper', 'scissors']                                         #choices list
bot_score = 0                                                                   #set computer score to 0
person_score = 0                                                                #set person score to 0

while True:                                                                     #forever loop
    if person_score == 2:                                                       #if person score = 2 do this
        print('you win! Congrats.')                                             #display
        break                                                                   #break loop
    elif bot_score == 2:                                                        #if computer score = 2 do this
        print('you lose. Good luck next time.')                                 #display
        break                                                                   #break loop
    else:                                                                       #else
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
        elif user_choice != 'rock' or 'paper' or 'scissors':
            print('please enter rock, paper, or scissors')