# Match operator
num = int(input("Enter the number= "))
num1 = int(input("Enter the number= "))
operator = input("Enter the operation= ")
match operator:
    case "+":
        print("Addition is", num + num1)
    case "-":
        print("Substraction is", num - num1)
    case "*":
        print("Multiplication is", num * num1)
    case "/":
        print("Division is", num / num1)
    case default:
        print("Invalid")

#Ternary operator
x = int(input("Enter the number= "))
operator = "Even" if x % 2 == 0 else "Odd"
print(operator)












