# Exception Handling :- It is way to handle unexpected errors without stopping the entire program execution

# Ex Error code

a=55
b=0
print(a/b)

# O/P:- Traceback (most recent call last):
#  File "<pyshell#4>", line 1, in <module>
#    print(a/b)
# ZeroDivisionError: division by zero


# Ex for try and except:-

try:
    a=55
    b=0
    print(a/b)
except ZeroDivisionError:
    print("We can't Divide any number by Zero")

# O/P: We can't Divide any number by Zero


# Common Exceptions:

# ZeroDivisionError: a/0 - 10/0
# TypeError: incorrect datatype - 'Ashiq'+25
# ValueError: invalid value - int('student')
# IndexError: out of range
# KeyError: Dictionary key not found
# FileNotFoundError: file does not exist


# Ex using multiple except:-

try:
    fn=int(input("Enter first number:"))
    sn=int(input("Enter second number:"))
    result=fn/sn
    print("Result:",result)

except ValueError:
    print("Kindly enter valid number")
except ZeroDivisionError:
    print("Second number can't be zero")
except IndexError:
    print("Second number can't be zero")
    
# O/P: Enter first number:20
# Enter second number:ashiq
# Kindly enter valid number

# Enter first number:10
# Enter second number:0
# Second number can't be zero

# Enter first number:10
# Enter second number:4
# Result: 2.5


# Ex using try,except,else and finally:-

try:
    num=int("125")
    result=num/10
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("Can't divide by zero")
else:
    print("Result=",result)
finally:
    print("It is done","\U0001F60A")
    
# O/P: Result= 12.5
# It is done 😊
