from colorama import Fore
while True:
    numberStudentsClass = int(input(Fore.GREEN+'number Students Class: '))
    scoreProgrammingLesson = float(input('score Programming Lesson: '))
    sum = 0
    minimum = scoreProgrammingLesson
    maximum = scoreProgrammingLesson
    for i in range(numberStudentsClass-1):
        scoreProgrammingLesson = float(input('score Programming Lesson: '))
        if minimum > scoreProgrammingLesson:
            minimum = scoreProgrammingLesson
        if maximum < scoreProgrammingLesson:
            maximum = scoreProgrammingLesson
        sum = sum+scoreProgrammingLesson
    avrage = sum/numberStudentsClass
    print(Fore.YELLOW, 'avrage: ', avrage,
          'minimum: ', minimum, 'maximum: ', maximum)
    exit = input('exit? y n ???  ')
    if exit == 'y':
        break
