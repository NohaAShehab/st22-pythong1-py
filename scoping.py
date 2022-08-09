print("----------- Scoping")

"1- local scope ------------------------------------"


# def myfun():
#     x = 10    # variable with local scope
#     "any variable defined inside the function cannot be accessed ouside it"
#     " x is accessed only in the function myfun"
#     print(x)
#     return True
#
#
# r = myfun()
# print(r)
#
# print(x)  # NameError: name 'x' is not defined

####################################################
# "course is considered to be a global variable ---> can be read from inside the function "
# course = "python"  # global scope
#
# #
# # def testfun():
# #     print(course)
# # testfun()
# #
# def modifyglobal():
#     course = "django"  # will  create new local variable inside the function
#     print(f"from inside the function {course}")  # django
#
#
# modifyglobal()
# print(f"------------------ {course}-----------")  # python

###########################################################

# course = "python"
#
#
# def modifycourse():
#     global course  # interpreter check if there is any variable in the global scope with name course
#     course = "django"
#     print(f"from the function {course}")
#
#
# modifycourse()
# print(f"===================== {course}========")

# ################################### function inside a function ###############################################3


# def outerfun():
#     name = "Ahmed"
#     print("---------- hi from  the outer function -----------------")
#
#     def innerfun():
#         print("####################################3hi from the inner function .....................")
#         print(name)
#         print("------------------- end of inner function ---------------------")
#
#     innerfun()
#
# outerfun()

##########################333

# def outerfun():
#     name = "Ahmed"  # is defined in the local scope of the outer function
#     print("---------- hi from  the outer function -----------------")
#
#     def innerfun():
#         name = "Mostafa"  # create new variable inside the innerfunction scope
#         print("####################################3hi from the inner function .....................")
#         print(name)
#         print("------------------- end of inner function ---------------------")
#
#     innerfun()
#     print(name)
#
# outerfun()

#####################################
def outerfun():
    name = "Ahmed"  # is defined in the local scope of the outer function
    print("---------- hi from  the outer function -----------------")

    def innerfun():
        nonlocal  name
        name = "Mostafa"  # create new variable inside the innerfunction scope
        print("####################################3hi from the inner function .....................")
        print(name)
        print("------------------- end of inner function ---------------------")

    innerfun()
    print(name)

outerfun()
