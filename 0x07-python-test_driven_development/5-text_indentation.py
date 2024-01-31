#!/usr/bin/python3
"""Defines a text indentation function"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':' characters.

    Args:
        text(str): The input text.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_marks = ['.', '?', ':']
    lines = []

    start_index = 0
    for i in range(len(text)):
        if text[i] in punctuation_marks:
            lines.append(text[start_index:i + 1].strip())
            lines.append('')
            start_index = i + 1

    if start_index < len(text):
        lines.append(text[start_index:].strip())

    for line in lines:
        print(line)
