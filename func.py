# Function: A function is reusable block of code which will perform specific task.


# User Defined Function(UDF): DF in python are custom,reusable blocks of code created by a programmer to perform specific,modular task.

# Functions with Parameters & Arguments

def test(name):
    print("Hello",name)

    
test("Ashiq")

# Hello Ashiq


# Function with return

def add(a,b):
    return a+b

result = add(40,50)
print(result)

# O/P: 90


# Function with default arguments

def genai(name ="Dhanush"):
    print("Hello",name)

    
genai()

# O/P: Hello Dhanush

genai("Ashiq")

# O/P: Hello Ashiq


# Keyword Arguments

def student(name,age):
    print(name,age)

    
student(age=25,name="Ashiq")

# O/P: Ashiq 25


# Positional Arguments

def sub(a,b):
    print(a-b)

    
sub(25,8)

# O/P: 17


# Variable length Arguments(*args)

def add(*args):
    print(sum(args))

    
add(66,34)

# O/P: 100

add(54,80,100,45,66,12010)

# O/P: 12355


# Keyword variable length Arguments(**kwargs)

def name(**kwargs):
    print(kwargs)

    
name(name="Ashiq",age=21,place="Mangadu")

# O/P: {'name': 'Ashiq', 'age': 21, 'place': 'Mangadu'}


# To square a given number in function

def square(a):
    return a*a

result=square(5)
print(result)

# O/P: 25


# Lambda function: It is a small,anonymous function that is defined without a name.

# To square a given number using Lambda function

square=lambda b: b*b
print(square(5))

# O/P: 25


# Lambda function double parameters

add=lambda a,b: a+b
print(add(34,57))

# O/P: 91


# To check odd or even in Lambda function

even_odd=lambda a: a%2==0
print(even_odd(5))

# O/P: False

print(even_odd(4))

# O/P: True


# Recursive function: It is a function that call itself to solve a problem or logic step by step.

# Recursive function to count numbers

def countsignal(s):
    if s==0:
        print("Stop")
    else:
        print(s)
        countsignal(s-1)

        
countsignal(5)

# O/P: 5
# O/P: 4
# O/P: 3
# O/P: 2
# O/P: 1
# O/P: Stop
