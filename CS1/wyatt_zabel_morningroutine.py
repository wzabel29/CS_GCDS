import time
from datetime import datetime, timedelta
print ("Alarm!")                                                                    #disply

current_time = datetime(2025, 10, 24, 6, 30, 0)                                     #set current time (the date) to 10/24/1025 6:30
print(current_time.strftime("%H:%M:%S"), end='\r')                                  #display current time as hour minute second

while True:                                                                         #forever loop
    snooze = input("Yes or No, Would you like to snooze?").lower()                  #sets phrase snooze to users imput in lowercase

    if snooze == "yes":                                                             #if users input = yes do this
        print("Go back to sleep")                                                   #display
        time.sleep(2)                                                               #pause for 2 seconds
        current_time += timedelta(minutes=5)                                        #add 5 minutes to the current time string
    elif snooze == "no":                                                            #if user unput = no do this
        print("wake up!")                                                           #display
        current_time += timedelta(minutes=1)                                        #add 1 minute to the current time string
        break                                                                       #break loop
    else:                                                                           #if user input doe snot = yes or no do this
        print("Please enter yes or no")                                             #display

print(current_time.strftime("%H:%M:%S"))                                            #display current time string

while True:                                                                         #display forever loop
    phone = input("Yes or no, Look at phone?").lower()                              #set phrase phone to user input in lower case

    if phone == "yes":                                                              #if user input = yes do this
        print("stay in bed for 15 min")                                             #display
        time.sleep(2)                                                               #pause for 2 seconds
        print('get out of bed')                                                     #display
        current_time += timedelta(minutes=15)                                       #add 15 minutes onto the current time string
        break                                                                       #break loop
    elif phone == "no":                                                             #if user input = no do this
        print('get out of bed')                                                     #display
        current_time += timedelta(minutes=1)                                        #add 1 minute to time string
        break                                                                       #break loop
    else:                                                                           #if user input does not equal yes or no do this
        print("Please enter either yes or no")                                      #display

print(current_time.strftime("%H:%M:%S"))                                            #display time string

while True:                                                                         #forever loop
    downstairs = input("Yes or no, go downstairs?").lower()                         #set phrase downstairs to user input in lowrcase

    if downstairs == "yes":                                                         #if user input = yes do this
        print("Eat Breakfast")                                                      #display
        break                                                                       #break loop
    elif downstairs == "no":                                                        #if user input = no do this
        print("Go to Bathroom")                                                     #display
        current_time += timedelta(minutes=1)                                        #add 1 minute to current time string
        time.sleep(1)                                                               #pause for 1 second
        print("Eat Breakfast")                                                      #display
        break                                                                       #break loop
    else:                                                                           #if user input does not = yes or no do this
        print("Please enter either yes or no")                                      #display

print(current_time.strftime("%H:%M:%S"))                                            #display current time string

while True:                                                                         #forever loop
    breakfast_choice = input("Waffles or Pancakes?").lower()                        #phrase breakfast_choice = user input lowercase

    if breakfast_choice == "waffles":                                               #if user input = waffles do this
        print('Eat Waffles')                                                        #display
        current_time += timedelta(minutes=10)                                       #add 10 minutes to current time string
        break                                                                       #break loop
    elif breakfast_choice == "pancakes":                                            #if user input = pancakes do this
        print('Eat Pancakes')                                                       #display
        current_time += timedelta(minutes=10)                                       #add 10 minutes to current time string
        break                                                                       #break loop
    else:                                                                           #if user input does not = waffles or pancakes do this
        print("Please enter either Pancakes or Waffles")                            #display

print(current_time.strftime("%H:%M:%S"))                                            #display current time string

print('Shower')                                                                     #display
current_time += timedelta(minutes=10)                                               #add 10 minutes to current time string
print(current_time.strftime("%H:%M:%S"))                                            #print current time string
time.sleep(1)                                                                       #pause for 1 second
print('Get dressed')                                                                #display
current_time += timedelta(minutes=10)                                               #add 10 minutes to current time string
print(current_time.strftime("%H:%M:%S"))

while True:                                                                         #forever loop
    temp = input("Yes or no, Is it cold outside").lower()                           #phrase temp = user imput lowercase

    if temp == "yes":                                                               #if user input = yes do this
        print("wear pants")                                                         #display
        current_time += timedelta(minutes=1)                                        #add 1 minute to current time string
        break                                                                       #break loop
    elif temp == "no":                                                              #if user input = no do this
        print("wear shorts")                                                        #display
        current_time += timedelta(minutes=1)                                        #add 1 minute to current time string
        break                                                                       #break loop
    else:                                                                           #if user input does not = yes or no do this
        print("Please enter either yes or no")                                      #display

print(current_time.strftime("%H:%M:%S"))                                            #display current time string

while True:                                                                         #forever loop
    sweatshirt = input("Yes or no, Is it cold enough to wear a sweatshirt?").lower()#phrase sweatshirt = user input lowercase

    if sweatshirt == "yes":                                                         #if user input = yes do this
        print("Wear sweatshirt")                                                    #display
        current_time += timedelta(minutes=1)                                        #add 1 minute to current time string
        break                                                                       #break loop
    elif sweatshirt == "no":                                                        #if user input = no do this
        print("Don't wear a sweatshirt")                                            #display
        current_time += timedelta(minutes=1)                                        #add 1 minute to current time string
        break                                                                       #break loop
    else:                                                                           #if user input does not = yes or no do this
        print("Please enter either yes or no")                                      #display

print(current_time.strftime("%H:%M:%S"))                                            #display current time string

print("pack back")                                                                  #display
current_time += timedelta(minutes=1)                                                #add 1 minute to current time string
print(current_time.strftime("%H:%M:%S"))                                            #display current time string

time.sleep(1)                                                                       #pause for 1 second

print("drive to school")                                                            #display
current_time += timedelta(minutes=10)                                               #add 10 minutes to current time string

time.sleep(1)                                                                       #pause for 1 second

print("Arrive at school")                                                           #display
print(current_time.strftime("%H:%M:%S"))                                            #display current time string

check_time = datetime(2025, 10, 24, 8, 0, 0)                                        #set check time to time school starts

if current_time == check_time:                                                      #if current time string = time school starts dxo this
    print("you are on time")                                                        #display
elif current_time  > check_time:                                                    #if current time string is greater than time school starts do this
    print("you are late")                                                           #display
else:                                                                               #if current time string does not = time school starts or greater than time school starts do this
    print("you are early")                                                          #display