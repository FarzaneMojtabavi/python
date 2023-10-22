# yek tas shbihsazi koni. ta vaghti 6 miyad jayeze dare dobare bendaze
tas=int(input('tas: '))
while True:
    if tas==6:
        tas=int(input('tas: '))
    if tas>6:
        print('error,just between 1-6')    
    if tas!=6:
        print(tas)
        exit=input('exit?y or n: ')
        if exit=='y':
            break