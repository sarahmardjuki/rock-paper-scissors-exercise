# game.py

print("Rock, Paper, Scissors, Shoot!")

print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")

# asking user for an input
x = input("Please choose either 'rock', 'paper', or 'scissors': ")
print("You chose: ", x)

# validate user inputs (case insensitive)
if x.lower() != "rock" and x.lower() != "paper" and x.lower() != "scissors":
    print("Please select either 'rock', 'paper', or 'scissors'. Thanks!")
    exit()

print("Done!")
exit()








