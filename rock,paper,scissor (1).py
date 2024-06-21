#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import random module to play the game
import random
def playgame():#creating a function without parameters / arguments
    # Define the options
    options = {
    "rock": "\U0001FAA8",  # 🪨
    "paper": "\U0001F4C4",  # 📄
    "scissors": "\U00002702"  # ✂
}
    print("Let's play the game  🪨,📄,✂!")

    while True:
        # Get user input
        user = input("Enter rock, paper, scissor or 'quit' to exit: ").lower()

        # Check if the user wants to quit
        if user == 'quit':
            print("Thanks for playing!😊")
            break

        # Validate user input
        if user not in options:
            print("Invalid input! Please enter rock, paper, or scissor.")
        else:
            # Randomly choose for the computer
            computer = random.choice(["rock", "paper", "scissors"]) 

            # Print the choices
            print(f"\n user chose: {options[user]} ({user})")
            print(f"Computer chose: {options[computer]} ({computer})\n")

            # Determine and print the result
            if user == computer:
                print("It's a tie!")
                print("Thanks for playing!😊")
            elif (user == "rock" and computer == "scissor") or \
                 (user == "paper" and computer == "rock") or \
                 (user == "scissor" and computer == "paper"):
                print("User wins!🏆")
            else:
                print("Computer wins!🤩")

# Call the function to start the game
playgame()


# In[ ]:




