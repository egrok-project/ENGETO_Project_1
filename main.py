# Projekt 1 - Textový Analyzátor
# Autor: Emil Grokhotov
# Popis: Jednoduchý nástroj v Pythonu pro analýzu textu. Nabízí analýzu počtu slov, rozdělení podle velikosti písmen a numerickou analýzu s ověřováním uživatelů.

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

USERS = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

SEPARATOR = "-" * 40

username = input("Username: ")
password = input("Password: ")

if USERS.get(username) != password:
    print("unregistered user, terminating the program...")
    quit()

print(SEPARATOR)
print(f"Welcome to the app, {username}")
print(f"We have {len(TEXTS)} texts to be analyzed.")
print(SEPARATOR)

choice = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")
if not choice.isdigit():
    print("Invalid input, terminating the program...")
    quit()

choice = int(choice)
if choice < 1 or choice > len(TEXTS):
    print("Invalid choice, terminating the program...")
    quit()

text = TEXTS[choice - 1]

import string
words = [w.strip(string.punctuation) for w in text.split()]

num_words = len(words)
titlecase_words = sum(1 for w in words if w.istitle())
uppercase_words = sum(1 for w in words if w.isupper() and w.isalpha())
lowercase_words = sum(1 for w in words if w.islower())
numeric_strings = [int(w) for w in words if w.isdigit()]

print(SEPARATOR)
print(f"There are {num_words} words in the selected text.")
print(f"There are {titlecase_words} titlecase words.")
print(f"There are {uppercase_words} uppercase words.")
print(f"There are {lowercase_words} lowercase words.")
print(f"There are {len(numeric_strings)} numeric strings.")
print(f"The sum of all the numbers {sum(numeric_strings)}")
print(SEPARATOR)

print("LEN|  OCCURRENCES  |NR.")
print(SEPARATOR)

lengths = {}
for w in words:
    l = len(w)
    if l > 0:
        lengths[l] = lengths.get(l, 0) + 1

for length in sorted(lengths):
    count = lengths[length]
    print(f"{length:>3}|{'*' * count:<18}|{count}")
