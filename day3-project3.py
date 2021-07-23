#Implements a game of rock paper
import random
round_num = 0
computer_score = 0
user_score = 0
while (round_num < 3):
  print("round number:" + str(round_num))

  user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
  if user_choice not in ["rock", "paper","scissors"]:
    print("Looks like you made an invalid choice '" + user_choice + "'. Pick from (rock, paper, scissors)")
    continue
  
  choices = ["rock","paper","scissors"]
  computer_choice = random.choice(choices)

  if user_choice == computer_choice:
    print("Its a tie, redo the round!")
    continue
  round_num += 1
  
  if user_choice == ("rock"):
    if computer_choice == ("scissors"):
      print("You win because rock smashes scissors!")
      user_score += 1
    elif computer_choice == ("paper"):
      print("You lose because paper wraps rocks!")
      computer_score += 1

  elif user_choice == ("paper"):
    if computer_choice == ("scissors"):
      print("You lose because scissors cuts paper!")
      computer_score += 1
    elif computer_choice == ("rock"):
      print("You win because paper wraps rocks!")
      user_score += 1


  elif user_choice == ("scissors"):
    if computer_choice == ("paper"):
      print("You win because scissors cuts paper!")
      user_score += 1
    elif computer_choice == ("rock"):
      print("You lose because rock smashes scissors!")
      computer_score += 1



if user_score > computer_score:
  print("Congratulations, you have beaten the computer by " +str(user_score - computer_score)+ " points!!!")
else:
  print("Sorry you lost, the computer beat you by " +str(computer_score - user_score)+ " points!!!")



  
    

 