# from modules import validateNumIntput, sayhello
#
# def sumnums():
#     num1 = validateNumIntput("Please enter num1 : ")
#     num2 = validateNumIntput("Please enter num2 : ")
#     sum = num1 + num2
#     return  sum
#     ##########################
#
#
# # res = sumnums()
# # print(res)
# #
# #
# # sayhello('Noha')

# ############################### import all the module
# import modules
#
# def sumnums():
#     num1 = modules.validateNumIntput("Please enter num1 : ")
#     num2 = modules.validateNumIntput("Please enter num2 : ")
#     sum = num1 + num2
#     return  sum


# ################### Alias

# import modules as m
#
# def sumnums():
#     num1 = m.validateNumIntput("Please enter num1 : ")
#     num2 = m.validateNumIntput("Please enter num2 : ")
#     sum = num1 + num2
#     return  sum
#
# #################################### package ######################33
# from validation.validatedata import validateIntInput
#
#
# x = validateIntInput("this my messge")


# #################### import module from package
# import validation.validatedata
#
# validation.validatedata.saywelcome("bla bla bla ")
#######################
import validation.validatedata as vd
vd.saywelcome("Ahmed")









