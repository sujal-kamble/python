fruits = ["apple", "chery","mango","banana"]
# print(fruits) #printing a list
# print(type(fruits)) #printing type of list
# print(len(fruits)) #printing the length of list
# if "mango" in fruits:  #finding the items in the list
#     print("mango is in the list")
# if "apple" in fruits:
#     print("apple is in the list")
# if "kiwi" not in fruits:
#     print("kiwi is not in the list")


# #Accessing the items in the list
# print(fruits[1]) #accessing by index position
# print(fruits[-2]) #accessing by negative index position
# print(fruits[1:3]) #accessing by range of indexes
# print(fruits[-3:-1]) #accessing by negative range of index position

# #adding items in the list
# fruits.append("mango") #adds mango at the end of the list
# print(fruits)
# fruits.insert(2, "mango") #adds mango at the index position 2
# print(fruits)
# more_fruits = ["Kiwi", "papaya"] #adds more_fruits to the fruits at the end
# fruits.extend(more_fruits)
# print(fruits)
# # fruits.clear() #clears the fruits list
# # print(fruits)
# fruits.copy() #copies all the items in the list
# print(fruits)

# #Removing items of the list
# fruits.remove("mango") #removes item from the list, it removes only one item or takes only one argument
# print(fruits)
# fruits.pop() #removes last item of the list
# print(fruits)
# fruits.pop(2) #removes item which is present at the index position 2
# print(fruits)

# #changing or updating item in the list
# fruits[2] = "lemon"
# print(fruits)
# fruits[1:3] = ["banana"]
# print(fruits)
# fruits[1:3] = "banana" #it takes string as a list and letters as items in the list
# print(fruits)

#sorting a list
fruits.sort() #sorts the list by using firts letters in each of the item in ascending order
print(fruits) 
fruits.reverse() #reverse the list
print(fruits)
fruits.sort(reverse = True) #descending order
print(fruits)

#Nested list
fruits.insert(2, ["sub","bus"])
print(fruits)
print(fruits[2][0])

num = [20,30,40,50,21,22]
num_1 = []
for i in num:
    if i > 25:
        num_1.append(i)
print(num_1)
#comrehensive list : When we want to make new list from the items of the exiting list comprehensive list is used
new_2 = [i for i in num if i > 25]
print(new_2)



a =  [10,20,15,12,14,16]
b = []
for i in a:
    if i>12:
        b.append(i)
print(b)

c = [i for i in a if i>12]
print(c)