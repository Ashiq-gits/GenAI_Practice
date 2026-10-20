# to remove multiple values of an element in a list using for loop

multilist=['vijay','goku','suriya','ajith']
remove_list=['goku','ajith']
for i in remove_list:
        multilist.remove(i)
        
print(multilist)


# output will be ['vijay', 'suriya']