from colorama import Fore
while True:
    r = int(input(Fore.GREEN+'Roll Dice: '))
    if r > 6:
        print('Error. Please enter between 1 and 6')
    while r == 6:
        rollDice = int(input('Well done roll the dice again: '))
        if rollDice > 6:
            print('Error. Please enter between 1 and 6')
            break
    exit = input(Fore.YELLOW+'exit? y n ??? ')
    if exit == 'y':
        break
