import random
import time

random_int = random.randint(1, 100)
guesses = 5

while guesses > 0:
    number = int(input('Guess a number 1-100'))

    if number > random_int:
        print(f"number to high! Try again. {guesses-1} guesses left.")
    elif number < random_int:
        print(f"number to low! Try again. {guesses-1} guesses left.")
    elif number == random_int:
        print("You won!")
        break
    guesses -= 1

print("number was")
time.sleep(1)
print(random_int)