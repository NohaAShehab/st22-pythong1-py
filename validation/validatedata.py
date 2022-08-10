print("----------validate data Module ----------------------")

"""

Any python file is considered to be a module 


"""

"ask the user to enter input and check if the input is string or not "


def validateIntInput(msg):
    val = input(msg)
    if val.isdigit():
        val = int(val)
        return val

    return validateIntInput(msg)


# x = validateNumIntput("please enter your age: ")
# print(x)



def saywelcome(name):
    print(f"Welcome {name}, Nice to meet you ")