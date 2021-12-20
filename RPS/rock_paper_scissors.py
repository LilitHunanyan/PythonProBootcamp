"""
This script is created for the implementation of a game known as RPS(rock, paper, scissors)
"""
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

pos = [rock, paper, scissors]
GameOver = False

while not GameOver:
    choice = int(input("Please enter your choice: Type 0 for Rock, 1 for Paper and 2 for Scissors."))

    assert (0 <= choice <= 2)

    random_choice = random.randint(0, 2)
    print(f"Your choice!\n{pos[choice]}")
    print(f"Computer choice!\n{pos[random_choice]}")

    if choice == 0 and random_choice == 2 or choice > random_choice:
        print("You win!")
    elif choice == random_choice:
        print("Draw!")
    else:
        print("You lose!")

    GameOver = False if input("You want to play again?(y/n)").lower() == "y" else True
