import os
import datetime
import functools
import random
import numerals
from time import sleep
from colorama import init
from colorama import Fore, Back, Style
from datetime import datetime, time


def clock():
    color = [Fore.GREEN, Fore.RED, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN]
    while True:
        show_time = datetime.now()
        str_show_time = show_time.strftime("%H |%M |%S")
        ww = random.choice(color)
        if "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" in str_show_time:
            new_0 = str_show_time.replace("0", numerals.zero_1st_str)
            new_1 = new_0.replace("1", (numerals.one_1st_str))
            new_2 = new_1.replace("2", numerals.two_1st_str)
            new_3 = new_2.replace("3", numerals.three_1st_str)
            new_4 = new_3.replace("4", numerals.four_1st_str)
            new_5 = new_4.replace("5", numerals.five_1st_str)
            new_6 = new_5.replace("6", numerals.six_1st_str)
            new_7 = new_6.replace("7", numerals.seven_1st_str)
            new_8 = new_7.replace("8", numerals.eight_1st_str)
            new_9 = new_8.replace("9", numerals.nine_1st_str)
            print(ww, new_9)
        if "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" in str_show_time:
            new_0 = str_show_time.replace("0", numerals.zero_2nd_str)
            new_1 = new_0.replace("1", (numerals.one_2nd_str))
            new_2 = new_1.replace("2", numerals.two_2nd_str)
            new_3 = new_2.replace("3", numerals.three_2nd_str)
            new_4 = new_3.replace("4", numerals.four_2nd_str)
            new_5 = new_4.replace("5", numerals.five_2nd_str)
            new_6 = new_5.replace("6", numerals.six_2nd_str)
            new_7 = new_6.replace("7", numerals.seven_2nd_str)
            new_8 = new_7.replace("8", numerals.eight_2nd_str)
            new_9 = new_8.replace("9", numerals.nine_2nd_str)
            print(ww, new_9)
        if "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" in str_show_time:
            new_0 = str_show_time.replace("0", numerals.zero_3rd_str)
            new_1 = new_0.replace("1", (numerals.one_3rd_str))
            new_2 = new_1.replace("2", numerals.two_3rd_str)
            new_3 = new_2.replace("3", numerals.three_3rd_str)
            new_4 = new_3.replace("4", numerals.four_3rd_str)
            new_5 = new_4.replace("5", numerals.five_3rd_str)
            new_6 = new_5.replace("6", numerals.six_3rd_str)
            new_7 = new_6.replace("7", numerals.seven_3rd_str)
            new_8 = new_7.replace("8", numerals.eight_3rd_str)
            new_9 = new_8.replace("9", numerals.nine_3rd_str)
            print(ww, new_9)
        if "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" in str_show_time:
            new_0 = str_show_time.replace("0", numerals.zero_4th_str)
            new_1 = new_0.replace("1", (numerals.one_4th_str))
            new_2 = new_1.replace("2", numerals.two_4th_str)
            new_3 = new_2.replace("3", numerals.three_4th_str)
            new_4 = new_3.replace("4", numerals.four_4th_str)
            new_5 = new_4.replace("5", numerals.five_4th_str)
            new_6 = new_5.replace("6", numerals.six_4th_str)
            new_7 = new_6.replace("7", numerals.seven_4th_str)
            new_8 = new_7.replace("8", numerals.eight_4th_str)
            new_9 = new_8.replace("9", numerals.nine_4th_str)
            print(ww, new_9)
        if "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" in str_show_time:
            new_0 = str_show_time.replace("0", numerals.zero_5th_str)
            new_1 = new_0.replace("1", (numerals.one_5th_str))
            new_2 = new_1.replace("2", numerals.two_5th_str)
            new_3 = new_2.replace("3", numerals.three_5th_str)
            new_4 = new_3.replace("4", numerals.four_5th_str)
            new_5 = new_4.replace("5", numerals.five_5th_str)
            new_6 = new_5.replace("6", numerals.six_5th_str)
            new_7 = new_6.replace("7", numerals.seven_5th_str)
            new_8 = new_7.replace("8", numerals.eight_5th_str)
            new_9 = new_8.replace("9", numerals.nine_5th_str)
            print(ww, new_9)
        if "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" in str_show_time:
            new_0 = str_show_time.replace("0", numerals.zero_6th_str)
            new_1 = new_0.replace("1", (numerals.one_6th_str))
            new_2 = new_1.replace("2", numerals.two_6th_str)
            new_3 = new_2.replace("3", numerals.three_6th_str)
            new_4 = new_3.replace("4", numerals.four_6th_str)
            new_5 = new_4.replace("5", numerals.five_6th_str)
            new_6 = new_5.replace("6", numerals.six_6th_str)
            new_7 = new_6.replace("7", numerals.seven_6th_str)
            new_8 = new_7.replace("8", numerals.eight_6th_str)
            new_9 = new_8.replace("9", numerals.nine_6th_str)
            print(ww, new_9)
        sleep(1.000000000)
        os.system('cls' if os.name=='nt' else 'clear')
clock()