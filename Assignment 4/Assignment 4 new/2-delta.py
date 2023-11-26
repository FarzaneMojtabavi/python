import math
def delta(a,b,c):
    result=b**2-4*a*c
    # return mesle print vali chap nmikone barmigardone
    return result
a=int(input())
b=int(input())
c=int(input())
# return yani berizesh to moteghayer Δ
# khasti chap kon ya nakon!
Δ=delta(a,b,c)

if Δ>0:
    x1=(b + math.sqrt(Δ)) / (2*a)
    x2=(b - math.sqrt(Δ)) / (2*a)
    print(x1,x2)
elif Δ==0:
    x=-b/a
    print(x)
elif Δ<0:
    print('no answer')