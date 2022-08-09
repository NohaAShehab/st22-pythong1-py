print("ranges")
""" ranges"""

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# r = range(10)
#
# "range(0,1,10) ---> start=0,1 ,stop-1 "
# r = list(r)
# print(r)
#
#
# myr = range(10, 100, 2)
# print(list(myr))
#
# for i in myr:
#     print(i)

# ###########33 "while loop"
"while ---> unknown number of times "
# x= 0
# while x < 5:
#     print(x)
#     x +=1
# #################### "Pass"


"""if(condition){
    ## testing 
}"""
#
# if True:
#     pass # represnet empty block
#
#
# for i in range(5):
#     pass
#
#
# for _ in range(5):
#     print(_)
########################3

#
# for i in range(10):
#     # if i==4:
#     #     continue
#     print(i)
# else:
#     "this block will be executed if the loop reached the end"
#     print("---------------- Here we are -------------------------------")
#
# print("-------------------------------------------")


# ##########3 input function

x = input("please enter number") # always return with string
if x.isdigit():
    x= int(x)
print(x)

###################
import getpass

s =  getpass.getpass("please eneter your password")






