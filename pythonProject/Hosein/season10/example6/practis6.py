from abc import ABC, abstractmethod

# class Employee(ABC):
#     @abstractmethod
#     def salary_calculate(self):
#         """"please implement method"""


# class HourlyEmployee(Employee):
#     def salary_calculate(self, x):
#         return x ** 2
    
# class SalariedEmployee(Employee):
#     def salary_calculate(self, x):
#         return x + 10
    

# a = HourlyEmployee()
# b = SalariedEmployee()
# print(a.salary_calculate(4))
# print(b.salary_calculate(4))

# --------------------------------------------

# class Car(ABC):
#     @abstractmethod
#     def start(self):
#         """"please implement method"""

#     def stop(self):
#         """"please implement method""" 


# class SportCar(Car):
#     def __init__(self, brand):
#         self.brand = brand

#     def start(self):
#         return "I am put 100km/h in the 8.3 second"
    
#     def stop(self):
#         return "I am stop in the 5 meter"


# class SedanCar(Car):
#     def __init__(self, brand):
#         self.brand = brand

#     def start(self):
#         return "I am put 100km/h in the 12 second"
    
#     def stop(self):
#         return "I am stop in the 7 meter"
    

# BMW = SportCar("bmw m4")
# BENZ = SedanCar("benz c200")

# print(BMW.start())
# print(BMW.stop())
# print(BMW.brand)

# ---------------------------------------------

# class Person(ABC):
#     @abstractmethod
#     def introduce(self):
#         """"please implenets method"""


# class Student(Person):
#     def __init__(self, name, age, plane):
#         self.name = name
#         self.age = age
#         self.plane = plane

#     def introduce(self):
#         return f"my name is {self.name} and {self.age} years old and i am a {self.plane}" 


# class Teacher(Person):
#     def __init__(self, name, age, plane):
#         self.name = name
#         self.age = age
#         self.plane = plane

#     def introduce(self):
#         return f"my name is {self.name} and {self.age} years old and i am a {self.plane}" 
    

# hosy = Student("Hossein", 18, "student")
# khalili = Student("Majid", 40, "teacher")

# print(hosy.introduce())
# print(khalili.introduce())