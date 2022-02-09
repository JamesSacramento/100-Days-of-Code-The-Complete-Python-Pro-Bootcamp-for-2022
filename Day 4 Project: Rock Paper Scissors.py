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

images = [rock, paper, scissors]
userI = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if userI >= 3 or userI < 0:
  print("Invalid Number, you lose")
else:
  print(images[userI])

  print("Computer Choose:")
  enemy_choice = random.randint(0,2)
  print(images[enemy_choice])

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
