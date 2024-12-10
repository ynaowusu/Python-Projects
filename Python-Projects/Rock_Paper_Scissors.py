
#Rock Paper Scissors Game With Computer 
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
 
game_images = [rock, paper, scissors]
print("Welcome To Rock Paper Scissors \n ")
print("There are three simple rules of the game: \n Rock wins against scissors \n Scissors win against paper \n Paper wins against rock")

game_start = input("Are you ready to play? Type y for Yes and n for no ")

if game_start == "y":
    print("Woohoo! Let's get started ")
    game_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
    if game_input in [0, 1, 2]:
        print(game_images[game_input])
    else:
        print("Error, type : 0,1 or 2")

    computer_list = [0, 1, 2]
    computer_choice = random.choice(computer_list)

    if computer_choice in computer_list:
        print(f"Computer choose: \n \n {game_images[computer_choice]} ")
    else:
        print("Error")

    if game_input == computer_choice:
        print("It's a tie!")
    else:
        if game_input >= 3 or user_choice < 0 :
            print("You lose ): ")
        elif game_input == 0 and computer_choice == 2:
            print("You win")
        
        elif game_input == 1 and computer_choice == 2:
            print("You lose ): ")

        elif game_input == 2 and computer_choice == 0:
            print("You lose ): ")
        elif computer_choice > game_input:
            print("You Win! ")
        
      
    
else:
    print("You are no fun ): ")


