import random

random_int = random.randint(1, 1000)
guesses = 5

while guesses > 0:
    number = int(input('Guess a number 1-1000'))

    if number > random_int:
        print(f"number to high! Try again. {guesses-1} guesses left.")
    elif number < random_int:
        print(f"number to low! Try again. {guesses-1} guesses left.")
    elif number == random_int:
        print("You won!")
        break
    guesses -= 1

print("number was {random_int}")