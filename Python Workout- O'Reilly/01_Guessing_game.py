import random


def guessing_game():
    number = random.randint(0, 100)
    count = 0
    while count <= 2:
        try:
            user_number = int(input("Please write a number from 1 to 100: \n"))
        except ValueError:
            raise ValueError("Please enter a valid integer!")
        if number > user_number and count <= 3:
            print(f"Too low!")
            count += 1
        elif number < user_number and count <= 3:
            print(f"Too high!")
            count += 1
        else:
            print(f"You're right! The number was {user_number}!")
            break


guessing_game()
