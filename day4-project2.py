# This program generates a list of 10 random numbers and prints the greatest number in the list 
import random
mylist = []
#create a list of 10 random values
for i in range(10) :
  number = random.randint(1,1000)
  mylist.append(number)

#sort the list in ascending order
mylist.sort()
#print greatest value in list
print("The generated list is: " + str(mylist))
print("The greatest number in the list is: " + str(mylist[-1]))