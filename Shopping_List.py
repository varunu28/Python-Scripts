#A script to create a shopping list

def show_help():
    print("You have following options:")
    print("1. HELP: Shows what options do you have.")
    print("2. DONE: Stops adding items to your list and shows you your final list")
    print("3. SHOW: Shows which items have you added to the list till now")

def show_list(item):
    if(len(item)>0):
        print("You have added following items in the list till now:")
        for n in item:
            print(n)
    else:
        print("You have not added anything in the list till now")

shop_list =[]

print("Welcome to the shopping list script")
print("Type HELP when you need help for menu items")
print("Type SHOW when you need to see the items in your list")
print("Type DONE when you are finished entering and want to see your final list")
print("Please enter the items in shopping your list")

inp = input()
while inp != "DONE":
  if inp == "HELP":
      show_help()
  elif inp == "SHOW":
      show_list(shop_list)
  else:
      shop_list.append(inp)
  inp = input()
  
if len(shop_list)!=0:
  print("Items in your shopping list are: ")
  i=0
  while i<len(shop_list):
    print(str(i+1) + ". " + shop_list[i])
    i+=1
else:
  print("Your shopping list is empty")



