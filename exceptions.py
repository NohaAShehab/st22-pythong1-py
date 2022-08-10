# print("-------------------------------------")
#
# print(name)  # runtime error --> exception
#
# print("################################")

#
# age = input("please enter your age ")
# age = int(age)

# print("--------------------------------- Exception handling -------------------")
# """
# try:
#     do something
# except:
#     what will happen if there is a problem with the code
#
# """
#
# # age = input("please enter your age : ")
# # # age = int(age)
# # try:
# #     age = int(age)
# # except:
# #     print('this value cannot be casted to int ')
# #
# #
# # print("-----------------------------------------------------------------")
# # print(f"your age is {age}")
#
# # # ########################################
# # age = input("please enter your age : ")
# # # age = int(age)
# # try:
# #     age = int(age)
# # except:
# #     print('this value cannot be casted to int ')
# # else:
# #     # this code will be executed if the try block executed successfully
# #     print(f"your age is {age}")
# #
# # print("-----------------------------------------------------------------")
#
# ######################################################33
# #
age = input("please enter your age : ")
try:
    age = int(age)
except Exception as e:
    print(f'The issue is : {e}')
else:
    # this code will be executed if the try block executed successfully
    print(f"your age is {age}")
finally:
    "this block will be executed always"
    print("&&&&&&&&&&&&&&&&&& Here end of the try block &&&&&&&&&&&&&&&&&&")
print("-----------------------------------------------------------------")

# #
# #
# # ###################################

# #
# ######################################3
#
# try:
#     print(salary)
# except Exception as myexception:
#     # f-style syntax
#     print(f"The issue is:  {myexception}")


###########################################################
#
# print("------------ Raising the exception --------------------------- ")
#
# from modules import  validateNumIntput
#
# def divnumbers():
#     num1 = validateNumIntput("please enter num1 : ")
#     num2 = validateNumIntput("please enter num2 : ")
#     if num2==0:
#         raise Exception("Sorry division by zero is not supported ...")
#     print(f"num1 = {num1}, num2= {num2}")
#     divres = num1/num2
#     return divres
#
#
# d= divnumbers()
#
#


# ######################### when to use the exceptions handling , raising the exception
"""
    1- Exception handling
        --> connect to database 
        --> dealing with files 
        --> sending emails 
        --> connect to network 
        --> socket programming (chat application)
        
        
    2- raising the exception   
        --> division by zero 
        --> invalid input 


"""








