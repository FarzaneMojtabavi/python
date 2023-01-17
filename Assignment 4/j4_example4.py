# tarif function
# def functionName():
#     name=input('name: ')
#     print(name)
# functionName()    
# functionName() 
# *******************************************************************
# moadele daraje 1
# [y=m*x+b]  -->  [8=3*x+2]  -->  [6=3*x]  -->  [x=2]
# [10=4x+1]  -->  [9=4x]  -->  [9=4*x]  -->  [9/4=4*x/4]  -->  [x=9/4]  -->  [x=2.25]
# agar yek y=m*x+b  dashte bashim, az 2 tarab -b mishe.   -->  [y-b=m*x]  -->  [y-b/m=x]
# [12=3*x+2] -->  [10=3*x]  -->  [12-2/3=x]  -->  [10/3=x]  -->  [x=3.33]
# y=int(input('y: '))
# m=int(input('m: '))
# b=int(input('b: '))
# x=(y-b)/m
# print(x)
# 20m.10:15  10:25/   10:30  10:45/ 13:50 14:10/14:42 15/
# *******************************************************************
# def moadele daraje 1
# def d1(y,b,m):
#     x=(y-b)/m
#     print(x)
# d1(8,4,2)
# d1(17,2,12)
# *******************************************************************
# function har adadi dadim 2 barabar kone
# def dobrabr(x):
#     print(x*2)
# dobrabr(5)
# dobrabr(8)
# *******************************************************************
# function zarb
# def zarb(x):
#     y=int(input('5*?='))
#     print(x*y)
# zarb(5)   
# *******************************************************************
# pyfiglet tarh be matn
# XXXXXXXXXXXXXXXXx
# *******************************************************************
# pass = jologiri az khataye khali bodn
# def m():
#     pass
# *******************************************************************
# hame ketabkhone import shode v ya faghat yeki mored nazar
# import math
# print(math.sin(6))
# from math import sin
# print(sin(8))
# *******************************************************************
# tamrina
# moadele darzaje 2
# 1 javab ya 2 javab ya javab nadare. az ro delta moshkhas mishe
# delta=b^2-4ac
# import math
# def delta(b,a,c):
#     result=b**2-4*a*c
#     if result<0:
#         print('no answer')
#     elif result==0:
#         x=(-b+math.sqrt(result))  
#         print(x)
#     else:
#         x1=(-b+math.sqrt(result))/(2*a)
#         x2=(-b-math.sqrt(result))/(2*a)
#         print(x1,"\n",x2)    
# b=int(input('b: '))   
# a=int(input('a: '))       
# c=int(input('c: '))    
# delta(a,b,c)  
# *******************************************************************
# jadval zarb be andaze mored nazar
# a=int(input('a: '))
# b=int(input('b: '))
# for i  in range(1,a+1):
#     for j in range(1,b+1):
#         x=i*j
#         print(x,end=' ')
#     print()    
# *******************************************************************
# function ke kalamat jomle beshmore
# word=input('word: ')
# wordCount=1
# space=0
# def count():
#     for i in word:
#         if i==' ':
#             wordCount+=1
#             space+=1
#     print(wordCount,' , ',space)        
# count()
# *******************************************************************
# adad factoriel hast ya na
# a=int(input())
# b=1
# for i in range(1,a):
#     b=b*(i+1)
#     if b==a:
#         print(b)
#         print('yes')
#         break
#     elif b>a or b<a:
#         print(b)
#         print('no')           
# *******************************************************************
# b.m.m-for
# k.m.m-for
# a=int(input('a: '))
# b=int(input('b: '))
# for i in range(1,a+1):
#     if a%i==0 and b%i==0:
#         bmm=i
# for j in range(b,(a*b)+1):
#     if j%a==0 and j%b==0:        
#         kmm=j
#         break
# print(kmm)  
# print(bmm)   
