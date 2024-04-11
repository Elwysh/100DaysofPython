# code the Hangman game

import random
import getpass as gp
import hangman_ascii as hang

def bank():
    path = "D:/Repositories/100DaysofPython/1_Beginner/7_Hangman/wordbank.txt"
    with open(path, "r") as f:
        wordlist = f.read().split()
        word = random.choice(wordlist)
        return word

def player_word():
    word = gp.getpass("Please input a word to be used in the game: ")
    return word

def word_choice():
    print("Welcome to Hangman!\n")
    while True:
        choice = input("Would you like to 1 - get a random word or 2 - put a custom word? (enter '1' or '2') - ")
        if choice == "1":
            print("You have chosen a random word. Please enjoy the game :)")
            word = bank()
            return word
        elif choice == "2":
            print("You have chosen to enter your own word. Please enjoy the game :)")
            word = player_word()
            return word
        else:
            print("It said to type either '1' or '2'. How did you fail this simple task?")

def game_setup(word):
    health = 0
    guesses = set()
    hidden_word = []
    for i in range(len(word)):
        hidden_word += "_"
    check_word = list(word)
    return hidden_word, check_word, health, guesses

def print_hangman(health):
    print(hang.HANGMANPICS[health])

def pick_letter(hidden_word, check_word, health, guesses):
    print_hangman(health)
    print(" ".join(hidden_word))
    if len(guesses) == 0:
        pass
    else:
        print(f"\nAlready guessed characters: {guesses}")
    
    while True:
        choice = input("Please enter your guess: ").lower()
        if len(choice) > 1:
            print("Please enter only one character.")
            continue
        elif choice in guesses:
            print("You have already guessed this character.")
            print(f"Your previous guessed were {guesses}")
            continue
        else:
            break
        
    if choice in check_word:
        for i in range(len(check_word)):
            if choice == check_word[i]:
                hidden_word[i] = choice
    else:
        print("Character is not in the word.")
        health += 1

    guesses.add(choice)
    return hidden_word, check_word, health, guesses

def win_condition(hidden_word, health):
    if health >= 7:
        print_hangman(health)
        print("You lost! Try again next time.")
        game_on = False
        return game_on
    elif "_" not in hidden_word:
        print("You found the word. GG EZ.")
        game_on = False
        return game_on
    else:
        game_on = True
        return game_on

def again():
    while True:
        again = input("Do you want to play again? y/n: ")
        if again == "y":
            break
        elif again == "n":
            print("Thanks for playing Hangman!")
            quit()
        else:
            print("Please type in 'y' or 'n'.")
            continue

# Game flow
while True:
    word = word_choice()
    hidden_word, check_word, health, guesses = game_setup(word)
    
    game_on = True
    
    while game_on:
        hidden_word, check_word, health, guesses = pick_letter(hidden_word, check_word, health, guesses)
        game_on = win_condition(hidden_word, health)

    again()
