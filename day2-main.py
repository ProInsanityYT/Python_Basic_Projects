a = 6
b = 7

print(a = b)


x = 10
y = 20

if (x > y):
  print("x is more than y")
elif (y > x):
  print("y is more than x")
else:
  print("x is equal to y")

userInput = int(input("Give Me An Integer Number"))
if (userInput > 2):
  print("Your number is greater than 2")
elif (userInput < 2):
  print("Your number is less than 2")
else:
  print("Your number is equal to 2 or exactly 2!")


  
def print_Hi():
  print("Hello there!")
print_Hi() #this is a function call


def add(numberOne, numberTwo):
	result = numberOne + numberTwo
	return result
variable = add(1, 2) 
print(variable) 


#Example of a single function:
def greeting(name):
	print("Hello " + name)
greeting("Bob")
#prints "Hello Bob"


def intro(name):
  print("Hello"  + name)
intro("AarnavC1")
#prints "Hello AarnavC1"



