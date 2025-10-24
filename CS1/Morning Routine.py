import time
import datetime
print ("Alarm!")

current_time = datetime.datetime(2025, 10, 24, 6, 30, 0) 
print(current_time.strftime("%H:%M:%S"), end='\r')

while True:
    snooze = input("Yes or No, Would you like to snooze?").lower()

    if snooze == "yes":
        print("Go back to sleep")
        time.sleep(2)
        current_time += datetime.timedelta(minutes=5)
    elif snooze == "no":
        print("wake up!")
        current_time += datetime.timedelta(minutes=1)
        break
    else:
        print("Please enter yes or no")

print(current_time.strftime("%H:%M:%S"))

while True:
    phone = input("Yes or no, Look at phone?").lower()

    if phone == "yes":
        print("stay in bed for 15 min")
        time.sleep(2)
        print('get out of bed')
        current_time += datetime.timedelta(minutes=15)
        break
    elif phone == "no":
        print('get out of bed')
        current_time += datetime.timedelta(minutes=1)
        break
    else:
        print("Please enter either yes or no")

print(current_time.strftime("%H:%M:%S"))

while True:
    downstairs = input("Yes or no, go downstairs?").lower()

    if downstairs == "yes":
        print("Eat Breakfast")
        break
    elif downstairs == "no":
        print("Go to Bathroom")
        current_time += datetime.timedelta(minutes=1)
        time.sleep(1)
        print("Eat Breakfast")
        break
    else:
        print("Please enter either yes or no")

print(current_time.strftime("%H:%M:%S"))

while True:
    breakfast_choice = input("Waffles or Pancakes?").lower()

    if breakfast_choice == "Waffles":
        print('Eat Waffles')
        current_time += datetime.timedelta(minutes=10)
        break
    elif breakfast_choice == "Pancakes":
        print('Eat Pancakes')
        current_time += datetime.timedelta(minutes=10)
        break
    else:
        print("Please enter either Pancakes or Waffles")

print(current_time.strftime("%H:%M:%S"))

print('Shower')
current_time += datetime.timedelta(minutes=10)
print(current_time.strftime("%H:%M:%S"))
time.sleep(1)
print('Get dressed')
current_time += datetime.timedelta(minutes=10)
print(current_time.strftime("%H:%M:%S"))

while True:
    temp = input("Yes or no, Is it cold outside").lower()

    if temp == "yes":
        print("wear pants")
        current_time += datetime.timedelta(minutes=1)
        break
    elif temp == "no":
        print("wear shorts")
        current_time += datetime.timedelta(minutes=1)
        break
    else:
        print("Please enter either yes or no")

print(current_time.strftime("%H:%M:%S"))

while True:
    sweatshirt = input("Yes or no, Is it cold enough to wear a sweatshirt?").lower()

    if sweatshirt == "yes":
        print("Wear sweatshirt")
        current_time += datetime.timedelta(minutes=1)
        break
    elif sweatshirt == "no":
        print("Don't wear a sweatshirt")
        current_time += datetime.timedelta(minutes=1)
        break
    else:
        print("Please enter either yes or no")

print(current_time.strftime("%H:%M:%S"))

print("pack back")
current_time += datetime.timedelta(minutes=1)
print(current_time.strftime("%H:%M:%S"))
time.sleep(1)
print("drive to school")
current_time += datetime.timedelta(minutes=10)
time.sleep(1)
print("Arrive at school")
print(current_time.strftime("%H:%M:%S"))