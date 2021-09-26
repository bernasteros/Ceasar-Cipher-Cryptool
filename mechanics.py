from os import system, name
from time import sleep as slp


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def game_on():
    print("\nStart new crypto-job?")
    run_game = input("Press 'Y' to start or any key to quit: ").lower()
    if run_game == "y":
        return True
    else:
        print("Crypto-Process stopped.\n Good Bye!")
        return False
    slp(1)
