import math
from colorama import Fore
n = int(input('n: '))
j=0
if n%2==0:
    print(Fore.RED,'#',end="")
else:
    print(Fore.BLUE,'*',end="")
for i in range(n-1):
    if j<=i:
        if n%2==0:
            print('*',end="")
            j=j+1
            n=n-1
        else:
            print('#',end="")    
            j=j+1
            n=n-1