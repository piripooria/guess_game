import random

# Initialize high score variable to infinity
high_score = float('inf')

while True:
    # Generate a random number between 1 and 100
    random_num = random.randint(1, 100)
    num_guess = 0

    while True:
        # Ask the user to guess a number or type "quit" to exit
        user_input = input(
            "Please guess a number between 1 and 100 (or type 'quit' to exit): ")
        if user_input.lower() == 'quit':
            # Exit the game if the user types "quit"
            break

        try:
            # Convert the user's input to an integer and increment the number of guesses
            user_guess = int(user_input)
            num_guess += 1

            if user_guess == random_num:
                # If the user guesses the correct number, print a congratulatory message
                # and update the high score if necessary
                print(
                    f"Congratulations! You guessed the number in {num_guess} guesses.")
                if num_guess < high_score:
                    print(
                        f"You have set a new high score of {num_guess} guesses!")
                    high_score = num_guess
                break

            elif user_guess > random_num:
                # If the user's guess is too high, print a message telling them to guess lower
                print("Too high!")
            else:
                # If the user's guess is too low, print a message telling them to guess higher
                print("Too low!")

        except ValueError:
            # If the user enters something other than an integer, print an error message
            # and ask them to enter a valid number
            print("Invalid input. Please enter a valid number.")

    if user_input.lower() == 'quit':
        # If the user types "quit", exit the game with a farewell message
        print("Thanks for playing! Goodbye!")
        break

    # Print the user's high score and ask if they want to play again with valid input
    while True:
        play_again = input("Do you want to play again? (y/n) ")
        if play_again.lower() == 'y':
            # If the user wants to play again, break out of the while loop and start a new game
            break
        elif play_again.lower() == 'n':
            # If the user does not want to play again, exit the program with a farewell message
            print("Thanks for playing! Goodbye!")
            exit()
        else:
            # If the user enters something other than "y" or "n", print an error message
            # and ask them to enter a valid response
            print("Invalid input. Please enter 'y' or 'n'.")

print("Thanks for playing! Goodbye!")
