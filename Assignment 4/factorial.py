from colorama import Fore
number=int(input('enter number:'))
fact=1
end=0
for i in range(1,number):
    fact=fact*(i+1)
    if fact==number:
        print(Fore.BLUE ,'yes')
        print('repeat counting:', i)
        print('factorial:',fact)
        break
    else:
        print(Fore.RED ,'no')
        print('repeat counting:', i)
        print('factorial:',fact)