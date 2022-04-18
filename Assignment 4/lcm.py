a=int(input('enter number1:'))
b=int(input('enter number2:'))
if a<b:
    mini=b
    maxi=a
else:
    mini=a
    maxi=b
muli=mini*maxi    
for i in range(1,muli):
    print('i',i)
    print((maxi*i)%mini)
    if((maxi*i)%mini==0):
        lcm=maxi*i    
        break
print(lcm)    