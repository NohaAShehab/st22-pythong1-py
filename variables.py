

# print("my first python script")
#
# # this is a comment in python
#
# # 1- to define variable in python ,,,
# x = 10
# name = "noha"
# X = 'iti'
#
# paragraph = 'welcome to it ' \
#             'nice to meet you '
#
# print(paragraph)
#
# # multi-line string
# p = """this is my first day with python
# python is so easy
# you will enjoy it
# """
#
# print(p)
# ##########################
# '''
#     Python is loosly dynamically typed lang...
#
#     no need to define the data of the variable
#
#    x = 10 # interpreter detect the datatype of the variable in the runtime
#
#    --> change data of the variable
# '''
#
# x = 10  #int
# x = 'iti'  # string
#
# # #### to display type of variable
#
# print(type(x))  # class str--->
# #############################  Python support type conversion ######################

# num = 100  # str
# num = str(num)  # valid

# num = '2022'
# num = int(num)  # convert from string to int

#
# num = 'noha'
# # num = int(num)  # invalid literal for int() with base 10: 'noha'
#
#
# """
#     you can only convert from str to int only if the string contains numeric value,
#
#     ---> str var  ---. varname.isdigit(),  varname.isnumeric()
# """
#
# # print(num.isdigit())
#
# ''' ++;  '''
#
# ''' == compare the values and datatypes '''
# # print(5=="5")  #
# # ''' True implicitly = 1 , False = 0'''
# # print(True == 1)
# # print(True==4)
#
#
# ######################
# print(10 and 0)  # False
#
# print(100 and 10)
#
# """ and --> all parts evaluate to True ---> and scan all the expression parts """
# # print(100 and 10 and 9)
# #
# # print(100 and 0 and 9)
#
#
# print(100 or 0 or 9)
#
#
# x = 10
# y = 1000
#
# if x and y:  # x and y (1000)
#     print("hiii")
#
# # ########################3 string
# # name = "Noha abdElHady"
# # print(len(name))
# # print(name.count("a"))
# # print(name[10])
# # print(name[-4])
#
#
# firstname = "Noha "
# midname = 'Abdelhady '
# lastname = "Shehab"
# fullname = firstname + midname + midname + lastname
# print(fullname)

#
# fullname= firstname + midname*2 + lastname
# print(fullname)


##########################3

# sen = "Welcome to python course provided by our Instructor @"
#
# print(sen.replace("@", "Noha"))
#
# print(sen.replace("@", "Ahmed"))

#############
# money = "I have @$ pound"
# # print(money.replace("@", 1000))
# print(money.replace("@", str(1000)))  # replace only string




totalmoney = 1000
name = "noha"
# temp = "Student {0} have total money ={1}"
#
# print(temp.format(name, totalmoney))
# print(temp.format(totalmoney,name))

# name = "noha"
# temp = "Student {studentname} have total money ={money}"
#
# print(temp.format(studentname=name, money=totalmoney))
# print(temp.format(money=totalmoney))

########################33 f-format

# year = 2019
# fname = 'noha'
# lastname  = 'shehab'
#
# myinfo = f"My name is {fname} {lastname} I am working in iti since {year}."
#
# print(myinfo)
# #####################33 trim

# msg = "     welcome to iti       "
#
# print(msg)
# print(len(msg))
# msg = msg.strip()  # remove spaces from the beginning and the end of the string
# print(msg)
# print(len(msg))


# msg = "%%%% My name is Noha %%% "
#
# print(msg)
# print(len(msg))
# msg = msg.strip("% a")  # remove spaces from the beginning and the end of the string
# print(msg)
# print(len(msg))


#############
# msg = "%%%% My name is Noha %%% a"
#
# print(msg)
# print(len(msg))
# msg = msg.lstrip("% a")  # remove specified chars from the left (beginning of the string)
# print(msg)
# print(len(msg))

# msg = "%%%% My name is Noha %%% a"
#
# print(msg)
# print(len(msg))
# msg = msg.rstrip("% a")  # remove specified chars from the right (end of the string)
# print(msg)
# print(len(msg))


###########################3
# txt = "                                "
# print(len(txt))
# if txt:
#     print("hi")
# else:
#     print("bye")
#
# print(txt.isspace())
############################## Numbers

c= 4+5j  # complex number
myc = complex(5,6)


















