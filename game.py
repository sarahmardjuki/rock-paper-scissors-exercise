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


# determine the winner
winners = {"paper": "scissors", "rock": "paper", "scissors": "rock"}

if user_choice == winners[computer_choice]:
    print(f"Congrats, {user_choice} beats {computer_choice}, you win!")
elif computer_choice == winners[user_choice]:
    print(f"Sorry, {computer_choice} beats {user_choice}, computer wins!")
else:
    print("Tie.")








