import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')
django.setup()

from account.models import *
from leaveform.models import *
from django.db.models import *

# queryset = User.objects.filter(department__name__in=['IT','SE','BS-CS'])
queryset1 = User.objects.filter(last_name__iexact='Usman')
print(' >>>>> Queryset 1 <<<<<',queryset1)

queryset2 =  Department.objects.filter(manager__email__icontains = "m")
print("Queryset 2 :",queryset2)

queryset3 = Department.objects.filter(created_at="2023-07-26T09:41:44.904752Z",)
print("Queryset 3 :",queryset3)

# queryset = User.objects.filter(department__name__in=['IT','SE','BS-SE','BS-CS'])
# queryset = User.objects.filter(last_name="usman")
# queryset = User.objects.exclude(department__name  = 'IT')
# queryset = User.objects.filter(last_name__icontains = "man")
# queryset = User.objects.filter(first_name__startswith = 'a')
# queryset = User.objects.filter(email__endswith = ".com")
# queryset = User.objects.all()
# queryset = User.objects.only("employee_id")
# queryset = User.objects.defer("department","date_of_joining")
# queryset = User.objects.values_list("first_name","last_name","email",flat=True)
# queryset = User.objects.exclude(id=3)
# queryset = User.objects.values("id","first_name","last_name","email")
# queryset = User.objects.select_related('department')[:3]
# queryset = User.objects.prefetch_related("department")[:2]
# queryset = User.objects.distinct("first_name")
# queryset = User.objects.select_related("organization").prefetch_related("department")
# queryset = User.objects.prefetch_related('department')
# queryset = User.objects.filter(organization__id=self.request.user.organization.id).exclude(id=self.request.user.id)
# print(queryset.count())
# print(queryset.exists())
# queryset = User.objects.values_list('id','last_name',named=True)
# queryset = User.objects.values("first_name","last_name")
# queryset = User.objects.values_list("email","date_of_joining")
# queryset = User.objects.values("id","department","organization")
# queryset = User.objects.all()[3:10]

# queryset = User.objects.exclude(last_name__endswith ='i')
# queryset = Department.objects.all().count()
# leave = Organization.objects.all().count()
# queryset = User.objects.filter(first_name__startswith='m') & User.objects.filter(last_name__startswith='U')
# queryset = User.objects.filter(Q(first_name__startswith='m')& Q(last_name__startswith='g'))
# queryset = User.objects.filter(id=1)
# queryset =User.objects.select_related('department').all()

# print(queryset,leave)
# queryset1 = TimeLog.objects.all().count()

# print('Logtime.....',queryset1)






# from datetime import date
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
 
    # a class method to create a Person object by birth year.
    # @classmethod
    # def fromBirthYear(cls, name, year):
    #     return cls(name, date.today().year - year)
 
    # a static method to check if a Person is adult or not.
    # @staticmethod
    # def isAdult(age):
    #     return age > 18
 
 
# person1 = Person('mayank', 21)
# person2 = Person.fromBirthYear('mayank', 1996)
 
# print(person1.age)
# print(person2.age)
 
# print the result
# print(Person.isAdult(22))




# class Dates:
#     def __init__(self,date):
#         self.date = date

    # def getDate(self):
    #     return self.date
    
#     @staticmethod
#     def toDashDate(date):
#         return date.replace("/","+")

# date = Dates("15-12-2016")
# dateFromDB = "15/12/2016"
# dateWithDash = Dates.toDashDate(dateFromDB)
# print(dateWithDash)
# if(date.getDate()==dateWithDash):
#     print("Equal")
# else:
#     print("Unequal")




# class Test :
#     @staticmethod
#     def static_method_1():
#         print('static method 1')

#     @staticmethod
#     def static_method_2() :
#         Test.static_method_1()

#     @classmethod
#     def class_method_1(cls) :
#         cls.static_method_2()

# call class method
# Test.class_method_1()

# class Dog():
#     count = 0
#     dog = []

#     def __init__(self,name):
#         self.name = name
#         Dog.count += 1
#         Dog.dog.append(name)
    
#     def bark(self,n):
#         print("{} say: {}".format(self.name,"woof!" * n))
#     def rollCall(n):
#         print("There are {}dogs.".format(Dog.count))
#         if n >= len(Dog.dog)or n<0:
#             print("they are:")
#             for dog in Dog.dog:
#                 print("{}".format(dog))
#         else:
#             print("The dog indexed at {} is {}.".format(n,Dog.dog[n]))

# fido = Dog("Fido")
# fido.bark(3)
# Dog.rollCall(-1)
# rex = Dog("rex")
# Dog.rollCall(0)

# class Employee(object):

#     def __init__(self,name,salary,project_name):
#         self.name = name
#         self.salary = salary
#         self.project_name = project_name
    
#     @staticmethod
#     def gather_requirement(project_name):
#         if project_name == 'ABC Project':
#             requirement = ["task_1","task_2","task_3"]
#         else:
#             requirement = ['task_1']
#         return requirement
    
#     def work(self):
#         requirement = self.gather_requirement(self.project_name)
#         for task in requirement:
#             print("completed",task)
    
# emp = Employee("Ali",12999,"ABC Project")
# emp.work()




# class Animal(object):
#     def __init__(self,name,species,kingdom):
#         self.name = name
#         self.species = species
#         self.kingdom = kingdom

    # @staticmethod
#     def information(kingdom):
#         if kingdom == 'Animalia':
#             info = ['lion','pantheria','Animalia']
#         else:
#             info = ['lion']
#         return info
    
#     def call(self):
#         info = self.information(self.kingdom)
#         for i in info:
#             print('information collected',i)
# anm = Animal("Lion","Pantheria","Animalia")
# anm.call()



# class Mobile:
#     @staticmethod
#     def show_model(m,p):
#         model = m
#         price = p

#         print("Model:",model,"Price:",price)
# realme = Mobile()
# Mobile.show_model("VIVO Y19",28000)

# class Mobile:
#     fp = 'Yes'

#     @staticmethod
#     def show_model():
#         print("FingerPrint:",Mobile.fp)
# realname = Mobile
# Mobile.show_model()


# class Bank:
#     bank_name = 'BOP'
#     rate_of_interest=12.25
#     @staticmethod
#     def simple_interest(prin,n):
#         si = (prin*n*Bank.rate_of_interest)/100
#         print("Real interest:",si)

# prin = float(input("Enter principle amount:"))
# n = int(input("enter number of years:"))
# Bank.simple_interest(prin,n)

# class Math:
#     def __init__(self,num):
#         self.num = num
#     def addtonum(self,n):
#         self.num = self.num + n
    
#     @staticmethod
#     def add(a,b):
#         return a+b
    
# a = Math(5)
# print(a.num)
# a.addtonum(6)
# print(a.num)


