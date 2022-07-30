number=int(input('enter number of rows: '))
print(number)
for i in range(number):
    for j in range(i,number-1):
        print("-",end="-")
    for j in range(i+1):
        print("*",end="-")
    for j in range(i):
        print("*",end="-")     
    print()     
for i in range(number):
    for j in range(i):
        print("-",end="-") 
    for j in range(i,number):
        print("*",end="-")
    for j in range(i,number-1):
        print("*",end="-")              
    print()      
#__or___________________________________________       
n = int(input("please enter rows:"))
for i in range(n):
    print("-" * (n-i), "*" * (2*i+1))  
for i in range(n-2, -1, -1):
    print("-" * (n-i), "*" * (2*i+1))