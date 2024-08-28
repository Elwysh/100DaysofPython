# Rock Paper Scrissors

import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scrissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

def playerinput():
    while True:
        try:
            choice = int(input("What do you choose? 1 for Rock, 2 for Paper or 3 for Scissors.: "))
            if choice not in (1, 2, 3):
                print("How hard is it to type '1', '2' or '3'?")
                continue
            return choice
        except:
            print("Please pick a number dummy.\n")
            continue

def pcinput():
    choice = random.randint(1, 3)
    return choice

def printascii(computer, player):
    if computer == 1:
        print("Computer plays Rock!\n" + rock)
    elif computer == 2:
        print("Computer plays Paper!\n" + paper)
    elif computer == 3:
        print("Computer plays Scissors!\n" + scrissors)
    if player == 1:
        print("Player plays Rock!\n" + rock)
    elif player == 2:
        print("Player plays Paper!\n" + paper)
    elif player == 3:
        print("Player plays Scissors!\n" + scrissors)
    
def wincondition(computer, player):
    if computer == player:
        print("It's a draw!\n")
    if computer == 1 and player == 2:
        print("Player wins!\n")
    elif computer == 2 and player == 1:
        print("Computer wins!\n")
    if computer == 3 and player == 1:
        print("Player wins!\n")
    elif computer == 1 and player == 3:
        print("Computer wins!\n")
    if computer == 2 and player == 3:
        print("Player wins!\n")
    elif computer == 3 and player == 2:
        print("Computer wins!\n")

def playagain():
    while True:
        again = input("Do you want to go again? y/n: ")
        if again == "y":
            break
        elif again == "n":
            print("Thanks for playing!")
            quit()
        else:
            print("Please type in 'y' or 'n'.")
            continue


while True:
    pc = pcinput()
    player = playerinput()
    
    printascii(pc, player)
    
    wincondition(pc, player)
    
    playagain()
