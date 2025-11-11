import random

colors = {                  
        'black': '\033[30m',   
        'red': '\033[31m',      
        'green': '\033[32m',    
        'yellow': '\033[33m',  
        'blue': '\033[34m',     
        'magenta': '\033[35m',  
        'cyan': '\033[36m',     
        'white': '\033[37m',    
        'reset': '\033[0m',     
        }

responses = [f'{colors["green"]}According to my sources, yes', f'{colors["red"]}Never', f'{colors["green"]}Most likely', f'{colors["green"]}yes', f'{colors["green"]}of course', f'{colors["green"]}signs point to yes', f'{colors["red"]}probobaly no', f'{colors["red"]}probably not', 'ask again', 'IDK, so ask again']
question_words = ['will', 'is', 'can', 'does', 'should']

while True:
    question = input('What would you like to know? ').lower()

    if question == '':
        print('Please enter something')
        continue
    first_word = question.split()[0]

    if '?' in question or first_word in question_words:
        print(random.choice(responses)+'\033[0m')
    else:
        print(f'{colors["red"]}ASK A QUESTION!'+'\033[0m')