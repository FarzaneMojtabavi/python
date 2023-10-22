# tabdl zaman be saniye 
# saat daghighe saniye begire saniye bede-01:00:20 3620 
while True:
    h=int(input('hour: '))
    m=int(input('minute: '))
    s=int(input('second: '))
    print(h,":",m,":",s)
    htos=h*3600
    mtos=m*60
    sum=htos+mtos+s
    print(sum,'second')
    exit=input('exit?y or n: ')
    if exit=='y':
        break