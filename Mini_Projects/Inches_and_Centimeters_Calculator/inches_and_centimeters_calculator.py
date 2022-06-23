import sys
import time

num = float(input("Please input the number that you want to convert: "))


def main_program():
    fromwhich = input("From which measurement do you want to convert (c for centimeters, i for inches): ")
    while fromwhich not in ['c', 'i']:
        print("Please enter c for centimeters, or i for inches.")
        fromwhich = input("From which measurement do you want to convert (c for centimeters, i for inches): ")
    if fromwhich == "c":
        centimeters()
    else:
        inches()
    another_try()


def centimeters():
    convert = num / 2.54
    print(f'The number {num} converted to inches is: {convert:.2f}!')


def inches():
    convert = num * 2.54
    print(f'The number {num} converted to centimeters is: {convert:.2f}!')


def another_try():
    global num
    another_convert = input("Do you want to convert another number (yes/no): ")
    while another_convert not in ['yes', 'no']:
        print("Please enter yes or no.")
        another_convert = input("Do you want to convert another number (yes/no): ")
    if another_convert == "yes":
        num = float(input("Please input the number that you want to convert: "))
        main_program()
    else:
        print("Thank you for using the program!")
        time.sleep(5)
        sys.exit()


main_program()
