import tkinter as tk
import random

choices = ["rock", "paper", "scissors"]

root = tk.Tk()
root.title("Rock Paper Scissors")

root.geometry("800x600")

# Function to get the computer's choice
def computer_choice():
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "It's a draw!"
    elif (user_choice == "rock" and comp_choice == "scissors") or \
         (user_choice == "paper" and comp_choice == "rock") or \
         (user_choice == "scissors" and comp_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

# Function for Rock button
def rock_selected():
    user_choice = "rock"
    comp_choice = computer_choice()
    result = determine_winner(user_choice, comp_choice)
    result_label.config(text=f"You chose {user_choice.capitalize()}\nComputer chose {comp_choice.capitalize()}\n{result}")

# Function for Paper button
def paper_selected():
    user_choice = "paper"
    comp_choice = computer_choice()
    result = determine_winner(user_choice, comp_choice)
    result_label.config(text=f"You chose {user_choice.capitalize()}\nComputer chose {comp_choice.capitalize()}\n{result}")

# Function for Scissors button
def scissors_selected():
    user_choice = "scissors"
    comp_choice = computer_choice()
    result = determine_winner(user_choice, comp_choice)
    result_label.config(text=f"You chose {user_choice.capitalize()}\nComputer chose {comp_choice.capitalize()}\n{result}")

result_label = tk.Label(root, text="Make a selection", font=("Arial", 16))
result_label.pack(side="top", pady=20)
# Create a frame to hold the buttons and center them
button_frame = tk.Frame(root)
button_frame.pack(expand=True)

# Create buttons inside the button_frame
button1 = tk.Button(button_frame, text="Rock", command=rock_selected)
button1.pack(pady=10)

button2 = tk.Button(button_frame, text="Paper", command=paper_selected)
button2.pack(pady=10)

button3 = tk.Button(button_frame, text="Scissors", command=scissors_selected)
button3.pack(pady=10)

root.mainloop()
