import time
print ("Alarm!")

while True:
    snooze = input("Yes or No, Would you like to snooze?").lower()

    if snooze == "yes":
        print("Go back to sleep")
    elif snooze == "no":
        print("wake up!")
        break
    else:
        print("Please enter yes or no")

while True:
    phone = input("Yes or no, Look at phone?").lower()

    if phone == "yes":
        print("stay in bed for 15 min")
        time.sleep(2)
        print('get out of bed')
        break
    else:
        print('get out of bed')
        break
while True:
    guess = input("Yes or no, go downstairs?").lower()

    if guess == "yes":
        print("Eat Breakfast")
        break
    else:
        print("Go to Bathroom")
        print("Eat Breakfast")
        break
while True:
    guess = input("Waffles or Pancakes?").lower()
    
    if guess == "Waffles":
        print('Eat Waffles')
        break
    elif guess == "Pancakes":
        print('Eat Pancakes')
        break
print('Shower')
print('Get dressed')
while True:
    guess = input("Yes or no, Is it cold outside").lower()
    if guess == "yes":
        print("wear pants")
        break
    else:
        print("wear shorts")
        break
while True:
    guess = input("Yes or no, Is it cold enough to wear a sweatshirt?").lower()
    if guess == "yes":
        print("Wear sweatshirt")
        break
    else:
        print("Don't wear a sweatshirt")
        break
print("pack back")
print("drive to school")
print("Arrive at school")