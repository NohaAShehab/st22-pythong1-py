print("------ functions --------------------")
#
# def getfullname(firstname, lastanme):
#     fname = f"{firstname} {lastanme}"
#     print(fname)
#     return
#
# x = getfullname("noha", "shehab")

############################
# def getfullname(firstname, lastanme):
#     fname = f"{firstname} {lastanme}"
#     print(fname)
#     return fname
#
# x = getfullname("noha", "shehab")
#
# m =  getfullname(10, 21)


# ##########3 specify the argumenents types

# def getfullname(firstname:str, lastanme:str):
#     fname = f"{firstname} {lastanme}"
#     print(fname)
#     return fname
#
# x = getfullname("noha", "shehab")
#
# m =  getfullname(10, 21)

#########################################
"You need to do the data validation "

# def sumnum(num1:int, num2:int):
#     res = num1 + num2
#     return  res
#
#
# s = sumnum(10, 20)
#
# m =  sumnum("10", "iti")
#
# n = sumnum(3, [4,5,6])


# def sumnum(num1:int, num2:int):
#     # check, num1, num2 are int ,---
#     if isinstance(num1, int) and isinstance(num2, int):
#         res = num1 + num2
#         return  res
#
#
#
# s = sumnum(10, 20)
#
# m =  sumnum("10", "iti")
#
# n = sumnum(3, [4,5,6])
######################
# def calnums():
#     x = input("please enter num1 ")  #string
#     y =  input("please enter num2 ")  #string
#     if x.isdigit() and y.isdigit():
#         res  = int(x)  + int(y)
#         return res
#
#     print("----- num1 and num2 should be numbers-----------")
#     return calnums()

##############3 function ====> predefined number of arguments
"functions in python support default arguments ----> default arguments must follow non default argument "

"min no of passed parameter user must pass is 1 , max_number is 3 "
# def summnum(num1, num2=100, num3=10):
#     print(f"{num1}, {num2}")
#
#
# summnum(36)
# summnum(5,7)

# ######################################
"write a function that ask the user to enter numbers and return with these numbers multiplied by 2 "


# def mulnum(*nums):  # function accepts zero or more parameter
#     print(nums)  # parameter the user pass ---> will be saved to a tuple
#     print(type(nums))
#     for i  in nums:
#         print(i*2)
#     print("---------------------------------")


# mulnum()
# mulnum(2,3,4,5)


###################################################

def introduceyourself(**args):
    print(args)
    pass

introduceyourself()
introduceyourself(name="noha", worksat="iti")
introduceyourself(name="Ahmed", age=20)
introduceyourself(fname="mohamed",lname="Mostafa",livesin="cairo",study="CS")


