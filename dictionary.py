# # #Dictionary: Stores key value pairs
# # #numbers can be duplicate but the keys should not be duplicate

#creating a dictionary
phones = { "sujal": 211512,
          "shubham": 512154,
          "nagu": 545454
          }
print(phones)

# #checking the type of dictionary
# print(type(phones))


# #checking the length of dictionary
# print(len(phones))


# #access the items in the dictionary
# print(phones["sujal"])
# print(phones.get("sujal"))
# print(phones.keys())
# print(phones.values())

# #update value in dict
# phones["sujal"] = 154546
# print(phones)

# #add elements in dict
# phones["jay"] = 56541
# print(phones)        #Here if you add element with the same key then the dictionary will update the value of the key only

# more_phones = {"Isha": 564684}
# phones.update(more_phones)
# print(phones)

# #remove elements in a dict 
# phones.pop("nagu")
# print(phones)

# # phones.popitem()  #This will remove the last added item
# # print(phones)

# # phones.clear() #This will clear the dictionary
# # print(phones)

# #printing elements of dictionary
# for i in phones:   #This will print keys of the dict
#     print(i)   

# for i in phones:  #This will print values of the dict
#     print(phones[i])

# for i in phones.items():   #This will print both keys and values of the dict   #elements as seperate items
#     print(i)

# for i,j in phones.items():  #i will have keys and j will have values
#     print(i,j)

# #nested dictionaries
# phones = {
#     "Area1":{
#         "a":0,
#         "b":1,
#         "c":2
#     },
#     "Area2":{
#         "x":4,
#         "y":5,
#         "z":6
#     }
# }
# print(phones["Area1"]["a"])  #accessing elements/values in the dict


# #Q1) Given a dictionary in python, write a python program to find the a of all items in the dictionary
# #method 1
# input_dic = {
#     "a": 300,
#     "b": 100,
#     "c": 200
# }
# a = 0
# for i in input_dic.values():
#     a = i + a
# print(a)

# #method 2
# print(sum(input_dic.values()))


#Q2) Given a string and number N, we need to mirror the characters from the N-th position up to the length of the 
#    string in alphabetical order. In mirror operation, we change 'a' to 'z and 'b' to 'y', and so on

input_string = input("Enter the string:")
n = int(input("Enter the position:"))

#creating a dictionary for mirror operation
alphabates = "abcdefghijklmnopqrstuvwxyz" 
reverse_alphabates = alphabates[::-1]  # start,end,step from right to left in a string
dict_ = dict(zip(alphabates,reverse_alphabates))  #two iterable values get combined using zip fuction and using type casting they are converted into dictionary
                                                     
prefix = input_string[0:n-1] # finding part of the string on which we will do mirror operation
suffix = input_string[n-1:]

mirror = ""                     # finding mirror string
for i in range(0,len(suffix)):
    mirror = mirror + dict_[suffix[i]]

res = prefix + mirror               #end result
print(res)
