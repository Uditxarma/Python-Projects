import random
import math

def play_game():
    print("Welcome to the Number Guessing Game:")
    print("------------------------------------")

    while True:
        try:
            # Take input for start and stop ranges
            start = int(input("Enter the starting range: "))
            stop = int(input("Enter the ending range: "))
            print("================================= \n")

            # Check if the ending range is greater than the starting range
            if start >= stop:
                print("Invalid input. Ending range should be greater than starting range.")
                continue

            # Generate random number within the range
            number_guessed = random.randint(start, stop)
            count = 0

            # Calculate the minimum number of guesses (chances)
            min_guesses = math.ceil(math.log2(stop - start + 1))
            remaining_chances = min_guesses  # Initialize remaining chances
            print("---------------------------------")
            print(f"You have {min_guesses} chances to guess the number!")
            print("---------------------------------\n")

            while True:
                try:
                    # Take input for guessed number
                    user_input = int(input(f"Enter your guessed number (Remaining chances: {remaining_chances}): \n"))

                    # Check if guessed number is out of range
                    if user_input < start or user_input > stop:
                        print(f"Please enter a number within the valid range ({start} - {stop}).")
                        print("---------------------------------\n")
                        continue

                    count += 1  # Increment the number of attempts
                    remaining_chances -= 1  # Decrease remaining chances

                    # Provide feedback based on the user's guess
                    if user_input < number_guessed:
                        print("Try Again! You guessed too low.")
                        print("---------------------------------\n")
                    elif user_input > number_guessed:
                        print("Try Again! You guessed too high.")
                        print("---------------------------------\n")
                    else:
                        # If the guess is correct
                        print("---------------------------------\n")
                        if count <= min_guesses:
                            print(f"Congratulations! You guessed it right in {count} attempts.")
                        else:
                            print(f"Good job! You guessed it right, but it took {count} attempts.")
                        print("---------------------------------\n")
                        break  # Exit inner loop when guessed correctly

                    # Check if the user has exceeded the minimum number of guesses
                    if remaining_chances == 0:
                        print(f"You're out of chances! The correct number was {number_guessed}.")
                        print("---------------------------------\n")
                        break

                    if count == min_guesses:
                        print(f"Hint: You've reached {count} guesses, which is the minimum!")
                        print("---------------------------------\n")

                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    print("---------------------------------\n")

            # Ask the user if they want to play again
            while True:
                response = input("Do you want to play again? (Y/N): ").strip().lower()
                if response in ["y", "n"]:
                    break
                else:
                    print("Invalid input. Please select Y or N.")
            
            if response == "n":
                print("Thank you for playing! Goodbye.")
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    play_game()
