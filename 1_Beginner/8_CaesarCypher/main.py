# Task description

alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def appstart():
    choice = input("Do you want to 'encode' or 'decode' your text ? ('e' or 'd') - ")
    text = input("Type your message: ").lower()
    shift = int(input("Enter the shift number: ")) % 26
    return choice, text, shift

def encode(text, shift):
    encoded_text = str()
    for letter in text:
        if letter not in alpha:
            encoded_text += letter
            continue
        new_index = alpha.index(letter) + shift
        if new_index <= 25:
            encoded_text += alpha[new_index]
        else:
            new_index = new_index - 26
            encoded_text += alpha[new_index]
    print(f"Your encoded text is '{encoded_text}'")

def decode(text, shift):
    decoded_text = str()
    for letter in text:
        if letter not in alpha:
            decoded_text += letter
            continue
        new_index = alpha.index(letter) - shift
        if new_index >= 0:
            decoded_text += alpha[new_index]
        else:
            new_index = new_index + 26
            decoded_text += alpha[new_index]
    print(f"Your decoded text is '{decoded_text}'")

def again():
    while True:
        again = input("Do you want encode/decode more text? y/n: ")
        if again == "y":
            break
        elif again == "n":
            print("Thanks for using our encoder/decoder!")
            quit()
        else:
            print("Please type in 'y' or 'n'.")
            continue


while True:
    choice, text, shift = appstart()
    if choice == "e":
        encode(text, shift)
    elif choice == "d":
        decode(text, shift)
    else:
        print("Please enter 'e' or 'd'.")
        continue

    again()
