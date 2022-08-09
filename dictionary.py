# dictionary
print("---------- this is sets -------- ")
# # Set
#
# " set ---> unsorted data structure  =--->(no index) "
#
# s = {"Python", "Django", "Postgres", "odoo"}
# print(s)
# print(type(s))
#
#
# '''2- set can hold different values form different datatypes,
# set doesn't allow duplicates
# '''
# s = {"Python", "Django", "Postgres", "odoo", 10, "odoo"}
#
# l = ["Ahmed", "Ali", "test", "Ahmed","Ahmed"]
# print(l.count("Ahmed"))
# newl = set(l)
#
# '3- calculate len of the set'
# print(len(s))
#
# '4- sets are mutable datatype --> can be updated after creation'
# s.add("new element")
# '5- pop element from the set'
# # popped=s.pop()  # remove from the last
# '5- remove element from the set'
# s.remove("Python")

'6 -  update sets '

# s1 = {"python", "postgres"}
# s2= {"django", "flask"}
#
# s1.update(s2)
# print(s1)


# '7- membership, check if python in s1, in operator'
# s1 = {"python", "postgres"}
# print("python" in s1)


'15- min and max ---> must be from the same type '

# s ={3,4,7,6,333}
# print(min(s))
#
#
# '16- loop over the set ---> iterable---> you can loop over its elements using for in '
# print("--------------------------------")
# for item in s:
#     print(item)
# ###################################################
""" from python 3.7  ---> dictionary items are sorted in the memory """

print("------------ dictionary -----------------")
"""key-value pair datatype --- 


    "name": "noha"

"""

'1- to define a dic'
# d =  {}
# d2 = dict([])


'2- dic can hold different values form different datatypes '
myinfo = {
    "name":"noha",
    "id":10,
    "track": "opensource",
    'courses': ["python", "postgres"],
    100: "ITI"

}
"no key duplication in dictionary"

'3- calculate len of the list'
print(len(myinfo))


'4- access list elements throught the index'
print(myinfo["name"])
print(myinfo[100]);


'5- dic are mutable datatype --> can be updated after creation'
myinfo["name"] = "NohaShehab"
myinfo[10]=101010  # 10 is considered to be a dictionary key


'6- add element at the end of the dic'

myinfo["city"] = "cairo"


'7- pop element from the dic-- > remove element at certain key '
popped=myinfo.pop(10)


'8- dic update'

d1 ={
    "name": "noha",
    "id": 10,
    "track": "opensource",
    'courses': ["python", "postgres"],
    100: "ITI"
}
d2 = {
    "test":"bla bla bla",
    "students":["Ahmed", "Ali"]
}

d1.update(d2)

# '9- get the keys of dic '
# print(myinfo.keys()) # dic_keys  ---> not subscriotable
# keys = myinfo.keys()
# print(type(keys))
#
# keys = list(keys)
# print(keys[0])

# '10- get the values of dic '
#
# print(myinfo.values()) # dic_values  ---> not subscriotable
# values = myinfo.values()
# print(type(values))
#
# values = list(values)
# print(values[0])

"11- dict_values "
# items = myinfo.items()  # dict_items
# print(items, type(items))
#
# items = list(items)
#
# print(items)


"12- loops"
# for i in myinfo:  # i --> represent the key
#     print(f"{i}, {myinfo[i]}")


for k,val in myinfo.items():
    print(f"k ---> {k}, value= {val}")


"12 - check existence ---> in operator"

print("NohaShehab" in myinfo) # check if the NohaShehab exists in the keys


print("NohaShehab" in myinfo.values())

"13- remove all elements from the dic in one step"

# myinfo.clear()

"14- delete or remvoe any varaible from the memory "

# del my-info
#
# del popped

del d2["test"]
#
"15- cast the dic into a list "

myinfo2 =  list(myinfo)  # retrun list of the keys



####### JSON