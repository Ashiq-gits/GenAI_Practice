#if statement example

age = 20
if age >= 18:
    print("You are eligible to vote.")


#if else statement example

age=17
if age>=18:
    print("eligible for vote")
else:
    print("not eligible for vote")


#elif statement example

mark=55
if mark>=90:
    print("Grade O+")
elif mark>=80:
    print("Grade A")
elif mark>=70:
    print("Grade B")
elif mark>=50:
    print("Grade C")    
else:
    print("Fail")


#nested if statement example

age=20
driving_license="Yes"
if age>=18:
    if driving_license=="Yes":
        print("You are eligible to drive.")
    else:
        print("You need a driving license to drive.")
else:
    print("You are not eligible to drive and get a driving license.")