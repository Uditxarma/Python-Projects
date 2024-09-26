# Number Guessing Game

Welcome to the **Number Guessing Game**! This is a fun, interactive console-based game where you try to guess a randomly selected number within a defined range. You will have a limited number of chances based on the size of the range.

## How It Works

1. **Input Range**: The game will prompt you to enter a starting and an ending range. The number to be guessed will be randomly generated within this range.
2. **Limited Chances**: The game will calculate the minimum number of guesses (chances) you have to find the correct number. This is based on the size of the range and is computed using logarithms.
3. **Hints**: For every guess, you will receive feedback on whether your guess is too high or too low.
4. **Winning**: If you guess the correct number within the allowed number of guesses, you win!
5. **Out of Chances**: If you use all your chances without guessing the correct number, the game will end and reveal the correct number.

## Features

- User-friendly prompts and feedback.
- Calculates the optimal number of guesses based on the range.
- Hints to help you guess the correct number.
- Option to play again after each game session.

## How to Play

1. **Run the script**: Start the game by running the Python script.
   ```bash
   python number_guessing_game.py
2. **Enter the Range**: Enter the starting and ending range when prompted. Make sure the starting range is smaller than the ending range.
3. **Start Guessing**: Use your chances wisely! After each guess, the game will tell you if the number is higher or lower than your guess.
4. **Win or Lose**: Guess the correct number within the allowed chances, or run out of chances and the game will reveal the correct number.
4. **Play Again**: After the game ends, you can play again by selecting "Y" or "N".

## Example:
 ```bash
Welcome to the Number Guessing Game:
------------------------------------
Enter the starting range: 1
Enter the ending range: 100
================================= 

You have 7 chances to guess the number!
---------------------------------

Enter your guessed number (Remaining chances: 7): 50
Try Again! You guessed too low.
---------------------------------

Enter your guessed number (Remaining chances: 6): 75
Try Again! You guessed too high.
---------------------------------

Enter your guessed number (Remaining chances: 5): 60
Congratulations! You guessed it right in 3 attempts.
---------------------------------

Do you want to play again? (Y/N): n
Thank you for playing! Goodbye.


