import math
number1=int(input("enter number 1: "))
number2=int(input("enter number 2: "))
number3=int(input("enter number 3: "))
delta=number2*number2-4*number1*number3
if delta<0:
      print('There is no answer')
elif delta==0:
      answer_one=(-number2+math.sqrt(delta))      
else:
      x1=(-number2+math.sqrt(delta))/(2*number1)
      x2=(-number2-math.sqrt(delta))/(2*number1)
      print(x1,"\n",x2)