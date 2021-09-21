from mechanics import refresh, game_on
from time import sleep as slp
from cryptocipher import ceasar

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
.
