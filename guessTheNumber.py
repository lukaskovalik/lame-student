from random import randint
name = input("Enter your name: ")
print(f"Well {name}, I've thought of a number between 1 and 100"
      f"\nand you have only 8 tries to guess it."
      f"\nWhat number do you think it is?")
tries = 8
number = randint(1, 100)

while True:
    if tries > 0:
        user_input = int(input())
        if user_input > number:
            tries-=1
            print(f"Your guess is higher. You have {tries} tries\n")
        elif user_input < number:
            tries-=1
            print(f"Your guess is lower. You have {tries} tries\n")
        elif user_input == number:
            print("You guessed the number!")
            break
        else:
            print("Wrong input, try again")
    else:
        print(f"You have run out of attempts. Secret number was {number}")
        quit()
