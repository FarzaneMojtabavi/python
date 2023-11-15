fact=1
t=int(input())
for i in range(1,t):
    fact=fact*(i+1)
    if fact==t:
        print('yes')
        print(fact)
        break
    else:
        print('no')
        print(fact)