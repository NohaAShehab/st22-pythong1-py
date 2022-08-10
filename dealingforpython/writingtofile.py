print("---------------- writing the file ---------------")


""" 
    open(filename, 'w') ---> 
    if the file exists ---> open the file for writing starting from the begining of the file 
    if the file is not exists --> python try to create the file 
"""

try:
    fileobj=open("students.txt","w")  # this will erase the data in the file
except Exception as e:
    print(f"issue is {e}")
else:
    print(fileobj)

    s=fileobj.write("My name is noha\n")  # s--> no of bytes written to the file
    fileobj.write("I lives in cairo")


