from tkinter import*
from tkinter.ttk import*

from time import strftime

root = Tk()
root.title("clock")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text = string)
    label.after(1000, time)

label = Label(root, font=(150), background = "cyan", foreground = "black")
label.pack(anchor = "center")
time()

mainloop()

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
    elif phone == "no":
        print('get out of bed')
        break
    else:
        print("Please enter either yes or no")

while True:
    downstairs = input("Yes or no, go downstairs?").lower()

    if downstairs == "yes":
        print("Eat Breakfast")
        break
    elif downstairs == "no":
        print("Go to Bathroom")
        time.sleep(1)
        print("Eat Breakfast")
        break
    else:
        print("Please enter either yes or no")

while True:
    breakfast_choice = input("Waffles or Pancakes?").lower()

    if breakfast_choice == "Waffles":
        print('Eat Waffles')
        break
    elif breakfast_choice == "Pancakes":
        print('Eat Pancakes')
        break
    else:
        print("Please enter either Pancakes or Waffles")

print('Shower')
time.sleep(1)
print('Get dressed')

while True:
    temp = input("Yes or no, Is it cold outside").lower()

    if temp == "yes":
        print("wear pants")
        break
    elif temp == "no":
        print("wear shorts")
        break
    else:
        print("Please enter either yes or no")

while True:
    sweatshirt = input("Yes or no, Is it cold enough to wear a sweatshirt?").lower()

    if sweatshirt == "yes":
        print("Wear sweatshirt")
        break
    elif sweatshirt == "no":
        print("Don't wear a sweatshirt")
        break
    else:
        print("Please enter either yes or no")

print("pack back")
time.sleep(1)
print("drive to school")
time.sleep(1)
print("Arrive at school")