color = "red"

while True:
    guess = input('Enter your color giess: ')

    if color == guess:
        print('you got it')
        break
    else:
        print('try again')