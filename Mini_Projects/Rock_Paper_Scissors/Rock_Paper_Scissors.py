import random
import sys
import time

player_input = input("Please enter rock, paper or scissors: ")

computer_choice = ""


def main_program():
    global player_input
    computer_response()
    another_game = input("Do you want to play another game (yes/no): ")
    while another_game not in ['yes', 'no']:
        print("You need to enter yes or no.")
        another_game = input("Do you want to play another game (yes/no): ")
    if another_game == "yes":
        player_input = input("Please enter rock, paper or scissors: ")
        main_program()
    else:
        print("Thank you for playing the game!")
        time.sleep(5)
        sys.exit()


# generating the value that the program will display after the user has chosen rock, paper or scissors
def computer_response():
    global computer_choice
    random_choice = random.randint(1, 3)
    if random_choice == 1:
        computer_choice = "rock"
    elif random_choice == 2:
        computer_choice = "paper"
    else:
        computer_choice = "scissors"
    who_won()


# handling the different cases
def who_won():
    global player_input
    checks()
    print(f'You chose: {player_input}')
    print(f'Computer chose: {computer_choice}')
    if player_input == "rock" and computer_choice == "rock":
        print_draw()
    elif player_input == "rock" and computer_choice == "paper":
        print_loss()
    elif player_input == "rock" and computer_choice == "scissors":
        print_win()
    elif player_input == "paper" and computer_choice == "rock":
        print_win()
    elif player_input == "paper" and computer_choice == "paper":
        print_draw()
    elif player_input == "paper" and computer_choice == "scissors":
        print_loss()
    elif player_input == "scissors" and computer_choice == "rock":
        print_loss()
    elif player_input == "scissors" and computer_choice == "paper":
        print_win()
    elif player_input == "scissors" and computer_choice == "scissors":
        print_draw()


def print_loss():
    print("You lost! Better luck next time!")


def print_win():
    print("You won! Congratulations!")


def print_draw():
    print("No one won! It's a draw!")


# a few checks for some edge cases
def checks():
    global player_input
    while player_input not in ['rock', 'paper', 'scissors']:
        print("You can only enter rock, paper or scissors.")
        player_input = input("Please enter rock, paper or scissors: ")


main_program()


