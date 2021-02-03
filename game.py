# game.py

import random # load the module to avoid `NameError: name 'random' is not defined`

# intro text

print("Rock, Paper, Scissors, Shoot!")

print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")


# asking user for an input
user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ")
print("You chose: ", user_choice)


# validate user inputs (case insensitive)
if user_choice.lower() != "rock" and user_choice.lower() != "paper" and user_choice.lower() != "scissors":
    print("Please select either 'rock', 'paper', or 'scissors'. Thanks!")
    exit()


# simulate computer selection
computer_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(computer_options)
print("The computer chose: ", computer_choice)









