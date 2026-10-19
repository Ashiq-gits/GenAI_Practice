# find largest num in list numbers=[3,5,7,2,8,1,4]

numbers=[3,5,7,2,8,1,4]
largest=0
for i in numbers:
    if i>largest:
        largest=i
        
print(f"largest number: {largest}")


# count vowels in a string string="education"

s='education' 
count=0
for i in s:
    if i in 'aeiou':
        count+=1
    
print(f"number of vowels: {count}")


# calculate the factorial of number=5

number=5
fact=1
for i in range(1,number+1):
    fact=fact*i
    
print('factorial of',number,'is:',fact)



# count positive numbers in list

numbers = [1,-2,3,-4,5]
count=0
for i in numbers:
    if i>0:
        count+=1
        
print(f'count of positive numbers are: {count}')


# count negative numbers in list
numbers = [1,-2,3,-4,5]
count=0
for i in numbers:
    if i<0:
        count+=1
        
print(f'count of negative numbers are: {count}')
        