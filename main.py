from charset import alphabet
from art import logo

#TODO: Combine decryption and encryption in a single function ceasar()
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

text = ""
print(logo)

direction = input("Type 'encode' to encrypt,\ntype 'decode' to decrypt: ").lower()

while len(text) == 0:
    text = input("Type your message: ").lower()

    shift = int(input("Type the shift number:\n"))
    
    if shift > 26:
        shift = shift % 26

ceasar(text, shift, direction)

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
