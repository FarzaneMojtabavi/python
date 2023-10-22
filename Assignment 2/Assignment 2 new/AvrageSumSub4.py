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