#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    i = 0

    while i < len(text):
        result += text[i]
        if text[i] in ['.', '?', ':']:
            result += "\n\n"
            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1  # Skip spaces after special characters
        i += 1

    # Print the processed text, removing leading/trailing spaces for each line
    for line in result.splitlines():
        print(line.strip())
