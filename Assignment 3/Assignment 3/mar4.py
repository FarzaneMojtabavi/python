mar=[]
n=int(input())
for i in range(n):
    if n%2==0:
       mar.append('#') 
    else:
        mar.append('*') 
    n=n-1
#  تبدیل هر عنصر به رشته
result = ''.join(str(x) for x in mar)
print(result)