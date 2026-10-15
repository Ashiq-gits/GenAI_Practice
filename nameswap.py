name='Mohamed Ashiq'
firstname, lastname = name[0:7],name[8:14] #...slices the string and assigns the first name and last name to variables
print(lastname , firstname) #...prints the last name and first name in reverse order


name='Mohamed Ashiq'
firstname, lastname = name[0:7],name[8:14] #...slices the string and assigns the first name and last name to variables
print(lastname[::-1] , firstname[::-1]) #...reverses the last name and first name and prints them in reverse order


name='Mohamed Ashiq'
firstname, lastname = name[0:7],name[8:14] #...slices the string and assigns the first name and last name to variables
print(lastname[::-1][::-1] , firstname[::-1][::-1]) #...reverses the reversed last name and reversed first name and prints them