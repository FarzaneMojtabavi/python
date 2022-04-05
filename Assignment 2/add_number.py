from colorama import Fore
Addition = 0
while True:
    number1 = int(input(Fore.GREEN+'enter number: '))
    Addition = Addition+number1
    if number1 == 0:
        print(Fore.YELLOW + 'resault:')
        print(Addition-number1, end='')
        break
