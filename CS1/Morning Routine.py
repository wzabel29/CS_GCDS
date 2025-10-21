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
