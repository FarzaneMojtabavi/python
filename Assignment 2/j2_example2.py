#moadel daneshjo
# for i in range(10):
#     name=input()
#     num1=float(input())
#     num2=float(input())
#     avg=(num1+num2)/2
#     print(avg)
# *******************************************************************
#password ba 3 bar tekrar
# for i in range(3):
#     us=input()
#     pas=int(input())
#     if us=='u' and pas==1:
#         print('welcome')
#         break
#     else:
#         print('error,try again')
# *******************************************************************
#mishe tedad tekrar halghe ham az vorodi gereft
# a=int(input())
# for i in range(a):
#     print(i+1,end='.')
# *******************************************************************
# 3 bar vorodi begire v be on andaze 3tare print kone
# for i in range(3):
#     e=int(input())
#     for j in range (e+i):
#         print('*', end='')
# *******************************************************************
# bazi hads adad
# import random
# def emtiyaz(a):
#    print('emtiyaz= ',10-a)     
# computer_random=random.randint(0,20)
# for i in range(10):
#     user_number=int(input())
#     if user_number==computer_random:
#         print('barande shodi')
#         break
#     elif user_number<0 or user_number>20:
#         print('to baze 1,20 nist..., error')   
#         emtiyaz(i)  
#     elif user_number>computer_random:
#         print('boro payin')
#         emtiyaz(i) 
#     elif user_number<computer_random:
#         print('boro bala')     
#         emtiyaz(i)    
# emtiyaz(i)    
# ******************************************************************* 
# ta vaghti shrt bargharare print kon
# x=5
# while x>2:
#     print('*',end='')
#     x=x-1
# ******************************************************************* 
# bazi hads adad ba while
# import random
# def emtiyaz(a):
#    print('emtiyaz= ',10-a)     
# computer_random=random.randint(0,20)
# while True:
#     user_number=int(input())
#     if user_number==computer_random:
#         print('barande shodi')
#         break
#     elif user_number<0 or user_number>20:
#         print('to baze 1,20 nist..., error')    
#     elif user_number>computer_random:
#         print('boro payin')
#     elif user_number<computer_random:
#         print('boro bala')      
# *******************************************************************  
# mive more alaghe- list
# fruits=['orange', 'apple','benana']
# print(fruits)
# fruits.append('sibzamini')
# print(fruits)
# fruits.insert(1,'limo')
# print(fruits)
# print(fruits[2])
# *******************************************************************  
# ,,,,, nomre haye daneshjo migire v nomrasho hesab mikone-- kharabe
# nomarat=[]
# cont=0
# i=[]
# while True:
#     a=int(input())
#     nomarat.append(a)
#     if a==-1:
#         break
#     cont=+1
#     i.append(nomarat)

#     # /cont    
# print(nomarat)
# print(i)
# *******************************************************************  
# tamrina
# ta vaghti exit nazadim adad begire v dar nahayat majmo print kune- bq while
# sums=0
# while True:
#     number=int(input())
#     sums=sums+number
#     if number==0:
#         print(sums)
#         break
# *******************************************************************  
# tabdl zaman be saniye 
# saat daghighe saniye begire saniye bede-01:00:20 3620 
# while True:
#     h=int(input('hour: '))
#     m=int(input('minute: '))
#     s=int(input('second: '))
#     print(h,":",m,":",s)
#     htos=h*3600
#     mtos=m*60
#     sum=htos+mtos+s
#     print(sum,'second')
#     exit=input('exit?y or n: ')
#     if exit=='y':
#         break
# *******************************************************************  
# tabdil saniye be zaman
# saniye begire v be saat daghighe saniye tabdil kone
# while True:
#     s=int(input('second'))
#     stoh=s//3600
#     stom=(s%3600)//60
#     stos=(s%3600)%60
#     print(round(stoh),":",round(stom),":",round(stos))
#     exit=input('exit?y or n: ')
#     if exit=='y':
#         break
# *******************************************************************  
# barname i benevisid ke ebteda tedad daneshjoyan class ra begirad va
# be tedad daneshjoyan class nomre dars barname nevisi daryaft konad
# sepas miyangin nomarat clas v bishtarin v kamtarin ra namayesh dahad
# while True:
#     tedadDaneshjo=int(input('tedad daneshjo: '))
#     nomreBarnamenivisi=float(input('nomre barnamenivisi: '))
#     sum=0
#     minimum=nomreBarnamenivisi
#     maximum=nomreBarnamenivisi
#     for i in range(tedadDaneshjo-1):
#         nomreBarnamenivisi=float(input('nomre barnamenivisi: '))
#         if minimum>nomreBarnamenivisi:
#             minimum=nomreBarnamenivisi
#         if maximum<nomreBarnamenivisi:
#             maximum=nomreBarnamenivisi    
#         sum=sum+nomreBarnamenivisi
#     avrage=sum/tedadDaneshjo
#     print('avrage: ', avrage,'minimum: ',minimum,'maximum: ',maximum)        
#     exit=input('exit?y or n: ')
#     if exit=='y':
#         break
# *******************************************************************  
# yek tas shbihsazi koni. ta vaghti 6 miyad jayeze dare dobare bendaze
# tas=int(input('tas: '))
# while True:
#     if tas==6:
#         tas=int(input('tas: '))
#     if tas>6:
#         print('error,just between 1-6')    
#     if tas!=6:
#         print(tas)
#         exit=input('exit?y or n: ')
#         if exit=='y':
#             break
# *******************************************************************  
# n daryaft kon v be haman tedad seri fibonacci da list ezafe kon
# fibo=[1,1]
# while True:
#     n=int(input('n: '))
#     for i in range(n):
#         fibo.append(fibo[i]+fibo[i+1])
#     print(fibo)    
#     exit=input('exit?y or n: ')
#     if exit=='y':
#         break
#     if exit=='n':
#         fibo=[1,1]