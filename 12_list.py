#list 

list_items = ["apple", "banana", "cherry", "date", "elderberry"]

for item in list_items:
     for i in range(len(item)):
          print(i,". Original List:", item.upper())
          break

print("================================================")
