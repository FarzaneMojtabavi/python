a=int(input('enter number1:'))
b=int(input('enter number2:'))
if a<b:
    mini=a+1
else:
    mini=b+1    
for i in range(1,mini):
    if(a%i==0 and b%i==0):
        gcd=i
print(gcd)