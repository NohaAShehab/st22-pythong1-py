print("")

"""1-Access modifiers

    public --> accessed anywhere in , out the class
    protected ---> accessed only inside the class or the derived class
    private ----> accessed only in the class --> need setters and getter 
    static ---> accessed via className 
    ----------------------------------------------
    in python ---> no access modifiers
    
    public --> accessed anywhere in , out the class (( no problem))
    protected ---> accessed only inside the class or the derived class ((_variablename)
    ###
    private ----> accessed only in the class --> need setters and getter ((__variablename) it works
    static ---> accessed via className  ((class variable ))
"""

#
# class Engineer:
#     def __init__(self, name, email, salary):
#         self.name = name
#         self._email = email
#         self.__salary = salary
#
#
#     def speak(self):
#         print(f"{self.name}, {self._email}")
#
# e = Engineer("Ahmed", "ahmed@gmail.com", 1000)
# print(e.name)
# e.speak()
# print(e._email) # ethically don't do that
# print(e.__salary)
# ##################
"3- setter and getter "


# class Engineer:
#     def __init__(self, name, email, salary):
#         self.name = name
#         self._email = email
#         self.__salary = salary
#
#     def speak(self):
#         print(f"{self.name}, {self._email}")
#
#     def setSalary(self, sal):
#         self.__salary = sal
#
#     def getSalary(self):
#         return self.__salary
#
#
# e = Engineer("Ahmed", "ahmed@gmail.com", 1000)
# print(e.name)
# e.name = "Ahmed Ali"
# e.speak()
# print(e._email)  # ethically don't do that
# print(e.getSalary())
# e.setSalary(20000)


##################################################
# "property"
#
# class Engineer:
#     def __init__(self, name, email, salary):
#         self.name = name
#         self._email = email
#         self.__salary = salary
#
#     def speak(self):
#         print(f"{self.name}, {self._email}")
#
#     # def setSalary(self, sal):
#     #     self.__salary = sal
#
#     # def getSalary(self):
#     #     return self.__salary
#     @property
#     def salary(self):
#         return self.__salary
#
#     @salary.setter
#     def salary(self, sal):
#         if isinstance(sal,int):
#             if sal > 1000:
#                 self.__salary = sal
#             else:
#                 self.__salary = 1000
#         else:
#             self.__salary =1000
#
#
#
# e = Engineer("Ahmed", "ahmed@gmail.com", 1000)
# print(e.name)
# e.name = "Ahmed Ali"
# e.speak()
# print(e._email)  # ethically don't do that
#
# # e.setSalary(20000)
# e.salary = 1
# # print(e.getSalary())
# print(e.salary)

################################3
# class Engineer:
#     def __init__(self, name, email, salary):
#         self.name = name
#         self._email = email
#         # self.__salary = salary
#         self.salary = salary
#
#     def speak(self):
#         print(f"{self.name}, {self._email}")
#
#     # def setSalary(self, sal):
#     #     self.__salary = sal
#
#     # def getSalary(self):
#     #     return self.__salary
#     @property  # use private variable
#     def salary(self):
#         return self.__salary
#
#     @salary.setter
#     def salary(self, sal):
#         if isinstance(sal,int):
#             if sal > 1000:
#                 self.__salary = sal
#             else:
#                 self.__salary = 1000
#         else:
#             self.__salary =1000
#
#     @property
#     def netsalary(self):
#         return self.__salary * .8
#
#
#
# e = Engineer("Ahmed", "ahmed@gmail.com", "test")
# print(e.name)
# # e.name = "Ahmed Ali"
# # e.speak()
# # print(e._email)  # ethically don't do that
# #
# # # e.setSalary(20000)
# # e.salary = 1
# # # print(e.getSalary())
# # print(e.salary)
# print(e.netsalary)
# print(e.__dict__)

############################## --- str----
class Engineer:
    def __init__(self, name, email, salary):
        self.name = name
        self._email = email
        # self.__salary = salary
        self.salary = salary

    def speak(self):
        print(f"{self.name}, {self._email}")

    @property  # use private variable
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, sal):
        if isinstance(sal, int):
            if sal > 1000:
                self.__salary = sal
            else:
                self.__salary = 1000
        else:
            self.__salary = 1000

    @property
    def netsalary(self):
        return self.__salary * .8

    def __str__(self):
        # must return with a string
        return f"Engineer({self.name},{self._email}, {self.__salary})"

    def __len__(self):
        # must return with an integer
        return len(self.__dict__)

    def __call__(self, *args, **kwargs):
        print(args, kwargs)
        print("object is not callable")

    def printEng(self):
        return f"Engineer({self.name},{self._email}, {self.__salary})"


e = Engineer("noha", "noha@gmail.com", 1000000)
print(e)
print(len(e))
# print(e.printEng())
e(10, name='noha')
l  =["fff", 444]
print(l)
print(l.__str__())
print(len(l))