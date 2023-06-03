#!/usr/bin/python3
from sys import argv
say_my_name = __import__('3-say_my_name').say_my_name

if __name__ == "__main__":
    if len(argv) == 3:
        say_my_name(argv[1], argv[2])
    elif len(argv) == 2:
        say_my_name(argv[1])
    else:
        print("Usage: ./3-main.py <first name> <last name>")
