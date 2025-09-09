#Sets: Container for storing multiple values in a variable
#properties of sets:
# 1) unordered: order of the items in the sets are not fixed    
#  2) immutable: cannot update exiting values but can add and remove    
#  3) Dublicates allowed: Dublicate items are not allowed     
#  4) Any datatype: Items in the tuple can be of any type    ex. a = "{"red"}   
#                                                                b = {1,2,3}
#                                                                c = {False, True}
#  5) Mix of different data types: In single tuple mix data types can be used  ex. d = {1,False,"Yes"}
#  6) Unindexed: Sets are unindexed as they are unordered

#creating a set
names = {"Sujal","sk","Rohit"}
print(names)

#checking length of set
print(len(names))

#checking type of set
print(type(names))

#accessing items of the set
for i in names:     #as sets are 
    print(i)

#checking if an item exits in a set
if "sk" in names:
    print("sk is present in names")

#add elements in set
names.add("ks")
print(names)

#add another sequence in a set
names_ = {"sd","sf"}
names.update(names_)
print(names)

#removing elements from a set
names.remove("sk")
print(names)
#names.remove("ds")  #It will throw error
#print(names)
names.discard("ds")   #This function will not throw an error if a value is not present in the set
print(names)

#joinin 2 sets
s1 = {1,2,3,4}
s2 = {5,6,7,8}

s3 = s1.union(s2)
print(s3)

s1.update(s2)
print(s1)

#keep only duplicates while joining
s1.intersection_update(s2)  #updates set s1 by adding only the intersection values of s1 and s2
print(s1)

#join without duplicates
s1.symmetric_difference_update(s2) #pdates set s1 by adding values without intersection values of s1 and s2
print(s1)