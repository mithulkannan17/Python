# plank timer

import time
print("Do you want to start")
options = input("Yes or NO: ")

if options == "Yes" or "yes":

  sets = int(input("Enter the number of set: "))
  second = int(input("Enter the time in seconds:"))
  for i in range(sets):
    print("starting set: ", i+1)
    for j in range(second):
        print(second - j, end="\r")
        time.sleep(1)  
    print("completed set: ", i+1)
    print("Resting time:")
    for k in range(30):
        print(30 - k, end="\r")
        time.sleep(1)
    print("End")


elif options == "No" or "no":
    print("Timer terminated")
else:
    print("Invalid input")