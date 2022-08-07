print("---- tuples-----")
"""
    tuple one of the basic data structure in python 
    --> sequence 
    --> immutable datatype --> once created cannot be 
    changed during the time 
"""
'1- to define a tuple'

# t = ()
# myt = tuple([])

'2- tuple can hold different values form different datatypes '
myt= ("Ahmed", 10,3.14, False, ['python', 'django'])

'3- calculate len of the tuple'
print(len(myt))


'4- access tuple elements throught the index'
print(myt[1])
print(myt[4][0])


'5 - tuple concatnetation '
t1 = ("python", "django", 'postgres')
t2= ("ai", "freelancing", "mongo", "python")
courses = t1 + t2


'6 - get index of element in the tuple '
print(t1.index("django"))

'7- membership, check if python in l1, in operator'
print("python" in t1)


'8- min and max ---> must be from the same type '
t= (4,5,6,7,666)
print(min(t))

names = ("noha", "Ahmed", "test","ali")
print(min(names))

print("--------------------------------")
for item in t:
    print(item)


'9- tuple of one item'
i = ("Ahmed",)

'10- convert list to tuple and vice versa'

# l1 = ["python", "django", 'postgres']
#
# l1 = tuple(l1)
#

course_t= ("python", "django", 'postgres')
course_t = list(course_t)




