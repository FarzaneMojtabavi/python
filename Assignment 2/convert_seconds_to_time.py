from colorama import Fore
while True:
    Second = int(input(Fore.GREEN+'enter second: '))
    StoH = Second//3600
    StoM = (Second % 3600)//60
    StoS = (Second % 3600) % 60
    print(Fore.YELLOW, round(StoH), ':', round(StoM), ':', round(StoS))
    exit = input('exit? y n ???  ')
    if exit == 'y':
        break
