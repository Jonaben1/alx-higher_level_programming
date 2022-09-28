#!/usr/bin/python3
"""write_file
"""


def read_file(filename="", text = ""):
    """Write a str filename and returns the
       number of characters written
    """

    with open(filename, mode = "w", encoding="utf-8") as writeFile:
        writeFile.write(text)
        return len(text)
