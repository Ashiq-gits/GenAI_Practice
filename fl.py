# for loop example

for i in range (10):
    print(i)


# use for loop to print even number upto 10

for i in range (2,11,2):
    print(i)


# for loop to print using (end=' ') to get horizontal with space output

name='Ashiq'
for i in name:
    print(i, end=' ')


# for loop using list

my_list=['ashiq','naveen','dhanush']
for i in my_list:
    print(i, end =',')


# to print 4 tables like 1 x 4 = 4,2 x 4 = 8 etc... using for loop

for i in range (1,11):
    print(i,'x 4 =',i*4)


# to print num=13 is odd or even using for loop

num=13
for i in range(num,num+1):
    if i%2==0:
        print('it is even')
    else:
        print('it is odd')


# for loop using break-->flow control statement

for i in range(10):
    if i==5:
        break
    print(i)


# for loop using pass

name='ashiq'
for i in name:
    pass


# for loop using continue

my_list=[2,5,-1,10,-5,0,-4]
for i in my_list:
    if i<0:
        continue
    print(i)