""""
┌───────────────────────────────────────────────────────────────────────────┐
│                            What's in a Name                               │
├───────────────────────────────────────────────────────────────────────────┤
│ Name: Wyatt Zabel                                                         │
| Course: CS2                                                               |
│ Log: Finished project (1.0)                                               |
| Bugs: N/K                                                                 │
│ Description:  A two-body gravitational simulation written in Python.      |
| The system models a binary star system interacting solely                 |
| under Newtons Law of Universal Gravitation.                               |
└───────────────────────────────────────────────────────────────────────────┘
"""

import random

def reverse_display():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    letters_reverse = letters[::-1]
    print(letters_reverse)


def count_vowels(user_string):
    vowels = {"a":0, "e":0, "i":0, "o":0, "u":0}

    for vow in user_string:
        if vow in vowels.keys():
            vowels[vow] += 1
    total_vowels = sum(vowels.values())
    for key, value in vowels.items():
        print(f'{key}: {value}')
    return vowels, total_vowels


def count_consonant(user_string):
    consonants = {"b":0, "c":0, "d":0, "f":0, "g":0, "h":0, "j":0, "k":0, "l":0, "m":0, "n":0, "p":0, "q":0, "r":0, "s":0, "t":0, "v":0, "w":0, "x":0, "y":0, "z":0}
    "bcdfghjklmnpqrstvwxyz"

    for con in user_string:
        if con in consonants.keys():
            consonants[con] += 1
    total_vowels = sum(consonants.values())
    for key, value in consonants.items():
        print(f'{key}: {value}')
    return consonants, total_vowels


def get_names(name):
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
    names = get_names(name)
    return names[0]


def middle_name(name):
    names = get_names(name)
    middle_names = names[1:len(names)-1]
    name = ''

    for n in middle_names:
        name += n
        return name


def last_name(name):
    names = get_names(name)
    return names[-1]


def hyphen_name(names): 
    return "-" in last_name(names)


def lowercase(user_string):
    lower = ""
    low = ""

    for char in user_string:
        if 65 <= ord(char) <= 90:
            low += chr(ord(char)+32)
        else:
            low += char

    lower += low
    return lower


def uppercase(user_string):
    upper = ''
    upp = ""
    
    for char in user_string:
        if 97 <= ord(char) <= 122:
            upp += chr(ord(char)-32)
        else:
            upp += char
    
    upper += upp
    return upper


def mixer(user_string):
    shuffle_l = list(user_string)

    for i in range(len(shuffle_l)):
        rand_i = random.randint(0, len(shuffle_l) - 1)
        shuffle_l[i], shuffle_l[rand_i] = shuffle_l[rand_i], shuffle_l[i]

    new_string = ''

    for char in shuffle_l:
        new_string += char
    return new_string


def palindrome(user_string):
    return user_string == user_string[::-1]


def initials(name):
    names = get_names(name)
    return uppercase(f"{names[0][0]},{names[-1][0]}")


def contains_title(name):
    titles_l = ["Dr", "Mr", "Ms", "Mrs", "Ph.d", "Sir"]

    for n in get_names(name):
        if n in titles_l:
            return True
    return False

print(contains_title(input("")))