#A script to create a shopping list

list =[]
print("Please enter the items in shopping your list")
inp = input()
while inp != "DONE":
  list.append(inp)
  inp = input()
  
if len(list)!=0:
  print("Items in your shopping list are: ")
  i=0
  while i<len(list):
    print(str(i+1) + ". "+list[i])
    i+=1
else:
  print("Your shopping list is empty")
