# OOPS - Object Oriented Programming System :- Python is an object-oriented language, allowing you to structure your code using classes and objects for better organization and reusability.
# Advantages of OOP
# Provides a clear structure to programs
# Makes code easier to maintain, reuse, and debug
# Helps keep your code DRY (Don't Repeat Yourself)
# Allows you to build reusable applications with less code

# Class :- It is a blueprint used to create an object.
# Object :- It is a actual instance of a class.
# Attributes :- It is a way to describe an object.
# Method :- Method is a function that is defined inside a class and is tied to the behavior of that class or its object.
# Encapsulation :- The practice of bundling data(variable) and the methods(functions)that operate on that data into a single unit such as a class while restricting direct access to some of the object's components.
# Inheritance :- It allows a new class(the child or subclass) to acquire the properties and methods(behaviors)of an existing class(the parent or superclass).
# Polymorphism :- Polymorphism in Python is a core object-oriented programming (OOP) concept that literally means "many forms." It allows different types of objects to respond to the same function or method call in their own unique way.
# Abstraction :- Abstraction in Python is the process of hiding complex implementation details from the user and exposing only the essential functionalities.

# Ex for class and object:-

class car:
    def start_engine(self,model,year):
        print(f"the {model}'s {year} engine started.")
    def stop_engine(self,model,year):
            print(f"the {model}'s {year} engine stopped.")

c=car()
c.start_engine("camry",2022)
c.stop_engine("mustang",2020)


# Constructor :- In Python, a constructor is a special method used to initialize an object's state when it is created from a class.

# Ex for constructor:-

class employee:
    def __init__(self,name,age):
        self.x=name
        self.y=age
    def name(self):
        print(self.x)
    def age(self):
        print(self.y)

e=employee(age=21,name="Ashiq")
e.name()
e.age()


# Types of Inheritance

# TYPES:-

# 1.SINGLE LEVEL INHERITANCE
# 2.MULTI-LEVEL INHERITANCE
# 3.MULTIPLE INHERITANCE
# 4.HIRARICAL INHERITANCE
# 5.HYBRID INHERITANCE

# 1.SINGLE LEVEL INHERITANCE. (USING ONE PARENT CLASS AND ONE CHILD CLASS)

class father:
    def house (self):
        print("pink")
class son (father):     # (PARENT TO CHILD REALATIONSHIP)
    def park (self):
        print("blue")

f=father()   # OUTPUT : PINK
f.house()

s=son()     # OUTPUT : PINK AND BLUE
s.house()
s.park()

# MULTI-LEVEL INHERITANCE. (USE ONE MORE CLASSES)

class grandfather:
    def house(self):
        print("pink")

class father(grandfather):
    def park(self):
        print("blue")

class son(father):
    def school(self):
        print("red")

g=grandfather()   # o/p : pink
g.house()

f=father()      # o/p : pink and blue
f.house()
f.park()

s=son()        # o/p : blue , pink , red
s.park()
s.house()
s.school()

# 3.MULTIPLE INHERITANCE (USING MULTIPLE PARENT CLASS AND ONE CHILE CLASS).

class father:
    def house(self):
        print("orange")

class mother:
    def school(self):
        print("yellow")

class son (father, mother):
    def park (self):
        print("gray")

f=father()  # o/p : orange
f.house()

m=mother()   # o/p : yellow
m.school()

s=son()       # o/p : yellow , orange , gray
s.school()
s.house()
s.park()


# 4. HIERARICAL INHERITANCE (ONE PARENT CLASS AND MULTIPLE CHILD CLASS).

class father:
    def house (self):
        print("pink")

class son (father):
    def park (self):
        print("blue")

class daughter (father):
    def school (self):
        print("yellow")

f=father()   # o/p : pink
f.house()

s=son()      #o/p : pink , blue
s.house()
s.park()

d=daughter()   #o/p : pink , yellow
d.house()
d.school()        

# 5.HYBRID (USING ALL INHERITANCE).

class dad:
    def house(self):
        print("pink")
class son (dad):
    def shop(self):
        print("blue")

class father:
    def hospital(self):
        print("yellow")

class daughter (father):
    def park(self):
        print("orange")

class elderson (father):
    def beach(self):
        print("gray")

d=dad()       # o/p : pink
d.house()

s=son()       #o/p : pink , blue
s.house()
s.shop()

f=father()      # o/p : yellow
f.hospital()

d=daughter()     # o/p : yellow , orange
d.hospital()
d.park()

e=elderson()      # o/p : yellow, gray
e.hospital()
e.beach()


# Polymorphism :- Overriding

class dad:
    def house(self):
        print("blue")
        
class son(dad):
    def house(self):
        print("green")

s=son()
s.house()         # o/p : green


# Abstraction :- 

from abc import ABC,abstractmethod

class dad(ABC):
    @abstractmethod
    def home(self):
        pass
    def shop(self):
        print("Dad is at home")

    @abstractmethod
    def work(self):
        pass

class son(dad):
    def shop(self):
        print("son is at the shop.")
    def home(self):
        print("son is at home.")
    def work(self):
        print("son is at work")

s=son()
s.home()
s.work()
s.shop()


# Encapsulation :-

# public:- ex: Name
# protected:- ex: _Name
# private:- ex: __Name

# Public :- Anyone can read or change these attributes from outside the class.

class Profile:
    def __init__(self, username):
        self.username = username  # Public attribute

# Creating the object
user = Profile("Alice")

# Accessing and modifying directly from outside
print(user.username)  # Output: Alice
user.username = "Bob"
print(user.username)  # Output: Bob

# Protected :- The single underscore _ is a signal to other programmers that these variables are intended for internal use and within child classes (inheritance).

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  # Protected attribute

class Manager(Employee):
    def show_salary(self):
        # Subclasses can freely access protected parent attributes
        return f"{self.name} earns ${self._salary}"

# Creating the object
mgr = Manager("Carlos", 80000)
print(mgr.show_salary())  # Output: Carlos earns $80000

# Private :- The double underscore __ completely locks the variable inside the class. Trying to access it directly from an object will cause a crash.

class Safe:
    def __init__(self, code):
        self.__code = code  # Private attribute

    def unlock(self, entered_code):
        # Can only be accessed by methods inside the class
        if entered_code == self.__code:
            return "Safe opened!"
        return "Wrong code!"

# Creating the object
my_safe = Safe("9999")

# print(my_safe.__code)  # CRASHES: AttributeError

# The only safe way to interact with the data:
print(my_safe.unlock("1234"))  # Output: Wrong code!
print(my_safe.unlock("9999"))  # Output: Safe opened!