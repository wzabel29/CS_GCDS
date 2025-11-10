import random

responses = ['According to my sources, yes', 'Never', 'Most likely', 'yes', 'of course', 'signs point to yes', 'probobaly no', 'probably not', 'ask again', 'IDK, so ask again']
#question_words = []

while True:
    question = input('What would you like to know? ')
    #first_word = figure out how to identify the first word in a string 

    if question : #if there is a "?" in question or first_word is in question_words
        print(random.choice(responses))
    else:
        print('ASK A QUESTION!')