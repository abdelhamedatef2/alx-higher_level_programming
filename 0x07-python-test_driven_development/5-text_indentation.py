#!/usr/bin/python3

"""Defination of text-indentation function."""

def text_indentation(text):
    """Print text after each (.,?,:) with new line.

    Args:
        text (string): text will be printed.
    Raises:
        TypeError: If text not str.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")

        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            print("\n")

            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1

            continue

        c += 1
