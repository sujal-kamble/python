#Finding factorial of n 
def factorial(n):
    #base case
    if n==0:
        return 1
    #recursive case
    ans = n * factorial(n-1)
    return ans
n = int(input("Enter n: "))
output = factorial(n)
print(output)

#Write a program to print numbers from n to 1
def number(n):
    if n==0:
        return
    print(n)
    number(n-1)

n = int(input("Enter n: "))
output_1 = number(n)
print(output_1)

#Write a program to print numbers from 1 to n
def number(n):
    if n==0:
        return
    
    number(n-1)
    print(n)

n = int(input("Enter n: "))
output_1 = number(n)
print(output_1)

#Write a program to print sum from 1 to n
def addition(n):
    if n==0:
        return 0
    if n==1:
        return 1
    add = n + addition(n-1)
    return add
n = int(input("Enter n: "))
output_2 = addition(n)
print(output_2) 

#Make a function which calculates 'a' raised to the power 'b' using recursion.
def power(a,b):
    if b == 0:
        return 1
    if b == 1:
        return a
    ans = a * power(a, b-1)
    return ans
a = int(input("Enter a: "))
b = int(input("Enter b: "))
output_2 = power(a,b)
print(output_2) 

#Make a function which calculates Fibonacce sequence using recursion
def fibonacci(n):
    if n==1:
        return 0
    if n==2:
        return 1
    ans = fibonacci(n-1)+fibonacci(n-2)
    return ans
n = int(input("Enter n: "))
for i in range(1,n+1):
    print(fibonacci(i))
