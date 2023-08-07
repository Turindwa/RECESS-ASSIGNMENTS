#Inheritance
"""class Animal:
    def __init__(self,name):
        self.name=name

        def eat(self):
            print(f"{self.name} is eating...")

class Dog(Animal):
    def bark(self):
        print(f"{self.name}is barking...")
class Cat(Animal):
    def meow(self):
       print(f"{self.name}is meowing...")
animal = Animal("Generic Animal")
dog=Dog("spot")
cat = Cat("Fluffy")

#Invoke call Eat Method
#animal.eat()
# dog.eat()
# dog.bark()
# cat.eat()
# cat.moew()

#Example2
class  Vehicle:
    def __init__(self,brand,color):
        self.brand = brand
        self.color =color
    def display_info(self):
        print("Brand:",self.brand)
        print("color:",self.color)

    def move(self):
        print("moving the vehicle...")


class Car(Vehicle):
    def __init__(self,brand,color,num_wheels):
        super().__init__(brand,color)
        self.num_wheels = num_wheels

class Car(Vehicle):
    def __init__(self,brand,color,num_wheels):
        super().__init__(brand,color)
        self.num_wheels = num_wheels

    def display_info(self):
        # super().display_info()
        print("Number of wheels:",self.num_wheels)

    def honk(self):
        print("Honking the horn...")

#create a carobject
my_car = Car("Toyota","Red",4) 


#Access and modify thecar atributes
print("Brand:", my_car.brand)
my_car.color = "Gray"

#invoke the car methods
my_car.display_info()
my_car.move()
my_car.honk()

   # Exercise1
    #Domonstrate using inheritence to calculate area and perimeter of circle and rectangle
import math

class Shape:
    def calculate_area(self):
        pass
    
    def calculate_perimeter(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return math.pi * self.radius**2
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


circle = Circle(5)
print("Circle:")
print("Area:", circle.calculate_area())
print("Perimeter:", circle.calculate_perimeter())

rectangle = Rectangle(4, 6)
print("\nRectangle:")
print("Area:", rectangle.calculate_area())
print("Perimeter:", rectangle.calculate_perimeter())
    

    #Example3
    #Multiple inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating...")

class Flyable:
    def fly(self):
        print(f"{self.name} is flying...")

class Bird(Animal, Flyable):
    def __init__(self, name,species):
        super().__init__(name)
        self.species = species

    def display_info(self):
        print(f"species:{self.species}")
        print(f"{self.name}")


#create a bird object
my_bird = Bird("Pigeon", "bird")

#invoke the bird methods
my_bird.eat()
my_bird.fly()
my_bird.display_info()

#Method overriding

class Animal:
    def make_sound(self):
        print("Animal is making a sound!")

class Dog(Animal):
    def make_sound(self):
        print("Dog is barking!")


class Cat(Animal):
    def make_sound(self):
        print("Cat is meowing!")

def make_animl_sound(animal):
    animal.make_sound()

#create objects
animal = Animal()
dog = Dog()
cat = Cat()

#calling make_animl_sound
make_animl_sound(animal)
make_animl_sound(dog)
make_animl_sound(cat)

#polymorphism allows you to write code that can work with different objects

#method overriding 
#method overloading

#Example4
class Shape:
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,width):
      self.length = length
      self.width = width

    def calculate_area(self):
        return self.length*self.width


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius

#create shape objects
rectangle = Rectangle(5,5)
circle = Circle(5)


#calculate display area
#calculate display area
print("Area of Rectangle:", rectangle.calculate_area())
print("Area of Circle:", circle.calculate_area())
#overloading functions
class Calculator:
    def add(self,x,y):
       return x+y
    def add(self,x,y,c):
      return x+y+c

#create object
calculatoc = Calculator()
  #Display output
#print(Calculator.add(7,2))
print(Calculator.add(1,2,3,3))

  #Abstraction
  #Allows you to focus on features and hide them from unnecessary 

  #Example5:
from abc import ABC, abstractclassmethod
class Vehicle(ABC):
   @abstractclassmethod
   def start(self):
     pass

   @abstractclassmethod
   def stop(self):
     pass

class Car(Vehicle):
    def start(self):
        print("starting the car...")

    def stop(self):
        print("stoping the car...")

class Truck(Vehicle):
    def start(self):
        print("starting the car...")

    def stop(self):
        print("stopping the car...")

#creating objects
truck = Truck()
car = Car()

truck.stop()
car.stop()

#Exercise
#Demonstrate abstraction by calculating the area of a circle and rectangle
import math

class Shape:
    def calculate_area(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius**2

class Rectangle(Shape):
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width


circle = Circle(5)
circle_area = circle.calculate_area()
print("Area of the circle:", circle_area)

rectangle = Rectangle(4, 6)
rectangle_area = rectangle.calculate_area()
print("Area of the rectangle:", rectangle_area)
"""



