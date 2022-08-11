class Employee:
    count = 0  # class variables
    country = "Egypt"
    __slots__ = ["name", "email", "salary"]
    # constructor
    def __init__(self, name, email,salary=10000):
        self.name = name  # instance variables
        self.email = email
        self.salary = salary
        Employee.count +=1

    # instance method
    def speak(self):  # self --> object- >>> memory location
        print(f"My name is {self.name}")

    # class method
    @classmethod
    def createNewStudent(cls):
        return cls("default", "default")

    # helper method
    @staticmethod
    def calnetsal(sal):
        return sal * .8

############### instance
s = Employee("Ahmed", "ahmed@gmail.com")
s.name = "Mohamed"
print(s.email)
s.speak()
##################3 class
print(Employee.count)
Employee.country = "USA"
news = Employee.createNewStudent()
################
news.salary = 3000
# cal net salary ---> using static method
"you call it using class name "
res = Employee.calnetsal(news.salary)
"you can call it using the instnace"
rr = s.calnetsal(s.salary)
m = s.calnetsal(6666666666666666)

# netsal = calnetsal(news.salary)
# mm = calnetsal(1000000000)