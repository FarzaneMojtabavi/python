def shatranji(n,m):
    for i in range(m):
        if i%2==0:
            for j in range(n):
                if j%2==0:
                    print("*",end="")
                else:
                    print("#",end="")
            print()     
        elif i%2!=0:
            for j in range(n):
                if j%2==0:
                    print("#",end="")
                else:
                    print("*",end="")
            print()                  
shatranji(19,3)       