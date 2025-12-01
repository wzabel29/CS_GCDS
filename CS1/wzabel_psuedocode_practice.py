import random

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'cyan', 'magenta']

color_1 = random.choice(colors)

attempts = 0

while attempts <= 3:
    prompt = input('enter a color... ').lower()
    if prompt == color_1:
        print(f'You got it in {attempts + 1} attempts!')
        exit()
    else:
        attempts += 1
        print(f'You did not get it...{attempts}/4 attempts used')

print('You have lost')

