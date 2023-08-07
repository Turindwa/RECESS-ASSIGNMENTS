#Exception handling
#Example1:
def fun(a):
    if a < 4:
        b = a-3
 
    # throws NameError if a >= 4
    print("Value of b = ", b)
     
try:
    fun(3)
    fun(5)
 
except ZeroDivisionError:
    print("An error Occurred ")
except NameError:
    print("NameError Occurred ")
finally:
    print("This is a finally block!")

#Example2
x=8
y="Jemmy"
try:
 z = x + y
 print(z)
except TypeError:#handles the type error
    print("an error occured")
finally:#this will always execute
    print("am jemily")
    

    #File handling
    #file handling in python allows you to perform a wide range of operations such as creating,reading,writing,appending,renaming and deleting files
    #it allows to work with different file types e.g text files, binary files
    #Example: using an Open() function;this is done before any other operation is done
    file = open('jem.txt', 'r')
    for each in file:
        print(each)#prints every line in the file
    #file.read()
        print(file.read())
    #reading the file using the "with statement"
    with open("jem.txt") as file:
        data = file.read()
        print(data)
    #using the split() function 
    # This splits the variable when space is encountered
    for line in data:
        word = line.plit()
        print(word) 
    #creating a file using the write() function
    file = open('jem.txt','w')
    file.write("This is the write command")
    #using append(); this is used to add some text to the file
    file.append("This is the append command")
    file.close() 



