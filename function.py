#Creating a function
def printhello():
    print("Hi")

#Calling a function
printhello()

#Function which takes two numbers as input and returns their sum 
def add(n1,n2):
    sum = n1+n2
    return sum
x=2
y=3
print("The sum is:", add(x,y))  #Here the copy of the object is created and assigned to local variable in function 
#                                 which will not change the value of original function

print("The sum is:", add(2,3))  #positional arguments

print("The sum is:", add(n1=2,n2=3))   #Keyword arguments (named arguments) : Arguments are passed by their name

def add(n1=0,n2=0):   #default arguments
    sum = n1+n2
    return sum
print("The sum is:",add())

def add_all_numbers(*args):   #arbitary arguments
    sum = 0
    for i in args:
        sum+=i
    return sum

output = add_all_numbers(1,2,3,4,5)
print("the sum is: ", output)


def student_info(**kewargs):   #arbitary arguments
    for x,y in kewargs.items():
        print(x,y)

student_info(name = "sujal", age = 20, city = "Ich")