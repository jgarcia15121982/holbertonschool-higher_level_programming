#!/usr/bin/python3
"""
5-text_indentation.py file
Functions:
-> text_indentation(text)
"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines after each of
    these characters: '.', '?' and ':'

    Args:
        text (str): The paragraph to divide

    Return:
        Nothing. The function prints the text separated by lines
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    quote = ""
    i = 0
    while i < len(text):
        if text[i] != "." and text[i] != "?" and text[i] != ":":
            quote += text[i]
        else:
            quote += text[i]
            print(quote)
            print()
            quote = ""
            while i < (len(text) - 1) and text[i+1] == " ":
                i += 1
        i += 1
    print(quote, end="")
