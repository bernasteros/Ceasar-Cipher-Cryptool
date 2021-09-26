from mechanics import clear, game_on
from time import sleep as slp
from cryptocipher import ceasar
from art import logo

while game_on():
    print(logo)
    text = ""
    shift = 0
    direction = ""

    while direction != "encode" or direction != "decode":
        direction = input(
            '''What operation do you wand to do?"
           
            type 'encode' 
            to shift forward,
            
            type 'decode' 
            to shift backward
            
            > ''').lower()
        if direction == "encode" or direction == "decode":
            break

    while len(text) == 0:
        text = input("Type your message\n> ").lower()

        if len(text) == 0:
            print("You need a text to " + direction + "!")

    while shift <= 0:
        shift = int(input("Type the shift number\n> "))
        if shift <= 0:
            print("Please enter a positive number!")

        if shift > 26:
            shift = shift % 26

    ceasar(text, shift, direction)
