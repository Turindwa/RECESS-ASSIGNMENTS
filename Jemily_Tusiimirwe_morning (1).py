age=21
if age<18:
    print("your underage")
elif age>= 18 and age <= 65:
 print("you are adult")
else:
    print("you are a senior citizen")
    #using a for loop
    fruits=[1,2,3,"jem","wee"]
    for x in fruits:
        print(x)
        #using while loops
j=1
while j<10:
   print(j)
   if j==6:
    break  #using break 
j += 1

#Exception handling
try:
    number=[1,2,3,4]
    print(number[5])
except IndexError:
    print("index is out of bounds")
finally:
    print("This is a finally block")

    #Another example
try:
    z="Jemily"
    print(z)
except:
    print("An error occured")
finally:
    print("This runs always")

#Assignment
#Using an input keyword to ask students about their mental health
name = input("Please enter your name:")
print("Hello" + name)
print("let me assess your mental health")
state = input("How do you feel today?")
print("You are really" + state )
print("Thanks for your time"  + name)
