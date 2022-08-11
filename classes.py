print("---------------- classes ------------------")


# emp1 = {
#     "name":"Ahmed",
#     "email": "ahmed@gmail.com",
#     "dept": "opensource"
# }
#
#
# emp2 = {
#     "name": "ali",
#     "email": "ali@gmail.com",
#     "dept": "opensource",
#     "salary": 4000
# }
# emp2 = dict([("name","noha")])
# print(type(emp2))

# class Employee:
#     pass
#
#
# e = Employee()
# print(e)
# print(type(e))
#

##################################
# ### class is considered to be object factory ---> generate more objects
# class Employee:
#     def __init__(self, empame, empemail):  # parameter --> refer to the memory location
#         print(self)
#         self.name = empame
#         self.email = empemail
#
#
# e = Employee("ahmed",
#              "ahmed@gmail.com")  # call function in the class __init__ --> this function used to create the object
# e2 = Employee("ali", "ali@gmail.com")
# # ## python support object-properties  representation in form of dic
# print(e2.__dict__)
###############################################################
# class Employee:
#     # parameter --> refer to the memory location of the object
#     def __init__(self, empame='', empemail=None):
#         print(self)
#         # ############3 name , email ====> properties ==> instance variables
#         self.name = empame
#         self.email = empemail
#
#     # instance method --> functionality is applied to the current object
#     def speak(self, message="nice to meet you"):
#         if self.email:
#             print(f"My name is {self.name}, you can contact me at {self.email} {message}")
#         else:
#             print(f"My name is {self.name}, {message}")
#
# e = Employee("ahmed",
#              "ahmed@gmail.com")
# # call function in the class __init__ --> this function used to create the object
# e.speak("hi , bye")
# e2 = Employee()
# e2.speak()
# # # ## python support object-properties  representation in form of dic
# # print(e2.__dict__)
#

# #################################################

# class Student:
#     #
#     def __init__(self, name="Ahmed"):
#         print("this function is being called where creating the object -constructor-")
#         self.name = name  # instance variable
#
#     # instance method
#     def sayHello(self):
#         print("Hello, I am a student")
#
#     ## to stop adding properties the object
#
#
#
#
# s = Student()
# # s.sayHello()
# "I am trying to modify the object structure in the run time "
# s.email = "ahmed@gmail.com"  # valid or not ?

############################ class variables

# class Student:
#     country = "Egypt"  # class variables
#     count = 0
#
#     def __init__(self, name="Ahmed"):
#         print("this function is being called where creating the object -constructor-")
#         self.name = name  # instance variable
#         # count number of instance
#         # Student.count +=1
#         # self.count +=1
#
#
#     # instance method
#     def sayHello(self):
#         print("Hello, I am a student")
#
#     ## to stop adding properties the object
#
#
# s = Student()
# s.name = "Mostafa"  # modify existing instance variable --> value
# s.email = "a@gmail.com"  # add new instance variable to the class
# print(Student.count)
# s2 = Student("Ali")
# print(Student.count)
#
# # you want to modify the value of the country
# Student.country = "USA"
# s2.country = "ABC"
#
# Student.country = "Egypt"
# print(s2.count)
# s2.count =10
# #################################### class method

class Student:
    country = "Egypt"  # class variables
    count = 0
    allowed = ["name"]
    def __init__(self, name):
        print("this function is being called where creating the object -constructor-")
        self.name = name  # instance variable
        # count number of instance
        Student.count +=1
        # self.count +=1

    # instance method
    def sayHello(self):
        print("Hello, I am a student")

    # class method is considered to be object factory --->  create new objects from the class
    # to use class method --> use python decorators
    @classmethod
    def createNewStudent(cls):
        print("------------ inside create new student ===============")
        print(cls)
        # return Student("default student")
        return cls("default student")

    # @classmethod
    # def testclassmethod(cls):
    #     print(cls)  # represent the class it self
    #     print(Student)

    @classmethod
    def getNumberofStudets(cls):
        return cls.count

    @classmethod
    def addStudents(cls, student1 , student2):
        print("-------------- adding 2 students ------------------------")
        if isinstance(student1, cls) and isinstance(student2, cls):
            name= f"{student1.name} {student2.name}"
            return cls(name)  # return new object




# Student.testclassmethod()
s = Student("Ali")
print(Student.getNumberofStudets())
s2 = Student("Ahmed")
print(Student.getNumberofStudets())
print(Student.count)



m = Student.createNewStudent()
print(m, type(m))

n = Student.addStudents(m,s)
