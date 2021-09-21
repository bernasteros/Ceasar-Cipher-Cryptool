from charset import alphabet
from art import logo
from os import system, name
from time import sleep as slp

#TODO: Combine decryption and encryption in a single function ceasar()

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def refresh():
    clear()
    print(logo)

def ceasar(start_text, shift, direction):

    msg_letters = [l for l in start_text]

    if direction == "decode":
        shift *= -1

    for m in msg_letters:
        if m not in alphabet:
            continue
        
        text_letter = msg_letters.index(m)
        alpha_letter = alphabet.index(m)
        alpha_index = len(alphabet) - 1

        


        new_position = alpha_letter + shift
        if alpha_letter == alpha_index or alpha_letter == 0:
            if direction == "decode":
                new_position = alpha_index - shift
            else:
                new_position = shift
        elif new_position > alpha_index:
            new_position = new_position - alpha_index
        elif new_position < 0:
            new_position = new_position + alpha_index
        else:
            msg_letters[text_letter] = alphabet[new_position]

    print(f"The {direction}d text is {''.join(msg_letters)}")

def game_on():
    print("\nStart new crypto-job?")
    run_game = input("Press 'Y' to start or any key to quit: ").lower()
    if run_game == "y":
        return True
    else:
        print("Crypto-Process stopped.\n Good Bye!")
        return False
    slp(1)

while game_on():
    text = ""
    shift = 0
    refresh()

    direction = input("Type 'encode' to encrypt,\ntype 'decode' to decrypt: ").lower()
    slp(1)
    refresh()

    while len(text) == 0:
        text = input("Type your message: ").lower()
        refresh()
        slp(1)

    while shift <=0:
        shift = int(input("Type the shift number: "))
        
        if shift > 26:
            shift = shift % 26
        refresh()
        slp(1)

    ceasar(text, shift, direction)
    slp(1)
#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
#e.g.
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
#print output: "The encoded text is mjqqt"

##HINT: How do you get the index of an item in a list:
#https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
.
