import random
import tkinter as tk

def check_guess():
    try:
        guess = int(guess_entry.get())
        global attempts
        attempts += 1
        if guess < number:
            feedback.config(text="Too low!")
        elif guess > number:
            feedback.config(text="Too high!")
        else:
            feedback.config(text=f"Correct! Attempts: {attempts}")
    except ValueError:
        feedback.config(text="Enter a valid number")

number = random.randint(1, 100)
attempts = 0

game = tk.Tk()
game.title("Guessing Game")
game.geometry("300x150")

tk.Label(game, text="Guess a number 1-100:").pack(pady=5)
guess_entry = tk.Entry(game)
guess_entry.pack()

tk.Button(game, text="Submit", command=check_guess).pack(pady=5)
feedback = tk.Label(game, text="")
feedback.pack()

game.mainloop()

