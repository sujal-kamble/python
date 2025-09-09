#Take an integer input and tell it is positive or negative
num = int(input("Enter the number:"))
if num > 0:
    print("Number is positive")
else:
    print("Number is negative")
    

#Take a positive integer and tell it is odd or even
num1 = int(input("Enter the number:"))
if num1 % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

#Q1
cost = int(input("Enter the cost price:"))
selling = int(input("Enter the selling price"))
if cost < selling:
    print("The seller has made profit")
    print("Profit is:", selling - cost)
elif cost == selling:
    print("The seller has made no profit no loss")
else:
    print("The seller has made loss")
    print("Loss is:", -(selling - cost))

#Take input percentage of student and print the grade according to the marks
marks = int(input("Enter the percentage of student: "))
if marks >= 80:
    print("Very good")
elif marks >= 60:
    print("Good")
elif marks >= 40:
    print("Average")
else:
    print("Fail")

#Take a positive intege input and tell it is a four digit number or not
num = int(input('Enter any number: '))
if num >= 1000 and num < 9999:
    print("It is a four digit number")
else:
    print("It is not a four digit number") 

#Take 3 positive integers input and print greatest of them
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
num_3 = int(input("Enter third number" ))
# if num_1 > num_2 and num_1 > num_3:
#     print("first number is the greatest number")
# elif num_2 > num_1 and num_2 > num_3:
#     print("second number is the greatest number")
# else:
#     print("third number is the greatest number")

# by using nested if-else
if num_1 > num_2:
    if num_1 > num_3:
        print(num_1, " is the greatest number")
    else:
        print(num_3, "is the greatest number")
else:
    if num_2 > num_3:
        print(num_2, 'is the greatest number')
    else:
        print(num_3, 'is the greatest number')

#take a positive integer input and tell if it is divisible by 5 or 3 not divisible by 15
a = int(input("Enter any number: "))
if a % 5 == 0 or a % 3 == 0:
    if a % 15 != 0:
        print(a, "number is divisible by 5 or 3 and not divisible by 15")
    else:
        print(a, "number is divisible by 3,5")