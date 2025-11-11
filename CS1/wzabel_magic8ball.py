import random                                                   #import                                                           

colors = {                                                      #color list
        'black': '\033[30m',                                    #black color
        'red': '\033[31m',                                      #red color
        'green': '\033[32m',                                    #green color
        'yellow': '\033[33m',                                   #yellow color
        'blue': '\033[34m',                                     #blue color
        'magenta': '\033[35m',                                  #magenta color
        'cyan': '\033[36m',                                     #cyan color
        'white': '\033[37m',                                    #white color
        'reset': '\033[0m',                                     #reset color
        }

responses = [f'{colors["green"]}According to my sources, yes', f'{colors["red"]}Never', f'{colors["green"]}Most likely', f'{colors["green"]}yes', f'{colors["green"]}of course', f'{colors["green"]}signs point to yes', f'{colors["red"]}probobaly no', f'{colors["red"]}probably not', 'ask again', 'IDK, so ask again']  #responses list
question_words = ['will', 'is', 'can', 'does', 'should','are']        #question words list

while True:                                                     #forever loop
    question = input('What would you like to know? ').lower()   #ask question

    if question == '':                                          #if user inputs nothing
        print('Please enter something')                         #display
        continue                                                #back to start
    first_word = question.split()[0]                            #set first word to first word in user input

    if '?' in question or first_word in question_words:         #if ? or first word is question word do this
        print(random.choice(responses)+'\033[0m')               #print random response and reset to nuetral after
    else:                                                       #else
        print(f'{colors["red"]}ASK A QUESTION!'+'\033[0m')      #display in red and reset to nuetral