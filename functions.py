#calculating the sum of n numbers
n = int(input("Enter n:"))   #taking input from the user
def sum_to_n(n):         #defining a function
    sum = 0
    for i in range(1,n+1):
        sum+=i
    return sum
print("The sum is:", sum_to_n(n))   #calling a function

#nested function
def outer_function():
    x = 3
    def inner_function():
        sum = 0
        y = 5
        sum = x+y
        return sum
    return inner_function()
output =  outer_function()
print(output)

#Pass by reference and pass by value
#pass by value
def inside_function(n):     #here values of original object/variable remains unchanged
    n+=1
    print("Inside function:",n)
n = 5
inside_function(n)
print("Outside function:",n)

#pass by reference
def modifylist(lst):        #here values of original object/variable gets modified according to function
    lst.append(4)
    print("Inside function: ", lst)
lst = [1,2,3]
modifylist(lst)
print("Outside function: ", lst)

def modifylist(lst):     #here values of original object/variable remains unchanged    
    # lst.append(4)       By using assignment operator we are not modifying the list but we are creating a new list
    lst = [3,5,4]
    print("Inside function: ", lst)
lst = [1,2,3]
modifylist(lst)
print("Outside function: ", lst)

#finding factorial of number
n = int(input("Enter n:"))

def factorial(n):
    res = 1
    if n==0:
        res = 1
    else:
        for i in range(1,n+1):
            res *=i
    return res

output = factorial(n)
print("Factorial of given number is:", output)


n = int(input("Enter the n: "))
def fact(n):
    ans = 1
    if n==0:
        ans = 1
    else:
        for i in range(1, n+1):
            ans*=i
    return ans

output = fact(n)
print(output)
    