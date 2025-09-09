n = int(input("Enter the value: "))
for i in range(n):
    for j in range(1 , n+1):
        print( "*", end = "")
    print()

for i in range(n+1):
    for j in range(1,i+1):
        print("*", end="")
    print()

for i in range(n+1):
    print(" " * (n-i), end = "")
    for j in range(1, i+1):
        print("*", end="" )
    print()

for i in range(n+1):
    print(" " * (n-i), end = "")
    for j in range(1, 2*i):
        print("*", end="")
    print()
print()

for i in range(n+1):
    for j in range(1, n+1-i):
        print("*", end="")
    print()


for i in range(n+1):
    print(" " * i, end = "")
    for j in range(1, n+1-i):
        print("*", end="")
    print()

for i in range(n+1):
    print(" " * i, end = "")
    for j in range(1, 2*(n-i)):
        print("*", end="")
    print()
















































































