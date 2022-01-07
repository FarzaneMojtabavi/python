Lesson1=float(input('Lesson 1: '))
Lesson2=float(input('Lesson 2: '))
Lesson3=float(input('Lesson 3: '))
if Lesson1>20 or Lesson2>20 or Lesson3>20 or Lesson1<0 or Lesson2<0 or Lesson3<0:
    print('Error. Enter between 0-20')
else:    
    avarage=(Lesson1+Lesson2+Lesson3)/3
    if avarage>=17:
        status='great'
    if 12<=avarage<17:
        status='normal'    
    if avarage<12:
        status='fail'
    print(status)
