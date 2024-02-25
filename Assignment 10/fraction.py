import fractions
# from fractions import Fraction
class kasr:
    def __init__(self,s,m):
        self.sorat=s
        self.makhraj=m
    def sum(self):
        ...
    def sub(self):
        ...
    def multiplication(self):
        ...
    def Division(self):
        ...
number1=kasr(4,4)
number2=kasr(0,6)
print(number1.sorat)
print(number2.makhraj)
print(fractions.Fraction(number1.sorat, number1.makhraj))
print(fractions.Fraction(number2.sorat, number2.makhraj))
# کسری که صورتش صفره نتیجه صفره
# کسری که صورت و مخرج برابره نتیجه یک