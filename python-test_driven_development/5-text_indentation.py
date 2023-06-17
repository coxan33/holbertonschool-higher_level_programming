#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    jump = [".", "?", ":"]
    i = 0
    while i < len(text):
        if text[i] in jump:
            print(text[i])
            print()
            i += 1
            while (text[i] == " "):
                i += 1
        else:
            print(text[i], end="")
            i += 1
