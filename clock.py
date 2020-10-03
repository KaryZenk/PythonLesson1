import colorama
from colorama import Fore, Back, Style
import datetime
import time
import random

BLOCK = 2*'\u2588'
digits = {
    0:
    [
        "000",
        "0 0",
        "0 0",
        "0 0",
        "000",
    ],
    1: [
        "00 ",
        " 0 ",
        " 0 ",
        " 0 ",
        "000",
    ],
    2: [
        "000",
        "  0",
        "000",
        "0  ",
        "000",
    ],
    3: [
        "000",
        "  0",
        "000",
        "  0",
        "000",
    ],
    4: [
        "0 0",
        "0 0",
        "000",
        "  0",
        "  0",
    ],
    5: [
        "000",
        "0  ",
        "000",
        "  0",
        "000",
    ],
    6: [
        "000",
        "0  ",
        "000",
        "0 0",
        "000",
    ],
    7: [
        "000",
        "  0",
        "  0",
        "  0",
        "  0",
    ],
    8: [
        "000",
        "0 0",
        "000",
        "0 0",
        "000",
    ],
    9: [
        "000",
        "0 0",
        "000",
        "  0",
        "000",
    ]
}
semicolon = [
    "   ",
    " 0 ",
    "   ",
    " 0 ",
    "   "
]
blank = [
    "   ",
    "   ",
    "   ",
    "   ",
    "   ",
]
blank_digit = [
    " ",
    " ",
    " ",
    " ",
    " ",
]
BLINK_FLAG = True


def get_current_time():
    return datetime.datetime.now()


def merge_digits(*args):
    result = ["", "", "", "", ""]
    for template in args:
        for i in range(5):
            result[i] += template[i]
    return result

def print_digits(current_time):
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

def color_generator():
    return random.choice([Fore.CYAN, Fore.GREEN, Fore.MAGENTA, Fore.RED])

def print_lines(clock):
    print(color_generator())
    for clock_line in clock:
        rendered_line = clock_line.replace('0', BLOCK).replace(' ', 2*' ')
        print(rendered_line)
    print(Style.RESET_ALL)


def clear_screen():
    print('\033[2J')


def sleep_for_a_while(period):
    time.sleep(period)


if __name__ == "__main__":
    colorama.init()
    while True:
        current_time = get_current_time()
        print_digits(current_time)
        sleep_for_a_while(0.5)
        clear_screen()
