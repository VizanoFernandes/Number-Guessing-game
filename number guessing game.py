import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def start_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    guess_entry.delete(0, tk.END)
    feedback_label.config(text="I have chosen a number between 1 and 100. Start guessing!")

def check_guess():
    global attempts
    try:
        guess = int(guess_entry.get())
        attempts += 1
        if guess < secret_number:
            feedback_label.config(text="Too low! Try again.")
        elif guess > secret_number:
            feedback_label.config(text="Too high! Try again.")
        else:
            feedback_label.config(text=f"Congratulations! You guessed it in {attempts} attempts.")
            messagebox.showinfo("Success", f"You guessed the number in {attempts} attempts!")
    except ValueError:
        feedback_label.config(text="Please enter a valid number.")

# Create the main application window
root = tk.Tk()
root.title("Number Guessing Game")

# Create a tabbed interface
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Game tab
game_tab = ttk.Frame(notebook)
notebook.add(game_tab, text="Game")

# Rules tab
rules_tab = ttk.Frame(notebook)
notebook.add(rules_tab, text="Rules")

# Game tab content
instructions_label = tk.Label(game_tab, text="Welcome to the Number Guessing Game!", font=("Arial", 14))
instructions_label.pack(pady=10)

feedback_label = tk.Label(game_tab, text="Click 'Start Game' to begin.", font=("Arial", 12))
feedback_label.pack(pady=10)

guess_entry = tk.Entry(game_tab, font=("Arial", 12))
guess_entry.pack(pady=5)

check_button = tk.Button(game_tab, text="Check Guess", font=("Arial", 12), command=check_guess)
check_button.pack(pady=5)

start_button = tk.Button(game_tab, text="Start Game", font=("Arial", 12), command=start_game)
start_button.pack(pady=10)

# Rules tab content
rules_label = tk.Label(
    rules_tab,
    text=(
        "Rules:\n"
        "1. Click 'Start Game' to begin.\n"
        "2. Enter your guess in the text box.\n"
        "3. The app will guide you if your guess is too high or too low.\n"
        "4. Keep guessing until you find the correct number!"
    ),
    font=("Arial", 12),
    justify="left"
)
rules_label.pack(pady=10, padx=10)

# Start the application
root.mainloop()
