#while loop condition

i = int(input("Enter the value of I: "))
j = int(input("Enter the value of J: "))
while i < 20:
    print(i)
    i += 1


# infinite loop
if(j > 10):
   while True:
    
      print(j,"Hello World")
      j = j + 1
      if j == 9999:
        print("Bye!")
        break
      else:
        print("I Am inside the loop condition")
else:
    print("I Have Exited the loop condition")
# use ctrl+c to exit from infinite loop


