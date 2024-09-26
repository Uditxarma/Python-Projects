import random
import math
import tkinter as tk
from tkinter import messagebox

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        
        # Set a solid background color
        self.master.configure(bg="#2c3e50")  # Solid background color

        # Styling for labels and inputs
        label_font = ("Helvetica", 14, "bold")
        input_font = ("Helvetica", 12)
        button_font = ("Helvetica", 14, "bold")

        # Starting Range Label and Entry (capitalized, white text)
        self.start_label = tk.Label(master, text="STARTING RANGE:", font=label_font, fg="white", bg="#2c3e50")
        self.start_label.pack(pady=10)
        self.start_entry = tk.Entry(master, font=input_font, bg="#f0f0f0", bd=2, relief="solid")
        self.start_entry.pack(pady=5, ipadx=5, ipady=5)

        # Ending Range Label and Entry (capitalized, white text)
        self.stop_label = tk.Label(master, text="ENDING RANGE:", font=label_font, fg="white", bg="#2c3e50")
        self.stop_label.pack(pady=10)
        self.stop_entry = tk.Entry(master, font=input_font, bg="#f0f0f0", bd=2, relief="solid")
        self.stop_entry.pack(pady=5, ipadx=5, ipady=5)

        # Start Game Button
        self.start_button = tk.Button(master, text="START GAME", command=self.start_game, bg='#5cb85c', fg='white', font=button_font, relief="raised", bd=4)
        self.start_button.pack(pady=20, ipadx=20, ipady=5)

        # Guessed Number Label and Entry (initially hidden, capitalized, white text)
        self.guess_label = tk.Label(master, text="ENTER YOUR GUESSED NUMBER:", font=label_font, fg="white", bg="#2c3e50")
        self.guess_entry = tk.Entry(master, font=input_font, bg="#f0f0f0", bd=2, relief="solid")

        # Guess Button
        self.guess_button = tk.Button(master, text="GUESS", command=self.check_guess, bg='#5bc0de', fg='white', font=button_font, relief="raised", bd=4)

        # Remaining Chances Label (initially hidden)
        self.remaining_label = tk.Label(master, text="", font=("Helvetica", 12), fg="white", bg="#2c3e50")
        
        # Play Again Button (initially hidden)
        self.play_again_button = tk.Button(master, text="PLAY AGAIN", command=self.play_again, bg='#5cb85c', fg='white', font=button_font, relief="raised", bd=4)
        self.play_again_button.pack_forget()  # Initially hidden

        # Reset the game
        self.reset_game()

    def reset_game(self):
        self.start = None
        self.stop = None
        self.number_guessed = None
        self.count = 0
        self.min_guesses = 0
        self.remaining_chances = 0

    def start_game(self):
        try:
            self.start = int(self.start_entry.get())
            self.stop = int(self.stop_entry.get())

            if self.start >= self.stop:
                messagebox.showerror("Invalid Input", "Ending range should be greater than starting range")
                return

            # Random number generation and calculation of minimum guesses
            self.number_guessed = random.randint(self.start, self.stop)
            self.min_guesses = math.ceil(math.log2(self.stop - self.start + 1))
            self.count = 0
            self.remaining_chances = self.min_guesses  # Set initial chances
            
            # Hide range input elements and display guessing interface
            self.start_label.pack_forget()
            self.start_entry.pack_forget()
            self.stop_label.pack_forget()
            self.stop_entry.pack_forget()
            self.start_button.pack_forget()

            self.remaining_label.config(text=f"Remaining Chances: {self.remaining_chances}")
            self.remaining_label.pack(pady=10)

            self.guess_label.pack(pady=10)
            self.guess_entry.pack(pady=5, ipadx=5, ipady=5)
            self.guess_button.pack(pady=10, ipadx=20, ipady=5)
        
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers for the range.")

    def check_guess(self):
        try:
            user_input = int(self.guess_entry.get())

            if user_input > self.stop or user_input < self.start:
                messagebox.showwarning("Invalid Guess", "Enter a number within the valid range.")
                return

            self.count += 1  # Increment guess count
            self.remaining_chances -= 1  # Decrease remaining chances

            if user_input < self.number_guessed:
                messagebox.showinfo("Try Again!", "You guessed too small.")
            elif user_input > self.number_guessed:
                messagebox.showinfo("Try Again!", "You guessed too high.")
            else:
                # Handle correct guess
                if self.count <= self.min_guesses:
                    messagebox.showinfo("Congratulations!", f"You guessed it right in {self.count} attempt(s).")
                else:
                    messagebox.showinfo("Good Job!", f"You guessed it right, but it took {self.count} attempts.")

                # Hide guessing elements and display "Play Again" button
                self.guess_label.pack_forget()
                self.guess_entry.pack_forget()
                self.guess_button.pack_forget()
                self.remaining_label.pack_forget()
                self.play_again_button.pack(pady=20, ipadx=20, ipady=5)
                return

            if self.remaining_chances > 0:
                self.remaining_label.config(text=f"Remaining Chances: {self.remaining_chances}")
            else:
                messagebox.showinfo("Out of Chances", f"You're out of chances! The correct number was {self.number_guessed}.")
                self.guess_label.pack_forget()
                self.guess_entry.pack_forget()
                self.guess_button.pack_forget()
                self.remaining_label.pack_forget()
                self.play_again_button.pack(pady=20, ipadx=20, ipady=5)

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def play_again(self):
        self.reset_game()

        # Hide the play again button and redisplay the range input elements
        self.play_again_button.pack_forget()
        self.start_label.pack(pady=10)
        self.start_entry.pack(pady=5, ipadx=5, ipady=5)
        self.stop_label.pack(pady=10)
        self.stop_entry.pack(pady=5, ipadx=5, ipady=5)
        self.start_button.pack(pady=20, ipadx=20, ipady=5)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x500")  # Set window size
    game = NumberGuessingGame(root)
    root.mainloop()
