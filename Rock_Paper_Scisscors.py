# Time to play Rock, Paper, Scissors!

# Import choice from the random module
from random import choice

# Define score variables
user_score = 0
computer_score = 0
ties = 0

# Welcome message
print("Let's play Rock, Paper, Scissors!")

# Create a loop to be able to play multiple times
while True:

    # Define the options available
    options = ["rock", "paper", "scissors"]

    # Create a loop incase user misspells
    while True:
        user_option = input(
            "Choose rock, paper or scissors (or type 'quit' to exit):\n").lower()
        if user_option == "quit":
            print("Thanks for playing, see you next time!")
            exit()
        if user_option not in options:
            print("That's not one of the options, try again")
        else:
            print(f"You choose: {user_option}")
            break

    # Define computer and print choice
    computer_option = choice(options)
    print(f"Computer choose: {computer_option}")

    # if statement to define what the outcome will be
    if user_option == computer_option:
        print("It's a tie!")
        ties += 1
    elif user_option == "rock" and computer_option == "scissors":
        print("You win!")
        user_score += 1
    elif user_option == "paper" and computer_option == "rock":
        print("You win!")
        user_score += 1
    elif user_option == "scissors" and computer_option == "paper":
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

# Print the score
    print(
        f"This is the total score:\nYour score: {user_score}\nComputer score: {computer_score}\nTies: {ties}")

# Ask if the user wants a rematch
    while True:
        rematch = input("Wanna play again? (yes/no)").lower()
        if rematch == "yes":
            print("Okay let's go again")
            break
        elif rematch == "no":
            print("Thanks for playing, see you next time!")
            exit()
