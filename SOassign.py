# what is the output of the following,and why?

s = "Python"
print(s[0],s[-1],s[6]) # The output of the code will be:P n IndexError: string index out of range


# what is the difference between positive and negative indexing? Given s = "Hello" , what does s[-2] return?

s = "Hello"
print(s[-2]) # The output of the code will be:l


# what happens when you access an index that is out of range in a string? How is this different from slicing out of range?

s = "Code"
print(s[10])  # This will raise an IndexError
print(s[1:10])  # This will return the substring from index 1 to 9 o/p:- ode


# How do you find the index of the first and last occurrence of a character in a string using indexing concepts?

s = "mississippi"
print(s.find('s'))  # This will return the index of the first occurrence of 's' o/p:- 2
print(s.rfind('s'))  # This will return the index of the last occurrence of 's' o/p:- 6


# what is the output of the following, and explain how negative indexing resolves?

s = "abcdef"
print(s[-1],s[-3],s[-6]) # The output of the code will be: f d a


# What is the syntax for slicing a string in Python? Explain each parts of s[start:stop:step].

# start: The index where the slice starts (inclusive)
# stop: The index where the slice ends (exclusive)
# step: The step size or the number of indices to skip between each character in the slice

s = "Python"
print(s[1:6:3])  # The output of the code will be: "yo".


# What is the output of the following slices, and why?

s="HelloWorld"
print(s[0:5])  # The output of the code will be: "Hello"
print(s[5:])  # The output of the code will be: "World"
print(s[:5])  # The output of the code will be: "Hello"
print(s[:])  # The output of the code will be: "HelloWorld"


# What happens when start is greater than stop in slice with a positive step? what is the output?

s="Python"
print(s[4:1])  # The output of the code will be an empty string because the start index is greater than the stop index with a positive step.


# How do you extract the last 3 characters of a string using slicing, without knowing the length?

s = "Python"
print(s[-3:])  # The output of the code will be: "hon"


# What is the difference between these two slices? What does each return?

s='abcdefgh'
print(s[::1])  # The output of the code will be: "abcdefgh" (the entire string)
print(s[::2])  # The output of the code will be: "aceg" (every second character starting from index 0)
print(s[1::2])  # The output of the code will be: "bdfh" (every second character starting from index 1)


# How do you reverse a string using slicing? What is the step value that achieves this?

s="Python"
print(s[::-1])  # The output of the code will be: "nohtyP". The step value of -1 reverses the string.


# What is the output of the following, and explain how negative step works?

s = "abcdefgh"
print(s[::-1]) # The output of the code will be: "hgfedcba".
print(s[::-2]) # The output of the code will be: "hfdb".
print(s[6:1:-1]) # The output of the code will be: "gfedc".


# How do you extract every 3rd character from a string starting from index 1? expected output: "12345".

s='a1b2c3d4e5'
print(s[1::2]) # The output of the code will be: "12345".


# What is the output of the following negative step in slices? Explain start and stop behavior when step is negative.

s='Python'
print(s[5:0:-1]) # The output of the code will be: "nohty".
print(s[5::-1]) # The output of the code will be: "nohtyP".
print(s[:0:-1]) # The output of the code will be: "nohty".


# How do slices handle start and stop values that exceed string boundaries with negative step?

s="hello"
print(s[100::-1]) # The output of the code will be: "olleh".
print(s[-100::-1]) # The output of the code will be: "empty".
print(s[::-100]) # The output of the code will be: "o". 


# How do you extract the middle portion of a string dynamically, regardless of its length?

s="abcdefghij"
print(s[3:-3]) # The output of the code will be: "defg". splits abc"defg"hij


# How do You use slicing to check if a string is a palindrome in a single line?

s="racecar"
print(s == s[::-1]) # The output of the code will be: True. This checks if the string is equal to its reverse, indicating it is a palindrome.


# What is the output of the following, and why does python not raise an error?

s="Hello"
print(s[1:100]) # The output of the code will be: "ello". Python does not raise an error because slicing allows for out-of-range indices.
print(s[-100:3]) # The output of the code will be: "hel". Python does not raise an error because slicing allows for out-of-range indices.
print(s[100:200]) # The output of the code will be: "". Python does not raise an error because slicing allows for out-of-range indices.


# How d you replace a portion of a string using slicing (since strings are immutable)?

s='Hello World'
a=s[0:6]
b=s[6:]
print(a + b.replace('World','Python')) # The output of the code will be: "Hello Python". But here we used replace method instead.

s='Hello World'
s=s[:6] + 'Python'
print(s) # The output of the code will be: "Hello Python". Here we used slicing to create a new string with the desired replacement.


# How does Python's slice() object work,how can you use it as a reusuable slicer?

s='abcdefghij'
my_slice=slice(1, 8, 2)
print(s[my_slice])  # The output of the code will be: "bdfh".

