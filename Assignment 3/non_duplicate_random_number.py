from json.tool import main
import random
from colorama import Fore
li = []
y = 1
while True:
    print(Fore.GREEN+"random number", end=' ')
    print(y, end='')
    print(":", end='')
    x = int(input())
    y = y+1
    if x not in li:
        li.append(x)
    else:
        print(Fore.RED+"Opps!! Repetitious")
        break
print(Fore.BLUE , li)