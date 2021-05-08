'''
CSC 101 Lab 7
Part 4: Rock, Paper, Scissors Game
Tyler Smith
10/7/2020
'''

import random     # For using the randint function

def convert_move_to_words(move):
   if move < 0 or move > 2:
      return "invalid move"
   elif move == 0:
      return "Rock"
   elif move == 1:
      return "Paper"
   else:
      return "Scissors"

print("Let's play Rock, Paper, Scissors!")
print("Rules: paper beats rock, rock beats scissors, and scissors beats paper.")
print()

# get player's move
player = int(input("Enter your move (0 for rock, 1 for paper, or 2 for scissors): "))

# generate random move for the computer
computer = random.randint(0, 2)

print("Your move is", convert_move_to_words(player))
print("The computer move is", convert_move_to_words(computer))

# use if/elif/else to determine and show who wins
if (player == computer):
   print ("its a tie!")
elif player == "0":
   if computer == "1":
      print("You win!")
elif player == "1":
   if computer == "2":
      print("You win!")
elif player == "2":
   if computer == "0":
      print("You win!")       
elif player == "0":
   if computer == "2":
      print("You Lose!")
elif player == "1":
   if computer == "0":
      print("You Lose!")
elif player == "2":
   if computer == "1":
      print("You Lose!")    



