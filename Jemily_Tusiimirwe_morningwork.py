#Day3
#Basic operators and Expressions(Input and output operators)
"""
-Arithmetic operators
+Addition
-Subtraction
*multiplication
/Division
//Divide
%Modulus
**Exponentiation

-Comparison Operators
==Equal to
!= Not Equal !==
>Greater than
< Less than
>= Greater than or equal to
<= Less than or equal to

-Logical Operators
Logical AND 'and'
Logical Not:'not'

-Assignment Operators
Assign value:'+='
Subtract and assign value:'-='
Multiply and assign value:'*='
Divide and assign value:'/='
Modulus and assign value:'%='
Exponentiate and assign value:'**='

-Membership Operators:
In:'In' operator:checks if a value exists in a sequence
Not in:'not in' operator: checks if a value does not exist in a sequence

-Identity operators
Is:'is' operator:checks if two values are the same
Is not: 'is not' operator:checks if two values are not the same

"""
#Examples
#Addition
x = 20 + 10
print(x)
#subtraction
b = 4 - 2
print(b)
#Division
y = 20 / 2
print(y)
#Divide
z = 20 // 2
print(z)
#modulus
d = 20 % 2
print(d)
#Multiplication
e = 2 * 3
print(e)
#Exponentiate
f = 2 ** 4
print(f)
#Comparison operators
a = 5
b = 9
if a <= b:
    print("a is less than or equal to b")
if a == b:
    print("a is equal to b")
    print(a==b)
if a > b:
    print("a is greater than b")
    #Not equal to
if(a != b):
 print(a)
#Logical operators
h = True
j = False
#logic and
print(h and b)
#logic or
print(a or b)
#logical NOT
print(not h)
print(not b)

#Assignment operators
#compound assignment operators
#Add and assign
g = 2
g += 5
print(g)
#membership operators
cars = ['jeep','telsa','BMW']
if 'jeep' in cars:
    print("jeep is in the list")
    #identity operators
    s = 12
    k = 12
    print(s is k)
    print(h is not k)
    m=[1,2,3]
    w=[1,2,3]
    print(m is w)
     #Bitwise operator
"""
These are used to perform operttions on bits of binary numbers
Bitwise AND ("&"):performs a bitwise AND operation between two corresponding bits of two integers
Bitwise OR ("|"):performs a bitwise OR operation between two corresponding bits of two integers
Bitwise XOR("^"):performs a bitwise X operation between two corresponding bits of two integers
Bitwise NOT("~":performs a bitwise NOT operation between two corresponding bits of two integers
Bitwise left shift(">>"):performs a bitwise left shift operation
Bitwise right shift ("<<"):performs a bitwise  right  shift operation
"""
#Bitwise AND
v=10
a=20
result_and=v & a
print(result_and)
#Bitwise OR
result_or=v | a
print(result_or)
#Bitwise XOR
result_xor=v ^ a
print(result_xor)
#Bitwise not
result_not=v ^ a
print(result_not)


def add(number1,number2):
        print(number1 + number2)
def subtract(number1,number2):
        print(number1 - number2)
def multiply(number1,number2):
        print(number1 * number2)
def divide(number1,number2):
        print(number1 / number2)
def main():
        print("simple calculator")
        number1 = float(input("Enter the first number:"))
        number2 = float(input("Enter the second number"))
        operator = input("Enter operator(+,-,*,/)")
if operator == '+':
    result = add(number1,number2)
elif operator == '-':
    result = subtract(nmber1,number2)
elif operator == '*':
    result = multiply(nmber1,number2)
elif operator == '/':
    result = divide(number1,number2)
else:
    print("invalid operator")

main()


    


