
print("--------------- lists ----------------------")

'1- to define a list'

# myl = []
#
# nameslist = list([])


'2- list can hold different values form different datatypes '

myl = ["Ahmed",  "iti","Ali", True, 34, "iti",25.5, ['python', "postgres"],  "iti" ]

'3- calculate len of the list'
print(len(myl))

'4- access list elements throught the index'
print(myl[1])
print(myl[5][0])

'5- lists are mutable datatype --> can be updated after creation'

myl[3] = "updated value"
# myl[10] = "noha"  # list assignment index out of range

'6- append element at the end of the list'
myl.append("appended")


'7- insert element in the list -- insert at certain position --- '
myl.insert(4, "Django")

'8- pop element from the list'
popped_item = myl.pop()

'pop can accept index ---> remove item at certain index'

mypopped_item= myl.pop(5)

'9- remove item from the list'

myl.remove("iti") # remove the first occurrence of the element


'10- sort the list --> list items must be from the same type ---> sort element in the same array'
# names = ["mostafa", "ahmed", "ali", "omar","mohamed", "sara", "Zainab"]
# # ascii code capital letter < ascii code of the small letter
# # names.sort()
# names.sort(reverse=True)

'11- reverse '
myl.reverse()

'12 -  extend lists '
l1 = ["python", "django", 'postgres']
l2= ["ai", "freelancing", "mongo", "python"]

l1.extend(l2)

'12 - list concatnetation '
l1 = ["python", "django", 'postgres']
l2= ["ai", "freelancing", "mongo", "python"]
courses = l1 + l2

'13 - get index of element in the list '
print(l1.index("django"))

'14- membership, check if python in l1, in operator'
print("python" in l1)

'15- min and max ---> must be from the same type '
l = [4,5,6,7,666]
print(min(l))


'16- loop over the list ---> iterable---> you can loop over its elements using for in '
print("--------------------------------")
for item in l:
    print(item)