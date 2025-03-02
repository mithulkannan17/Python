# for loop conditions

name = input("Enter your name: ")
list = ["blue", "green", "yellow"]
for letter in name:
    if letter.isalpha():
        print(letter)
        for i in letter:
            print(i)
    else:
        print(letter, "is not a letter")
print("_____________________________________________________")
for color in list:
    print(color)
    for i in color:
        print(i)
print("================================================")

# to print multi

for j in range(100):
    if j % 2 == 0:
        print(j)

print("================================================")
for k in range(1,100,3):
    print(k)
    