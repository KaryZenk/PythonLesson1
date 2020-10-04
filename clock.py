import colorama
from colorama import Fore, Back, Style
import datetime
import time
import random
from numbers import digits, semicolon, blank, blank_digit  # My dict + symbols

BLOCK = 2*'\u2588'

BLINK_FLAG = True


def get_current_time():  # Create our laptop time
    return datetime.datetime.now()


def merge_digits(*args):  # Loop from 5 iteration + merge with a loop
    result = ["", "", "", "", ""]
    for template in args:
        for i in range(5):
            result[i] += template[i]
    return result

def print_digits(current_time):  # Return our digits from dict
    global BLINK_FLAG  # показывает, что это из глобальной области
    hour0 = digits[current_time.hour//10]
    hour1 = digits[current_time.hour%10]
    minute0 = digits[current_time.minute//10]
    minute1 = digits[current_time.minute%10]
    second0 = digits[current_time.second//10]
    second1 = digits[current_time.second%10]
    sep = semicolon if BLINK_FLAG else blank  # ternarary operator 
    BLINK_FLAG = not BLINK_FLAG
    clock = merge_digits(
        blank_digit,
        hour0, blank_digit, hour1,
        sep,
        minute0, blank_digit, minute1,
        sep,
        second0, blank_digit, second1
    )
    print_lines(clock)

def color_generator():  # random color generator
    return random.choice([Fore.CYAN, Fore.GREEN, Fore.MAGENTA, Fore.RED])

def print_lines(clock):  # printing our lines
    print(color_generator())
    for clock_line in clock:
        rendered_line = clock_line.replace('0', BLOCK).replace(' ', 2*' ')
        print(rendered_line)
    print(Style.RESET_ALL)


def clear_screen():  # Clear screen
    print('\033[2J')


def sleep_for_a_while(period):  # Sleeping period
    time.sleep(period)


if __name__ == "__main__":
    colorama.init()
    while True:  # Create loop to draw our clock
        current_time = get_current_time()
        print_digits(current_time)
        sleep_for_a_while(0.5)
        clear_screen()
