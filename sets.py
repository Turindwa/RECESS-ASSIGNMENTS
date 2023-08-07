#exercise  find the length of your set ,data type,accessing items in a set,add items,add two sets together
# creating a set using curly braces
set1={1,2,3,4}
print(len(set1))

#creating using a list
set3=set(["one","two","five"])
print(set3)

#printing a datatype
print(type(set1))

#printing the datatype of each element in a set
set5={1,"five",3,"jemily"}
data=set()
for x in set5:
    data.add(type(x))
    print(data)

    #Accessing items in a set using a for loop
    set7={4,5,6,8}
    for i in set7:
        print(i)

        #adding elements in a set
set7.add(9)
print(set7)
        #adding two sets together
print(set7.union(set5))