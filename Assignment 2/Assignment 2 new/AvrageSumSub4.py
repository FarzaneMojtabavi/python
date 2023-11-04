# barname i benevisid ke ebteda tedad daneshjoyan class ra begirad va
# be tedad daneshjoyan class nomre dars barname nevisi daryaft konad
# sepas miyangin nomarat clas v bishtarin v kamtarin ra namayesh dahad
while True:
    tedadDaneshjo=int(input('tedad daneshjo: '))
    nomreBarnamenivisi=float(input('nomre barnamenivisi: '))
    sum=0
    minimum=nomreBarnamenivisi
    maximum=nomreBarnamenivisi
    for i in range(tedadDaneshjo-1):
        nomreBarnamenivisi=float(input('nomre barnamenivisi: '))
        if minimum>nomreBarnamenivisi:
            minimum=nomreBarnamenivisi
        if maximum<nomreBarnamenivisi:
            maximum=nomreBarnamenivisi    
        sum=sum+nomreBarnamenivisi
    avrage=sum/tedadDaneshjo
    print('avrage: ', avrage,'minimum: ',minimum,'maximum: ',maximum)        
    exit=input('exit?y or n: ')
    if exit=='y':
        break

#or
n=int(input())
b=int(input())
max=b
min=b
sum=0
for i in range(n-1):
    b=int(input())
    if b>max:
        max=b
    if b<min:
        min=b
    sum=sum+b
print(sum)
avg=sum/n
print(avg)
