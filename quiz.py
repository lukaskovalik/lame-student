import random

user_wins = 0
computer_wins = 0
option = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit").lower()
    if user_input == "q":
        break

    if user_input not in ["rock", "paper", "scissors"]:
        print("Wrong input")
        continue

    random_number = random.randint(0, 2) #rock 1, paper 2, scissors 3


print("Goodbye")

