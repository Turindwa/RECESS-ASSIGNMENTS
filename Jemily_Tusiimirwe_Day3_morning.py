#oop
#class
#Encapsulation
#polymorphism
#Inheritance
#Abstraction

class Car:
 def __init__(self,make,model,year):
  self.make=make
  self.model=model
  self.year=year

 def start_engine(self):
    print("Engine started")

 def stop_engine(self):
    print("Engine stopped")
    
    my_car = Car("Toyota","Corolla",2022)
    print(my_car.make)
    print(my_car.model)
    print(my_car.year)
    my_car.start_engine()
    my_car.stop_engine()


#Example2
class BankAccount:
    def __init__(self,account,balance):
     self.account_number= account_number
     self.balance=balance
    
    print("Insufficienf funds")

    def display_balance(self):
        print("Account Number:",self.account_number)
        print("Balance:",self.balance)

        #Example3: Rectangle
class Rectangle:
        def __init__(self,length,width):
            self.length=length
            self.width=width
        def clculate_area(self):#method
            return self.length*self.width

        def calculate_perimeter(self):#method
            return 2*(self.length + self.width)

            #create a Rectangle
            my_rectangle = Rectangle(15,5)
            print(my_rectangle.length)
            print(my_rectangle.eidth)
            print(my_rectangle.calculate_perimeter)
            print(my_rectangle.clculate_area)


            #student

class Student:
    def __init__(self,name, year,course):
     self.name = name
     self.year = year
     self.course = course

    def display_details(self):
      print("Name:", self.name)
      print("Year:", self.Year)
      print("Course:", self.course)

          #create a student object
    my_student = Student("Jemily", 3 ,"Software Engineering")

          #Display the student details
    my_student.display_details()
    
    #object
class Person:
        def __init__(self,name,age):
          self.name = name 
          self. age=age
        def greet(self):
            print("Hello,my name is",self.name)
            print("Iam",self.age,"years old")

            #create a person object

            my_person1 = Person("Jem",35)
            my_person2 = Person("Moses",24)
            #Accessing
            print(my_person1.name)
            print(my_person1.age)
            print(my_person2.name)
            print(my_person2.age)
            
            #invoking the object method
            my_person1.greet()
            my_person2.greet()

    #Exercise: calculate the area and circumference of a circle
class Circle:
        def __init__(self,radius):
          self.radius=radius

        def calculate_area(self):
            return 3.14*self.radius*self.radius
        def calculate_circumference(self):
            return 2*3.14*self.radius
#create a circle object
my_circle = Circle(5)
print(my_circle.radius)
#displaying area and circumference
print(my_circle.calculate_area())
print(my_circle.calculate_area())


#Exercise2:calculate area and perimeter of a rectangle
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.radius = width
    def calculate_area(self):
        return self.length * self.width
    def calculate_perimeter(self):
        return 2*(self.length + self.width)

    my_rec = Rectangle(2,4)
    print(my_rec.calculate_perimeter())
    print(my_rec.calculate_area())
     
#Calculate and display employee bonuses[15%] of salary{employee1:150000,employee2:230000}
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def display(self):
        print(self.name, "earns a salary worth",self.salary)
    def calculate_bonus(self):
        if self.salary > 50000:
            print(self.salary *0.15)
        else:
            print(self.salary)
            employee1 = Employee("Jem", 150000)
            employee1.display()
            employee1.calculate_bonus()
            employee2 = Employee("Isaac", 230000)
            employee2.display()
            employee2.calculate_bonus()


#Encapsulation
    #Example with bank account

class BankAccount:
  def __init__(self,account_number,balance):
    self._account_number = account_number#encapsulates the account number attribute
    self._balance = balance#Encaplsulates the balance attribute
def deposit(self,amount):
    self._balance += amount #Encapsulates the deposit

def withdraw(self,amount):
    if self._balance >= amount:
        self._balance -+ amount
    else:
        print("Insufficient funds ")

def get_balance(self):
    return self.balance

    #create a Bank object
    my_account = BankAccount("123456789",1000)

    #Access the bank and modify encapsulated account
    print(my_account._account_number)
    print(my_account._balance)
    my_account.deposit(500)
    print(my_account._balance)
    my_account.withdraw(100)
    print(my_account._balance)

    #Exercise 2: covert temperature(37 celsius) from celsius to fahrenheit and make sure you encapsulate 
    class Temperature:
        def __init__(self,celsius):
            self.celsius = celsius

        def fahrenheit(self):
            return(self.celsius*0/5) +32
    
    my_temp = Temperature(37)
    print(my_temp.fahrenheit())
#Assignment1:show encapsulation with employee information to give 
# a pay incrementation(salary with employee information to new salary) e.g from 850000 to 1000000
class Employee:
    def __init__(self,name,salary):
        self._name = name
        self._salary = salary
    def old_salary(self):
       return self._salary
    def new_salary(self,inrement_amount):
       self._salary += inrement_amount

       employee = Employee("Jemmy",850000)
       print("Name:", employee._name)
       print("current salary:",employee.old_salary())
        

       inrement_amount = 150000
       employee.new_salary(inrement_amount)
       print("New salary:",employee.new_salary())



















