# n daryaft kon v be haman tedad seri fibonacci da list ezafe kon
fibo=[1,1]
while True:
    n=int(input('n: '))
    for i in range(n):
        fibo.append(fibo[i]+fibo[i+1])
    print(fibo)    
    exit=input('exit?y or n: ')
    if exit=='y':
        break
    if exit=='n':
        fibo=[1,1]