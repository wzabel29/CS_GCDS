print ("Alarm!")
while True:
    guess = input("Yes or No, Would you like to snooze?").lower()
    if guess == "yes":
        print("Go back to sleep")
    else:
        print("wake up!")
        break
while True:
    guess = input("Yes or no, Look at phone?").lower()
    if guess == "yes":
        print("stay in bed")
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
    guess = input("Waffles or Pancakes?")
    if guess == "Waffles":
        print('Eat Waffles')
        break
    else:
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
print("pack back")
print("drive to school")
print("Arrive at school")