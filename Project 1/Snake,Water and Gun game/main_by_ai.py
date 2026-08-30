import sys
import random

# 1. Setup Data
og = {1: "Snake", 0: "Gun", 2: "Water"}
conversion = {"s": 1, "g": 0, "w": 2}

# 2. Get Choices
computer_letter = random.choice(["s", "g", "w"])
user_input = input("Enter your choice (s for Snake, g for Gun, w for Water): ").lower()

# 3. Validate Input FIRST (before using it in a dictionary)
if user_input not in conversion:
    print("You have entered a wrong alphabet!")
    sys.exit()

# 4. Convert letters to numbers
user_num = conversion[user_input]
computer_num = conversion[computer_letter]

# 5. Show choices (using the names from the 'og' dictionary)
print(f"Computer chose {og[computer_num]}")
print(f"You chose {og[user_num]}")

# 6. Game Logic (Indented properly)
if computer_num == user_num:
    print("It's a draw!")
else:
    if computer_num == 1 and user_num == 0:    # Snake vs Gun
        print("You Won!")
    elif computer_num == 1 and user_num == 2:  # Snake vs Water
        print("You Lose!")
    elif computer_num == 2 and user_num == 0:  # Water vs Gun
        print("You Lose!")
    elif computer_num == 2 and user_num == 1:  # Water vs Snake
        print("You Won!")
    elif computer_num == 0 and user_num == 1:  # Gun vs Snake
        print("You Lose!")
    elif computer_num == 0 and user_num == 2:  # Gun vs Water
        print("You Won!")
    else:
        print("Something went wrong!")