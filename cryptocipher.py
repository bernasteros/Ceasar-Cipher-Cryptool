from charset import alphabet

# Function changes the input characters in the style of the ceasar_cipher
# In our case we classically change the number of the letter by shifting 
# it a certain number of characters forward (encode) or backward (decode)

def ceasar(start_text, shift, direction):

# The input message is splitted 
# into its characters and put on a list
    msg_letters = [l for l in start_text]

# Decide on the direction of the letter movement
    if direction == "decode":
        shift *= -1

# Every letter in the start_text is assigned 
# to the index of our alphabet key. 
# If it is not a part of the alphabet 
# (numbers, symbols) it will be ignored.
    end_string = ""
    for m in msg_letters:
        if m not in alphabet:
            continue
        
        text_letter = msg_letters.index(m)
        alpha_letter = alphabet.index(m)
        alpha_index = len(alphabet) - 1
        

# The simplest scenario: If the new position
# after the shift is on the index of the alphabet 
# the original letter will be replaced by the 
# shifted letter of the alphabet.          
        new_position = alpha_letter + shift

        if new_position > alpha_index:
            new_position = new_position - alpha_index - 1
        
        msg_letters[text_letter] = alphabet[new_position] 
        end_string += msg_letters[text_letter]           
    print(f"The {direction}d text is {end_string}")