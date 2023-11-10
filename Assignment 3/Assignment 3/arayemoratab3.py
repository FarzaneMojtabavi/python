lists=[]
tedad=int(input('chanbar?'))
for i in range(tedad):
    adad=int(input())
    lists.append(adad)
print(lists)
for i in range(len(lists)-1):
    if lists[i]>lists[i+1]:
        j='no'
        break
    else:
        j='yes'
print(j)