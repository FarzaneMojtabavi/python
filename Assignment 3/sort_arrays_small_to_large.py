from json.tool import main
import random
from colorama import Fore
li = []
y = 1
counts=0;
number= int(input())
for i in range(number):
    print(Fore.GREEN+"number", end=' ')
    print(y, end='')
    print(":", end='')
    x = int(input())
    y = y+1
    li.append(x)   
print(Fore.BLUE , li)
for i in range(len(li)-1):
    if li[i]>li[i+1]:
        print('n')
        counts=counts+1
        print(counts)
        break
if counts==0:
    print('y') 
    print(counts)

