#using f string
name = input("Enter the name: ")
age = int(input("Enter the age: "))
print(f"My name is",name, "and my age is",age)
print(f"My name is {name} and my age is {age}")

#using format method()
name = input("Enter the name: ")
age = int(input("Enter the age: "))
print("My name is {} and my age is {}".format(name,age))

#using % method()
name = input("Enter the name: ")
age = int(input("Enter the age: "))
print("My name is %s and my age is %d" %(name,age))