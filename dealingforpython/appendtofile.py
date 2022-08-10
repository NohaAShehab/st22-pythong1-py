print("---------------- writing the file ---------------")


""" 
    open(filename, 'a') ---> 
    if the file exists ---> open the file for writing starting from the end of the file 
    if the file is not exists --> python try to create the file 
"""

try:
    fileobj=open("students.txt","a")  #
except Exception as e:
    print(f"issue is {e}")
else:
    print(fileobj)

    # data = fileobj.write("this my lines\n")

    l = ['Ahmed\n', "Ali\n", "Mohamed\n", "Sara\n"]
    fileobj.writelines(l)


