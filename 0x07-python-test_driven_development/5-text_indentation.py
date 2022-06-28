#!/usr/bin/python3
"""
Module 5-text_indentation
Contain a method that print a text
The text with 2 new lines after each of these characters: ., ? and :
Takes one text argumnet
"""


def text_indentation(text):
    """a text with 2 new lines after each of these characters: ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    new_line = [line.strip(' ') for line in text.split("\n")]
    output = "\n".join(new_line)
    print(output, end="")
