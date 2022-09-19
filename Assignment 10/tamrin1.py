class course:
    def __init__(self,name,unit):
        self.name=name
        self.unit=unit
class person:
    def __init__(self,name,family,birthday,national_code,city,country):
        self.name=name
        self.family=family
        self.birthday=birthday
        self.national_code=national_code
        self.city=city
        self.country=country
    def show(self):
        print(
        self.name,
        self.family,
        self.birthday,
        self.national_code,
        self.city,
        self.country)    

class student(person):
    def __init__(self,name,family,birthday,national_code,city,average=0,country='iran'):
        person.__init__(self,name,family,birthday,national_code,city,country)
        if average>20: 
            average=20
        self.average=average
    def study(self):
        pass
    def show(self):
        print(self.name,
        self.family,
        self.birthday,
        self.national_code,
        self.city,
        self.country,
        self.average)   
class teacher(person):
    def __init__(self,name,family,birthday,national_code,city,salary,country='iran'):
        person.__init__(self,name,family,birthday,national_code,city,country)
        self.salary=salary
    def show(self):
        print(self.name,
        self.family,
        self.birthday,
        self.national_code,
        self.city,
        self.country,
        self.salary)      
me=student('farzane','mojtabavi','28/9/78','1234','mashhad',16)        
me.show()
friend=student('shima','noferesti',None,'1235',None,17,'german')
friend.show()
morabi=teacher('ostad','ostadi',None,'1236',56,000,000)
morabi.show()


# class course:
#     def __init__(self,name,unit):
#         self.name=name
#         self.unit=unit
#     class student:
#         def __init__(self,name,family,birthday,national_code,id,city,average=0,country='iran'):
#             self.name=name
#             self.family=family
#             self.birthday=birthday
#             self.national_code=national_code
#             self.id=id
#             self.city=city
#             if average>20: 
#                 average=20
#             self.average=average
#             self.country=country
#         def show(self):
#             print(self.name,
#             self.family,
#             self.birthday,
#             self.national_code,
#             self.id,
#             self.city,
#             self.average,
#             self.country)
#     class teacher:
#         def __init__(self,name,family,birthday,national_code,city,salary,country='iran'):
#             self.name=name
#             self.family=family
#             self.birthday=birthday
#             self.national_code=national_code
#             self.city=city
#             self.salary=salary
#             self.country=country
#         def show(self):
#             print(self.name,
#             self.family,
#             self.birthday,
#             self.national_code,
#             self.city,
#             self.salary,
#             self.country)    
#     me=student('farzane','mojtabavi','28/9/78','1234','mashhad',16)        
#     me.show()
#     friend=student('shima','noferesti',None,'1235',None,None,'german')
#     friend.show()
#     morabi=teacher('ostad','ostadi',None,'1236',56,000,000)
#     morabi.show()

