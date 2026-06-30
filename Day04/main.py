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


game_images=[rock,paper,scissors]
user_choose=int(input('What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors :\n'))

if user_choose >= 0 or user_choose <= 2:
    print(game_images[user_choose])


print("Computer Choose:\n")
computer_choose=random.randint(0,2)
print(game_images[computer_choose])


if user_choose >= 3 or user_choose < 0:
    print("You typed an invalid option! You lose")

elif user_choose== 0 and computer_choose==2:
    print("You win!")

elif user_choose==1 and computer_choose==0:
    print("You win!")

elif user_choose==1 and computer_choose==2:
    print("You lose!")

elif user_choose==2 and computer_choose==1:
    print("You win!")

elif user_choose==2 and computer_choose==0:
    print("You lose!")

elif computer_choose > user_choose:
    print("You lose!")

else:
    print("Match Draw!")
