def r(t):
    count=1
    for i in t:
        if i==' ':
            count+=1
    print(count)
r('aaa bbb ccc')

or:
def w(ww):
    word=1
    lenword=0
    space=0
    for i in ww:
        if i==' ':
            word+=1
            space+=1
        else:
            lenword+=1
    print('word:',word,'lenword:',lenword,'space:',space)
w(input())
