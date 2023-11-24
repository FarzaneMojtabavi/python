def z(v,t):
    for i in range(1,v+1):
        for j in range(1,t+1):
            b=i*j
            print(b,end=' ')
        print()
z(5,6)

or:
def zrb(n,m):
    for i in range(n):
        for j in range(m):
            print((i+1)*(j+1),end=' ')
        print()
zrb(int(input()),int(input()))
