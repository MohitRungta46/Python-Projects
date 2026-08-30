# S for Snake, W for Water and G for Gun.

import sys
import random

Computer = random.choice(["s","g","w"])
User  = input("Enter your choice in it's first alphabet: ").lower()

if User not in ("s", "w", "g"):
    print("You have entered a wrong alphabet!")
    sys.exit()

og = {1: "Snake", 0: "Gun", 2: "Water"}
Conversion = {"s":1, "g":0 , "w": 2}
user = Conversion[User]

Conversion = {"s":1, "g":0 , "w": 2}
computer = Conversion[Computer]


print(f"Computer chose {og[computer]}\nYou chose {og[user]}")

if (computer == user):
        print("It's a draw!")

else:
        
    if (computer == 1 and user == 0):
        print("You Won!")
            
    elif (computer == 1 and user == 2):
        print("You Lose!")

    elif (computer == 2 and user == 0):
        print("You Lose!")

    elif (computer == 2 and user == 1):
        print("You Won!")

    elif (computer == 0 and user == 1):
        print("You Lose!")

    elif (computer == 0 and user == 2):
        print("You Won!")

    else:
        print("Something went wrong!")

