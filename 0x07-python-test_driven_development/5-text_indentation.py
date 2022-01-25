#!/usr/bin/python3
"""Module to indent a text
"""


def text_indentation(text):
    """ text_indentation function:
            Function to indent a text

        Args:
            text(str): the text to indent

        Return:
            the text indented
    """
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")

    c = ""
    for i in range(len(text)):
        c += text[i]
        if text[i] in ".?:":
            print((c + '\n').lstrip(' '))
            c = ""
    print(c.lstrip(' '), end='')
