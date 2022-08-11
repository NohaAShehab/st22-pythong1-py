print("")
#
# # all the class in Python ---> data structure class inherits from class Object
# # all classes implicitly inherits class object
#
# class Test:
#     def __init__(self,name, email):
#         self.name = name
#         self.email = email
#
#
# t = Test("Ali", "")
################################ -1 define basic inheritance ###################################################
"1- basic inheritance"
# class Person:
#     def __init__(self, name, gender, nid):
#         self.name = name
#         self.gender = gender
#         self.nid = nid
#
#     def speak(self):
#         print(f"My name is {self.name}, called from the parent class")
#
#
# class Employee(Person):
#     pass
#
#
# e = Employee("Ahmed", "a@gmail.com", 10)
# e.speak()
################################
# "2- def __init__ in the Employee "
# class Person:
#     def __init__(self, name, gender, nid):
#         self.name = name
#         self.gender = gender
#         self.nid = nid
#
#     def speak(self):
#         print(f"My name is {self.name}, called from the parent class")
#
#
# class Employee(Person):
#     def __init__(self,email, dept,salary):
#         self.email = email
#         self.dept = dept
#         self.salary = salary
#
#
# e = Employee("Ahmed", "a@gmail.com", 10)
# # e.speak()
##################3
"3- call the parent constructor in the child"
# "2- def __init__ in the Employee "
# class Person:
#     def __init__(self, name="", gender="", nid=""):
#         self.name = name
#         self.gender = gender
#         self.nid = nid
#
#     def speak(self):
#         print(f"My name is {self.name}, called from the parent class")
#
#
# class Employee(Person):
#     # def __init__(self,email, dept,salary, name="emp",gender="male", nid=1):
#     def __init__(self,email, dept,salary):
#
#         super().__init__()
#         self.email = email
#         self.dept = dept
#         self.salary = salary
#
#
# e = Employee("Ahmed", "a@gmail.com", 10)
# # e.speak()

#########################################
"2- def speak in the Employee "
class Person:
    def __init__(self, name="", gender="", nid=""):
        self.name = name
        self.gender = gender
        self.nid = nid

    def speak(self):
        print(f"My name is {self.name}, called from the parent class")


class Employee(Person):
    # def __init__(self,email, dept,salary, name="emp",gender="male", nid=1):
    def __init__(self,email, dept,salary):
        super().__init__()
        self.email = email
        self.dept = dept
        self.salary = salary

    def speak(self):
        super().speak()
        print("this function is called from the Employee class ")

e = Employee("Ahmed", "a@gmail.com", 10)
e.name ="noha"
e.speak()