import random
import sys
import time

# creating a variable to store the player's lives, defaults to 6
lives = 6


def main_function():
    global lives
    # generating a random number between 1 and 50
    magic_number = random.randint(1, 50)

    while True:
        random_lives()
        # checking if the player's lives have reached 0
        if lives == 0:
            print("You couldn't guess the number.")
            # asking the player if they want to try playing the game again
            another_try = input("Do you want to try again (yes/no): ")
            # if they do, the game is restarted
            if another_try == "yes":
                lives = 6
                main_function()
            # if they don't, the game ends
            else:
                print("Thank you for playing!")
                time.sleep(5)
                break
        lives -= 1
        # get a new guess by the user on every loop
        current_number = int(input("Enter a number between 1 and 50: "))
        # checking the possible cases - the current_number can either be higher, lower, or equal to the magic number
        if current_number < magic_number:
            print("The number that you've entered is lower than the magic number!")
            print(f'You have {lives} lives left.')
        elif current_number > magic_number:
            print("The number that you've entered is higher than the magic number!")
            print(f'You have {lives} lives left.')
        elif current_number == magic_number:
            print("Congratulations! You've guessed the magic number!")


def random_lives():
    global lives
    additional_lives_chance = random.randint(1, 10)
    if additional_lives_chance == 5:
        lives += 2
        print(f"Congratulations! You've won 2 additional lives! You now have {lives} lives total.")
    else:
        pass

# calling the function, so the code above can be executed
main_function()
