# Arithmetic operations
# simple calculator

print("Enter two numbers")

num1 = int(input())
num2 = int(input())

print("1. +")
print("2. -")
print("3. *")
print("4. /")
print("5. %")
print("Enter the operator to calculate")
operator = input()

if operator == "+":

    print(num1 + num2)

elif operator == "-":

    print(num1 - num2)

elif operator == "*":

    print(num1 * num2)

elif operator == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Cannot divide by zero")

elif operator == "%":
    if num2 != 0:
        print(num1 % num2)
    else:
        print("Cannot divide by zero")
else :
    print("Invalid operator")




