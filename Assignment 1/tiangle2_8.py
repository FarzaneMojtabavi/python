import math
from sympy import *
vatar = float(input('number one: '))
moghabel = float(input('number two: '))
mojaver = float(input('number three: '))
if vatar+moghabel > mojaver and vatar+mojaver > moghabel and moghabel+mojaver > vatar:
    d = True
else:
    d = False
if vatar == moghabel and moghabel == mojaver:
    d = "motesivi sagheyn"
if vatar == moghabel or moghabel == mojaver or vatar == mojaver:
    d = "motesavi sagheyn"
if pow(vatar, 2) == pow(moghabel, 2)+pow(mojaver, 2) or pow(moghabel, 2) == pow(mojaver, 2)+pow(vatar, 2) or pow(mojaver, 2) == pow(vatar, 2)+pow(moghabel, 2):
    d = "ghaemo zaviye"
print(d)    