#Assignment1:Deadline 01 july 2023
#create a receipt printing program with GUI interface, 
#a more advanced detail earns you more points
#Answer

import tkinter as tk
from tkinter import messagebox

def print_receipt():
    customer_name = customer_name_entry.get()
    items = []
    total_price = 0  # Variable to calculate the total price of all items
    for i in range(len(item_entries)):
        item_name = item_entries[i].get()
        item_quantity = quantity_entries[i].get()
        item_price = price_entries[i].get()
       
        if not item_quantity:
            messagebox.showwarning("Error", "Please fill in the quantity for item {}".format(i+1))
            return

        total_price += int(item_quantity) * float(item_price)  # Calculate total price for each item
        items.append((item_name, item_quantity, item_price))

    receipt_text = "Customer: {}\n\n".format(customer_name)

    # Add items table to the receipt
    receipt_text += "Item\t\tQuantity\tUnit Price\tTotal Price\n"
    receipt_text += "--------------------------------------------------\n"
    for item in items:
        receipt_text += "{}\t\t{}\t\t${}\t\t${:.2f}\n".format(item[0], item[1], item[2], int(item[1]) * float(item[2]))
    receipt_text += "--------------------------------------------------\n"

    receipt_text += "Total Price: ${:.2f}\n".format(total_price)
    receipt_text += "\nThank you for your purchase!"

    receipt_textbox.delete(1.0, tk.END)  # Clear any previous content
    receipt_textbox.insert(tk.END, receipt_text)


def add_item_field():
    row = len(item_entries) + 6  # Add 2 to account for existing rows (Customer Name and Item Name)
   
    # Item Name entry
    item_label = tk.Label(app, text="Item Name:")
    item_label.grid(row=row, column=0, padx=5, pady=5)
    item_entry = tk.Entry(app)
    item_entry.grid(row=row, column=1, padx=5, pady=5)
    item_entries.append(item_entry)

    # Quantity entry
    quantity_label = tk.Label(app, text="Quantity:")
    quantity_label.grid(row=row, column=2, padx=5, pady=5)
    quantity_entry = tk.Entry(app)
    quantity_entry.grid(row=row, column=3, padx=5, pady=5)
    quantity_entries.append(quantity_entry)

    # Price entry
    price_label = tk.Label(app, text="Unit Price:")
    price_label.grid(row=row, column=4, padx=5, pady=5)
    price_entry = tk.Entry(app)
    price_entry.grid(row=row, column=5, padx=5, pady=5)
    price_entries.append(price_entry)

def clear_fields():
    customer_name_entry.delete(0, tk.END)
    for entry in item_entries:
        entry.delete(0, tk.END)
    for entry in quantity_entries:
        entry.delete(0, tk.END)
    for entry in price_entries:
        entry.delete(0, tk.END)
    receipt_textbox.delete(1.0, tk.END)

# Create the main application window
app = tk.Tk()
app.title("Receipt Printing Program")

# Create and arrange the widgets
customer_name_label = tk.Label(app, text="Customer Name:")
customer_name_label.grid(row=0, column=0, padx=5, pady=5)
customer_name_entry = tk.Entry(app)
customer_name_entry.grid(row=0, column=1, padx=5, pady=5)

item_entries = []
quantity_entries = []
price_entries = []

add_item_button = tk.Button(app, text="Add Item", command=add_item_field)
add_item_button.grid(row=1, column=0, padx=5, pady=5)

print_button = tk.Button(app, text="Print Receipt", command=print_receipt)
print_button.grid(row=1, column=1, padx=5, pady=5)

clear_button = tk.Button(app, text="Clear Fields", command=clear_fields)
clear_button.grid(row=1, column=2, padx=5, pady=5)

receipt_textbox = tk.Text(app, height=10, width=60)
receipt_textbox.grid(row=2, columnspan=6, padx=5, pady=5)

# Start the application event loop
app.mainloop()
            
   