grocerylist = []
condition = True
while (condition):
  item = (input("What is the item you bought?: "))
  if item != "finished":
    grocerylist.append(item)
  else:
    condition = False
print("Your grocery list is"  + str(grocerylist))
