import tkinter as tk
import random

"""
I got the idea for this project from one of my assignemnts when taking Python at Bellevue University.
I created most of this game and input my code into chatgpt to help me correct my code.
One thing I learned about was frames and that I could use multiple frames to make the game.
"""
sides = ["heads", "tails"]
pot = 1000  # Starting pot amount

# Create the main window
root = tk.Tk()
root.title("Heads or Tails")
root.geometry("800x600")

# Function to get the user's bet amount from the Entry widget
def get_bet():
    try:
        bet_amount = float(bet_entry.get())
        if bet_amount < 10 or bet_amount > pot:
            result_label.config(text="Please enter a valid bet amount (between 10 and your pot).")
            return None
        return bet_amount
    except ValueError:
        result_label.config(text="Please enter a valid bet amount.")
        return None

# Function to get the computer's choice (coin flip)
def coin_flip():
    return random.choice(sides)

# Function to determine the winner and update the pot
def determine_win(user_choice, flip_result, bet_amount):
    global pot
    if user_choice == flip_result:
        pot += bet_amount
        return f"You Win! Your new pot: ${pot}"
    else:
        pot -= bet_amount
        return f"You Lose. Your new pot: ${pot}"

# Function to update the pot label on the betting screen
def update_pot_label():
    pot_label.config(text=f"Current Pot: ${pot}")

# Function to switch to the heads/tails selection screen
def go_to_select_screen():
    bet_amount = get_bet()
    if bet_amount is not None:
        update_pot_label()  # Update the pot display before switching screens
        betting_frame.pack_forget()  # Hide betting frame
        select_frame.pack(expand=True)  # Show selection frame

# Function to handle when heads is selected
def heads_selected():
    bet_amount = get_bet()
    if bet_amount is None:
        return
    user_choice = "heads"
    flip_result = coin_flip()
    result = determine_win(user_choice, flip_result, bet_amount)
    show_result(flip_result, result, user_choice)

# Function to handle when tails is selected
def tails_selected():
    bet_amount = get_bet()
    if bet_amount is None:
        return
    user_choice = "tails"
    flip_result = coin_flip()
    result = determine_win(user_choice, flip_result, bet_amount)
    show_result(flip_result, result, user_choice)

# Function to show the result screen
def show_result(flip_result, result, user_choice):
    select_frame.pack_forget()  # Hide selection frame
    result_frame.pack(expand=True)  # Show result frame
    result_label.config(text=f"You chose: {user_choice.capitalize()} \nCoin flip result: {flip_result.capitalize()}\n{result}")

# Function to go back to the betting screen to play again
def play_again():
    bet_entry.delete(0, tk.END)  # Clear the bet entry
    result_frame.pack_forget()  # Hide result frame
    betting_frame.pack(expand=True)  # Show betting frame again
    update_pot_label()  # Update the pot label

# Betting screen (frame)
betting_frame = tk.Frame(root)
betting_frame.pack(expand=True)

# Label to show current pot
pot_label = tk.Label(betting_frame, text=f"Current Pot: ${pot}", font=("Arial", 14))
pot_label.pack(pady=10)

# Label and Entry for entering bet amount
bet_label = tk.Label(betting_frame, text="Enter your bet amount ($):\n Bet Minimum is $10", font=("Arial", 14))
bet_label.pack(pady=10)
bet_entry = tk.Entry(betting_frame, font=("Arial", 14))
bet_entry.pack(pady=10)

# Submit button to go to selection screen
submit_button = tk.Button(betting_frame, text="Submit Bet", command=go_to_select_screen, font=("Arial", 14))
submit_button.pack(pady=20)

# Heads/Tails selection screen (frame)
select_frame = tk.Frame(root)

# Heads and Tails buttons
button1 = tk.Button(select_frame, text="Heads", command=heads_selected, font=("Arial", 14))
button1.pack(pady=10)
button2 = tk.Button(select_frame, text="Tails", command=tails_selected, font=("Arial", 14))
button2.pack(pady=10)

# Result screen (frame)
result_frame = tk.Frame(root)

# Result label
result_label = tk.Label(result_frame, text="Result will be displayed here", font=("Arial", 16))
result_label.pack(pady=20)

# Play Again button
play_again_button = tk.Button(result_frame, text="Play Again", command=play_again, font=("Arial", 14))
play_again_button.pack(pady=20)

# Start the game on the betting screen
root.mainloop()
