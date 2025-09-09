# # arithmetic operators
# num_1 = int(input('Enter the first number: '))
# num_2 = int(input('Enter the second number: '))
# print("sum", num_1 + num_2)
# print("difference", num_1 - num_2)
# print("multiplication", num_1 * num_2)
# print("division", num_1 / num_2)
# print("floor division", num_1 // num_2)
# print("exponentiation", num_1 ** num_2)
# print("remainder", num_1 % num_2)

# #Assignment operators
# n1 = 5
# n2 = n1
# print( n1, n2)
# n2 += n1
# print( n1, n2)
# n2 -= n1
# print( n1, n2)
# n2 *= n1
# print( n1, n2)
# n2 /= n1
# print( n1, n2)
# n2 %= n1
# print( n1, n2)
# n2 //= n1
# print( n1, n2)
# n2 **= n1
# print( n1, n2)
# #n2 &= n1
# # print( n1, n2)
# # n2 |= n1
# # print( n1, n2)
# # n2 ^= n1
# # print( n1, n2)
# # n2 >>= n1
# # print( n1, n2)
# # n2 <<= n1
# # print( n1, n2)

# #comparison operators
# n1 = 5
# n2 = 9
# print(n1 > n2)
# print(n1 < n2)
# print( n1 == n2)
# print( n1 != n2)
# print( n1 >= n2)
# print( n1<= n2)

#logical operators
exp = 7 > 5
exp1 = 6 < 9
print( exp and exp1)
print( exp or exp1)
print( not(exp), not(exp1))

#identity operators
x = 6
y = 9
print( x is y)
print( x is not y)

#membership operators
fruits = [ "apple", "mango", "cherry", "banana"]
print( "banana" in fruits)
print("apple" not in fruits)

#bitwise operators
a = 2
b = 3
c = 8
print( a & b)
print( a | b)
print( a ^ b) # gives bitwise XOR operation => for that it first converts decimal numbers to binary numbers 
             #and by using XOR table gives output
print( ~b)
print( a << b)
print(~a)
print(~c)                