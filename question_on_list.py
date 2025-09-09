# #Q1)Given a list in python and provided the index of the elements, write a program to swap  the two elements in the list.
# #method 1
# a = [26,65,19,90]  #idx1=0 and idx2=2 
# b = []
# b.append(a[0]) 
# a[0]= a[2]
# a[2] = b[0]
# print(a)

# #method 2
# a = int(input("Enter the size: "))
# b = []
# for i in range(a):
#     num = int(input())
#     b.append(num)
# print(b)

# c = int(input("Enter the first index position: "))
# d = int(input("Enter the second index position: "))

# e = b[c]
# b[c] = b[d]
# b[d] = e
# print(b)

#Q2) Given three arrays, we have to find common elements in three sorted lists using sets.
ar1 = [1,5,10,20,40,80]
ar2 = [6,7,20,60,100]
ar3 = [3,4,15,20,30,70,80,120]

s1 = set(ar1)
s2 = set(ar2)
s3 = set(ar3)

s1.intersection_update(s2)
s3.intersection_update(s1)
print(s3)

#Q3) 