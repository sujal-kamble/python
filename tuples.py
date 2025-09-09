#Tuples: used to store multiple items in a variable
#properties of tuple:
# 1) ordered: order of the items in the tuple is fixed    ex. colours = ("red","blue","green")
#  2) immutable: cannot update exiting values but can add and remove    
#  3) Dublicates allowed: Dublicate items are allowed     ex. colours = ("red", "blue", "green", "red")
#  4) Any datatype: Items in the tuple can be of any type    ex. a = ("red")   
#                                                                b = (1,2,3) 
#                                                                c = (False, True)
#  5) Mix of different data types: In single tuple mix data types can be used  ex. d = (1,False,"Yes")

#creating a tuple
colours = ("red", "blue","green")

#creating tuple with one item
fruit = ("mango") #It will this item as str not as tuple 
fruits = ("mango",)  #After adding , it will consider the item is in tuple
fruits_ = tuple("mango") #another representation of tuple

#checking the type of tuple
print(type(colours))

#checking length of tuple
print(len(colours))

#accessing item in the tuple (same as list)
print(colours[1]) #accessing by index position
print(colours[-2]) #accessing by negative index position
print(colours[1:3]) #accessing by range of indexes
print(colours[-3:-1]) #accessing by negative range of index position

#checking if an item is present in the tuple
if "red" in colours:
    print("red is present in colours")

# traverse the tuple
for i in colours:
    print(i)

#concatenate 2 tuples
more_colours = ("orange", "brown")
colours = colours + more_colours
print(colours)

#unpacking a tuple 
# colour1, colour2, colour3 = colours  #variables used for unpacking must be equal to the items in the tuple
# print(colour1, colour2, colour3)


#Question of tuple
#Reverse the tuple
first = (1,2,3,4,5)
list = []
for i in reversed(first):
    list.append(i)
output_tuple = tuple(list)
print(output_tuple)

first = (1,2,3,4,5)
list = []
for i in first:
    list.append(i)
list.reverse()
output_tuple = tuple(list)
print(output_tuple)



