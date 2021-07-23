#This program prints a number pyramid based on a user entered number
x = int(input("Enter A Number From 1 to 10: "))
for i in range(1,x+1):
  for j in range(1,i+1):
    print(j,end='')
  print('')