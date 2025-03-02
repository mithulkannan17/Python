# Funtions


# Function to calculate the geometric Mean (G-Mean)
def calulateGmean(a, b):
    gmean = (a*b)/(a+b)
    print(gmean)

# Function to check the Greater than
def IsGreater(a, b):
    if a > b:
        print("A is Greater than B")
    elif a == b:
        print("A is equal to B")
    else:
        print("B is Greater than A")

# funtion to calculate the sum 
def sum(a, b):
    sum = a+b
    print("Sum is: ",sum)

c = int(input("Enter the value of A: "))

d = int(input("Enter the value of B: "))

calulateGmean(c, d)
IsGreater(c, d)
sum(c, d)
