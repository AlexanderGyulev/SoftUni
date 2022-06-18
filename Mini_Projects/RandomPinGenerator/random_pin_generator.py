import random
import sys
import time


how_many_digits = int(input("How many digits do you want your PIN code to have (max 50): "))

# main function, generating a number once the user specifies the desired number of digits
def main_function():
    generate_number()
    # ask the user if they want to generate another PIN
    another_pin = input("Do you want to generate another PIN (yes/no): ")
    while another_pin not in ['yes', 'no']:
        print("You need to enter yes or no.")
        another_pin = input("Do you want to play another game (yes/no): ")
    while another_pin == "yes":
        generate_number()
        another_pin = input("Do you want to generate another PIN (yes/no): ")
        while another_pin not in ['yes', 'no']:
            print("You need to enter yes or no.")
            another_pin = input("Do you want to play another game (yes/no): ")
    else:
        print("Thank you for using the program!")
        time.sleep(5)
        sys.exit()


# generate a random number between 0 and 9 and loop it until the desired number of digits is reached
def generate_number():
    checks()
    total_pin = ""
    for _ in range(how_many_digits):
        new_num = random.randint(0, 9)
        new_num = str(new_num)
        total_pin += new_num
    print(total_pin)


# checking for possible edge cases, for example if the user tries to create a PIN with 0 digits, or if digits > 50
def checks():
    global how_many_digits
    while how_many_digits == 0:
        print("The number of digits has to be greater than 0!")
        how_many_digits = int(input("How many digits do you want your PIN code to have (max 50): "))
    while how_many_digits > 50:
        print("The number of digits has to be less than 50")
        how_many_digits = int(input("How many digits do you want your PIN code to have (max 50): "))


# calling the main function
main_function()
