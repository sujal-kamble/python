# Syntax 
# Using single quote: 'Hello'
# Using double quote: "Hello"
# Using triple quote: '''Hello'''

# Strigs
# 1) Sequence of characters within '', "", ''' ''',
# 2) Immutable but(I can create new string bu manipulating original string)
# 3) ''' ''' are also used for assignig multiline string(paragraph) to a variable
# 4) Array like indexing

# Creating and printing a string
name1 = 'sujal'
name2 = "Sujal \n"
name3 = '''SUJAL \n'''
name4 = '''Never        
 Settle'''   #assigning multiline string(paragraph) to a variable
print(name1,name2,name3,name4)

#type of string
print(type(name1))
print(type(name2))
print(type(name3))
print(type(name4))

#Array like indexing in string
print(name1[2:])
print(name1[2:4])
print(name1[:3])
print(name1[-1:])   #negative indexing
print(name1[-4:-1])
print(name1[:-2])

#traversing a string
#using for loop
for i in name1:
    print(i, end=' ')
print()

#using list comprehension
list = [char for char in name1]
for i in list:
    print(i, end=' ')
print()

#finding the length of the string
print(len(name1))

#finding a character/substring in a string
print(name1.find('s'))
print(name1.find('j'))
print(name1.find('uja'))

#slicing in string   (slicing and indexing is same)
# s u j a l
# 0 1 2 3 4 
print(name1[1:3])
print(name1[:2])
print(name1[2:]) 
print(name1[-2:])
print(name1[:-3])
print(name1[-4:-2])

#Modifying strings
#for converting characters to uppercase
str1 = (name1.upper())
print(str1)

#for converting characters to lowercase
str2 = str1.lower()
print(str2)


#for capatilizing the first character of string
str3 = (str2.capitalize())
print(str3)

#for stripping/removing any trailing whitspaces
str4 = "   hello    "
print(str4)
str5 = print(str4.strip())

#replacing substring (str1.replace(old_substring, new_substring, count))
str1 = "Hello world, what a beautiful world this is!"
print(str1.replace("world","earth"))    #This will replace all "world" words from the string
print(str1.replace("world","earth",1))   #This will replace only 1 "world" word which is coming first







