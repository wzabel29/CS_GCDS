import random                                                               #import
import time                                                                 #import

choices = ['rock', 'paper', 'scissors']                                     #choices list
bot_score = 0                                                               #set computer score to 0
person_score = 0                                                            #set person score to 0

while person_score < 2 and bot_score < 2:                                   #loop goes on untilperson score and bot score are above 1
    user_choice = input('Enter rock, paper, or scissors...').lower()        #set user choice to input in lower case
    
    if user_choice not in choices:                                          #if user does not enter rock, paper, or scissors do this
        print('please enter rock, paper, or scissors.')                     #display
        continue                                                            #goes back to start of loop
    bot_choice = random.choice(choices)                                     #bot choice is random from choices list
    print(f'your choice was... {user_choice}')                              #display
    print(f'computer choice is... {bot_choice}')                            #display
    
    if user_choice == bot_choice:                                           #if user choice and bot choice are the same do this
        print('You tied. Go again.')                                        #display
        continue                                                            #goes back to start of loop
    elif user_choice == 'rock' and bot_choice == 'paper':                   #if user choice = rock and bot choice = paper do this
        print('You lose  :(')                                               #display
        bot_score += 1                                                      #add 1 to bot score
    elif user_choice == 'rock' and bot_choice == 'scissors':                #if user picks rock and bot scissors do this
        print('You win!')                                                   #display
        person_score += 1                                                   #add 1 to person score
    elif user_choice == 'paper' and bot_choice == 'rock':                   #if user picks paper and bot pick rock do this
        print('You win!')                                                   #dipslay
        person_score += 1                                                   #add 1 to person score
    elif user_choice == 'paper' and bot_choice == 'scissors':               #if user picks paper and bot picks scissors do this
        print('You lose  :(')                                               #display
        bot_score += 1                                                      #add one to bot score
    elif user_choice == 'scissors' and bot_choice == 'paper':               #if user picks scissors and bot picks paper do this
        print('You win!')                                                   #display
        person_score += 1                                                   #add 1 to person score
    elif user_choice == 'scissors' and bot_choice == 'rock':                #if user picks scissors and bot picks rock do this
        print('You lose  :(')                                               #display
        bot_score += 1                                                      #add 1 to bot score
        
    time.sleep(1)                                                           #pause 1 second
    print(f'Your score is... {person_score}.')                              #display
    time.sleep(1)                                                           #pause 1 seconds
    print(f'Computer score is... {bot_score}.')                             #display
    time.sleep(1)                                                           #pause 1 seconds

if person_score == 2:                                                       #if person score = 2 do this
    print('you win! Congrats.')                                             #display
else:                                                                       #else
    print('you lose. Good luck next time.')                                 #display