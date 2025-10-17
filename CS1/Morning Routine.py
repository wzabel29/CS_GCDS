print ("Alarm!")
while True:
    guess = input("Yes or No, Would you like to snooze?").lower()
    if guess == "yes":
        print("Go back to sleep")
    else:
        print("wake up!")
        break
