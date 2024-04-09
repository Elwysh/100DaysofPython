# Code a random password generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator Nyanthousand!")

def choice():
    while True:
        try:
            characters = int(input("How many total characters would you like in your password? - ")) 
            nr_symbols = int(input("How many symbols would you like? - "))
            nr_numbers = int(input("How many numbers would you like? - "))
            if characters < nr_symbols + nr_numbers:
                print("The number of total characters has to be higher than sum of the number of symbols and numbers.")
                continue
            nr_letters = characters - nr_symbols - nr_numbers
            return nr_letters, nr_symbols, nr_numbers
        except:
            print("Please put in numbers.")
            continue

def genletters(nr_letters):
    oletters = []
    if nr_letters == 0:
        return oletters
    for i in range(nr_letters):
        n = random.randint(0, 51)
        oletters += letters[n]
    return oletters

def gensymbols(nr_symbols):
    osymbols = []
    for i in range(nr_symbols):
        n = random.randint(0, 8)
        osymbols += symbols[n]
    return osymbols

def gennumbers(nr_numbers):
    onumbers = []
    for i in range(nr_numbers):
        n = random.randint(0, 9)
        onumbers += numbers[n]
    return onumbers

def combinegen(oletters, osymbols, onumbers):
    password = oletters + osymbols + onumbers
    random.shuffle(password)
    password = "".join(password)
    print(f"Your password is {password} \n")


def again():
    while True:
        again = input("Do you want to generate another password? y/n: ")
        if again == "y":
            break
        elif again == "n":
            print("Thanks for using Password Generator Nyanthousand!")
            quit()
        else:
            print("Please type in 'y' or 'n'.")
            continue

while True:
    nr_letters, nr_symbols, nr_numbers = choice()
    
    oletters = genletters(nr_letters)
    osymbols = gensymbols(nr_symbols)
    onumbers = gennumbers(nr_numbers)
    
    combinegen(oletters, osymbols, onumbers)
    
    again()
