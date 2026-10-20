# List with methods

mylist=[1,2,3,4]
print(mylist)
# O/P:[1, 2, 3, 4]

print(mylist.append(1))
# O/P:None

print(mylist)
# O/P: [1, 2, 3, 4, 1]

print(mylist.extend([5,6]))
# O/P: None

print(mylist)
# O/P: [1, 2, 3, 4, 1, 5, 6]

print(mylist.insert(5,5))
# O/P: None

print(mylist)
# O/P: [1, 2, 3, 4, 1, 5, 5, 6]

print(mylist.pop())
# O/P: 6

print(mylist)
# O/P: [1, 2, 3, 4, 1, 5, 5]

print(mylist.pop(4))
# O/P: 1

print(mylist)
# O/P: [1, 2, 3, 4, 5, 5]

print(mylist.remove(5))
# O/P: None

print(mylist)
# O/P: [1, 2, 3, 4, 5]

print(mylist.append(2))
None

print(mylist)
# O/P:[1, 2, 3, 4, 5, 2]

print(mylist.count(2))
# O/P: 2

print(mylist.reverse())
# O/P: None

print(mylist)
# O/P:[2, 5, 4, 3, 2, 1]

print(mylist.reverse())
# O/P:None

print(mylist)
# O/P:[1, 2, 3, 4, 5, 2]

print(mylist[2])
# O/P: 3

print(mylist.index(2))
# O/P: 1


# Tuple with methods

mytuple=(1,2,3,4,1,4,5,6,1,7,8,9,1,10,1,2)
print(mytuple.count(1))
# O/P: 5

print(mytuple.count(2))
# O/P: 2

print(mytuple.count(4))
# O/P: 2

print(mytuple.index(10))
# O/P: 13

print(mytuple.index(9))
# O/P: 11

print(mytuple[8])
# O/P: 1


# Set with methods

myset={1,2,2,4,6,4,7,1}
print(myset)
# O/P: {1, 2, 4, 6, 7}

print(myset.add(8))
# O/P: None

print(myset)
# O/P: {1, 2, 4, 6, 7, 8}

print(myset.clear())
# O/P: None

print(myset)
# O/P: set()


myset={'ashiq','harrish','dhanush','goku'}
print(myset.add('bharath'))
# O/P: None

print(myset)
# O/P: {'goku', 'ashiq', 'bharath', 'harrish', 'dhanush'}

print(myset.add('vegeta'))
# O/P: None

print(myset)
# O/P: {'goku', 'ashiq', 'bharath', 'harrish', 'vegeta', 'dhanush'}

print(myset.remove('bharath'))
# O/P: None

print(myset)
# O/P: {'goku', 'ashiq', 'harrish', 'vegeta', 'dhanush'}


# Dictionary with methods

mydict={'name':'ashiq','age':21,'sub':'python'}
print(mydict)
# O/P: {'name': 'ashiq', 'age': 21, 'sub': 'python'}

print(mydict['name'])
# O/P: ashiq

mydict['age']=22
print(mydict)
# O/P: {'name': 'ashiq', 'age': 22, 'sub': 'python'}

mydict['place']='mangadu'
print(mydict)
# O/P: {'name': 'ashiq', 'age': 22, 'sub': 'python', 'place': 'mangadu'}

print(mydict.update({'age':23}))
# O/P: None

print(mydict)
# O/P: {'name': 'ashiq', 'age': 23, 'sub': 'python', 'place': 'mangadu'}