# File Handling
# File handling in Python refers to the process of creating, reading, updating, and deleting files directly from your code.

# Create/Write file without "with" method

file=open("demo.txt","w")
file.write("Hello \n")
file.write("This is Demo")
file.close()

# Create/Write file "with" method

with open("ashiq.txt","w") as file:
    file.write("Welcome to the world")


# Read file

with open("ashiq.txt","r") as file:
    data=file.read()
    print(data)


# Append mode

with open("ashiq.txt","a") as file:
    file.write("\n This is append line. \n")
    file.write("This is 2nd append line.")


# Readline mode

with open("ashiq.txt","r") as file:
    line=file.readline()
    print(line)


# Readlines mode

with open("ashiq.txt","r") as file:
    line=file.readlines()
    print(line)


# X mode

with open("ashiq.txt","x") as file:
    file.write("new file")


# A file has 100 lines we have to print "This is for demo"in 55th line using for loop

with open("demo.txt", "a") as f:
    for i in range(1, 101):
        if i == 55:
            f.write("this is for demo\n")
        else:
            f.write(f"This is line {i}\n")

with open("demo.txt","r")as file:
    line=file.readlines()
    print(line)