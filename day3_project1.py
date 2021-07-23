import random
number = random.randint(1,15)
for i in range(5,0,-1):
  userGuess = int(input("Please Enter An Integer From 1 - 15: "))
  if userGuess == number:
    print("Congratulations, you have guessed the right number!!")
    break
  if userGuess != number:
    j = i - 1
    print("You have " + str(j) + " lives remaining")
  if i == 1:
    print("You have run out of lives, the correct number is " + str(number))
