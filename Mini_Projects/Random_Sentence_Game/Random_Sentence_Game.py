import random
import sys
import time


total_words = ''

random_words = ['car', 'train', 'clock', 'music', 'video', 'happiness', 'duck', 'juice', 'laptop', 'kids', 'browser',
                'interactive', 'approval', 'time', 'chances', 'wrong', 'musical', 'unfair', 'others', 'improvise',
                'crazy', 'printer', 'programming', 'desktop', 'window', 'wardrobe', 'desk', 'chair', 'bed', 'result',
                'success', 'painting', 'sunshine', 'empty', 'loyalty', 'meaning', 'therefore', 'however', 'fridge',
                'private', 'possible', 'factor', 'magical', 'friendly', 'extremely', 'letters', 'sentence', 'security',
                'drink', 'professional', 'mainstream', 'popular', 'dramatic', 'additional', 'complete', 'solution',
                'sometimes', 'particular', 'decide']


def main_program():
    global total_words
    level = input("Choose the hardness level (easy/medium/hard): ")
    level = level.lower()
    while level not in ['easy', 'medium', 'hard']:
        print("The possible options are easy, medium or hard.")
        level = input("Choose the hardness level (easy/medium/hard): ")
    if level == "easy":
        for x in range(10):
            new_word = random.choice(random_words)
            # avoiding a bug where a space will be added after the last word in the generated sentence
            if x < 9:
                total_words = total_words + new_word + ' '
            else:
                total_words = total_words + new_word
    elif level == "medium":
        for x in range(15):
            new_word = random.choice(random_words)
            if x < 14:
                total_words = total_words + new_word + ' '
            else:
                total_words = total_words + new_word
    elif level == "hard":
        for x in range(20):
            new_word = random.choice(random_words)
            if x < 19:
                total_words = total_words + new_word + ' '
            else:
                total_words = total_words + new_word
    print("This is the 'sentence' that you need to type:")
    print(total_words)
    correctness_check()


def correctness_check():
    global total_words
    sentence_input = input("Please input the above sentence here: \n")
    if sentence_input == total_words:
        print("Congratulations! You wrote the sentence correctly!")
    else:
        print("Oh no! You've made a typo!")
    total_words = ''
    try_again()


def try_again():
    another_try = input("Do you want to try again (yes/no): ")
    while another_try not in ['yes', 'no']:
        print("You need to enter yes or no.")
        another_try = input("Do you want to try again (yes/no): ")
    if another_try == 'yes':
        main_program()
    else:
        print("Thank you for using this program!")
        time.sleep(5)
        sys.exit()


main_program()
