#رنامه ای بنویسید که با دریافت وزن(کیلوگرم) و قد فرد(متر)
#شاخص را برای آن فرد محاسبه و در مورد توده بدنی فرد پیام مناسب چاپ نماید
import math
Height=float(input('height: '))
Weight=float(input('weight: '))
BMI=Weight/((Height ** Height))
print(BMI)
if(BMI<18.5):
    print("Underweight")
elif(18.5<=BMI<=24.9):
    print("Normal")    
elif(25<=BMI<=29.9):
    print("overweight")   
elif(30<=BMI<=34.9):
    print("obese")     
elif (BMI>35):
    print("Ectremely obese")      
else:
    print("Ooops!")    