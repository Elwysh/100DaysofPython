# Code a silent/secret auction where nobody knows each others bid and shows the winner at the end

# import os

def setup():
    bidders = {}
    item = input("What are we bidding for? - ")
    bidding = True
    return bidders, item, bidding

def add_bidder(item):
    global bidders
    print(f"Hello, today we are bidding for '{item}'!")
    name = input("What is your name? - ")
    bid = int(input("How much are you bidding? - "))
    bidders[name] = bid
    print("\033c", end="", flush=True)

def another_bid():
    while True:
        again = input("Are there more people bidding? y/n: ")
        if again == "y":
            bidding = True
            return bidding
        elif again == "n":
            bidding = False
            return bidding
        else:
            print("Please type in 'y' or 'n'.")
            continue

def results(item):
    highest = 0
    second_highest = 0
    winner = None
    
    for k,v in bidders.items():
        if v >= highest:
            second_highest = highest
            highest = v
            winner = k

    if highest > second_highest:
        print(f"The winner of the auction is {winner} with a bid of {highest}!\nCongratulations on winning the {item}!")
    elif highest == second_highest:
        print("Multiple people had the same highest bid. Please go again.")

def again():
    while True:
        again = input("Do you want to auction another item? y/n: ")
        if again == "y":
            break
        elif again == "n":
            print("Thanks for using our silent auction code!")
            quit()
        else:
            print("Please type in 'y' or 'n'.")
            continue


while True:
    bidders, item, bidding = setup()
    
    while bidding:
        add_bidder(item)
        bidding = another_bid()
    
    results(item)
    
    again()

