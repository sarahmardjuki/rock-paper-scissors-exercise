# game.py

# import all the modules and third-party packages that we need
import os
import random # load the module to avoid `NameError: name 'random' is not defined`
from dotenv import load_dotenv # see: https://github.com/theskumar/python-dotenv

#set the environment vars
load_dotenv() # invokes / uses the function we got from the third-party package. this one happens to read env vars from the ".env" file. see the package docs for more info
PLAYER_NAME = os.getenv("PLAYER_NAME", default="Player One") # uses the os module to read the specified environment variable and store it in a corresponding python variable


# intro text

print("Rock, Paper, Scissors, Shoot!")

print("-------------------")
print(f"Welcome '{PLAYER_NAME}' to my Rock-Paper-Scissors game...")
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


# determine the winner and print out result
winners = {"paper": "scissors", "rock": "paper", "scissors": "rock"}

print("-------------------")
if user_choice == winners[computer_choice]:
    print(f"Congrats, {user_choice} beats {computer_choice}, you win!")
elif computer_choice == winners[user_choice]:
    print(f"Sorry, {computer_choice} beats {user_choice}, computer wins!")
else:
    print("Tie.")
print("-------------------")

# send the player a friendly farewell message
print("Thanks for playing. Please play again soon!")





