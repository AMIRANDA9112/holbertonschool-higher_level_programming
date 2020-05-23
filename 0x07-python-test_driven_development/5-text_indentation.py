#!/usr/bin/python3
"""
text_indentation make new line automatic while
have a sign how '?', '.', ':'
"""
def text_indentation(text):
    """

    :param text: string to indent
    """
    templetter = ""

    if type(text) != str:
        raise TypeError("text must be a string")

    for letter in text:
        templetter += letter
        if letter in ['?', '.', ':']:
            print(templetter.strip() + "\n")
            templetter = ''
    print(templetter.strip(), end="")
