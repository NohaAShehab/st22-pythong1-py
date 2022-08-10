print("---------- Modules ----------------------")

"""

Any python file is considered to be a module 


"""

"ask the user to enter input and check if the input is string or not "


def validateNumIntput(msg):
    val = input(msg)
    if val.isdigit():
        val = int(val)
        return val

    return validateNumIntput(msg)


# x = validateNumIntput("please enter your age: ")
# print(x)



def sayhello(name):
    print(f"Hello {name}, Nice to meet you ")