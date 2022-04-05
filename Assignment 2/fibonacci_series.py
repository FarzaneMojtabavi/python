from colorama import Fore
fibo = [1, 1]
while True:
    number = int(input(Fore.GREEN+'number? '))
    for i in range(number):
        fibo.append(fibo[i]+fibo[i+1])
    print(Fore.BLUE, fibo)
    exit = input('exit? y n ???  ')
    if exit == 'n':
        fibo = [1, 1]
    elif exit == 'y':
        break
