import random
import csv

def secure_password(length):
    """
    creates random password for user
    Args:
        length (int) length user wants for password
    Returns:
        new_password (str) new created password with user length
    """
    characters_list = [
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    
    "!", "#", "$", "%", "&", "*", "+", "-", ":", ";", "@", "^", 
    "_"
]
    new_password = ""

    for i in range(length):
        new_password += random.choice(characters_list)                  #adds character to list
    return new_password                                                 #returns new password


def is_integer(num_int):
    """
    sees if user prompt is int
    Args:
        num_int(str): user prompt
    Returns:
        boolean based if user prompt is int
    Raises:
        ValueError if user prompt not int
    """
    try:                                                                #tries to convert to int
        int(num_int)
        return True                                                     #returns true
    except ValueError:                                                  #if error
        return False                                                    #return false


def get_integer():
    """
    gets an int from user
    Args:
        none
    Returns:
        num(int): int from user
    """
    while True:
        num = input("enter a number over 8 and under 20: ")

        if is_integer(num):                                             #runs int function
            return int(num)                                             #returns int
        else:
            print("please enter an integer over 8 and under 20")


def secure_password_checker():
    """
    checks how complex a password is
    Args:
        none
    Return:
        suggestion (str): complex password
    """
    uppercase = "QWERTYUIOPASDFGHJKLZXCVBNM"
    number = "1234567890"
    while True:
        uppers = 0
        numbers = 0
        suggestion = input("Please enter a password with: \n 1) an uppercase letter \n 2) a number \n 3) more than 8 characters \n Enter here: ")
        for character in suggestion:
            if character in uppercase:
                uppers += 1                                         #adds 1 to upper cases
            elif character in number:  
                numbers += 1                                        #adds 1 to numbers
        if len(suggestion) > 8 and uppers > 0 and numbers > 0:      #if the length is over 8, has an uppercase and there are numbers
            return suggestion                                       #return
        else:
            print("please meet the requirements")


def password_changer(apps, passwords):
    """
    changes password for user
    Args:
        apps (list): the app the user is creating a password for
        passwords (list): the password for the username for the app the user chose
    Return:
        passwords (list): new password in passwords list
    """
    changing_app = input("What app do you want to change your password")

    if changing_app in apps:                                        #if app in app list
        idx = apps.index(changing_app)                              #index = index of app in list
        secure = input("would you like a secure password (y/n): ").lower()

        if secure == "n":
            new_password = secure_password_checker()                #runs secure password checker func
        elif secure == "y": 
            new_password = secure_password(get_integer())           #creates secure password
        passwords[idx] = new_password                               #replaces with new password
    else:
        print("please enter an app you already have added")


def username_changer(apps, usernames):
    """
    changes username for user
    Args:
        apps (list): the app the user is creating a password for
        usernames (list): the unsernames for the passwrod for the app the user chose
    Return:
        usernames (list): new username in usernames list
    """
    changing_app = input("What app do you want to change your username")

    if changing_app in apps:
        idx = apps.index(changing_app)                              #index = index of app in list
        new_username = input("what would you like your username to be")
        usernames[idx] = new_username                               #username = new username
    else:
        print("please enter an app you already have added")


def password_adder(apps, usernames, passwords):
    """
    Prompt the user to enter apps and their usernames and passwords to store in the parallel arrays above
    Args:
        apps (list): the app the user is creating a password for
        usernames (list): the username of the user for the app
        passwords (list): the password for the username for the app the user chose
    Return:
        apps (list): new apps list after user added their app
        usernames (list): new usernames list after user added their username
        passwords (list): new passwords list after user added their password
    """
    app = input("what app would you like to create a password for: ")
    username = input("what username would you like for the app: ")
    secure = input("would you like a secure password (y/n): ").lower()

    if secure == "y":
        password = secure_password(get_integer())                 #create secure password
    else:
        password = secure_password_checker()                      #runs secure password checker
    apps.append(app)                                              #add to list
    usernames.append(username)                                    #add to list
    passwords.append(password)                                    #add to list


def print_passwords(apps, usernames, passwords):
    """
    prints the current apps, usernames, and passwords vertically
    Args:
        apps (list): the app the user is creating a password for
        usernames (list): the username of the user for the app
        passwords (list): the password for the username for the app the user chose
    Print:
        the current apps, usernames, and passwords vertically
    """
    for i in range(len(apps)):                                  #for each app in list
        print(f"app: {apps[i]}, username: {usernames[i]}, password: {passwords[i]}") #siplay app with index, username with same index, and password with same index


def get_passwords(apps, usernames, passwords):
    """
    allows user to enter a app and get the username and password for it
    Args:
        apps (list): the app the user is creating a password for
        usernames (list): the username of the user for the app
        passwords (list): the password for the username for the app the user chose
    Print:
        the app with username and password
    """
    print("Here are the apps you can get a username and passsword from:")

    for i in range(len(apps)):                                #runs through list and displays apps
        print(f"{i+1}: {apps[i]}")

    choice = input("which app would you like to get the username and password: ").lower()

    for i in range(len(apps)):
        if choice == apps[i]:                                 #if app is the same
            print(f"app: {apps[i]}, username: {usernames[i]}, password: {passwords[i]}") #print
            return
    print(f'{choice} is not here.')                         
     

def excel_exporter(apps, usernames, passwords, filename):
    """
    exports apps, usernames, and passwords to excel spreadsheet
    Args:
        apps (list): the app the user is creating a password for
        usernames (list): the username of the user for the app
        passwords (list): the password for the username for the app the user chose
        filename (variable): the filename of the csv file
    Return:
        filename (arg:csv file): excel spreadsheet of apps, usernames, and passwords of user
    """
    data = zip(apps, usernames, passwords)                  #data = to all lists

    with open(filename, 'w', newline='') as f:              #open as csv with filename
        writer = csv.writer(f)
        writer.writerow(['App', 'Username', 'Password'])
        writer.writerows(data)
    print(f'Data saved to {filename}')


def main():
    """
    menu for what user would like to do
    """
    apps = []
    usernames = []
    passwords = []

    options = """here is what you can do:
1) add an app, its username, and password
2) display all your apps with their username and password
3) display a specific apps username and password
4) change password for an app
5) change username for an app
6) exports apps, usernames, and passwords into an excel spreadsheet
    """
    print(options)
    tries = 3
    master_password = "passwordkeeper11"

    while tries > 0:
        user_password = input("Enter the master password to begin")

        if user_password == master_password:
            break
        else:
            tries -= 1
            print(f"You have {tries} tries left")

    while True:
        number = input("Enter the number of the task you would like to do (Press 'q' to quit or 'o' to see options): ").strip()

        if number.lower() == "q":
            break
        elif number.lower() == "o":
            print(options)
        elif number == "1":
            password_adder(apps, usernames, passwords)          #runs password adder
        elif number == "2":
            print_passwords(apps, usernames, passwords)         #runs print password
        elif number == "3":                        
            get_passwords(apps, usernames, passwords)           #runs get password
        elif number == "4":
            password_changer(apps, passwords)                   #runs password changer
        elif number == "5":
            username_changer(apps, usernames)                   #runs username changer
        elif number == "6":
            filename = input('Enter desired file name (include .csv): ')
            excel_exporter(apps, usernames, passwords, filename)#runs excel exporter
        else:
            print("Please enter a number from 1-6")


main()                                                          #runs main function