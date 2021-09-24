from charset import alphabet

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

        if new_position >=0 or new_position <= alpha_index:
            msg_letters[text_letter] = alphabet[new_position]
            continue               
        elif alpha_letter == 0 and direction == "decode":
            msg_letters[text_letter] = alphabet[alpha_index - shift]
        elif alpha_letter == alpha_index and direction == "encode":
            msg_letters[text_letter] = alphabet[shift - 1]

    print(f"The {direction}d text is {''.join(msg_letters)}")