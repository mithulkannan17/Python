# if else condition
a = int(input("Enter your age: "))
print("Your age: ", a)

if a >= 18:
    print("You can drive")
else:
    print("You cannot drive")
print("================================")
# nested if else condition

b = int(input("Enter your marks: "))
print("Your marks: ", b)

if b >= 85:
    print("Grade: A")
elif b >=60:
    print("Grade: B")
elif b >= 45:
    print("Grade: C")
elif b >= 35:
    print("Grade: D")
elif b < 35:
    print("Grade: F")
else:
    print("Invalid input")
print("================================")
