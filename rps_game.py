import random

user_wins = 0
computer_wins = 0
option = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in ["rock", "paper", "scissors"]:
        print("Wrong input")
        continue

    random_number = random.randint(0, 2) #rock 1, paper 2, scissors 3
    computer_pick = option[random_number]
    print("Computer picked ", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "scissors":
        print("Nobody won! Again!")

    elif user_input == "rock" and computer_pick == "rock":
        print("Nobody won! Again!")

    elif user_input == "paper" and computer_pick == "paper":
        print("Nobody won! Again!")

    else:
        print("You lose!")
        computer_wins += 1

print("You score " + str(user_wins) + ".")
print("Computer score " + str(computer_wins) + ".")
print("Goodbye")

