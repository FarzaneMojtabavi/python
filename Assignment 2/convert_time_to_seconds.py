from colorama import Fore
while True:
    hour = int(input(Fore.GREEN+'enter hour: '))
    minute = int(input('enter minute: '))
    second = int(input('enter second: '))
    print(Fore.YELLOW, hour, ':', minute, ':', second, '= ', end='')
    HtoS = hour*3600
    MtoS = minute*60
    sum = HtoS + MtoS + second
    print(sum, 'second')
    exit = input('exit? y n ???  ')
    if exit == 'y':
        break
