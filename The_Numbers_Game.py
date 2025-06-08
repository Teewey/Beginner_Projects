# The numbers game

# Import the random module
from random import randint

total_rounds = 0


def get_input(prompt):
    user_input = input(prompt).lower()
    if user_input == "quit":
        print("Thanks for playing, see you next time!")
        exit()
    return user_input


# Print welcome message and choose difficulty
print("Welcome, let's play the numbers game! Can you guess the correct number? (type 'quit' to exit)")


while True:
    select_difficulty = get_input(
        "Start by choosing difficulty\nEasy (1-5)\nMedium (1-10)\nHard (1-50)\nInput:\n")

    while select_difficulty not in ["easy", "medium", "hard"]:
        select_difficulty = get_input(
            "Please select one of the difficulties: Easy, Medium or Hard:\n")

    def play_loop(range_start, range_end):
        global total_rounds
        guesses = 0
        # Define variable and set a range of randint
        random_number = randint(range_start, range_end)

        # Create a while loop, ask the player to input a number between 1-5
        # Guess until correct

        while True:
            try:
                player_guess = int(
                    get_input(f"Guess a number between {range_start} and {range_end}:\n"))
                guesses += 1
            except ValueError:
                print("That was not a valid number, please try again")
                continue
            if player_guess == random_number:
                print(
                    f"Congratulations! You guessed correctly in {guesses} tries!")
                total_rounds += 1
                break

            elif player_guess < random_number:
                print("Too low, try again!")
            elif player_guess > random_number:
                print("Too high, try again!")

    if select_difficulty == "easy":
        play_loop(1, 5)
    elif select_difficulty == "medium":
        play_loop(1, 10)
    elif select_difficulty == "hard":
        play_loop(1, 50)

    print(f"You have played {total_rounds} times")

    while True:
        try_again = get_input("Wanna play again (yes/no)?\n")
        if try_again == "yes":
            break
        elif try_again == "no":
            exit()
