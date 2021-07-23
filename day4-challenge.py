#This program prints "luck!"" and then prints all the items of the list
challenging_list = [["This", "is", "a", "challenge", "problem"], ["Good", "luck!"], [1, 2, 3, 5, 8, 13, 21, 34]]

print(challenging_list[1][1])
for i in challenging_list:
  for j in i:
    print(j)
