# REGULAR EXPRESSIONS
"""[]	A set of characters	"[a-m]"
\	Signals a special sequence (can also be used to escape special characters)	"\d"
.	Any character (except newline character)	"he..o"
^	Starts with	"^hello"
$	Ends with	"world$"
*	Zero or more occurrences	"aix*"
+	One or more occurrences	"aix+"
{}	Exactly the specified number of occurrences	"al{2}"
|	Either or	"falls|stays"
()	Capture and group
\A	Returns a match if the specified characters are at the beginning of the string	"\AThe"
\b	Returns a match where the specified characters are at the beginning or at the end of a word	r"\bain"
r"ain\b"
\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word	r"\Bain"
r"ain\B"
\d	Returns a match where the string contains digits (numbers from 0-9)	"\d"
\D	Returns a match where the string DOES NOT contain digits	"\D"
\s	Returns a match where the string contains a white space character	"\s"
\S	Returns a match where the string DOES NOT contain a white space character	"\S"
\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"
\W	Returns a match where the string DOES NOT contain any word characters	"\W"
\Z	Returns a match if the specified characters are at the end of the string	"Spain\Z
"""
# EXAMPLE 1 demonstrating regex| match first word, group word, all numbers
import re
a= "hello, i am new here and am learning python for the first time"
text=re.search(r"\b\w+\b$", a)
if text:
    print("last word is ",text.group())

txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

def validate_email(email):
    pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern,email):
        return True
    else:
        return False
email1="jemily@gmail.com"
email2="jemily@gmail.com"
print(validate_email(email1))
print(validate_email(email2))
# example 2
# Generators and iterators
# yield keyword is used for generators
# iterator '__iter__' "__next__" iterator
"""def factorial(n):
    if n==0:
        yield 1
    else:
        # yield n*factorial(n-1)
        fact = 1
        for i in range(1, n+1):
            fact*=1
        yield fact
for i in range(1, 10):
    print(*factorial(i))"""

# example3 an iterator is an object which implements the iterator protocol, which consist of the methods __iter__()
# and __next__()
# generate function that yields the square of numbers from 1 to 10
def squares():
    for i in range(1, 10):
        yield i**2
# create an iterator object that yields the squares from 1 to 10
squares_iterator = squares()
# print the 1st 5 squares of nos from 1-10
for i in range(5):
    print(next(squares_iterator))

# decorators @my_decorator
def my_decorator(func):
    def inner():
        print("this is my decorator")
        func()
    return inner
@my_decorator
def outer_decorator():
    print("this is outer_decorator")
outer_decorator()
#Example2 of iterators
class MyNumbers:
 # __iter__() is same as iter()
  def __iter__(self):
   self.a = 1
   return self

  # __next__() is same as next()
  def __next__(self):
    # 20th is the highest value
    if self.a <= 5:
       x = self.a
      # Manually increment
       self.a += 1
      # returning the iterator to the function call
       return x

# Create the object of the class
myclass = MyNumbers()
# get an iterator using iter()
myiter = iter(myclass)

# printing the values using a for-in loop
for x in myiter:
 print(x)
# Another example of Generators
def PowerTwoGen( max=0 ):
   n = 1
   while n < max:
       yield 2 ** n
       n += 1

a = PowerTwoGen(6)
b
for i in a:
   print(i)