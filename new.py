#simple python programming related to string, interger and float 
name = ("sujal")
roll_number = 62
percentage = 94.77
mobile_number = ("7218215696")
print(name, roll_number, mobile_number )

print("My name is " + name, " My roll number is", roll_number , "and my mobile number is ", mobile_number)
# here + is added to the same data types i.e string after a string and not for different data types i.e 
# interger after string.

print(type(name)) #gives data type of variable
print(type(roll_number))
print(type(mobile_number))
print("I have changed my roll number to ", roll_number - 30)


#use of seperator
print("My name is " + name, " My roll number is", roll_number , "and my mobile number is ", mobile_number, sep="-")


# Use of dictionary
contacts = {"sujal": 21151262,
            "kartik": 21151213,
            "aditya": 21151240,
            "ashish": 21151206}
info = input("Search name :")
print(info,   contacts[info])

#Ascii and unicode values
letter = "r"
print(ord(letter))

number = "5"
print(ord(number))

ascii_value = 56
print(chr(ascii_value))

ascii_value_1 = 76
print(chr(ascii_value_1))




