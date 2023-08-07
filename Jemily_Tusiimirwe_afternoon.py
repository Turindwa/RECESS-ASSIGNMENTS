#Assignment on tuples
phone=("samsung","iphone","tecno","tecno","samsung")
print(phone)
#exercise use the len()with this tuple example
phone_length = len(phone)
print(phone_length)
#tuples showing different data types
data = ("Jemmy", 20,True,3.2)
print(data[0])
print(data[2])
#Assignment on strings
#use len function to determine the length of your string
name = "Jemily Tusiimirwe"
name_length = len(name)
print("the length is:", name_length)
#give an example of using a for loop in a string
for x in name:
    print(x)
#give  an example of slicing in strings
sub1 = name[0:5] 
sub2 = name[:7]
print(sub1)
print(sub2)
#Assignment on dictionaries
#Exercise one:use the values() method to return a list of all values in the dictionary
my_dict = {1:"apple",2:"banana",3:"food"}
my_list = list(my_dict.values())
print(my_list)
#Exercise Two:to check if a key exists in your dictionary
if 1 in my_dict:
    print("The key exists")
else:
    print("The key doesnot exist")
#Exercise Three:Give an example on how to change dictionary items,how to update items
my_dict[1] = "mango"
print(my_dict)
#Exercise Four:Give an example on how to add dictionary items,how to remove dictionary items
#adding a key-value pair to the dictionary
my_dict[5] = "irish"
print(my_dict)
#Removing items from the dictionary
del my_dict[2]
print(my_dict)
#Exercise five:Give an example on how you can loop through a dictionary and also how to nest dictionaries
for key,value in my_dict.items():
    print(key, "->",value)
    #nesting dictionries
    employee1 ={"name":"Jemmy", "age":20}
    employee2 ={"name":"Rose","age":30}
    #nesting
    employees = {"employee1":employee1,"employee2":employee2}
    for employee_info in employees.items():
        print(employee_info)
        #Assignment on Booleans
        #Exercise on how to use a condition to show how to use booleans
        x = int(input("Enter a value"))
        if x > 0:
            print("its posistive")
        elif x < 0:
            print("its negative")
        else:
            print("its zero.")

