n=int(input())
m=int(input())
for i in range(n):
    if i%2==0: 
        for j in range(m):
            if j%2==0:
                print('*',end='')
            else: 
                print('#',end='')   
        print()    
    elif i%2==0: 
        for j in range(m):
            if i%2==0:
                print('#',end='')
            else: 
                print('*',end='')   
        print()       

