print("----------- Reading from file ------------------")

"write console application that reads the file content"


"1- open the file with read mode---> open(filename,readmode) "
try:
    fileobj = open("mycv.txt", "r")
    # fileobj = open("mycv.txt")  # consider the mode to be read mode

except Exception as e:
    print(f"issue with opening the file {e}")
else:
    print(fileobj)
    # here I will use the object to read the data from the file
    # "read the data into one string "
    # data = fileobj.read() # read the data into one string
    # print(data)
    "read the data into lines"
    lines = fileobj.readlines()  # read file content in a list (each element represent the lines in the file
    print(lines)

    fileobj.close()
