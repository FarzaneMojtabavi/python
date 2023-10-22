# tabdil saniye be zaman
# saniye begire v be saat daghighe saniye tabdil kone
while True:
    s=int(input('second'))
    stoh=s//3600
    stom=(s%3600)//60
    stos=(s%3600)%60
    print(round(stoh),":",round(stom),":",round(stos))
    exit=input('exit?y or n: ')
    if exit=='y':
        break