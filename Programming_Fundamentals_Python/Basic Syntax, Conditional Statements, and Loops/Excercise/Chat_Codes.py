total_messages = int(input())

current_number = 0


def main():
    global current_number
    for i in range(total_messages):
        current_number = int(input())
        checks()


def checks():
    if current_number == 88:
        print("Hello")
    elif current_number == 86:
        print("How are you?")
    elif current_number < 88:
        print("GREAT!")
    elif current_number > 88:
        print("Bye.")


if __name__ == '__main__':
    main()