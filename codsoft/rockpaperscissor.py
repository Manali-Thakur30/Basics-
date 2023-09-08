import random
import tkinter as tk
from tkinter import messagebox

# Initialize scores
user_score = 0
computer_score = 0

def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    global user_score, computer_score

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        user_score += 1
        return "You win!"
    else:
        computer_score += 1
        return "Computer wins!"

def play_game():
    user_choice = user_choice_var.get()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    update_scores()

    result_window = tk.Toplevel(root)
    result_window.title("Result")
    result_label = tk.Label(result_window, text=f"Computer chose {computer_choice}. {result}")
    result_label.pack()

    play_again_button = tk.Button(result_window, text="Play Again", command=result_window.destroy)
    play_again_button.pack()

    quit_button = tk.Button(result_window, text="Quit", command=quit_game)
    quit_button.pack()

def update_scores():
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

def quit_game():
    if messagebox.askyesno("Quit Game", "Are you sure you want to quit?"):
        root.quit()

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

# Set the size of the window
root.geometry("400x400")  # Set width and height in pixels

# Set the background color of the entire window
root.configure(bg="black")

# Create a label and options for the user to choose
user_choice_label = tk.Label(root, text="Rock, Paper, or Scissors:", bg="lavender", fg="black", font=("Arial", 16))
user_choice_label.pack(fill=tk.X)
#user_choice_label.pack()

# result_label = tk.Label(root, text="", bg="black")
# result_label.pack()
# result_label = tk.Label(root, text="", bg="black")
# result_label.pack()

user_choice_var = tk.StringVar()
user_choice_var.set("Rock")  # Default choice
user_choices = ["Rock", "Paper", "Scissors"]
user_choice_menu = tk.OptionMenu(root, user_choice_var, *user_choices)
user_choice_menu.pack(padx= 40, pady= 40)

# Create a button to play the game
play_button = tk.Button(root, text="Play", bg="red", fg="white", command=play_game)
play_button.pack(padx= 30, pady= 10)

# Create a label to display the result
result_label = tk.Label(root, text="", bg="black")
result_label.pack()

# Create labels to display user and computer scores
user_score_label = tk.Label(root, text="Your Score: 0", bg="black", fg="white")
user_score_label.pack()

computer_score_label = tk.Label(root, text="Computer Score: 0", bg="black", fg="white")
computer_score_label.pack()

# Start the GUI event loop
root.mainloop()

# Show "Thank You for Playing" message when quitting
messagebox.showinfo("Thank You", "Thank you for playing!")
