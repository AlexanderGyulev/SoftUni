import random
import sys
import time


def main_function():
    # generating a random number between 1 and 50
    magic_number = random.randint(1, 50)

    # creating a variable to store the player's lives, defaults to 6
    lives = 6

    while True:
        # get a new guess by the user on every loop
        current_number = int(input("Enter a number between 1 and 50: "))
        # checking the possible cases - the current_number can either be higher, lower, or equal to the magic number
        if current_number < magic_number:
            print("The number that you've entered is lower than the magic number!")
            lives -= 1
        elif current_number > magic_number:
            print("The number that you've entered is higher than the magic number!")
            lives -= 1
        elif current_number == magic_number:
            print("Congratulations! You've guessed the magic number!")
            # asking the player if they want to try playing the game again
            another_try = input("Do you want to try again (yes/no): ")
            # if they do, the game is restarted
            if another_try == "yes":
                main_function()
            # if they don't, the game ends
            else:
                print("Thank you for playing!")
                time.sleep(5)
                sys.exit()
        # checking if the player's lives have reached 0
        if lives == 0:
            print(f"You couldn't guess the number. The number was {magic_number}!")
            # asking the player if they want to try playing the game again
            another_try = input("Do you want to try again (yes/no): ")
            # if they do, the game is restarted
            if another_try == "yes":
                main_function()
            # if they don't, the game ends
            else:
                print("Thank you for playing!")
                time.sleep(5)
                sys.exit()

# calling the function, so the code above can be executed
main_function()
