# در برنامه ماشین حساب که در کلاس نوشته شد ،  قابلیت های زیر را بیفزایید(با تبدیل رادیان به درجه برای توابع مثلثاتی)
# Radical sin cot cos tan factorial
import math
import colorama
from colorama import Fore, Back, Style
num1 = float(input(Fore.WHITE + "Enter number one: "))
num2 = float(input(Fore.WHITE + "Enter number two: "))
operation = input(Fore.RED +"Enter character (+ - * /) or write other: ")
if operation == "+":   result = num1+num2
elif operation == "-": result = num1-num2
elif operation == "*": result = num1*num2
elif operation == "/":
    if num2 != 0: result = num1/num2
    else: print(Fore.Red + 'Can not divide by zero')
if operation == 'other':
    operation = input(
        Fore.WHITE + 'Enter (radical or sin or cot or cos or tan or factorial): ')
    num3 = input('number one or num two? ')
    if operation == "radical":
        if num3 == 'one':
            if num1 == 0 and num1 == 1:
                print(
                    Fore.WHITE + 'The square root of the numbers is zero and one is the number itself')
            else: result = math.sqrt(math.degrees(num1))
        elif num3 == 'two':
            if num1 == 0 and num1 == 1:
                print(
                    Fore.WHITE + 'The square root of the numbers is zero and one is the number itself')
            else:result = math.sqrt(math.degrees(num2))
    elif operation == "sin":
        if num3 == 'one': result = math.sin(math.degrees(num1))
        elif num3 == 'two': result = math.sin(math.degrees(num2))
    elif operation == "cot":
        if num3 == 'one': result = math.cot(math.degrees(num1))
        elif num3 == 'two': result = math.cot(math.degrees(num2))
    elif operation == "cos":
        if num3 == 'one': result = math.cos(math.degrees(num1))
        elif num3 == 'two': result = math.cos(math.degrees(num2))
    elif operation == "tan":
        if num3 == 'one': result = math.tan(math.degrees(num1))
        elif num3 == 'two': result = math.tan(math.degrees(num2))
    elif operation == "factorial":
        if num3 == 'one': result = math.factorial(math.degrees(num1))
        elif num3 == 'two': result = math.factorial(math.degrees(num2))
print(Fore.YELLOW + 'result: ')
print(result)