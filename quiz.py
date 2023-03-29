name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road. You can go right or left, infront crossroad. "
                "\nWhich way do you wanna go: ").lower()
if answer == "left":
    answer = input("You come to the river, you can walk around or swim \nWhat do you choose? ").lower()
    if answer == "swim":
        print("You swam accros and were eaten by a giant fish")
    elif answer == "walk" or "walk around":
        print("You walk for many miles, ran out of water and you lost game.")
    else:
        print("Wrong input")
elif answer == "right":
    answer = input("You came to the bridge that looks wobly. \nYou wanna cross or go back? (cross/back)")
    if answer == "cross":
        answer = input("You cross the bridge and met stranger. \nDo you talk to him? (yes/no)")
        if answer == "yes":
            print("You talk to the stranger and win the game, gold, medal and all shit.")
        elif answer == "no":
            print("Stranger get offended and you lose.")
        else:
            print("Wrong input")
    elif answer == "back":
        print("You go back to main road and nothing more happend.")
    else:
        print("Wrong input")
else:
    print("Wrong input")
print("thanx for the time you wasted on this game")