import sys
import time


temp = float(input("Please enter a temperature: "))


def main_program():
    which_temp = input("From which temperature do you want to calculate (c for Celsius/f for Fahrenheit): ")
    while which_temp not in ['f', 'c']:
        print("You need to enter c for Celsius or f for Fahrenheit.")
        which_temp = input("From which temperature do you want to calculate (c for Celsius/f for Fahrenheit): ")
    if which_temp == "c":
        fahrenheit()
    else:
        celsius()
    another_calc()


def celsius():
    to_celsius = (temp - 32) * 0.5556
    print(f'Temperature in Celsius is: {to_celsius:.2f} degrees')


def fahrenheit():
    to_fahrenheit = (temp * 1.8) + 32
    print(f'Temperature in Fahrenheit is: {to_fahrenheit:.2f} degrees')


def another_calc():
    global temp
    another_calculation = input("Do you want to convert another temperature (yes/no): ")
    while another_calculation not in ['yes', 'no']:
        print("Please enter yes or no.")
        another_calculation = input("Do you want to convert another temperature (yes/no): ")
    if another_calculation == "yes":
        temp = float(input("Please enter a temperature: "))
        main_program()
    else:
        print("Thank you for using the program!")
        time.sleep(5)
        sys.exit()


main_program()
