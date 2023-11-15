import math
def de(a,b,c):
    d=b*b-4*a*c
    if d>0:
        aa=(-b+math.sqrt(d))/(2*a)
        bb=(-b-math.sqrt(d))/(2*a)
        print(aa)
        print(bb)
    if d==0:
        ans=(-b+math.sqrt(d))
    if d<0:
        print('javab nadare')
de(5,44,14)