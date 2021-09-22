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

        if new_position > alpha_index:
            new_position = new_position - alpha_index
        elif new_position < 0:
            new_position = new_position + alpha_index
        else:
            msg_letters[text_letter] = alphabet[new_position]

    print(f"The {direction}d text is {''.join(msg_letters)}")