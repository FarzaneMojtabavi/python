number1=int(input('number 1: '))
number2=int(input('number 2: '))
for i in range(1,number1+1): 
    for j in range(1,number2+1):
        y=i*j
        print(y,end=" ")
    print()