import math
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# 1-barname i benevisid ke 2 adad ba ham jam kone.
# [_START___________________________________________________________]
# print('1-barname i benevisid ke 2 adad ba ham jam kone')
# number_1=int(input('number 1: '))
# number_2=int(input('number 2: '))
# print(number_1+number_2)
# [_END_____________________________________________________________]

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# 2-tabdil dama bar hasb santigrad be farenhaite
# ---*9 /5 +32---
# [_START___________________________________________________________]
# print('2-tabdil dama bar hasb santigrad be farenhaite')
# cg=int(input('cg: '))
# fh=cg*9/5+32
# print('fh: ',fh)
# [_END_____________________________________________________________]

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# 3-esm v sen v shahr begire
# [_START___________________________________________________________]
# print('3-esm v sen v shahr begire')
# name=input('name: ')
# age=int(input('age: '))
# city=input('city: ')
# print(name,'',age,'',city)
# [_END_____________________________________________________________]

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# 4-masahat mostatil
# (length_number+width_number)/2
# [_START___________________________________________________________]
# print('4-masahat mostatil')
# length_number=float(input('Length: '))
# width_number=float(input('width: '))
# rectangle_area=(length_number+width_number)/2
# print('rectangle_area: ',rectangle_area)
# [_END_____________________________________________________________]

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# 5-mohit v masahat dayere
# faghat shoa mikhaym==Radius-->شعاع, perimeter-->محیط, area-->مساحت
# Radius*Radius* == Radius**2
# 3.14 == import math --> math.pi
# [_START___________________________________________________________]
# print('5-mohit v masahat dayere')
# Radius=int(input('Radius: '))
# perimeter=Radius**2*math.pi
# area=2*Radius*3.14
# print('Radius',Radius,'','perimeter',perimeter,'','area',area)
# [_END_____________________________________________________________]

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# 6-taghsim
# adad dovom 0 nabashe kochiktar avali nabashe
# [_START___________________________________________________________]
# print('6-taghsim')
# a=int(input('number a: '))
# b=int(input('number b: '))
# if b==0 or b>a:
#     result='khata'
# if b!=0 and b<=a:
#     result=a/b
# print(result)
# [_END_____________________________________________________________]

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# 7-sehat username v password
# [_START___________________________________________________________]
# print('7-sehat username v password')
# username=int(input('username: '))
# password=int(input('username: '))
# if username==123 and password==123:
#     print('welcome')
# else:
#     print('khata')
# [_END_____________________________________________________________]

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# [_START___________________________________________________________]
# 8-mashinhesab
# print('8-mashinhesab')
# number_one=int(input('number_one: '))
# number_two=int(input('number_two: '))
# operation=input('operation: ')
# if operation=='+':
#     result=number_one+number_two
# elif operation=='-':
#     result=number_one-number_two
# elif operation=='*':
#     result=number_one*number_two
# elif operation=='/':
#     result=number_one/number_two
# else:
#     result='error'
# print(number_one,operation,number_two,'=',result)
# [_END_____________________________________________________________]

# *******************************************************************
# ▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞ EXAMPLE ▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞▞
# *******************************************************************

# 7-mashinhesab kamel(radical,sin,cos,tan,cot,+,-,/,*)
# print('7-mashinhesab kamel(radical,sin,cos,tan,cot,+,-,/,*)')
# number_one = int(input('number_one: '))
# operation = input('operation: ')
# if operation == 'radical' or operation == 'sin' or operation == 'cot' or operation == 'cos' or operation == 'tan':
#     if operation == 'radical':
#         if operation == 0 or operation == 1:
#             print('error')
#         else:
#             result = math.sqrt(math.degrees(number_one))
#     elif operation == 'sin':
#         result = math.sin(math.degrees(number_one))
#     elif operation == 'cot':
#         result = math.cot(math.degrees(number_one))
#     elif operation == 'cos':
#         result = math.cos(math.degrees(number_one))
#     elif operation == 'tan':
#         result = math.tan(math.degrees(number_one))
#     print(number_one, operation)    
# elif operation == '+' or operation == '-' or operation == '*' or operation == '/':
#     number_two = int(input('number_two: '))
#     if operation == '+':
#         result = number_one+number_two
#     elif operation == '-':
#         result = number_one-number_two
#     elif operation == '*':
#         result = number_one*number_two
#     elif operation == '/':
#         if number_two == 0 or number_two > number_one:
#             result = 'khata'
#         if number_two != 0 and number_two <= number_one:
#             result = number_one/number_two
#     print(number_one, operation, number_two)        
# else:
#     result = 'error'
# print('=', result)
# *******************************************************************
# 8-3 zelee mosalas migirim v moshakhas mikonim mishe rasm kard ya na
# print('example 8-3 zelee mosalas migirim v moshakhas mikonim mishe rasm kard ya na')
# z1=int(input('zelee 1:'))
# z2=int(input('zelee 2:'))
# z3=int(input('zelee 3:'))
# if z1+z2>z3 and z1+z3>z2 and z2+z3>z1:
#     result=True
# else:
#     result=False   
# print(result)    
 
# *******************************************************************
# 9-bmi
# Height=float(input('height: '))
# Weight=float(input('weight: '))
# BMI=Weight/((Height ** 2))
# print(BMI)
# if(BMI<18.5):
#     print("Underweight")
# elif(18.5<=BMI<=24.9):
#     print("Normal")    
# elif(25<=BMI<=29.9):
#     print("overweight")   
# elif(30<=BMI<=34.9):
#     print("obese")     
# elif (BMI>35):
#     print("Ectremely obese")      
# else:
#     print("Ooops!")  
 
# *******************************************************************
# 10-moadel
# Lesson1=float(input('Lesson 1: '))
# Lesson2=float(input('Lesson 2: '))
# Lesson3=float(input('Lesson 3: '))
# if Lesson1>20 or Lesson2>20 or Lesson3>20 or Lesson1<0 or Lesson2<0 or Lesson3<0:
#     print('Error. Enter between 0-20')
# else:    
#     avarage=(Lesson1+Lesson2+Lesson3)/3
#     if avarage>=17:
#         status='great'
#     if 12<=avarage<17:
#         status='normal'    
#     if avarage<12:
#         status='fail'
#     print(status)