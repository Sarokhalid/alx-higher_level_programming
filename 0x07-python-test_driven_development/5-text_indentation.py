#!/usr/bin/python3
"""module for text_indentation methoed"""


def text_indentation(text):
    """methoed for adding 2 new lines after '.?:' char
    Args:
        text: the str text
   Raises:
        TypeError: if text is not a str
   """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for delim in ".?:":
        # print(delim, text.split(delim))
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])
    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
