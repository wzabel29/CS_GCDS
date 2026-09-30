""""
┌───────────────────────────────────────────────────────────────────────────┐
│                            What's in a Name                               │
├───────────────────────────────────────────────────────────────────────────┤
│ Name: Wyatt Zabel                                                         │
| Course: CS2                                                               |
│ Log: Finished project (1.0)                                               |
| Bugs: N/K                                                                 │
│ Description:  Functions without using the helper class.                   |
| a set of methods to manipulate and interrogate an array of characters.    |
└───────────────────────────────────────────────────────────────────────────┘
"""

import random

def reverse_display():
    """Reverses the alphabet

    Args:
        n/a

    Prints:
        letters_reverse(list): reverse alphabet

    """
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    letters_reverse = letters[::-1]
    print(letters_reverse)


def count_vowels(user_string):
    """Counts the amount of each vowel in a string

    Args:
        user_string (str): The user inputed string

    Returns:
        vowels(dict): The dictionary of the count of each vowel
        total_vowels(int): The total amount of vowels

    """
    vowels = {"a":0, "e":0, "i":0, "o":0, "u":0}

    for vow in user_string:
        if vow in vowels.keys():
            vowels[vow] += 1
    total_vowels = sum(vowels.values())
    for key, value in vowels.items():
        print(f'{key}: {value}')
    return vowels, total_vowels


def count_consonant(user_string):
    """Counts the amount of each consonant in a string
    
        Args:
            user_string (str): The user inputed string
    
        Returns:
            consonants(dict): The dictionary of the count of each consonant
            total_consonants(int): The total amount of consonants
    
        """
    consonants = {"b":0, "c":0, "d":0, "f":0, "g":0, "h":0, "j":0, "k":0, "l":0, "m":0, "n":0, "p":0, "q":0, "r":0, "s":0, "t":0, "v":0, "w":0, "x":0, "y":0, "z":0}
    "bcdfghjklmnpqrstvwxyz"

    for con in user_string:
        if con in consonants.keys():
            consonants[con] += 1
    total_consonants = sum(consonants.values())
    for key, value in consonants.items():
        print(f'{key}: {value}')
    return consonants, total_consonants


def get_names(name):
    """Takes a name and turns it into indivisual list indexes
    
        Args:
            user_string (str): The user inputed string
    
        Returns:
            names(list): A name seprated into list indexes
    
        """
    names = []
    current_name = ""

    for char in name:
        if char == " ":
            names.append(current_name)
            current_name = ""
        else:
            current_name += char
    names.append(current_name)
    return names


def first_name(name):
    """returns the first name in a list
    
        Args:
            name(str): The user inputed name
    
        Returns:
            names[0](index): The first index in the names list
    
    """
    names = get_names(name)
    return names[0]


def middle_name(name):
    """returns the middle name/s in a list
        
        Args:
            name(str): The user inputed name
        
        Returns:
            name(str): The middle names
        
    """
    names = get_names(name)
    middle_names = names[1:len(names)-1]
    name = ''

    for n in middle_names:
        name += n
        return name


def last_name(name):
    """returns the last name in a list
            
        Args:
            name(str): The user inputed name
            
        Returns:
            name(str): The last name
            
    """
    names = get_names(name)
    return names[-1]


def hyphen_name(names): 
    """returns boolean if hyphen in name
            
        Args:
            names(str): The user inputed name
            
        Returns:
            boolean
            
    """
    return "-" in last_name(names)


def lowercase(user_string):
    """makes all characters in a string lowercase
                
        Args:
            user_string (str): The user inputed string
                
        Returns:
            lower(str): The string in all lowercase
                
    """
    lower = ""
    low = ""

    for char in user_string:
        if 65 <= ord(char) <= 90:                                           #ord is ascii value 
            low += chr(ord(char)+32)
        else:
            low += char

    lower += low
    return lower


def uppercase(user_string):
    """makes all characters in a string uppercase
                    
        Args:
            user_string (str): The user inputed string
                
        Returns:
            upper(str): The string in all uppercase
                    
        """
    upper = ''
    upp = ""
    
    for char in user_string:
        if 97 <= ord(char) <= 122:                                          #ord is ascii value 
            upp += chr(ord(char)-32)                                    
        else:
            upp += char
    
    upper += upp
    return upper


def mixer(user_string):
    """randomly mixes characters in a string
                
    Args:
        user_string(str): The user inputed string
                
    Returns:
        new_string(str): The mixed string
                
    """
    shuffle_l = list(user_string)

    for i in range(len(shuffle_l)):
        rand_i = random.randint(0, len(shuffle_l) - 1)
        shuffle_l[i], shuffle_l[rand_i] = shuffle_l[rand_i], shuffle_l[i]   #chnages index of list indexis

    new_string = ''

    for char in shuffle_l:
        new_string += char
    return new_string


def palindrome(name):
    """returns boolean if palindrome
                
        Args:
            name(str): The user inputed name
                
        Returns:
            boolean
                
        """
    return first_name(name) == first_name(name)[::-1]


def initials(name):
    """returns initials of a name
                
        Args:
            name(str): The user inputed name
                
        Returns:
            f string(str): The initials in uppercase
                
        """
    names = get_names(name)
    return uppercase(f"{names[0][0]},{names[-1][0]}")                   #first index first character


def contains_title(name):
    """returns boolean if name contains title
                
        Args:
            names(str): The user inputed name
                
        Returns:
            boolean
                
        """
    titles_l = ["Dr", "Mr", "Ms", "Mrs", "Ph.d", "Sir"]

    for n in get_names(name):
        if n in titles_l:
            return True
    return False


def main():
    """
    menu for what user would like to do
    """

    options = """here is what you can do:
1. Reverse and display list
2. Determine the number of vowels
3. Consonant frequency
4. Return first name
5. Return last name
6. Return middle name(s)
7. Return boolean if last name contains a hyphen
8. Function to convert to lowercase
9. Function to convert to uppercase
10. Modify array to create a random name (mix up letters)
11. Return boolean if first name is a palindrome
12. Make initials from name
13. Return boolean if name contains a title/distinction
    """

    while True:
        number = input("Enter the number of the task you would like to do (Press 'q' to quit or 'o' to see options): ").strip()

        if number.lower() == "q":
            break
        elif number.lower() == "o":
            print(options)
        elif number == "1":
            reverse_display()
        elif number == "2":
            print(count_vowels(input("Enter a phrase: ")))
        elif number == "3":                        
            print(count_consonant(input("Enter a phrase: ")))
        elif number == "4":
            print(first_name(input("Enetr a name: ")))
        elif number == "5":
            print(last_name(input("Enetr a name: ")))
        elif number == "6":
            print(middle_name(input("Enetr a name: ")))
        elif number == "7":
            print(hyphen_name(input("Enetr a name: ")))
        elif number == "8": 
            print(lowercase(input("Enter a phrase: ")))
        elif number == "9":
            print(uppercase(input("Enter a phrase: ")))
        elif number == "10":
            print(mixer(input("Enter a phrase: ")))
        elif number == "11":
            print(palindrome(input("Enetr a name: ")))
        elif number == "12":
            print(initials(input("Enetr a name: ")))
        elif number == "13":
            print(contains_title(input("Enetr a name: ")))
        else:
            print("Please enter a number from 1-13")


main()