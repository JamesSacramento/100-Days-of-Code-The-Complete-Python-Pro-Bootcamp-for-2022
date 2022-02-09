import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

userI = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if userI == 0:
  print(rock)
elif userI == 1:
  print(paper)
elif userI == 2:
  print(scissors)

print("Computer Choose:")
enemy_choice = random.randint(0,2)

if enemy_choice == 0:
  print(rock)
elif enemy_choice == 1:
  print(paper)
elif enemy_choice == 2:
  print(scissors)
#Logic
if userI == enemy_choice:
  print("It's a draw")
elif userI == 2 and enemy_choice == 1:
  print("You Win")
elif userI == 1 and enemy_choice == 0:
  print("You Win")
elif userI == 0 and enemy_choice == 2:
  print("You Win")
else:
  print("You Lose")

#Rock crushes scissors, scissors cut paper, and paper covers rock
