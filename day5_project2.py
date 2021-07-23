phonebook = {}
while (True):
  name = input("What is your name?: ")
  if name != "finished":
    number = input("What is your phone number?: ")
    phonebook[name] = number
  else:
    break
print(sorted(phonebook))
print("Here is Your Phone Book: "  + str(phonebook))
print("The length of your phonebook is " + str(len(phonebook)))