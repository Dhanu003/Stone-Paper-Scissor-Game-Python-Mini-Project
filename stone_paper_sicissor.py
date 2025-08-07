
""" 
Case 1: Stone

Stone vs Stone    = Match Tie
Stone vs Paper    = Paper Wins
Stone vs Scissor  = Stone Wins

Case 2: Paper

Paper vs Paper    = Match Tie
Paper vs Stone    = Paper Wins
Paper vs Scissor  = Scissor Wins

Case 3: Scissor

Scissor vs Scissor = Match Tie
Scissor vs Stone   = Stone Wins
Scissor vs Paper   = Scissor Wins


"""

import random as r

# Using plain values for logic 
items = ["Stone", "Paper", "Scissor"]

# Emojis for display
emoji = {
    "Stone": "Stone 🪨",
    "Paper": "Paper 📄",
    "Scissor": "Scissor ✂️"
}

print("Let’s play! 🎮")
user_input = input("Tell me your choice: Stone, Paper, or Scissor? = ").capitalize()

# Taking input
if user_input not in items:
    print("Invalid choice! Please choose Stone, Paper, or Scissor.")
else:
    comp_input = r.choice(items)

    print(f"\nAwesome! You chose: {emoji[user_input]}")
    print(f"I choose: {emoji[comp_input]}")

    # Logic starts
    if user_input == comp_input:
        print("Both chose the same: Match Tie 🤝")

    elif user_input == "Stone":   #Case 1
        if comp_input == "Paper":
            print("Paper wraps Stone: Hurray! I Win 😎 , You Lose")
        else:
            print("Stone breaks Scissor: You Win! 🎉")

    elif user_input == "Paper":  # Case 2
        if comp_input == "Scissor":
            print("Scissor cuts Paper: Hurray! I Win 😎 , You Lose")
        else:
            print("Paper wraps Stone: You Win! 🎉")

    elif user_input == "Scissor": #Case 3
        if comp_input == "Stone":
            print("Stone breaks Scissor: Hurray! I Win 😎 , You Lose")
        else:
            print("Scissor cuts Paper: You Win! 🎉")
