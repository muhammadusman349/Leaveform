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




class Animal(object):
    def __init__(self,name,species,kingdom):
        self.name = name
        self.species = species
        self.kingdom = kingdom

    # @staticmethod
    def information(kingdom):
        if kingdom == 'Animalia':
            info = ['lion','pantheria','Animalia']
        else:
            info = ['lion']
        return info
    
    def call(self):
        info = self.information(self.kingdom)
        for i in info:
            print('information collected',i)
anm = Animal("Lion","Pantheria","Animalia")
anm.call()
