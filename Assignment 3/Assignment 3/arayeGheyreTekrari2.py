import random
n=[]
for i in range(5):
    a=random.randint(0,9)
    if a not in n:
        n.append(a)
print(n)


