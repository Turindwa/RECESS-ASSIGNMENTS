#Exercise one
#Lists
name=["Jemmy","Ben","Cathy","Molly","Cissy"]
print(name[1])
#Changing the value
name[0]="John"
print(name)
#adding an item to the list
name.append("Bethel")
print(name)
#adding an item at a particular index
name.insert(3,"Bonitah")
print(name)
#removing an item
name.remove("Ben")
print(name)
#printing last item
print(name[-1])
#second list
numbers = [1,2,3,4,5,6,7]
print(numbers[2:5])
#list of countries
country = ["Uganda","Kenya","Tanzania"]
go = country.copy()
print(go)
#looping through
for c in country:
    print(c)
    #alist of animal names
    animal = ["dog","cat","cow","zebra"]
    #ascending order
    ascending =sorted(animal)
    print(ascending)
    #descending
    descending = sorted(animal, reverse=True)
    print(descending)
    #printing animal names with letter 'a'in them
    animal_with_a=[]
for ani in animal:
    if "a" in ani:
        animal_with_a.append(ani)
        print(animal_with_a)
#joining two lists
first_name =["Jemily",]
second_name =["Tusiimirwe"]
joined=first_name + second_name
print(joined)

#Exercise 2 (Tuples)
x = ("samsung","iphone","tecno","redmi")
print("my favorite phone is:"+ x[1] )
#printing the second last item
print(x[-2])
#updating iphone to itel
updated = x[:1] + ("itel",) + x[2:]
print(updated)
#adding an item in a tuple
new_x = x + ("Hwawei",)
print(new_x)
#looping through a tuple
for item in x:
    print(item)
    #deleting an item from a tuple
    new_tuple = x[1:]
    print(new_tuple)
    #tuple constructor
    city = (["Kampala","Mbarara","Fortportal","Masaka"])
    #unpacking a tuple
    city1,city2,city3 = city
    print(city1)
    #using range of indexes
    print(city[1:4])
    #joining teo tuples
    name_one= ("Jemily")
    name_two = ("Tusiimirwe")
    My_name = name_one + name_two
    print(My_name)
    #multiplying a tuple of colors by 3
    colors = ("red","blue","green")
    multi = colors * 3
    print(multi)
#Returning the number of times 8 appears in a tuple
thistuple = (1,3,7,8,7,5,4,6,8,5)
count = thistuple.count(8)
print(count)

#Exercise 3(sets)
#using set constructor
fav = set(["tea","coffee","juice"])
#adding items to the set
fav={"tea","coffee","juice"}
fav.add("soda","water")
#checking if an element exists in the set
myset = {"oven","kettle","microwave","refrigerator"}
item = "microwave"
if item in myset:
    print("Element exists")
else:
    print("element doesnot exist")
    #looping through a set
for g in myset:
    print(g)
   #adding elements in a list to those in a set
    set = {1,2,3,4}
    list = [5,6]
    set.update(list)
    print(set)
    #joining two sets
    set1 = {20,30}
    set2 ={"John","Jemmy"}
    joined = set1.union(set2)
    print(joined)

    #Exercise4(Strings)
    #concatenating a string and an integer
    a=30
    b="phone"
concat= b + str(a)
print(concat)
    #printing a string without spaces
txt = " Hello, Uganda! "
word = txt.strip()
print(text)
#converting the text to uppercase
upper = txt.upper()
print(upper)

#Replacing character "u" with "v"
me=txt.replace('u','v')
print(me)
#using a range of characters
y = "I am proudly Ugandan"
print(y[1:4])
#correcting an error
x= 'All"Data Scientists" are cool!'

#Exercise5(Dictionaries)
shoes = {
    "brand": "Nick",
    "color": "black",
    "size":40
}
print(shoes[size])
#changing Nick to Adidas
shoes["brand"] = "Adidas"
print(shoes["brand"])
#adding another value pair
shoes["type"] = "Sneakers"
print(shoes)
#returning the list of keys
keys = list(shoes.keys())
print(keys)
#returning list of values
values = list(shoes.values())
print(values)
#checking if size exists
if "size" in shoes.keys():
    print("size exists")
#looping through the dictionary
for n in shoes:
    print(n)
    #removing a certain item
    del shoes["color"]
    ptint(shoes)
    #empty the dictionary
    del shoes
    #copy of the dictionary
    jemmy = {
        "name":"jem",
        "year": 20
    }
    ne= jemmy.copy()
    print(ne)
    #nested dictionary
    jem = {
     "stud":{
     "nam":"jemmy",
        "age": 30},
        
         "gal": {  "campus":"muk",
         "year":2
        }
    }

    print (jem["stud"]["nam"])

    









































































































































































































