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
    vowels = "aeiou"
    vowel_count = 0

    for vow in user_string:
        if vow in vowels:
            vowel_count += 1
    return vowel_count


def count_consonant(user_string):
    consonant = "bcdfghjklmnpqrstvwxyz"
    consonant_count = 0

    for con in user_string:
        if con in consonant:
            consonant_count += 1
    return consonant_count

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
    lower = ''
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
    first_shuffle = user_string[::random.randint(-len(user_string)+1, 0) ]
    second_shuffle = first_shuffle[::random.randint(0, len(user_string)-1)]
    return second_shuffle

print(mixer(input("")))