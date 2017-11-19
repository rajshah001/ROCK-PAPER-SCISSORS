import random
import time
# Introduction
print("""-----------WELCOME TO THE ROCK PAPER SCISSORS GAME-----------
FOR ROCK PRESS 0
FOR PAPER PRESS 1
FOR SCISSORS PRESS 2""")

# It takes the input from the user and assigns a value to user_move variable.
while True:
    print("TO QUIT THE GAME PRESS 3")
    user_move = ""
    usr_input = int(input())
    if usr_input == 0:
        user_move = "ROCK"
    if usr_input == 1:
        user_move = "PAPER"
    if usr_input == 2:
        user_move = "SCISSORS"
    if usr_input == 3:
        break
    if usr_input > 3:
        print("PLEASE ENTER A VALID MOVE.")
        continue
    print("USER :" + user_move)

# Generates a random move from computer and assigns the value of it to computer_move
    computer_available_move = ["ROCK", "PAPER", "SCISSORS"]
    computer_move = random.choice(computer_available_move)
    print("COMPUTER :" + computer_move)

# Logic for win,lose and tie condition
    if user_move == computer_move:
        print("IT IS A TIE.")
    else:
        if "ROCK" in user_move:
            if "PAPER" in computer_move:
                print("THE COMPUTER WINS")
            elif "SCISSORS" in computer_move:
                print("THE USER WINS")
        if "PAPER" in user_move:
            if "SCISSORS" in computer_move:
                print("THE COMPUTER WINS")
            elif "ROCK" in computer_move:
                print("THE USER WINS")
        if "SCISSORS" in user_move:
            if "ROCK" in computer_move:
                print("THE COMPUTER WINS")
            elif "PAPER" in computer_move:
                print("THE USER WINS")
# If you are running the code on main python shell it waits for 3 second before terminating.
time.sleep(3)
