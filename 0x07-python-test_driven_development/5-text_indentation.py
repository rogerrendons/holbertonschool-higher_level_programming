#!/usr/bin/python3
"""
    Its a function that slit text

"""


def text_indentation(text):
    """

        text_indentation: split a text

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.replace("?", '?\n\n')
    text = text.replace(".", '.\n\n')
    text = text.replace(":", ':\n\n')
    text = text.replace("?\n\n ", '?\n\n')
    text = text.replace(".\n\n ", '.\n\n')
    text = text.replace(":\n\n ", ':\n\n')
    print(text.strip(' '), end="")
