import random
import sys
import time

password_length = int(input("How long do you want your password to be (max 50 characters): "))
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z']
capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=']

symbols_combined = letters + capital_letters + digits + symbols

# main function, calls the generate_pass() function and asks if the user wants to generate another password
def main_program():
    global password_length
    generate_pass()
    another_password = input("Do you want to generate another password (yes/no): ")
    while another_password == "yes":
        password_length = int(input("How long do you want your password to be (max 50 characters): "))
        generate_pass()
        another_password = input("Do you want to generate another password (yes/no): ")

    else:
        print("Thank you for using the program!")
        time.sleep(5)
        sys.exit()


# the function that generates the password - it chooses a random character
def generate_pass():
    checks()
    final_password = ""
    for _ in range(password_length):
        random_pw = random.choice(symbols_combined)
        final_password += random_pw
    print(final_password)


# a few checks for some possible edge cases
def checks():
    global password_length
    while password_length == 0:
        print("The password must be longer than 0 symbols.")
        password_length = int(input("How long do you want your password to be (max 50 characters): "))
    while password_length > 50:
        print("Password must not be longer than 50 characters.")
        password_length = int(input("How long do you want your password to be (max 50 characters): "))


main_program()
